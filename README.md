## End-to-End-ML-Project

## creating virtual environment:

conda create -n mlproj python=3.8 -y

## Activate the environment:
conda activate mlproj

## requirements installation:
pip install -r requirements.txt

## Project Workflow:
1) update config.yaml (inside config directory)
2) update schema.yaml
3) update params.yaml (to initialize our model, add parameters in this file.)
4) update the entity
5) update the configuration manager in src config (configuration.py)
6) update the components
7) update the pipeline
8) update the main.py
9) update the app.py