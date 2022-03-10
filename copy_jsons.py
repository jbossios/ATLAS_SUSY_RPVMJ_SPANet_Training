import os

if __name__ == '__main__':
  eos_in = '/eos/atlas/atlascerngroupdisk/phys-susy/RPV_mutlijets_ANA-SUSY-2019-24/spanet_jona/SPANET_OptionFiles/'
  eos_out = '/eos/atlas/atlascerngroupdisk/phys-susy/RPV_mutlijets_ANA-SUSY-2019-24/spanet_jona/SPANET_package_backup_notebook/SPANet/options_files/'
  versions = [f'v{i}' for i in range(91,92)] # input versions
  commands = []
  for version in versions:
    option_file = list(os.listdir(f'{eos_in}{version}/'))[0]
    command = f'cp {eos_in}{version}/{option_file} {eos_out}'
    commands.append(command)
  command = ' && '.join(commands)
  command += ' &'
  print(command)
  os.system(command)
