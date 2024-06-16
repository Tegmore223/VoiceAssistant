#Голосовой Ассистент
#Список доступных голсовых команд - readme.txt

import speech_recognition
import webbrowser
import os

webbrowser.register('chrome', None, webbrowser.BackgroundBrowser("C:/Program Files/Google/Chrome/Application/chrome.exe"))

sr = speech_recognition.Recognizer()
sr.pause_threshold = 0.5  # создаем паузу, после которой ассистент примет нашу команду
sr.energy_threshold = 1500  # устанавливаем более высокий порог энергии

def main():
    while True:
        query = listen_comand()

        for google in ['искать', 'гугл', 'найди', 'найти']:
            if google in query:
                search_on_google()

        for wiki in ['вики', 'википедия']:
            if wiki in query:
                search_on_wiki()

        for music in ['включи музыку', 'музыка', 'хочу послушать музыку']:
            if music in query:
                Music()

        for GPT in ['открой ChatGPT', 'открой искусственный интеллект', 'мне нужен искусственный интеллект', 'ChatGPT', 'Искусственный интеллект', 'чат gpt']:
            if GPT in query:
                ChatGPT()

        for weather in ['погода', 'данные о погоде', 'узнать погоду', 'какая погода']:
            if weather in query:
                Wether()

        for OpenFManager in ['проводник', 'файлы', 'открыть проводник']:
            if OpenFManager in query:
                File_manager()


def listen_comand():
    try:
        with speech_recognition.Microphone() as mic:
            sr.adjust_for_ambient_noise(source=mic, duration=0.5)
            audio = sr.listen(source=mic)
            query = sr.recognize_google(audio_data=audio, language='ru-RU').lower()
        print(query)
        return query

    except speech_recognition.UnknownValueError:
        print('Я не понял что вы сказали')

def search_on_google():
    print('что надо найти?')
    search_term = listen_comand()
    print('Открываю Google...')

    url = f"https://www.google.com/search?q={search_term}"
    webbrowser.get('chrome').open_new_tab(url)

def search_on_wiki():
    print('Что именно вы хотите найти в Википедии? ')
    search_term = listen_comand()
    print('Открываю Википедию...')

    url = f"https://ru.wikipedia.org/wiki/{search_term}"
    webbrowser.get('chrome').open_new_tab(url)

def Music():
    print('Открываю Yandex Music...')
    url = f"https://music.yandex.ru/users/yamusic-daily/playlists/156956347"
    webbrowser.get('chrome').open_new_tab(url)

def ChatGPT():
    print('Открываю ChatGPT...')
    url = f'https://chatgpt.com/?model=auto'
    webbrowser.get('chrome').open_new_tab(url)

def Wether():
    print("Октрываю данные о погоде...")
    url = f'https://yandex.ru/pogoda/kazan?lat=55.796129&lon=49.106414'
    webbrowser.get('chrome').open_new_tab(url)

def File_manager():
    print('Открываю проводник...')
    os.system("explorer")

if __name__ == "__main__":
    main()

