from typing_extensions import Required
from fastapi import FastAPI, Request
from fastapi.params import Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import starlette.status as status
from starlette.responses import RedirectResponse, Response  

#creating a FastAPI object
app = FastAPI()  

#configuring the static, which serve static
app.mount("/static", StaticFiles(directory="static"), name="static")

#configuring the HTML pages
templates = Jinja2Templates(directory="templates")

#declaring urls
@app.get("/", response_class=HTMLResponse)
def index(request : Request):
    return templates.TemplateResponse("index.html", { "request" : request })

@app.get("/aboutus",response_class=HTMLResponse)
def about_us(request : Request):
    return templates.TemplateResponse("about_us.html",{"request":request})

@app.get("/3d_laser",response_class=HTMLResponse)
def laser_scanning_3d(request : Request):
    return templates.TemplateResponse("3d_laser.html",{"request":request})

@app.get("/details/{id}",response_class=HTMLResponse)
def details(request : Request, id):
    return templates.TemplateResponse("details.html",{"request":request, "id": id})

@app.get("/sum/{a}/{b}")
def sum(request : Request, a : int, b: int ):
    return templates.TemplateResponse("sum.html", {"request":request, "total": a + b})

@app.get("/register",response_class=HTMLResponse)
def register(request :Request):
    return templates.TemplateResponse("register.html",{"request":request})

@app.post("/register",response_class=HTMLResponse)
def post_register(request :Request,username : str = Form(...), password : str = Form(...)):
    #database -> inserting or updating, can be done POST request
    return templates.TemplateResponse("register.html",{"request":request,"uname" : username, "pswrd" : password})