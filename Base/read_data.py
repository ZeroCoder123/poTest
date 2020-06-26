import yaml,os

def read_data(file_name):
    path_name = os.getcwd() + os.sep + "Data" + os.sep + file_name + ".yml"
    with open(path_name,'r',encoding='utf-8') as f:
        return yaml.load(f,Loader=yaml.FullLoader)