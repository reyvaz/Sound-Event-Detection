<br>

# Sound Event Detection

Builds an algorithm that automatically detects the occurrence of a sound event
and its onset.

An LSTM-based deep learning network that uses transformations of the mel
spectrogram achieves an event-based error rate of 0.06 and a F1-score of 0.97.

Files:

- [sed_main.ipynb](sed_main.ipynb) Notebook to run all algorithms and report
- [sed_utils.py](sed_utils.py) Contains functions required by the notebook above
- [meta](meta) Contains meta data for the audio files
- [sed_trained.h5](sed_trained.h5) The trained model in Keras
- [index.html](index.html) Edited html version of the `sed_main.ipynb` notebook
- [html_config.py](html_config.py) Configuration settings for the html exporter
- [README.md](README.md) This file

The audio data created for this project can be found
[here](https://zenodo.org/record/3236975#.XPSRDdNKjgt)

[**See the rendered notebook**](https://htmlpreview.github.io/?https://github.com/reyvaz/Sound-Event-Detection/blob/master/sed_main.ipynb)

[**See the rendered html report**](https://reyvaz.github.io/Sound-Event-Detection)

<br>
