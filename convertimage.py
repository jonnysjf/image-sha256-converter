import hashlib as hs
import base64
import glob
from pathlib import Path

def chash():

    print('Lista de imagem: \n')
    mypath = './img/'
    list_file = Path(mypath).glob("*.jpg")
    list_file = sorted(list_file)

    for i, file in enumerate(list_file):
        print(f'[{i}]\t{file.name}')

    img = input('Selecione a imagem: \n')
    
    print(f'Imagem selecionada: {list_file[i].name}\n')
    op = int(input('Deseja continuar:\n[1] SIM\n[2] NAO\n'))

    str_image = base64.b64encode(img) if op == "Y" else print('Programa Finalizado...')

    opt = int(input('Imagem convertida, deseja salvar Hash em arquivo:\n[1] SIM\n[2] NAO\n'))
    img_name = str(list_file[i].name)

    saveFile(str_image, img_name) if opt == 1 else print('Programa Finalizado...')

def saveFile(hash, img_name):
    file_name= (f'hash_from_{img_name}.txt')
    print(file_name)
    file_save =  open(file_name,'a')
    file_save.write(str(hash))

    print(f'Hash da Imagem {img_name}, salvo no arquivo: {file_name}')

def main():
    option = int(input('[1] Converter Imagem emm Hash \n[2] Converter Hash emm Imagem'))

    chash() if option == 1 else print('swds')

if __name__ == '__main__':
    main()


