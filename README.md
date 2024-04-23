# Django API Referral System

## Installation

Before starting to use the project, make sure you have Python 3 and Poetry installed on your computer.

1. **Install Poetry**:
    ```bash
    curl -sSL https://install.python-poetry.org | python3 -
    ```
   
2. **Clone the project**:
   ```bash
   $ 
   $ 
   ```

3. **Install dependencies**:
   ```bash
   poetry install
   ```
   
4. **Set up the database:**:

Now you should make `.env` file

   ```bash
   $ touch .env
   ```
then, fill the fields in the `.env`

   ```txt
   SECRET_KEY=
   
   # Database
   DB_NAME=
   DB_USER=
   DB_PASSWORD=
   DB_PORT=
   ```

   ```bash
   python3 manage.py migrate
   ```

## Usage
To start the Django development server, run the following command:

   ```bash
   python3 shell
   python3 manage.py runserver
   ```
   or
   ```bash
   poetry run python3 manage.py runserver
   ```


This will start the development server at http://localhost:8000/.

To create the database tables, run the following command:

```bash
(venv)$ python manage.py migrate
```

You can access the Django admin panel at http://localhost:8000/admin/. To create a superuser account, run the following command and follow the prompts:

```bash
(venv)$ python manage.py createsuperuser
```