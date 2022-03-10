import os
import sys

if __name__ == '__main__':
  run_type = 'train' # options: train, test, predict
  path = '/eos/atlas/atlascerngroupdisk/phys-susy/RPV_mutlijets_ANA-SUSY-2019-24/spanet_jona/SPANET_OptionFiles/'
  versions = [i for i in range(72, 92)]
  commands = []
  for version in versions:
    inpath = f'{path}v{version}/'
    for infile in os.listdir(inpath):
      if run_type == 'train':
        command = f'python3 train.py -of options_files/{infile} --random_seed 1 --gpus 1 > Log_v{version}_{run_type} 2>&1'
      else:
        print(F'ERROR: {run_type} not implemented yet, exiting')
        sys.exit(1)
      commands.append(command)
  command = ' && '.join(commands)
  command += ' &'
  print(command)
