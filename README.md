## A simple website and Telegram bot to display the current menu from a single file menu.txt. 
[![Docker Build](https://github.com/youonmyown/website-telebot-from-1file/actions/workflows/docker-image.yml/badge.svg?branch=main)](https://github.com/youonmyown/website-telebot-from-1file/actions/workflows/docker-image.yml)

This project was conceived and integrated for a cafe in the medical center where I work. Perhaps someone will find it useful.

## Usage

Create a `config.py` file in the repository directory and add the line
```
TOKEN = 'your_bot_token'
```

### Docker run
```
docker compose up -d
```

### Warning: 
This project is designed for local use within an isolated local network. Follow these recommendations:
```
This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
```
