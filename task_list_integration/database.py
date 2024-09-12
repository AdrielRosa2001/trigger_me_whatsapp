from peewee import SqliteDatabase

# Criação da instância do banco de dados
db = SqliteDatabase('meu_banco.db')

def initialize_db():
    from models import Message  # Importação local para evitar importação circular
    db.connect()
    db.create_tables([Message], safe=True)
    print("Banco de dados inicializado e tabelas criadas.")

def close_db():
    if not db.is_closed():
        db.close()
        print("Conexão com o banco de dados fechada.")