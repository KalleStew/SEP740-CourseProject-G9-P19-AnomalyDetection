# SEP740 Project 19: Anomaly Detection Using Autoencoders

## 👥 Group Members
* Member 1 Name (Student ID)
* Member 2 Name (Student ID)
* Member 3 Name (Student ID)

## 📖 Project Overview
This repository contains the codebase for SEP740 Project 19. The objective is to develop an anomaly detection system using autoencoder neural networks trained on the KDD Cup 1999 dataset to identify anomalous network traffic (cyberattacks).

## ⚙️ Prerequisites & Setup
1. Clone this repository to your local machine.
2. Ensure you have Python 3.9+ installed.
3. Create and activate a virtual environment:
    ```
    python -m venv venv
    source venv/bin/activate  # On Windows use: venv\Scripts\activate
    ```
4. Install dependencies:
    ```
    pip install -r requirements.txt
    ```

## 💾 Dataset Instructions
1. Download the KDD Cup 1999 dataset.
2. Extract the dataset and place the `kddcup.data_10_percent.gz` file into the `data/raw/` directory. 
*Note: Do not commit the dataset to GitHub. The `data/` directory is git-ignored.*

## 🚀 How to Run the Code
To replicate the results outlined in our final report, execute the scripts in the following order:

1. **Preprocess the data:**
   `python src/data_preprocessing.py`
   *(Cleans, normalizes, and splits the data into `data/processed/`)*

2. **Train the Autoencoder:**
   `python src/train.py`
   *(Trains the baseline model and saves weights to `models/`)*

3. **Evaluate the Model:**
   `python src/evaluate.py`
   *(Generates Precision, Recall, and F1 scores, and saves reconstruction error plots to `results/`)*

---

## 🔄 Group Git Workflow Guide

To prevent code conflicts and lost work, our team follows a **Feature Branch Workflow**. Please adhere to these steps when contributing to the project:

### 1. Never work directly on the `main` branch.
The `main` branch should only contain working, tested code. 

### 2. Create a branch for your task.
Before starting new work, pull the latest changes and create a branch:
    ```
    git checkout main
    git pull origin main
    git checkout -b feature/your-feature-name
    ```
*(Use prefixes like `feature/`, `bugfix/`, or `docs/` for clarity).*

### 3. Commit your changes regularly.
Write clear, descriptive commit messages:
    ```
    git add .
    git commit -m "Add normalization logic to data_preprocessing.py"
    ```

### 4. Push and create a Pull Request (PR).
When your code is ready, push your branch to GitHub:
    ```
    git push origin feature/your-feature-name
    ```
Go to GitHub, open a Pull Request against the `main` branch, and tag at least one team member to review your code. Once approved, it will be merged into `main`.