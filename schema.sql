--テーブルがあったら削除する
DROP TABLE IF EXISTS customers;

--テーブルがなければ作る
CREATE TABLE IF NOT EXISTS posts (
    id SERIAL PRIMARY KEY NOT NULL,
    title VARCHAR(20),
    detail TEXT,
    image VARCHAR(50),
    link VARCHAR(50)
--    img_url TEXT

);