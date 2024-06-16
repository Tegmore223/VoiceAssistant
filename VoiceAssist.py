import speech_recognition
import webbrowser
import os

webbrowser.register('chrome', None, webbrowser.BackgroundBrowser("C:/Program Files/Google/Chrome/Application/chrome.exe"))

sr = speech_recognition.Recognizer()
sr.pause_threshold = 0.5  # создаем паузу, после которой ассистент примет нашу команду
sr.energy_threshold = 1500  # устанавливаем более высокий порог энергии

def main():
    start_listening()

def start_listening():
    query = listen_comand()

    if query in ['искать', 'гугл', 'найди', 'найти']:
        search_on_google()

    elif query in ['вики', 'википедия']:
        search_on_wiki()

    elif query in ['включи музыку', 'музыка', 'хочу послушать музыку']:
        Music()

    elif query in ['открой ChatGPT', 'открой искусственный интеллект', 'мне нужен искусственный интеллект', 'ChatGPT',
                'Искусственный интеллект', 'чат gpt', 'нейросеть']:
        ChatGPT()

    elif query in ['погода', 'данные о погоде', 'узнать погоду', 'какая погода']:
        Weather()

    elif query in ['проводник', 'файлы', 'открыть проводник']:
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
        start_listening()

def search_on_google():
    print('что надо найти?')
    search_term = listen_comand()
    print('Открываю Google...')

    url = f"https://www.google.com/search?q={search_term}"
    webbrowser.get('chrome').open_new_tab(url)
    start_listening()

def search_on_wiki():
    print('Что именно вы хотите найти в Википедии? ')
    search_term = listen_comand()
    print('Открываю Википедию...')

    url = f"https://ru.wikipedia.org/wiki/{search_term}"
    webbrowser.get('chrome').open_new_tab(url)
    start_listening()

def Music():
    print('Открываю Yandex Music...')
    url = f"https://music.yandex.ru/users/yamusic-daily/playlists/156956347"
    webbrowser.get('chrome').open_new_tab(url)
    start_listening()

def ChatGPT():
    print('Открываю ChatGPT...')
    url = f'https://chatgpt.com/?model=auto'
    webbrowser.get('chrome').open_new_tab(url)
    start_listening()

def Weather():
    print("Открываю данные о погоде...")
    url = f'ССЫЛКА'
    webbrowser.get('chrome').open_new_tab(url)
    start_listening()

def File_manager():
    print('Открываю проводник...')
    os.system("explorer")
    start_listening()

if __name__ == "__main__":
    main()

