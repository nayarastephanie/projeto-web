# Projeto Web - Gerenciamento de Usuários

Este é um projeto web simples desenvolvido com FastAPI para gerenciar uma lista de usuários. Permite adicionar usuários e visualizar a lista existente.

## Funcionalidades

- Página inicial com formulário para adicionar usuários
- Lista de usuários cadastrados
- Interface web responsiva usando HTML e CSS

## Tecnologias Utilizadas

- **FastAPI**: Framework web para Python
- **Jinja2**: Motor de templates para renderização de HTML
- **Uvicorn**: Servidor ASGI para executar a aplicação
- **Python-multipart**: Para lidar com formulários multipart

## Instalação

1. Clone ou baixe o repositório para sua máquina.

2. Navegue até o diretório do projeto:
   ```
   cd projeto-web
   ```

3. Crie um ambiente virtual (se ainda não existir):
   ```
   python -m venv venv
   ```

4. Ative o ambiente virtual:
   - No Windows:
     ```
     venv\Scripts\activate
     ```

5. Instale as dependências:
   ```
   pip install -r requirements.txt
   ```

## Como Executar

1. Certifique-se de que o ambiente virtual está ativado.

2. Execute o servidor:
   ```
   uvicorn main:app --reload
   ```

3. Abra o navegador e acesse `http://127.0.0.1:8000` para ver a aplicação em funcionamento.

## Estrutura do Projeto

```
projeto-web/
├── main.py              # Arquivo principal da aplicação FastAPI
├── requirements.txt     # Dependências do projeto
├── static/
│   └── style.css        # Arquivos CSS para estilização
└── templates/
    ├── index.html       # Página inicial com formulário
    └── usuarios.html    # Página de listagem de usuários
```

