--テーブルがあったら削除する
DROP TABLE IF EXISTS customers;

--テーブルがなければ作る
CREATE TABLE IF NOT EXISTS customers (
    name TEXT,
    age INTEGER
);

--テストデータを挿入
INSERT INTO
    customers
VALUES
    ('Bob', 15),
    ('Tom', 57),
    ('Ken', 76)