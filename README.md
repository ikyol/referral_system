# Django API Referral System

## Installation

Before starting to use the project, make sure you have Python 3 and Poetry installed on your computer.

1. **Install Poetry**:

```bash
curl -sSL https://install.python-poetry.org | python3 -
```

2. **Clone the project**:

```bash
git clone git@github.com:ikyol/referral_system.git
cd referral_system
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

Postman collection link:

```bash
https://warped-water-548970.postman.co/workspace/New-Team-Workspace~13ba1d27-b7ad-4a10-8e5b-9d7f38389333/collection/34427856-885635f7-eed3-42d0-bede-24a060d4bb4f?action=share&creator=34427856
```

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

Also you can check all the API methods at http://localhost:8000/docs/.

First method to send verification code at http://localhost:8000/account/verification/
You should send POST request with body:
```bash
phone_number: +71234567901
```

with the verification code that u receive send POST request to http://localhost:8000/account/verify-code/
with body:
```bash
verification_code: 1234
```

Also you can use your invite code to invite other people at http://localhost:8000/account/activate-invite-code/
with body:
```bash
invite_code: VZawNz
```

Then you can check your profile at http://localhost:8000/account/profile/