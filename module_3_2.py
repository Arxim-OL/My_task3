# Задача "Рассылка писем"

def send_email (message, recipient, *, sender = "university.help@gmail.com"):
    if test_str (recipient) == False or test_str (sender) == False:
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")
        return
    if sender == recipient:
        print ("Нельзя отправить письмо самому себе!")
        return
    if sender == "university.help@gmail.com":
        print(f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}")
    else:
        print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}")
    return

def test_str (t_str): # Проверка адреса на валидность
    test = False
    l = len(t_str)
    if t_str [l-4:] == ".com" or \
       t_str [l-3:] == ".ru" or \
       t_str [l-4:] == ".net":
        if '@' in t_str:
            test = True
    return test


send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')