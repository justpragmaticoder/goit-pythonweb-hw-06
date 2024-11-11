There are already commited migrations for the demonstration

### Install dependencies (3.10 python is used)
```bash
pip install -r requirements.txt
```

### Run docker compose

```bash
docker-compose up -d
```

### Delete c5972fcbaa30_initial_migration file

```bash
alembic revision --autogenerate -m "Initial migration"
```

```bash
alembic upgrade head
```

### Run my_select.py for demonstration
```bash
python my_select.py
```

or

```bash
python3 my_select.py
```