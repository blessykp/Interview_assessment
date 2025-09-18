# 🚀 Interview Assessment – FastAPI JWT Authentication

This project demonstrates a **FastAPI** application with **JWT Authentication** using OAuth2 Password Flow.  
It provides secure login, token generation, and protected API endpoints.

---

## 📌 Features
- 🔐 **JWT Authentication** with OAuth2 PasswordBearer  
- 🧑‍💻 Login endpoint (`/token`) that returns an access token  
- 👤 Protected user endpoint (`/users/me`)  
- 📚 Interactive API docs with **Swagger UI** (`/docs`) and **ReDoc** (`/redoc`)  
- 🗄️ Easily extendable to connect with real databases (MySQL/Postgres/etc.)  

---

## ⚙️ Tech Stack
- [FastAPI](https://fastapi.tiangolo.com/) – Web framework  
- [Uvicorn](https://www.uvicorn.org/) – ASGI server  
- [Python-JOSE](https://github.com/mpdavis/python-jose) – JWT handling  
- [Passlib](https://passlib.readthedocs.io/) – Password hashing  

---

## 🛠️ Installation

### 1. Clone repository
```bash
git clone https://github.com/blessykp/Interview_assessment.git
cd Interview_assessment
```

### 2. Create virtual environment
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

---

## ▶️ Running the App

Start the FastAPI app with Uvicorn:

```bash
uvicorn main:app --reload --port 8000
```

API will be available at:
```
http://127.0.0.1:8000
```

Swagger UI:
```
http://127.0.0.1:8000/docs
```

ReDoc:
```
http://127.0.0.1:8000/redoc
```

---

## 🔑 Authentication Flow

1. Go to `/docs`  
2. Click on **`POST /token`**  
3. Enter credentials:
   - **Username:** `test`  
   - **Password:** `mypassword` (or whichever user you add in `fake_users_db`)  
4. Copy the generated `access_token`  
5. Authorize Swagger by clicking **Authorize 🔓** → paste token with `Bearer <your_token>`  
6. Access **`GET /users/me`** – now it will return the current logged-in user 🎉  

---

## 🗄️ Database (Future Scope)

Currently, the project uses a **fake in-memory database**.  
You can replace it with MySQL/Postgres by integrating SQLAlchemy or Tortoise ORM.

Example for MySQL setup in `.env`:
```
DATABASE_URL=mysql+pymysql://user:password@localhost/db_name
```

---

## 📜 License
This project is for **educational and assessment purposes** only.  
