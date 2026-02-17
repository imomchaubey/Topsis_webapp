import os
import pandas as pd
import numpy as np
from flask import Flask, render_template, request, send_file

app = Flask(__name__)

# Folder settings
UPLOAD_FOLDER = 'uploads'
RESULT_FOLDER = 'results'

# Ensure directories exist [cite: 12]
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(RESULT_FOLDER, exist_ok=True)

def perform_topsis(input_path, weights, impacts):
    # Load the data [cite: 13, 14]
    df = pd.read_csv(input_path)
    
    # Requirements: First column is usually names, rest are numeric [cite: 14]
    data = df.iloc[:, 1:].values.astype(float)
    
    # 1. Normalization 
    norm_data = data / np.sqrt((data**2).sum(axis=0))
    
    # 2. Weighted Normalized Matrix 
    weighted_data = norm_data * weights
    
    # 3. Ideal Best and Ideal Worst [cite: 2, 16]
    ideal_best = []
    ideal_worst = []
    
    for i in range(len(impacts)):
        if impacts[i] == '+':
            ideal_best.append(max(weighted_data[:, i]))
            ideal_worst.append(min(weighted_data[:, i]))
        else:
            ideal_best.append(min(weighted_data[:, i]))
            ideal_worst.append(max(weighted_data[:, i]))
            
    # 4. Euclidean Distance 
    dist_best = np.sqrt(((weighted_data - ideal_best)**2).sum(axis=1))
    dist_worst = np.sqrt(((weighted_data - ideal_worst)**2).sum(axis=1))
    
    # 5. Performance Score 
    scores = dist_worst / (dist_best + dist_worst)
    
    # Update DataFrame with Topsis Score and Rank 
    df['Topsis Score'] = scores
    df['Rank'] = df['Topsis Score'].rank(ascending=False).astype(int)
    
    return df

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    # 1. Get data from the form [cite: 39]
    file = request.files['file']
    weights_str = request.form.get('weights')
    impacts_str = request.form.get('impacts')

    # 2. Validation Checks [cite: 41, 42, 43]
    try:
        w_list = [float(x) for x in weights_str.split(',')]
        i_list = [x.strip() for x in impacts_str.split(',')]
    except ValueError:
        return "Error: Weights must be numeric and separated by commas."

    if len(w_list) != len(i_list):
        return "Error: Number of weights and impacts must be the same." [cite: 41]

    for imp in i_list:
        if imp not in ['+', '-']:
            return "Error: Impacts must be either + or -." [cite: 42]

    # 3. Save the uploaded file temporarily [cite: 12]
    input_path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(input_path)

    # 4. Run TOPSIS Logic
    try:
        result_df = perform_topsis(input_path, w_list, i_list)
        
        # Save result file
        result_filename = "result_" + file.filename
        output_path = os.path.join(RESULT_FOLDER, result_filename)
        result_df.to_csv(output_path, index=False)
        
        # 5. Send file for download 
        return send_file(output_path, as_attachment=True)
        
    except Exception as e:
        return f"An error occurred during processing: {str(e)}"

if __name__ == '__main__':
    app.run(debug=True)