import os
import subprocess
import glob
import re
import json

def extract_exif(directory):
    
    for path, subdirs, files in os.walk(directory):
        for file in files:
            full_file_path = os.path.join(path, file)
            full_file_path = full_file_path.encode(encoding="utf-8")
            exiftool_command = [r'[Insira o destino de seu arquivo Exiftool de nome exiftool.exe]', '-w', 'txt', full_file_path]
            subprocess.run(exiftool_command)
    if subdirs == True:
        for subdir in subdirs:
            subdirec = os.path.join(path, subdir)
            for path, subdirs, files in os.walk(subdirec):
                for file in files:
                    full_file_path = os.path.join(path, file)
                    full_file_path = full_file_path.encode(encoding="utf-8")
                    exiftool_command = [r'[Insira o destino de seu arquivo Exiftool de nome exiftool.exe]', '-w', 'txt', full_file_path]
                    subprocess.run(exiftool_command)

def modification_time(directory, destination_path):
    # Verificar se o arquivo JSON existe
    json_file_path = os.path.join(destination_path, 'MODIFICATIONTIME.json')
    if os.path.exists(json_file_path):
        # Carregar o JSON existente
        with open(json_file_path, 'r', encoding="UTF-8") as json_file:
            json_data = json.load(json_file)
    else:
        # Criar um novo JSON vazio
        json_data = {}

    for path, subdirs, files in os.walk(directory):
        for file in glob.glob(os.path.join(path, '*.txt')):
            file_name = os.path.basename(file.replace('.txt', ''))
            modify_date_lines = set()
            file_modify_date_lines = set()
            with open(file, 'r', encoding="ISO-8859-1") as f:
                for line in f:
                    if line.startswith('Modify Date'):
                        modify_date_lines.add(line)
                    if line.startswith('File Modification Date/Time'):
                        file_modify_date_lines.add(line)
            if modify_date_lines:
                for line in modify_date_lines:
                    separator = line.split()
                    if len(separator) >= 1:
                        arg1 = separator[3].replace(':', '/')
                        arg2 = separator[4]
                        # Adicionar uma nova entrada ao JSON
                        json_data[file_name] = f"{arg1} {arg2}"
            elif file_modify_date_lines:
                for line in file_modify_date_lines:
                    separator = line.split()
                    if len(separator) >= 1:
                        arg1 = separator[4].replace(':', '/')
                        arg2 = separator[5]
                        # Adicionar uma nova entrada ao JSON
                        json_data[file_name] = f"{arg1} {arg2}"
    if subdirs == True:
        for subdir in subdirs:
            subdirec = os.path.join(path, subdir)
            for path, subdirs, files in os.walk(subdirec):
                    for file in glob.glob(os.path.join(path, '*.txt')):
                        file_name = os.path.basename(file.replace('.txt', ''))
                        modify_date_lines = set()
                        file_modify_date_lines = set()
                        with open(file, 'r', encoding="ISO-8859-1") as f:
                            for line in f:
                                if line.startswith('Modify Date'):
                                    modify_date_lines.add(line)
                                if line.startswith('File Modification Date/Time'):
                                    file_modify_date_lines.add(line)
                        if modify_date_lines:
                            for line in modify_date_lines:
                                separator = line.split()
                                if len(separator) >= 1:
                                    arg1 = separator[3].replace(':', '/')
                                    arg2 = separator[4]
                                    # Adicionar uma nova entrada ao JSON
                                    json_data[file_name] = f"{arg1} {arg2}"
                        elif file_modify_date_lines:
                            for line in file_modify_date_lines:
                                separator = line.split()
                                if len(separator) >= 1:
                                    arg1 = separator[4].replace(':', '/')
                                    arg2 = separator[5]
                                    # Adicionar uma nova entrada ao JSON
                                    json_data[file_name] = f"{arg1} {arg2}"

    # Escrever o JSON final de volta no arquivo JSON
    with open(json_file_path, 'w', encoding="UTF-8") as json_file:
        json.dump(json_data, json_file, ensure_ascii=False, indent=4)


def remove_txt(directory):
        for path, subdirs, files in os.walk(directory):
            for file in glob.glob(os.path.join(path, '*.txt')):
                os.remove(file)
            if subdirs == True:
                for subdirectory in subdirs:
                    subdirec = os.path.join(path, subdirectory)
                    for path, subdirs, files in os.walk(subdirec):
                        for file in glob.glob(os.path.join(path, '*.txt')):
                            os.remove(file)

def change_metadatas(json_file_path, directory):
    # Ler o conteúdo do arquivo JSON
    with open(fr"{json_file_path}\MODIFICATIONTIME.json", 'r', encoding="UTF-8") as json_file:
        json_data = json.load(json_file)

    for path, _, files in os.walk(directory):
        for file in files:
            file_name = os.path.basename(file)
            file_name, file_extension = os.path.splitext(file_name)
            file_name_without_extension = file_name
            # Verificar se o nome do arquivo existe como chave no JSON
            if file_name_without_extension in json_data:
                file_name = file_name_without_extension 
                new_modification_time = json_data[file_name]
                file_path = os.path.join(path, file)
                # Utilizar o subprocesso para alterar a data de modificação do arquivo
                try:
                    subprocess.run(["powershell", f"cd '{path}'; $arquivo=(gi '.\\{file}'); $data='{new_modification_time}'; $arquivo.LastWriteTime=$data"], shell=True)
                except Exception as e:
                    print(f"Erro ao alterar a data de modificação do arquivo {file_name}: {e}")
        if _ == True:
            for subdirectory in _:
                subdirec = os.path.join(path, subdirectory)
                for path, _, files in os.walk(subdirec):
                    for file in files:
                        file_name = os.path.basename(file)
                        file_name, file_extension = os.path.splitext(file_name)
                        file_name_without_extension = file_name
                        # Verificar se o nome do arquivo existe como chave no JSON
                        if file_name_without_extension in json_data:
                            file_name = file_name_without_extension 
                            new_modification_time = json_data[file_name]
                            file_path = os.path.join(path, file)
                            # Utilizar o subprocesso para alterar a data de modificação do arquivo
                            try:
                                subprocess.run(["powershell", f"cd '{path}'; $arquivo=(gi '.\\{file}'); $data='{new_modification_time}'; $arquivo.LastWriteTime=$data"], shell=True)
                                print(f"Data de modificação do arquivo {file_name} alterada para {new_modification_time}")
                            except Exception as e:
                                print(f"Erro ao alterar a data de modificação do arquivo {file_name}: {e}")
                    
# Extrair os metadados dos arquivos
extract_exif(input('Insira aqui o caminho do diretório dos arquivos que terão os metadados substituídos: '))

# Gerar o arquivo MODIFICATIONTIME.txt e extrair as datas de modificação
modification_time(input('Repita o endereço: '), input('Insira o endereço de destino do arquivo MODIFICATIONTIME (não pode ser o mesmo): '))

# Remover arquivos TXT
remove_txt(input('(Exclusão de TXTs criados) Repita o caminho do diretório dos arquivos que terão os metadados substituídos: '))

# Alterar metadados
change_metadatas(input('Insira o diretório onde está o .json: '),
                 input('Insira o diretório que terão os metadados mudados: '))
