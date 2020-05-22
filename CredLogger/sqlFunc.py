import sqlite3

class SqlFunc:
    def __init__(self, db):
        self._connection = sqlite3.connect(str(db))
        self._cursor = self._connection.cursor()


#input string like e.g. last="hello". this means column name, "=" and finally the string (Non string values will be converted to string). A "select * from 'table' WHERE 'kwargs'" clause will be executed without empty strings as args.
    def getNotNullStr(self, table, **kwargs):
        SELECT = "SELECT * FROM {str(table)} WHERE "
        ValidArgs = []

        for i in kwargs:
            if i != "" | None:
                ValidArgs.append(str(i))

        SELECT += " && ".join(str([ValidArgs, ";"]))

        self._cursor.execute(SELECT)
        return str(self._cursor.fetchall())