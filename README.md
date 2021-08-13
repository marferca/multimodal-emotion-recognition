# Comparing supervised and unsupervised approaches to multimodal emotion recognition

This repository contains data and code that support the findings of the following article:

Fernández Carbonell, M., Boman, M., & Laukka, P. (submitted). Comparing supervised and unsupervised approaches to multimodal emotion recognition.

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
You are finally ready to run the Jupyter Notebooks and replicate the results.

## Results
### Supervised learning results
* Unimodal
    * Audio: [Modeling](https://github.com/marferca/multimodal-emotion-recognition/blob/main/3.supervised_learning/late_fusion/code/0_0_audio_modeling.ipynb) | [Feature importance](https://github.com/marferca/multimodal-emotion-recognition/blob/main/3.supervised_learning/late_fusion/code/0_1_audio_model_interpretation.ipynb)
    * Video: [Modeling](https://github.com/marferca/multimodal-emotion-recognition/blob/main/3.supervised_learning/late_fusion/code/1_0_video_modeling.ipynb) | [Feature importance](https://github.com/marferca/multimodal-emotion-recognition/blob/main/3.supervised_learning/late_fusion/code/1_1_video_model_interpretation.ipynb)
* Multimodal
    * Late fusion: [Modeling](https://github.com/marferca/multimodal-emotion-recognition/blob/main/3.supervised_learning/late_fusion/code/2_fusion_techniques.ipynb)
    * Early fusion: 
        * eGEMAPS + AUs: [Modeling](https://github.com/marferca/multimodal-emotion-recognition/blob/main/3.supervised_learning/early_fusion/code/early_fusion_modeling_egemaps_aus.ipynb) | [Feature interpretation](https://github.com/marferca/multimodal-emotion-recognition/blob/main/3.supervised_learning/early_fusion/code/model_interpretation_egemaps_aus.ipynb)
        * GEMAPS + AUs: [Modeling](https://github.com/marferca/multimodal-emotion-recognition/blob/main/3.supervised_learning/early_fusion/code/early_fusion_modeling_gemaps_aus.ipynb)

### Unsupervised learning results
* Traditional approach: [Before dimensionality reduction](https://github.com/marferca/multimodal-emotion-recognition/blob/main/4.unsupervised_learning/traditional_approach/code/0_multimodal_unsupervised_learning_before_dim_red.ipynb) | [After dimensionality reduction](https://github.com/marferca/multimodal-emotion-recognition/blob/main/4.unsupervised_learning/traditional_approach/code/2_multimodal_unsupervised_learning_after_dim_red.ipynb)
* Exploratory approach: You can interactively visualize the data and inspect the results [here](https://projector.tensorflow.org/?config=https://raw.githubusercontent.com/marferca/multimodal-emotion-recognition/main/4.unsupervised_learning/exploratory_approach/tf_embedding_projector/projector_config.json). 

## Citation

```bibtex
@{
}
```
