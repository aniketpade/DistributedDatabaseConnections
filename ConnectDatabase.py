import pyodbc
import pandas


def db_1():
    connection_db_1 = pyodbc.connect('''DRIVER = {SQL Server Native});
                                        Server = 'db 1 server name'
                                        Trusted_connection = yes;''')
    cursor_db_1 = connection_db_1_cursor()
    return connection_db_1, cursor_db_1


def db_2():
    connection_db_2 = pyodbc.connect('''DRIVER = {SQL Server Native});
                                        Server = 'db 2 server name'
                                        Trusted_connection = yes;''')
    cursor_db_2 = connection_db_2_cursor()
    return connection_db_2, cursor_db_2
