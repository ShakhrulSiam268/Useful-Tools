import pyodbc
import sys
import pandas as pd


class DBtoCSV:
    def __init__(self, server, Database, UID, PWD, tablename):
        self.server = server
        self.Database = Database
        self.UID = UID
        self.PWD = PWD
        self.tablename = tablename

    def connect_to_db(self):
        odbc_driver = '{ODBC Driver 17 for SQL Server}'
        native_driver = '{SQL Server Native Client 11.0}'
        driver = native_driver
        connection = None
        if sys.platform == 'linux':
            driver = odbc_driver
        else:
            driver = native_driver
        connection = pyodbc.connect(
            f"""Driver={driver};
            Server={self.server};
            Trusted_Connection=no;
            Database={self.Database};
            UID={self.UID};
            PWD={self.PWD};"""
        )
        return connection

    def get_columns(self):
        connection = self.connect_to_db()
        cursor = connection.cursor()
        table_name_query = f"select Column_name from INFORMATION_SCHEMA.COLUMNS where TABLE_NAME='{self.tablename}'"
        cursor.execute(table_name_query)
        data = cursor.fetchall()
        columns = []
        for d in data:
            columns.append(d[0])
        return columns

    def get_dataframe(self, save=True):
        connection = self.connect_to_db()
        cursor = connection.cursor()
        SQL_COMMAND = f"select * from {self.tablename}"
        cursor.execute(SQL_COMMAND)
        data = cursor.fetchall()
        rows = []
        for customer in data:
            row = []
            for item in customer:
                row.append(item)
            rows.append(row)
        columns = self.get_columns()
        data_df = pd.DataFrame(rows, columns=columns)
        if save:
            data_df.to_csv('output.csv', sep=',', encoding='utf-8', index=False)
            print('Database saved successfully.')
        return data_df




