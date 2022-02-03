from datetime import datetime
from fastapi import FastAPI, Request, Cookie
from fastapi.params import Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import sqlite3
import starlette.status as status
from starlette.middleware.sessions import SessionMiddleware
from starlette.responses import RedirectResponse, Response
from fastapi.security import HTTPBasic, HTTPBasicCredentials


app = FastAPI()

security = HTTPBasic()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
def login1(request: Request):
    return templates.TemplateResponse("login1.html", {"request": request})


URLPath(path="/login1")


@app.get("/Products", response_class=HTMLResponse)
def Products(request: Request):
    return templates.TemplateResponse("login2.html", {"request": request})


URLPath(path="/login2")


@app.get("/newsfeed", response_class=HTMLResponse)
def newsfeed(request: Request):
    return templates.TemplateResponse("payment.html", {"request": request})


URLPath(path="/payment")


@app.get("/payment1", response_class=HTMLResponse)
def login(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})


URLPath(path="/payment1")


@app.get("/product", response_class=HTMLResponse)
def register(request: Request):
    return templates.TemplateResponse("register.html", {"request": request})


URLPath(path="/product")


@app.get("/product1", response_class=HTMLResponse)
def product1(request: Request):
    return templates.TemplateResponse("product1.html", {"request": request})


URLPath(path="/product1")


@app.get("/product2", response_class=HTMLResponse)
def product2(request: Request):
    return templates.TemplateResponse("product2.html", {"request": request})


URLPath(path="/product2")


@app.get("/product3", response_class=HTMLResponse)
def product3(request: Request):
    return templates.TemplateResponse("vegetables.html", {"request": request})


URLPath(path="/product3")


@app.get("/cart", response_class=HTMLResponse)
def cart(request: Request):
    return templates.TemplateResponse("cart.html", {"request": request})


URLPath(path="/cart")


@app.get("/about us", response_class=HTMLResponse)
def seeds(request: Request):
    return templates.TemplateResponse("fertilizer.html", {"request": request})


URLPath(path="/about us")

# return templates.TemplateResponse("index.html",{"request" : request, "message" : "succesfully added!!" })
