# -*- coding: utf-8 -*-
print("Iniciando script...")
import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()
print("Bibliotecas carregadas")

DB_HOST = os.getenv("DB_HOST")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_PORT = os.getenv("DB_PORT", 5432)

print(f"Tentando conectar no host: {DB_HOST}...")

try:
    conn = psycopg2.connect(
        host=DB_HOST,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        port=DB_PORT,
    )
    print("Conexao com o banco realizada com sucesso!")
    conn.close()
except Exception as e:
    print("Erro ao conectar no banco:")
    print(e)
