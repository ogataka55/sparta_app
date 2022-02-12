--テーブルがあったら削除する
DROP TABLE IF EXISTS customers;

--テーブルがなければ作る
CREATE TABLE IF NOT EXISTS posts (
    id SERIAL PRIMARY KEY NOT NULL,
    title VARCHAR(20),
    detail TEXT,
    image VARCHAR(50)
--    img_url TEXT

);

----テストデータを挿入
--INSERT INTO
--    posts
--VALUES
--    (1, '確認テスト', '中尊寺 金色堂')