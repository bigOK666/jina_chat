# jina_chat

minimal fullstack chat with jina and plantomini

![](https://github.com/shaomaiguanguan/jina_chat/blob/main/platominichatbot.gif)

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
