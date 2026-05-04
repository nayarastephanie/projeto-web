from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# arquivos estáticos (CSS)
app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

usuarios = []

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {"request": request}
    )

@app.post("/adicionar")
def adicionar(nome: str = Form(...)):
    usuarios.append(nome)
    return RedirectResponse(url="/usuarios", status_code=303)

@app.get("/usuarios", response_class=HTMLResponse)
def listar(request: Request):
    return templates.TemplateResponse(
        "usuarios.html",
        {"request": request, "usuarios": usuarios}
    )