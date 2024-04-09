import os
import glob
import csv

def locateTxt(directory, directory_csv):
    for path, subdirs, files in os.walk(directory):
        for file in glob.glob(os.path.join(path, '*.txt')):
            with open(directory_csv, 'a') as csvfile:
                csv.writer(csvfile, delimiter=',').writerow([f'{file}',],)
            print(file)
    if subdirs == True:
        for subdir in subdirs:
            subdirectory = os.path.join(path, subdir)
            print(subdirectory)
            for path, subdirs, files in os.walk(subdirectory):
                for file in glob.glob(os.path.join(path, '*.txt')):
                    with open(directory_csv, 'a') as csvfile:
                        csv.writer(csvfile, delimiter=',').writerow([f'{file}',])
                    print(file)

locateTxt(input('Insira o diretorio: '),
          input('insira o caminho do csv: '))