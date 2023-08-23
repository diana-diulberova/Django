from django.shortcuts import render
from django.http import HttpResponse
from random import randint
import logging
from lorem_text import lorem

logger = logging.getLogger(__name__)

def text(title, text):
    return f'<h1>Сайт ДОМАШНЕЕ ЗАДАНИЕ №1</h1>' \
           f'<h2>{title}</h2>' \
           f'<p>{text}</p>'

def general(request):
    title = 'Главная страница сайта'
    paragraph_length = 15
    body_text = lorem.paragraphs(paragraph_length)
    logger.info(f'Page "general" is open')
    return HttpResponse(text(title, body_text))

def about(request):
    title = 'О себе'
    paragraph_length = 15
    body_text = lorem.paragraphs(paragraph_length)
    logger.info(f'Page "about" is open')
    return HttpResponse(text(title, body_text))
