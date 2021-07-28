from db import cursor, conn

def alterTable():
    sql = "ALTER table informacao add id_uf int references uf;"
    cursor.execute(sql)
    print("Coluna id_uf adicionada com sucesso")

def updateInfos():
    sql = "SELECT id, sigla from uf;"
    cursor.execute(sql)

    ufs = cursor.fetchall()

    for uf in ufs:
        # print(i[0], i[1])
        sql = "UPDATE informacao set id_uf = ? where uf = ?;"
        cursor.execute(sql,(uf[0], uf[1]))
        print("id_uf {} salvo com sucesso".format(uf[1]))
    conn.commit()