# TOPSIS Implementation Project - 102317189

This project is a complete implementation of the **Technique for Order of Preference by Similarity to Ideal Solution (TOPSIS)**. It is divided into three parts: a command-line utility, a distributed Python package, and a Flask-based web service.

---

## 🛠️ Project Parts

### Part-I: Command Line Program
[cite_start]A Python-based command-line tool that performs the TOPSIS calculation on a CSV dataset[cite: 3, 4].
* [cite_start]**Usage**: `python <program.py> <InputDataFile> <Weights> <Impacts> <OutputResultFileName>` [cite: 6]
* [cite_start]**Example**: `python topsis.py data.csv "1,1,1,2" "+,+,-,+" output-result.csv` [cite: 8]

### Part-II: Python Package (PyPi)
[cite_start]The logic is structured as a package named **Topsis-Om-102317189** for distribution on PyPi[cite: 21, 22].
* [cite_start]**Package Name**: `Topsis-Om-102317189` [cite: 22]
* [cite_start]**Structure**: Includes `setup.py`, `requirements.txt`, and the source code[cite: 23].

### Part-III: Web Service
[cite_start]A Flask web application that provides a graphical interface for processing TOPSIS requests[cite: 28].
* [cite_start]**Inputs**: Users upload a CSV file and specify weights, impacts, and an email ID[cite: 30, 32, 33, 36, 39].
* [cite_start]**Output**: The results (Topsis Score and Rank) are processed and provided for download[cite: 40].

---

## 📋 Mandatory Requirements & Validations

The program includes strict validation checks as per the assignment instructions:
* [cite_start]**Correct Parameters**: Ensures all 4 command-line parameters are provided[cite: 10].
* [cite_start]**File Validation**: Checks for "File not Found" and ensures the file has 3+ columns[cite: 12, 13].
* [cite_start]**Numeric Values**: Validates that columns from the 2nd to the last contain only numeric values[cite: 14].
* [cite_start]**Weight/Impact Match**: Confirms the number of weights, impacts, and columns are identical[cite: 15].
* [cite_start]**Impact Symbols**: Restricts impacts to only `+` or `-`[cite: 16].
* [cite_start]**Input Formatting**: Weights and impacts must be separated by commas (`,`)[cite: 17].

---

## 🚀 Getting Started

### 1. Prerequisites
Ensure you have Python installed and the following libraries:
* `pandas`
* `numpy`
* `flask`

### 2. Installation
1. Clone the repository:
   ```bash
   git clone [https://github.com/imomchaubey/Topsis_webapp.git](https://github.com/imomchaubey/Topsis_webapp.git)

   
