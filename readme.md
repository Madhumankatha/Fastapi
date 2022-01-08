pip install 

Jinja2  - HTML RENDERING ENGINE
uvicorn - APP SERVER
fastapi - WEB BASED FRAMEWORK BASED PYTHON
python-multipart - HANDLING FILE UPLOADS

Create Project Structure

static -> css, js, images
templates -> html pages
app.py -> main python program
app_db.db -> database file (SQLite) (creating later)

TO Run Server

$ uvicorn filename:object_name

ex:
$ uvicorn app:app


Open the url ->  http://127.0.0.1:8000

Types of URL:

base url : http://127.0.0.1:8000

absolute url:
http://127.0.0.1:8000/details/1 -> Path variables

Query Parameters
http://127.0.0.1:8000/details/1&pageno=1&pagesize=10

http://127.0.0.1:8000/addToCart/12 -> add product id 12 -> cart
http://127.0.0.1:8000/addToCart/7 -> add product id 7 -> cart
http://127.0.0.1:8000/addToCart/5 -> add product id 5 -> cart

http://127.0.0.1:8000/cart/ -> fetch all the products like price, qty, product name

To Handle The Post request:

GET, POST -> http://127.0.0.1:8000/Regsiter

Form Validation

input[type="email"]
required
pattern="^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,}$"
type="password"

Swagger UI:
http://127.0.0.1:8000/docs