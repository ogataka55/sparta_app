import os

import psycopg2 as psycopg2
from dotenv import load_dotenv

load_dotenv()


def get_connection():
    """コネクションを貼る関数"""
    dsn = os.environ.get("DATABASE_URL")
    return psycopg2.connect(dsn)


def cursor_execute(sql):
    """sqlを実行する関数 select文なら実行結果を返す"""
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(sql)
            if sql.split(" ")[0] == "SELECT":
                customers = cur.fetchall()
                return customers


def init_db():
    """データベースの初期化を行う関数"""
    with open('schema.sql', encoding="utf-8") as f:
        cursor_execute(f.read())


def get_all_customers():
    sql = "SELECT * FROM customers;"
    customers = cursor_execute(sql)
    return customers


if __name__ == '__main__':
    init_db()

    print(init_db.__doc__)
