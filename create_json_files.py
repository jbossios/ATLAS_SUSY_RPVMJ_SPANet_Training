import os
import sys
import copy
import json
from default_dict import default_dict

input_files = [
    '/eos/atlas/atlascerngroupdisk/phys-susy/RPV_mutlijets_ANA-SUSY-2019-24/ntuples/tag/input/mc16e/signal/HighStats/PROD0/h5/v0/user.abadea.GGrpv2x3ALL_minJetPt50_minNjets6_maxNjets8_RDR_dr_v0.h5',
]

def create_json(input_file, network_version, evt_type, output_path):
    # Create output folder
    output_folder = f'{output_path}{network_version}/'
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    # Prepare dict to write
    final_dict = copy.deepcopy(default_dict)
    final_dict[f'training_file'] = f'{input_file}'
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
    out_path = '/eos/atlas/atlascerngroupdisk/phys-susy/RPV_mutlijets_ANA-SUSY-2019-24/spanet_jona/SPANET_OptionFiles/'
    starting_network_version = 96
    event_types = ['partial']  # options: partial, full
    # Do not modify (below this line)
    counter = starting_network_version
    for input_file in input_files:  # loop over input file versions
        for case in event_types:
            create_json(input_file=input_file, network_version=f'v{counter}', evt_type=case, output_path=out_path)
            counter += 1
    print('>>> ALL DONE <<<')
