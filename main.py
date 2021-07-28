import requests
import json
from create_table import createTableInformacao, createTableUf
from insert_values import getDataFromUrl,inserUfValues
from verifica_dados import selectData, verifyItens
from ajustes_informacao import alterTable, updateInfos
from db import cursor, conn

url = "https://covid19-brazil-api.now.sh/api/report/v1"
headers = {}

response = requests.request("GET", url,headers=headers)

data = json.loads(response.text)
#  Criando as table as que serão utilizadas para guardar as informações
createTableUf()
createTableInformacao()


# Inserir valores dos estados brasileiros
inserUfValues(data)

# Verificar se os dados estão corretos
verifyItens()

# Buscando informações entre duas datas e inserindo todas as informações no banco
getDataFromUrl()

# Verificando se os dados estão corretos

selectData()

alterTable()
updateInfos()
# createTableDados()
# getDataFromUrl()
