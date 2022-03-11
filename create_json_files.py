import os
import sys
import copy
import json
from default_dict import default_dict

def create_json(input_path, input_version, network_version, evt_type, output_path):
  # Create output folder
  output_folder = f'{output_path}{network_version}/'
  if not os.path.exists(output_folder):
    os.makedirs(output_folder)
  # Prepare dict to write
  final_dict = copy.deepcopy(default_dict)
  for case in ['testing', 'training']:
    input_file_name = [h5_file for h5_file in os.listdir(f'{input_path}{input_version}') if 'h5' in h5_file and case in h5_file][0]
    final_dict[f'{case}_file'] = f'{input_path}{input_version}/{input_file_name}'
  final_dict[f'partial_events'] = False if evt_type=='full' else True
  # Write dict to output file
  output_file_name = f'{output_folder}signal_{network_version}_{evt_type}.json'
  if os.path.exists(output_file_name): # exit if output file exists
    print(f'ERROR: {output_file_name} already exists, exiting')
    sys.exit(1)
  with open(output_file_name, 'w') as ofile:
    json.dump(final_dict, ofile, indent=4)

if __name__ == '__main__':
  # Settings
  in_path = '/eos/atlas/atlascerngroupdisk/phys-susy/RPV_mutlijets_ANA-SUSY-2019-24/spanet_jona/SPANET_inputs/'
  out_path = '/eos/atlas/atlascerngroupdisk/phys-susy/RPV_mutlijets_ANA-SUSY-2019-24/spanet_jona/SPANET_OptionFiles/'
  starting_network_version = 72
  versions = [f'v{i}' for i in range(41,61)] # input versions
  event_types = ['partial'] # options: partial, full
  # Do not modify (below this line)
  counter = starting_network_version
  for version in versions: # loop over input versions
    for case in event_types:
      create_json(input_path=in_path, input_version=version, network_version=f'v{counter}', evt_type=case, output_path=out_path)
      counter += 1
  print('>>> ALL DONE <<<')
