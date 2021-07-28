import sqlite3

conn = sqlite3.connect('covid_19.db')
cursor = conn.cursor()
# conn.close();