# Contributing Guide

## Purpose
This repository uses a simple feature-branch workflow so the team can collaborate on data, modeling, and documentation without overwriting one another's work.

## Branch Workflow
1. Sync `main` before starting new work.
2. Create a short-lived branch for one task.
3. Commit in small, reviewable chunks.
4. Open a pull request against `main` when the task is ready.

Example:

```bash
git checkout main
git pull origin main
git checkout -b feature/eda-notebook
```

## Repository Rules
- Do not commit raw datasets, model artifacts, or generated results.
- Keep notebook filenames ordered so the workflow is easy to follow.
- Prefer clear commit messages that explain the change, not just the file name.
- Keep code, notebook prose, and figures reproducible from a clean clone.

## Notebook Guidelines
- Place exploratory work in `notebooks/`.
- Add markdown cells that explain the purpose of each major step.
- Use relative paths from the notebook location.
- Reset and rerun notebooks before merging to ensure they still execute cleanly.

## Pull Request Checklist
- Code runs from a fresh environment.
- Data paths are correct and documented.
- Large generated outputs are excluded from version control.
- Any new assumptions are captured in the phase notes or README.

## Need Help
If a change affects the dataset format, preprocessing assumptions, or model evaluation logic, update the supporting documentation in the same pull request.
