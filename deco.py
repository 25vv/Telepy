import requests
import os
from zipfile import ZipFile
import shutil

with open('Telepy_Test_pack_code.zip', 'wb') as f:
    f.write(requests.get('https://github.com/25vv/telepy-data/archive/refs/heads/main.zip', headers={'Authorization': "token " + os.environ['G_API']}).content)

with ZipFile('Telepy_Test_pack_code.zip', 'r') as zip:
    zip.extractall()

for f in os.listdir('telepy-data-main'):
    shutil.move(os.path.join('telepy-data-main' ,f), os.getcwd())
