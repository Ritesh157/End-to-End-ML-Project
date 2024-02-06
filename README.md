## End-to-End-ML-Project

## creating virtual environment:

conda create -n mlproj python=3.8 -y

## Activate the environment:
conda activate mlproj

## requirements installation:
pip install -r requirements.txt

## Project Workflow:
update config.yaml (inside config directory)
update schema.yaml
update params.yaml (to initialize our model, add parameters in this file.)
update the entity
update the configuration manager in src config (configuration.py)
update the components
update the pipeline
update the main.py
update the app.py