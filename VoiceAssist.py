import speech_recognition
import webbrowser

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



def listen_comand():
    try:
        with speech_recognition.Microphone() as mic:
            sr.adjust_for_ambient_noise(source=mic, duration=0.5)
            audio = sr.listen(source=mic)
            query = sr.recognize_google(audio_data=audio, language='ru-RU').lower()
        print(query)
        return query

    except speech_recognition.UnknownValueError:
        return 'Я не понял что вы сказали'

def search_on_google():
    print('что надо найти?')
    search_term = listen_comand()

    url = f"https://www.google.com/search?q={search_term}"
    webbrowser.get('chrome').open_new_tab(url)

    return 'Открываю'

def search_on_wiki():
    print('Что именно вы хотите найти в Википедии? ')
    search_term = listen_comand()
    print(search_term)

    url = f"https://ru.wikipedia.org/wiki/{search_term}"
    webbrowser.get('chrome').open_new_tab(url)

    return 'Открываю'

if __name__ == "__main__":
    main()
