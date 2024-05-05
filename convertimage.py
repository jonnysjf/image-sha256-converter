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
    op = input('Deseja continuar: [Y] ou [N] ?')

    str_image = base64.b64encode(img) if op == 'Y' else print('Programa Finalizado...')

    opt = input('Imagem convertida, deseja salvar Hash em arquivo: [Y] ou [N] ?')


    saveFile(str_image, img) if opt == 'Y' else print('Programa Finalizado...')

def saveFile(hash, img):
    file_name= (f'hash_from_{img}.txt')
    with open(file_name,'a') as file_save:
        file_save.write(hash)

    print(f'Hash da Imagem {img}, salvo no arquivo: {file_save}')

def main():
    option = int(input('[1] Converter Imagem emm Hash \n[2] Converter Hash emm Imagem'))

    chash() if option == 1 else print('swds')

if __name__ == '__main__':
    main()


