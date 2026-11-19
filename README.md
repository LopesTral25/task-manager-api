
# Task Manager API

API REST para gerenciamento de tarefas, desenvolvida com Python e FastAPI, utilizando SQLite para persistência de dados.

## Tecnologias utilizadas

- Python
- FastAPI
- SQLite
- Pydantic
- Pytest
- Uvicorn

## Funcionalidades

- Criar tarefas
- Listar todas as tarefas
- Buscar tarefa por ID
- Atualizar tarefas
- Excluir tarefas
- Validar dados de entrada
- Tratar erros de recursos não encontrados
- Testes automatizados das rotas

## Estrutura do projeto

```text
task-manager-api/
├── app/
│   ├── main.py
│   ├── database.py
│   └── routes/
│       └── tasks.py
├── tests/
│   └── test_main.py
├── .gitignore
├── pytest.ini
└── requirements.txt
```

## Instalação

Clone o repositório:

```bash
git clone https://github.com/LopesTral25/task-manager-api.git
```

Entre na pasta:

```bash
cd task-manager-api
```

Crie um ambiente virtual:

```bash
python -m venv .venv
```

Ative o ambiente virtual no Windows:

```powershell
.venv\Scripts\Activate.ps1
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

## Executando a API

Inicie o servidor:

```bash
python -m uvicorn app.main:app --reload
```

Acesse a documentação interativa:

http://127.0.0.1:8000/docs

## Executando os testes

Execute:

```bash
pytest -v
```

O projeto possui testes automatizados para verificar as principais operações da API.

## Autor

**Adelson Lopes**

GitHub: https://github.com/LopesTral25
