import os
import socket

hostname = socket.gethostname()
ip_hka = socket.gethostbyname(hostname)

def welcomeprocedure():
    print("Добро пожаловать в CodeExecute!")
    uname = input("Введите свое имя пользователя: ")
    
    with open('metadata.json', 'w') as f:
        f.write(f"{uname}\n")
        f.write(f"{ip_hka}")
    
    return uname

uname = welcomeprocedure()

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    qww9 = input(f"привет {uname} ! , введи путь к файлу который надо запустить :")

    try:
        # Способ с обработкой кодировки вручную
        file = open(qww9, 'rb')  # открываем в бинарном режиме
        content = file.read()
        file.close()
        code = content.decode('utf-8')  # декодируем вручную
        exec(code)
    except UnicodeDecodeError:
        try:
            # Пробуем другую кодировку если utf-8 не работает
            code = content.decode('cp1251')
            exec(code)
        except Exception as e:
            print(f"Ошибка кодировки: {e}")
    except Exception as e:
        print(f"обнаружена ошибка: {e}")

main()