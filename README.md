# jina_chat

minimal fullstack chat with jina and plantomini

# Quick start

In `platomini` folder:

## Setup environments

```
python -m venv venv
pip install -r requirements.txt
```

## Start backend

```
jina flow --uses flow.yml
```

## Start client

```
python client.py
```

# Test

```
pytest .\test\test_protocols.py
```
