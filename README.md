# Telesend
use it to send message to all of your private chats in telegram.

## Telegram API
it needs an api_id and an api_hash. you can go to [https://my.telegram.org/auth](https://my.telegram.org/auth) and create a new app. Then copy api_id and api_hash to the program.

## Delay:
be aware that sending message to a huge number of chats can be recognized as abuse. so you can add delay time to avoid that a little. if you have N chats and you set the delay to D, it takes about N * D seconds to send everybody the message.

## How to use
### clone the repo:
$```git clone https://github.com/hayatisaeed/Telesend.git```

### install virtualenv:
virtualenv: $```pip install virtualenv```

### change your directory:
$```cd Telesend```

### create a virtualenv:
$```virtualenv venv```

### activate venv:
$```source venv/bin/activate```

### install needed module (telethon):
telethon: $```pip install telethon```

### run python file:
$```python3 main.py```

then enter needed data and enjoy it.
