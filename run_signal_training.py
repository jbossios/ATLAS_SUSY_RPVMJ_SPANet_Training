import os
import sys

if __name__ == '__main__':
  run_type = 'predict' # options: train, test, predict
  path = '/eos/atlas/atlascerngroupdisk/phys-susy/RPV_mutlijets_ANA-SUSY-2019-24/spanet_jona/SPANET_OptionFiles/'
  versions = [i for i in range(72, 92)]
  commands = []
  for version in versions:
    inpath = f'{path}v{version}/'
    for infile in os.listdir(inpath):
      if run_type == 'train':
        command = f'python3 train.py -of options_files/{infile} --random_seed 1 --gpus 1 > Log_v{version}_{run_type} 2>&1'
      elif run_type == 'predict':
        with open(f'options_files/{infile}', 'r') as opt:
          lines = opt.readlines()
          for line in lines:
            if 'testing' in line and 'h5' in line:
              h5_file = line.split(':')[1].replace(',' ,'').replace('"', '')
        command = f'python3 predict.py ./spanet_output/version_{version} ./signal_full_v{version}_output.h5 -tf{h5_file} --gpus > Log_v{version}_{run_type} 2>&1'
      else:
        print(F'ERROR: {run_type} not implemented yet, exiting')
        sys.exit(1)
      commands.append(command)
  command = ' && '.join(commands)
  command += ' &'
  print(command)
  os.system(command)
