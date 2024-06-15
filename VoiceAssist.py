import speech_recognition
import webbrowser

webbrowser.register('chrome', None,webbrowser.BackgroundBrowser("C:/Program Files/Google/Chrome/Application/chrome.exe"))

sr = speech_recognition.Recognizer()
sr.pause_threshold=0.5 # создаем паузу, после которой ассистент примет нашу команду

def listen_comand():
    try:
        with speech_recognition.Microphone() as mic:
            sr.adjust_for_ambient_noise(source=mic, duration=0.5)
            audio = sr.listen(source=mic)
            query = sr.recognize_google(audio_data=audio, language='ru-RU').lower()
        print(query)

    except speech_recognition.UnknownValueError:
        return 'Я не понял что вы сказали'

commands_dict = {'commands':{
'search_for_information_on_google':
['искать', 'гугл', 'найди' ,'найти']}}


def main():
    query = listen_comand()

    for k, v in commands_dict['commands'].items():
        if query in v:
            print(globals()[k]())

def search_on_google():
    print('что надо найти?')
    try:
        with speech_recognition.Microphone() as mic:
            sr.adjust_for_ambient_noise(source=mic, duration=0.5)
            audio = sr.listen(source=mic)
            search_term = sr.recognize_google(audio_data=audio, language='ru-RU').lower()


    except speech_recognition.UnknownValueError as e:
        return 'Я не понял что вы сказали'

    url = f"https://www.google.com/search?q={search_term}"
    webbrowser.get('chrome').open_new_tab(url)

    return 'Открываю'


if __name__=='__main__':
    main()
    search_on_google()
