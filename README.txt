README - Script de Modificação de Metadados

Descrição
Este script foi desenvolvido para modificar metadados em massa dos arquivos em um diretório especificado. Ele automatiza o processo de alteração de datas de ultima modificação dos arquivos para seu valor original.

Obs: Script não funciona em arquivos TXT.

Como funciona
Com a ajuda da ferramenta Exiftool, todos os arquivos do diretório são scaneados e a partir disso um arquivo .txt é criado com todas os metadados dos arquivos, incluindo sua data de modificação original. 
Uma das funcões do script é obter essa informação, armazena-la em dicionário, para envia-las posteriormente a um arquivo JSON. Este que terá como chave o nome do arquivo e em seu valor as informações coletadas através dos metadados.

O próximo passo é a exclusão dos .txt`s criados pelo o Exiftool, por isso, é importante utilizar o script "Locate_txt.py" em pastas que você não souber se existem .txt`s ou não, pois o uso do script excluirá eles caso existam.

Após isso, os metadados dos arquivos serão modificados.
