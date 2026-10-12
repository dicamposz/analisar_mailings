import os
import pandas as pd
from pathlib import Path

version_analiser = "____________ | Analisar Mailing v1.0.0 | ____________"
archive_mailing = "nenhum arquivo escolhido"
archive_csv = "nenhum arquivo escolhido"
mounth = ...
user_option = 1
archive_opc = False

def verificar_telefones(archive_mailing, archive_csv, mounth, user_option):
    
    ...
    

while True:
    os.system("cls")
    print(version_analiser)

    print(f"\n\n[1] Escolher arquivo - {archive_mailing}\n[2] Processar arquivo\n[0] Sair")

    try:
        user_option = int(input("\nEscolha a opção: "))
    except ValueError:
        print("Digite apenas números!")
        input("\nDigite qualquer tecla para continuar: ")
        continue

    if user_option == 0:
        break
    
    match user_option:
        
        case 1:
            os.system("cls")
            print(version_analiser)
            
            while True:
                try:
                    while True:
                        archive_mailing = input("\n\nDigite o local do arquivo mailing: ")
                        verificador_extensao = archive_mailing[-4:]
                        if verificador_extensao != "xlsx":
                            print("\nEscolha um arquivo com estensão .xlsx")
                            continue
                        else:
                            archive_mailing = Path(archive_mailing)
                            break
                    break
                except:
                    print("\nArquivo invalido")
                    continue
        case 2:
            os.system("cls")
            print(version_analiser)
            
            if archive_mailing == "nenhum arquivo escolhido":
                print("\nNenhum mailing foi inserido!")
                input("\n\nDigite qualquer tecla para continuar: ")
                continue
            
            while True:
                try:
                    while True:
                        archive_csv = input("\nDigite o caminho do arquivo .csv: ")
                        verificador_extensao = archive_csv[-3:]
                        if verificador_extensao != "csv":
                            print("\nEscolha um arquivo com estensão .csv")
                            continue
                        else:
                            archive_csv = Path(archive_csv)
                            break
                    break
                except:
                    print("\nArquivo invalido")        
                    continue
            
            print(f"\nProcessando arquivo {archive_mailing} em {archive_csv}")
            verificar_telefones()
print("\n\nExiting...")