CREATE DATABASE if not exists agenda;

USE agenda;

CREATE TABLE if not exists contatos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(255) NOT NULL,
    telefone VARCHAR(20) NOT NULL
);

select * from contatos;

truncate table contatos;