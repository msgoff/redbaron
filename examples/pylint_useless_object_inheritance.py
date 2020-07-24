from redbaron import RedBaron
from file_utils import listfiles
from file_utils import read_file
from sys import argv

project_path = argv[1]

for file_name in listfiles(project_path,'.py'):
    source_code = read_file(file_name)
    red = RedBaron(source_code)
    resp = red.find_all('ClassNode')
    while resp:
            if resp[0].inherit_from.find('namenode',value='object'):
                print(file_name)
                print(resp[0].name)
            resp.pop(0)
