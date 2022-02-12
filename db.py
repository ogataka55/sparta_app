import os

import psycopg2
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
                posts = cur.fetchall()
                return posts


def init_db():
    """データベースの初期化を行う関数"""
    with open('schema.sql', encoding="utf-8") as f:
        cursor_execute(f.read())


def get_all_posts():
    sql = "SELECT * FROM posts;"
    posts = cursor_execute(sql)
    return posts


def get_one_post(id):
    with get_connection() as conn:
        with conn.cursor() as cur:
            sql = "SELECT * FROM posts WHERE id=%(id)s;"
            params = {'id': id}
            cur.execute(sql, params)
            post = cur.fetchone()
            return post


def add_post(title, detail, img, link):
    with get_connection() as conn:
        with conn.cursor() as cur:
            # postsテーブルに挿入するSQL 値は後から
            sql = "INSERT INTO posts(title,detail,image,link) VALUES (%(title)s, %(detail)s, %(img)s, %(link)s);"
            params = {'title': title, 'detail': detail, 'img': img, 'link': link}
            cur.execute(sql, params)


def edit_post(id, n_title, n_detail, n_img, n_link):
    with get_connection() as conn:
        with conn.cursor() as cur:
            # postsテーブルを編集するSQL 値は後から
            sql = "UPDATE posts SET title=%(n_title)s, detail=%(n_detail)s, image=%(n_img)s, link=%(n_link)s WHERE " \
                  "id=%(id)s "
            params = {'id': id, 'n_title': n_title, 'n_detail': n_detail, 'n_img': n_img, 'n_link': n_link}
            cur.execute(sql, params)


def delete(id):
    with get_connection() as conn:
        with conn.cursor() as cur:
            sql = "DELETE FROM posts WHERE id=%(id)s;"
            params = {'id': id}
            cur.execute(sql, params)


if __name__ == '__main__':
    init_db()

    # print(init_db.__doc__)
