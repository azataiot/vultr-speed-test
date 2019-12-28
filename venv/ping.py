import pickle
import os
import subprocess
from pyzt import inputs,inputi
import re

os.system('azt')

with open('server_list.azd', 'rb') as server_addr:
    addr = pickle.load(server_addr)

# test_data = {
#     'first':{
#         'min':2334,
#         'avg':133,
#         'max':123123,
#         'stddev':21312
#     }
# }
ping_data = {

}

repeat = inputi('How many times should we test the connection?')

for each in addr:
    output = subprocess.check_output(
        ['ping', f'{each}', '-c', f'{repeat}'], universal_newlines=True)
    data = re.findall(r'round-trip min/avg/max/stddev =(.*?)ms', output)[0]
    ping_data[f'{each}']={}
    ping_data[f'{each}']['min'] = float(data.split('/')[0])
    ping_data[f'{each}']['avg'] = float(data.split('/')[0])
    ping_data[f'{each}']['max'] = float(data.split('/')[0])
    ping_data[f'{each}']['stddev'] = float(data.split('/')[0])


mins = []
for each in ping_data.keys():
    print(each,'------','MIN:',ping_data[f'{each}']['min'],'AVG',ping_data[f'{each}']['avg'])
    mins.append(ping_data[f'{each}']['min'])

print(f'Find the fastest node for current internet: {list(ping_data.keys())[mins.index(min(mins))]}')