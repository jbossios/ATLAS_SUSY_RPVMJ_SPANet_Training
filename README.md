# Produce SPANet JSON files and submit training and evaluation jobs

## Create JSON files

Get Python3.8+

```
source Setup.sh
```

Check ```default_dict.py``` to make sure SPANet's settings are of your liking.

Set the following in ```create_json.files.py```:

- ```starting_network_version```: should be a version number never used before
- ```versions```: set the list of input versions (one JSON file will be produce for each input version)
- ```event_types```: set list of event types from ['partial', 'full'] where 'partial' means SPANet will use fully+partial recontructable gluinos, while 'full' only fully reconstructable gluinos.

Run ```create_json_files.py```

```
python create_json_files.py
```

Copy produced JSON files to the SPANET package on EOS with ```copy_jsons.py```. First, choose the ```versions``` than need to be copied and then run script:

```
python copy_jsons.py
```

## Submit training/evaluation jobs

**NOTE:** This step is currently ran in a Jupyter notebook from Kubeflow (do not forget to run ```kinit USERNAME``` before running to get EOS access).

Set the following in ```run_signal_training.py```:

- ```run_type```: 'train' or 'predict'
- ```versions```: list of SPANet network versions to run (should match JSON's versions)

Run:

```
python3 run_signal_training.py
```

Set ```versions``` in ```copy_predictions.py```:

- ```versions```: list of SPANet's predictions (i.e. versions) to copy (should match JSON's versions)

Run script in the following way:

```
python3 copy_predictions.py
```
