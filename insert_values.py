from db import cursor, conn
import pandas as pd
import requests
import json
def inserUfValues(dados):
    # print(dados)
    sql = """
    insert into uf (nome, sigla) VALUES (?, ?);
    """

    for dado in dados['data']:
        # print(dado['state'], dado['uf'])
        cursor.execute(sql,(dado['state'], dado['uf']))
        conn.commit()
        print("uf {} salvo com sucesso".format(dado['uf']))

def insertInformacaoValues(data):
    sql = """
    insert into informacao (uf, cases, deaths,suspects,refuses,datetime) values (?,?,?,?,?,?)
    """
    cursor.execute(sql,(data['uf'], data['cases'], data['deaths'], data['suspects'],data['refuses'], data['datetime']))
    conn.commit()
    print(data['uf'], data['datetime'] + "salvo com sucesso")

def getDataFromUrl():
    dateRange = pd.date_range(start='02/1/2020', end='07/19/2021');
    for i in dateRange:
        dateCalenda = str(i).split(' ')[0].replace('-','')
        url = 'https://covid19-brazil-api.vercel.app/api/report/v1/brazil/{}'.format(dateCalenda)
        response = requests.request("GET", url,headers={})
        data = json.loads(response.text)
        for d in data['data']:
            if d is not None:
                insertInformacaoValues(d)