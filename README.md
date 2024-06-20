# Sistema de Gerenciamento de Produtos com Flask e SQLAlchemy
Este projeto utiliza Flask como framework web para Python e SQLAlchemy para interação com um banco de dados SQLite. Ele permite o gerenciamento básico de produtos, incluindo adição, edição, e exclusão de registros.

# Estrutura do Projeto
app.py: Arquivo principal que inicializa a aplicação Flask, configura a conexão com o banco de dados SQLite, e define as rotas principais.

controllers/routes.py: Módulo que contém as rotas da aplicação Flask, responsáveis por manipular requisições HTTP e interagir com o banco de dados.

models/database.py: Arquivo que define a estrutura do banco de dados utilizando SQLAlchemy. Inclui a definição da classe Produto que mapeia para a tabela produto.

views/: Diretório que contém os templates HTML para renderização das páginas web.

static/: Diretório para arquivos estáticos como CSS, JavaScript, imagens, etc.

# Funcionalidades
Adicionar Produto: Permite adicionar novos produtos através de um formulário web.

Editar Produto: Permite editar os detalhes de um produto existente.

Excluir Produto: Permite excluir um produto da base de dados.

Listar Produtos: Apresenta todos os produtos cadastrados em uma tabela com opções de edição e exclusão.
