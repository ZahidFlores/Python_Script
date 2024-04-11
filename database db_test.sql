create database db_test
use db_test

CREATE TABLE users (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), age INT);
INSERT INTO users (name, age) VALUES ('John', 30), ('Alice', 25), ('Bob', 35);

select * from users;