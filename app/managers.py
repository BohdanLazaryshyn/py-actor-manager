import sqlite3

from models import Actor


class ActorManager:
    def __init__(self) -> None:
        self._connection = sqlite3.connect("cinema.db3")
        self.table = "actors"

    def create(self, first_name_: str, last_name_: str) -> None:
        self._connection.execute(
            f"INSERT INTO {self.table} (first_name, last_name) VALUES (?, ?)",
            (first_name_, last_name_)
        )
        self._connection.commit()

    def all(self) -> list:
        actors_cursor = self._connection.execute(
            f"SELECT id, first_name,last_name FROM {self.table}")
        return [Actor(*row) for row in actors_cursor]

    def update(
            self,
            id_to_update: int,
            first_name_: str,
            last_name_: str) -> None:
        self._connection.execute(
            f"UPDATE {self.table} SET "
            "first_name = (?), "
            "first_name = (?)"
            "WHERE id = (?)",
            (first_name_, last_name_, id_to_update)
        )
        self._connection.commit()

    def delete(self, id_to_delete: int) -> None:
        self._connection.execute(
            f"DELETE FROM {self.table} "
            "WHERE id = (?)",
            (id_to_delete,)
        )
        self._connection.commit()
