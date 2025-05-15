import os
import oracledb
import json
import serial
from datetime import datetime

# Conexão com banco SQLite
conn = oracledb.connect(
     user='rm565606',
     password="fiap25",
     dsn='oracle.fiap.com.br:1521/ORCL')
cursor = conn.cursor()

# Criando as tabelas 
cursor.execute("""
CREATE TABLE IF NOT EXISTS FAZENDA (
    id_fazenda INTEGER PRIMARY KEY,
    nome_fazenda TEXT,
    loc_fazenda TEXT,
    area_plantio FLOAT,
    unidade_medida_area TEXT
);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS CULTURAS (
    id_cultura INTEGER PRIMARY KEY,
    id_fazenda INTEGER,
    nome_cultura TEXT,
    tipo_cultura TEXT,
    area_cultura FLOAT,
    data_plantio TEXT,
    data_colheita TEXT,
    status_cultura TEXT,
    FOREIGN KEY(id_fazenda) REFERENCES FAZENDA(id_fazenda)
);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS SENSOR_PH (
    id_senso_PH INTEGER PRIMARY KEY,
    id_cultura INTEGER,
    PH_registrado FLOAT,
    valor_PH FLOAT,
    variacao_PH FLOAT,
    data_hora TEXT,
    status_sensor TEXT,
    loc_sensor TEXT,
    FOREIGN KEY(id_cultura) REFERENCES CULTURAS(id_cultura)
);
""")

conn.commit()


# Função para inserir dados
def inserir_sensor_ph(id_cultura, valor_PH, variacao_PH, status_sensor, loc_sensor):
    data_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cursor.execute("""
        INSERT INTO SENSOR_PH (id_cultura, PH_registrado, valor_PH, variacao_PH, data_hora, status_sensor, loc_sensor)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (id_cultura, valor_PH, valor_PH, variacao_PH, data_hora, status_sensor, loc_sensor))
    conn.commit()

# Função para consultar dados
def consultar_sensores_ph():
    cursor.execute("SELECT * FROM SENSOR_PH")
    for linha in cursor.fetchall():
        print(linha)

# Função para atualizar os dados
def atualizar_ph(id_senso_PH, novo_valor_PH):
    cursor.execute("""
        UPDATE SENSOR_PH
        SET valor_PH = ?, PH_registrado = ?
        WHERE id_senso_PH = ?
    """, (novo_valor_PH, novo_valor_PH, id_senso_PH))
    conn.commit()

# Função para remover dados
def remover_sensor_ph(id_senso_PH):
    cursor.execute("DELETE FROM SENSOR_PH WHERE id_senso_PH = ?", (id_senso_PH,))
    conn.commit()