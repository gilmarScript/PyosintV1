#!/usr/bin/python3

import argparse
import requests.exceptions 
from resources.agentk import run
from resources.webagent import run_main
from sys import argv as argu
import resources.enumsub as subdom
import os



G = '\033[92m'  
Y = '\033[93m'  
B = '\033[36m'  
R = '\033[91m' 
W = '\033[0m'
L = "\033[90m"

def parse_arg():
    parser = argparse.ArgumentParser(epilog='\tExample: \r\npython3 ' + argu[0] + " ")
    parser._optionals.title = "OPTIONS"
    parser.add_argument("-m",'--module',help="Para especificar o módulo a ser usado ",required=True)
    parser.add_argument("-n",'--name' ,help="Nome de usuário ou nome de domínio ",required=True)
    parser.add_argument("-o",'--output' ,help="Nome do arquivo de saída ",default=None)
    parser.add_argument("-t",'--threads',help="Para definir o valor do fio ",type=int,default=50)
    parser.add_argument("-l",'--limit',help="To set the max limit for web crawling",default=30)
    parser.add_argument("-v","--verbose",help="Para habilitar verboso",nargs='?',default=False)
    parser.add_argument("-p",'--ports',help="Para definir as portas para enumeração de subdomínio{separar usando vírgulas eg: 80,443}")
    return parser.parse_args()

#````````````````````````````````````````````````````````````````````````````````````````

#````````````````````````````````````````````````````````````````````````````````````````
def main():
    agrument = parse_arg()
    
    module=agrument.module
    name = agrument.name
    output = agrument.output
    thread = agrument.threads
    limit = agrument.limit
    port = agrument.ports
    verbose = agrument.verbose

    if (module == "find"):
        run(username=name,output=output,threads=thread)
    elif (module == "crawl" or module == "scrap" or module == "web"):
        run_main(x=name,max=limit,filename=output)
    elif  (module == "enum" or module == "sub-domain"):
            subdom.main(domain=name,threads=thread,savefile=output,ports=port,verbose=verbose)
    else:
        print(f"\n {R} Module não Encontrado ")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"{Y}Interrupção de teclado encontrada Saindo do programa :) {W}")
        exit(0)
    except requests.exceptions.MissingSchema:
        print(f"{R}\n Esquema ausente. Talvez você sinta falta 'http://' ")
