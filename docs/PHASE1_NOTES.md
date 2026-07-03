# Phase 1 Notes

## Phase 1 Goal
Establish a reproducible baseline for anomaly detection on the KDD Cup 1999 dataset using an autoencoder trained on normal traffic only.

## Phase 1 Deliverables
- Repository structure for code, notebooks, data, and outputs
- Data dictionary for the KDD99 features
- Exploratory Data Analysis notebook
- Baseline preprocessing, training, and evaluation scripts
- Clear collaboration workflow for the team

## Working Assumptions
- The Phase 1 EDA workflow uses `data/raw/kddcup.data_10_percent_corrected` as its default raw dataset.
- The repository keeps `data/raw/kddcup.names` and `data/raw/training_attack_types` so schema loading and attack-family grouping remain reproducible.
- The baseline model trains on normal connections and uses reconstruction error as the anomaly score.
- The EDA notebook should be runnable from a fresh checkout with only the documented dependencies installed.

## Open Items
- Decide whether the final baseline uses TensorFlow or PyTorch.
- Define the anomaly threshold selection method for the first report draft.
- Record any preprocessing decisions that affect feature scaling or encoding.

## Team Checklist
- Keep documentation synchronized with code changes.
- Update the notebook and notes together when the dataset path or preprocessing assumptions change.
- Record results in `results/` only when they are meant to be shared.

## Suggested Phase 1 Milestone Order
1. Load and inspect the raw KDD99 data.
2. Confirm the feature names and data types.
3. Quantify class imbalance and duplicate records.
4. Build the preprocessing pipeline.
5. Train the first autoencoder baseline.
6. Evaluate reconstruction error on held-out data.
