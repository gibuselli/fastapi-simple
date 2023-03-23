from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()

templates = Jinja2Templates(directory="templates")

@app.get("/", response_class="templates")
def pagina_inicial(request: Request):
    dados = {
        "pagina": "Página Inicial!"
    }
    
    return templates.TemplateResponse(
        "pagina.html",
        {"request": request, "dados": dados}
    )
    
    
@app.get("/page/{page_name}", response_class=HTMLResponse)
def pagina_dinamica(request: Request, page_name: str):
    dados = {
        "pagina": nome_da_pagina
    }
    
    return templates.TemplateResponse(
        "pagina.html",
        {"request": request, "dados": dados}
    )