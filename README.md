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

To open a jupyter notebook on Kubeflow, follow these steps:

1. ssh -D 8090 lxplus.cern.ch
2.  google-chrome --proxy-server=socks5://127.0.0.1:8090
3. Go to https://ml.cern.ch
4. Create a notebook using 1 GPU and the following image: gitlab-registry.cern.ch/ai-ml/kubeflow_images/atlas-pytorch-gpu:0183442cdb7ad58434d6626b2ac6ff2befffa9a9

Get SPAnet:

```
cp -r /eos/atlas/atlascerngroupdisk/phys-susy/RPV_mutlijets_ANA-SUSY-2019-24/spanet_jona/SPANET_package_backup_notebook/SPANet .
cd SPANet/
``` 

The ```run_signal_training.py``` and ```copy_predictions.py``` scripts should be already on the copied SPANet version, but clone this repo if they need to be updated.

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
