# Prerequisites

Before you start, make sure you have the following installed on your system:

- **Python** (Download from [here](https://www.python.org/downloads/))
- **pip** (Usually comes with Python, but you can install/update it using `python -m ensurepip --default-pip`)
- **Virtual Environment** (Optional but recommended, install using `pip install virtualenv`)

### Setting Up a Django Project

Follow these steps to set up your Django project:

#### 1️⃣ Create a Virtual Environment
```sh
python -m venv .venv
```

#### 2️⃣ Activate the Virtual Environment
- **Windows:**
  ```sh
  .\.venv\Scripts\activate
  ```
- **Mac/Linux:**
  ```sh
  source .venv/bin/activate
  ```

#### 3️⃣ Install Django
```sh
pip install django
```

#### 4️⃣ Create a `requirements.txt` file (optional)
```sh
pip freeze > requirements.txt
```

#### 5️⃣ Start a New Django Project
```sh
django-admin startproject myproject
```
Alternatively, if you want to name your project `tweet`:
```sh
django-admin startproject tweet
```

#### 6️⃣ Navigate into the Project Directory
```sh
cd tweet
```

#### 7️⃣ Save Dependencies Again (optional)
```sh
pip freeze > requirements.txt
```

#### 8️⃣ Run Database Migrations
```sh
python manage.py makemigrations
python manage.py migrate
```

#### 9️⃣ Run the Development Server
```sh
python manage.py runserver
```

Your Django project should now be running! Open `http://127.0.0.1:8000/` in your browser to check.

