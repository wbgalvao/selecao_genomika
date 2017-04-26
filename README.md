# Processo Seletivo Genomika
Resolução dos problemas propostos no processo de seleção para a vaga de estágio em bioinformática da Genomika.

## Problema 1
O primeiro desafio apresentado trata-se do processo de *genome assembly*. O problema apresentado deve ser resolvido através do descobrimento da menor superstring comum entre *reads* de um genoma. Esse problema é classificado como **NP-Completo**, ou seja, não existe uma solução eficiente para o mesmo. Desse modo, dentro do diretório `problema1` existem dois arquivos: `fragment_assembler.py` e `greedy_fragment_assembler.py`.

1. O comando `$ python3 fragment_assembler.py [arquivo_de_entrada.txt]` criará um arquivo `output.txt` contendo a menor superstring comum entre as strings presentes no arquivo de entrada (desde que não exista strings repetidas no input). Contudo, trata-se de uma solução lenta, baseada apenas na sobreposição de strings em ordem. O tempo de execução cresce exponencialmente a medida que o tamanho do arquivo de entrada cresce.
2. O comando `$ python3 greedy_fragment_assembler.py [arquivo_de_entrada.txt]` é uma solução mais performática, baseada em grafos de sobreposição de strings. Contudo, não há como certificar que o conteúdo do arquivo `output.txt` irá sempre conter a menor superstring comum, apesar de esse ser o caso na maioria das execuções.

Os dois scripts apresentados têm como base as aulas expostas no MOOC [Algoritmos para Sequenciamento de DNA](https://www.coursera.org/learn/dna-sequencing), apresentado através do [Coursera](https://www.coursera.org/).

## Problema 2
O segundo desafio apresentado trata-se de uma aplicação web, com backend em Python, para consultar a relação entre doenças e genes em um banco de dados local. A aplicação utiliza o framework *Flask* e o banco de dados *SQLite*, como proposto.

### Configurando ambiente para execução do projeto
1. **Instale o** [**SQLite**](https://www.sqlite.org/download.html).
  * Para sistemas operacionais baseados no Debian você pode usar o comando `$ sudo apt-get update && sudo apt-get install -y sqlite3 libsqlite3-dev`
2. **Crie um ambiente virtual para o projeto**
  * Utilize o [virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/en/latest/) para criar seu ambiente. Vá para o diretório do projeto e execute o comando `$ mkvirtualenv PhenoApp_env`
  * Instale as dependências do projeto: `$ pip3 install flask psycopg2`
    * Caso você encontre problemas com permissões, tente executar o comando acima utilizando o prefixo `$ sudo -H`
    
  ### Executando a aplicação
  1. No diretório raiz do projeto, crie o arquivo de banco de dados local: `$ touch local_phenodb.db`
  2. Crie a tabela `pheno_db` no seu banco de dados local. Para facilitar, utilize o arquivo `create_pheno_db.sql` em conjunto com o comando `sqlite3`: `$ sqlite3 local_phenodb.db < create_pheno_db.sql`
  3. Execute o script de sincronização de banco de dados `$ python3 update_local.py`
  4. Crie  uma instância da aplicação `$ python3 app.py`
  
A aplicação estará sendo executada no endereço **localhost:5000**.
