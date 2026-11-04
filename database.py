import pymysql

class ConexaoMySQL:

    def __init__(self):
        self.host = "localhost"
        self.user = "root"
        self.password = ""
        self.database = "endereco"
        self.port = 3306
        self.conexao = None
        self.cursor = pymysql.cursors.DictCursor

def abrir(self):
    try:
        # Estabelece a conexão com o banco de dados MySQL usando os parâmetros fornecidos.
        self.conexao = pymysql.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database,
            port=self.port,
            cursorclass=pymysql.cursors.DictCursor,
        )

        # Retorna a conexão para ser utilizada em outras partes do código.
        return self.conexao

    except pymysql.MySQLError as erro:
        # Em caso de erro na conexão, imprime a mensagem de erro e retorna None.
        print(f"Erro ao conectar ao MySQL: {erro}")
        return None

# Método que fecha a conexão caso ela esteja aberta.
def fechar(self):
    if self.conexao and self.conexao.open:
        self.conexao.close()
    else:
        print("Nenhuma conexão aberta para fechar.")