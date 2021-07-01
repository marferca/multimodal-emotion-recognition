# Comparing supervised and unsupervised approaches to multimodal emotion recognition

This repository contains data and code that support the findings of the following article:

Fernández Carbonell, M., Boman, M., & Laukka, P. (submitted). Comparing supervised and unsupervised methods in multimodal emotion recognition.

## Reproducing the results
### Getting the code

You can download a copy of all the files in this repository by cloning the
[git](https://github.com/marferca/multimodal-emotion-recognition) repository:

    git clone https://github.com/marferca/multimodal-emotion-recognition


### Setting up a Python virtual environment
We use `conda` to create the virtual environment and manage project dependencies in isolation, but feel free to use any other similar tool. Run the following commands in the repository folder (where `requirements.txt` is located) to create a conda environment with the required packages.

Create a conda environment with Python 3.7 and pip:
```create environment
conda create -n mul-emo-recog python=3.7 pip
```
Activate the conda environment:
```activate environment
conda activate mul-emo-recog
```
Install the required packages from `requirements.txt`:
```install requirements
pip install -r requirements.txt
```

### Getting started
Before running any code you need to activate the conda environment:
```activate environment
conda activate mul-emo-recog
```
Launch JupyterLab:
```launch jupyter lab
jupyter lab
```
You are finally ready to run the Jupyter notebooks and replicate the results.

## Citation

```bibtex
@{
}
```
