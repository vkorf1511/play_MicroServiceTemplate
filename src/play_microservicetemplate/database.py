import os
import sqlite3
from datetime import datetime, timezone
from pathlib import Path
from uuid import uuid4


DATABASE_PATH = Path(
    os.environ.get(
        "BIRTHDAY_DB_PATH",
        Path(__file__).resolve().parents[2] / "data" / "birthdays.sqlite3",
    )
)


def save_birthday(value: str) -> dict[str, str]:
    DATABASE_PATH.parent.mkdir(parents=True, exist_ok=True)
    birthday_id = str(uuid4())
    timestamp = datetime.now(timezone.utc).isoformat()

    with sqlite3.connect(DATABASE_PATH) as connection:
        connection.execute(
            """CREATE TABLE IF NOT EXISTS birthdays (
                id TEXT PRIMARY KEY,
                timestamp TEXT NOT NULL,
                value TEXT NOT NULL
            )"""
        )
        connection.execute(
            "INSERT INTO birthdays (id, timestamp, value) VALUES (?, ?, ?)",
            (birthday_id, timestamp, value),
        )

    return {"id": birthday_id, "timestamp": timestamp, "value": value}


def get_latest_birthday() -> dict[str, str] | None:
    DATABASE_PATH.parent.mkdir(parents=True, exist_ok=True)

    with sqlite3.connect(DATABASE_PATH) as connection:
        connection.execute(
            """CREATE TABLE IF NOT EXISTS birthdays (
                id TEXT PRIMARY KEY,
                timestamp TEXT NOT NULL,
                value TEXT NOT NULL
            )"""
        )
        row = connection.execute(
            "SELECT id, timestamp, value FROM birthdays ORDER BY timestamp DESC LIMIT 1"
        ).fetchone()

    if row is None:
        return None

    return {"id": row[0], "timestamp": row[1], "value": row[2]}