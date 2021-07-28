from db import cursor

def createTableUf():
    sql = """
        create table if not exists uf(
            id integer primary key autoincrement not null,
            nome text not null,
            sigla text not null
        );
    """

    cursor.execute(sql)
    print("Tabela UF criada com sucesso")
    

def createTableInformacao():
    sql = """
    create table if not exists informacao(
        id integer primary key autoincrement not null,
        uf text not null,
        cases real not null,
        deaths real not null,
        suspects real not null,
        refuses real not null,
        datetime TIMESTAMP not null
    );
    """

    cursor.execute(sql)
    print("Tabela Informacao criada com sucesso")