from db import cursor

def verifyItens():
    sql = "select * from uf;"
    cursor.execute(sql)
    print(cursor.fetchall())

def selectData():
    # Limitado a 10 devido a quantidade de dados
    sql = "SELECT * from informacao limit 10;"

    cursor.execute(sql)
    print(cursor.fetchall())