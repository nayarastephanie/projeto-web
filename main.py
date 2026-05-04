from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

app = FastAPI()

templates = Jinja2Templates(directory="templates")

# "Banco de dados" em memória
usuarios = []

# Página inicial (formulário + conteúdo)
@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# Recebe dados do formulário
@app.post("/adicionar")
def adicionar(nome: str = Form(...)):
    usuarios.append(nome)
    return RedirectResponse(url="/usuarios", status_code=303)

# Lista usuários
@app.get("/usuarios", response_class=HTMLResponse)
def listar(request: Request):
    return templates.TemplateResponse("usuarios.html", {
        "request": request,
        "usuarios": usuarios
    })