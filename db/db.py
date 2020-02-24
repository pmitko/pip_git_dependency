from typing import Any, Tuple, Sequence, Optional, List, Dict


class Db(object):
    # autocommit=True is required in case of  multi statement SQLs (otherwise you'll end up with commands out of sync, ...)
    def __init__(self, host: str, user: str, password: str, name: str, preparedStatement: bool = True, autocommit: bool = True) -> None:
        self._connection = None  # make sure attribute exists also in case when connect ends with an exception
        self._cursor = None

    def __del__(self) -> None:
        self.close()

    @property
    def lastRowId(self) -> int:
        return self._cursor.lastrowid

    def close(self) -> None:
        if self._connection is not None and self._connection.is_connected():
            self._connection.close()

    def execute(self, sql: str) -> None:
        self._cursor.execute(sql)

    def executeMany(self, sql: str, params: [Tuple, List]) -> None:
        self._cursor.executemany(sql, params)

    def executePrepared(self, sql: str, params: [Tuple, List, Dict]) -> None:
        self._cursor.execute(sql, params)

    def fetchOne(self) -> Optional[Any]:
        return self._cursor.fetchone()

    def fetchAll(self) -> Sequence[Tuple]:
        return self._cursor.fetchall()

    def commit(self) -> None:
        self._connection.commit()

    def rollback(self) -> None:
        self._connection.rollback()
