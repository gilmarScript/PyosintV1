<h3><p align="center">gilmarscript</p></h3>

<h1 align="center">
 PyosintOffical
 </h1>
 
 <h4 align='center'>Enumeração de subdomínio, Web scraping e localização de nomes de usuário como scripts de automação escritos em python
<br></h4>

<details>
  <summary><h3>Informações breves: </h3></summary>

A principal funcionalidade deste programa foi dividida em 3 partes <br>
 * Find - Módulo para pesquisar nomes de uso formam uma lista de <b><i>326</i></b> websites
 * Scrap - Para desfazer um site para extrair todos os links de um determinado site e armazená-lo em um arquivo
 * Enum - Para automatizar a busca de subdomínios de um determinado domínio de diferentes serviços

 No módulo Scrap, os resultados são armazenados automaticamente na pasta <i> output/web </i> com o endereço IP do site como o nome do arquivo <br><br>
 Os serviços usados são<i> <b> Virus Total,PassiveDns,CrtSearch,ThreatCrowd</i></b><br>

 <details>
  <summary><h3>API: </h3></summary>
 <details>
 <b> Enum </b> módulo uma chave Api de <b>Virus total</b> que você pode obter de ir <a href="https://www.virustotal.com/gui/sign-in"> Aqui </a><br>
 
<img src = "https://github.com/d8rkmind/datacontainer/blob/main/data/pictures/mceclip0.png" width=1080p>
<img src = "https://github.com/d8rkmind/datacontainer/blob/main/data/pictures/Untitled.png" width=1080p>

<b>Paste</b> the key  inside api.json file:

<img src ="https://raw.githubusercontent.com/d8rkmind/datacontainer/main/data/pictures/Screenshot%20at%202021-09-16%2016-07-42.png" width=1080p>

<i> * se este passo não for feito, o total de vírus pode bloquear o seu pedido</i>
  
  <details>
  <summary><h3>Manual de instrução</h3></summary> 
   
   A seguir estão os subcomandos que funcionam este programa<br>

Arguments |Shot<br>form |Long<br>form| Functionality
----------|-- | ----|---------
 Name| -n| --name| Para especificar o nome de domínio ou nome de usuário a ser usado
 Module| -m| --module| Para especificar qual módulo usar
 Output | -o| --output| Para especificar o nome do arquivo de saída
 Thread | -t| --threads | Para especificar o número de threads a serem usados<br> <i> [ Não aplicável ao rastreamento da Web ] </i> 
  Limit| -l | --limit| para especificar o valor máximo de URLs da Web a serem rastreados<br><i> [Aplicável apenas ao rastreamento da Web ] </i>
 Verbose| -v| --verbose| Para habilitar o modo detalhado <br><i>[ Aplicável apenas à Enumeração ]</i>
 Ports| -p| --ports| Para especificar as portas a serem verificadas<br><i> [ Aplicável apenas à Enumeração ]</ii>
 Help | -h| --help| Para Mostrar as opções de ajuda
 <br>
   
   
# Instalação

````
git clone https://github.com/jovemsigilosodobembr/PyosintOffical.git
cd 
PyosintOffical

pip3 install -r requirements.txt  
````
   
  ###### Linux commands:

# Uso:

```
python3 pyosint.py [OPTIONS]
```


 ``` 
 python3 pyosint.py -m find -n exampleuser               <-- Username-caçar
 
 python3 pyosint.py -m scrap -n http://scanme.nmap.org   <-- Sucatando usando bot
 
 python3 pyosint.py -m enum -n google.com                <-- Enumeração de subdomínio
 ``` 
   
Visite o meu canal: 
