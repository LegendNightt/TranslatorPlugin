# -*- coding: utf-8 -*-
# by LegendNightt

from googletrans import Translator

translator = Translator()


# Translator
def translatorA(msg):
    translation = translator.translate(msg, dest='en')
    if translation.src == 'en':
        spanishtrans = translator.translate(msg, dest='es')
        text = spanishtrans.text
    else:
        universaltrans = translator.translate(msg, dest='en')
        text = universaltrans.text
    return str(text)


# MCDReforged
def on_info(server, info):
    if info.is_player == 1 and info.content.startswith('t '):
        result = translatorA(info.content[2:])
        server.say('§7[T]<' + info.player + '> §f' + result)


def on_load(server, old):
    server.add_help_message('Translator (t )',
                            'Use t and space and then what you want to translate, EN to ES and ES to EN auto')