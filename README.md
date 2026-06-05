# Learning GitHub Actions & Dependabot

This is a starter project to explore GitHub Actions CI/CD workflows and Dependabot dependency management.

## What's included:

- **`.github/workflows/ci.yml`**: A Python CI workflow that runs on every push/PR
  - Sets up Python 3.11
  - Installs dependencies
  - Runs tests (pytest)

- **`.github/dependabot.yml`**: Dependabot configuration
  - Monitors `requirements.txt` for Python package updates
  - Checks GitHub Actions for updates
  - Creates PRs weekly on Mondays

- **`requirements.txt`**: Python dependencies (requests, flask, pytest)

- **`main.py`**: A simple Flask app

## Next steps:

1. Create a new repo on GitHub
2. Push this code to GitHub
3. Enable Dependabot in repo settings
4. Watch for Dependabot PRs as dependencies update

## Learning notes:

- GitHub Actions workflows are YAML files in `.github/workflows/`
- Each workflow has `on:` (triggers), `jobs:`, and `steps:`
- Dependabot creates PRs when updates are available
- You control what gets merged (CI must pass first)
