import sys
import pandas as pd
import numpy as np

def topsis(input_file, weights, impacts, output_file):
    try:
        data = pd.read_csv(input_file)
    except FileNotFoundError:
        print("Error: File not found.")
        sys.exit(1)

    if data.shape[1] < 3:
        print("Error: Input file must contain at least 3 columns.")
        sys.exit(1)

    numeric_data = data.iloc[:, 1:]

    if not all(np.issubdtype(dtype, np.number) for dtype in numeric_data.dtypes):
        print("Error: All columns except first must be numeric.")
        sys.exit(1)

    weights = weights.split(',')
    impacts = impacts.split(',')

    if len(weights) != numeric_data.shape[1] or len(impacts) != numeric_data.shape[1]:
        print("Error: Number of weights, impacts and columns must match.")
        sys.exit(1)

    if not all(i in ['+', '-'] for i in impacts):
        print("Error: Impacts must be '+' or '-'.")
        sys.exit(1)

    weights = np.array(weights, dtype=float)

    norm = np.sqrt((numeric_data**2).sum())
    normalized = numeric_data / norm

    weighted = normalized * weights

    ideal_best = []
    ideal_worst = []

    for i in range(len(impacts)):
        if impacts[i] == '+':
            ideal_best.append(weighted.iloc[:, i].max())
            ideal_worst.append(weighted.iloc[:, i].min())
        else:
            ideal_best.append(weighted.iloc[:, i].min())
            ideal_worst.append(weighted.iloc[:, i].max())

    ideal_best = np.array(ideal_best)
    ideal_worst = np.array(ideal_worst)

    distance_best = np.sqrt(((weighted - ideal_best)**2).sum(axis=1))
    distance_worst = np.sqrt(((weighted - ideal_worst)**2).sum(axis=1))

    score = distance_worst / (distance_best + distance_worst)

    data['Topsis Score'] = score
    data['Rank'] = score.rank(ascending=False).astype(int)

    data.to_csv(output_file, index=False)
    print("Result saved to", output_file)


if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: python topsis.py <inputFile> <weights> <impacts> <outputFile>")
        sys.exit(1)

    _, input_file, weights, impacts, output_file = sys.argv
    topsis(input_file, weights, impacts, output_file)

def main():
    import sys
    if len(sys.argv) != 5:
        print("Usage: topsis <inputFile> <weights> <impacts> <outputFile>")
        sys.exit(1)

    _, input_file, weights, impacts, output_file = sys.argv
    topsis(input_file, weights, impacts, output_file)

