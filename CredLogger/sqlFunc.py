import sqlite3

class SqlFunc:
    def __init__(self, db):
        self._connection = sqlite3.connect(str(db))
        self._cursor = self._connection.cursor()
        self.QueryOut = []

#input string like e.g. last="hello". this means column name, "=" and finally the string (Non string values will be converted to string). A "select * from 'table' WHERE 'kwargs'" clause will be executed without empty strings as args.
    def getInNotNull(self, table, **kwargs):
        SELECT = f"SELECT * FROM {table} WHERE"

        for i,key in enumerate(kwargs):
            if kwargs.get(val) != "":
                SELECT += " && ".join([key, kwargs.get(key)])
        SELECT += ";"

        self._cursor.execute(SELECT)
        self._connection.commit()
        self.QueryOut.append(self._cursor.fetchall())

    
    def lastQOut(self):
        return self.QueryOut[len(self.QueryOut)]