import configparser

class ReadConfig:
    def read_config(self,file_name,section,option):
        cf=configparser.ConfigParser()
        cf.read(file_name,encoding='utf-8-sig')
        return eval(cf.get(section,option))

if __name__ == '__main__':
    print(ReadConfig().read_config('../CONFIG_file/api_config', 'SHEET', 'sheetName'))