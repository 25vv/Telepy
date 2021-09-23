import urllib.request
import os
from zipfile import ZipFile
import shutil

opener = urllib.request.build_opener()
opener.addheaders = [('Authorization', 'token ' + os.environ['G_API'])]
urllib.request.install_opener(opener)
urllib.request.urlretrieve('https://github.com/25vv/telepy-data/archive/refs/heads/main.zip', "Telepy_Test_pack_code.zip")

with ZipFile('Telepy_Test_pack_code.zip', 'r') as zip:
    zip.extractall()

for f in os.listdir('telepy-data-main'):
    shutil.move(os.path.join('telepy-data-main' ,f), os.getcwd())
