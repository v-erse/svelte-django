# svelte + django

This is an app example for Svelte and Django.

The Svelte frontend uses Webpack (instead of rollup) for bundling.

We proxy our `/api` requests through to the Django backend using webpack's devserver.

It also uses [Faker](https://github.com/joke2k/faker) to generate fake name's and addresses for demonstration.

## How to use

Install the dependencies for the frontend...

```bash
cd frontend
npm install
```

...and the dependencies for the backend in a python virtual environment...

```bash
cd backend
python3 -m venv env
. env/bin/activate
pip3 install -r requirements.txt
```

...then start the frontend devserver...

```bash
npm run dev
```

...open another terminal to start the django server:

```bash
python manage.py runserver
```
