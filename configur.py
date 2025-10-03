import os #для получения данных о пользователе и директиории
import shlex  #для парсинга

def get_os_prompt(): #функция, формирующая приглашение

    username = os.getlogin()
    current_dir = os.getcwd()
    return f"{username}@Windows:{current_dir}$ "


def parse_input(user_input): #функция для парсинга строки
  
    parts = shlex.split(user_input)
    if not parts: #если строка пуста
        return None, []

    command = parts[0] #команда
    arguments = parts[1:] #аргументы
    return command, arguments

def cmd_ls(arguments): #заглушка команды ls
    print(f"Команда 'ls' вызвана с аргументами: {arguments}")

def cmd_cd(arguments): #заглушка команды cd
    print(f"Команда 'cd' вызвана с аргументами: {arguments}")

def main():
    print("Команды ls, cd")
    print("Для выхода введите 'exit'.")

    while True: #цикл repl
        try:
            user_input = input(get_os_prompt()).strip() #читаем ввод юзера
            if not user_input: #если пустая строка
                continue
                
            command, arguments = parse_input(user_input) #парсим на команду и аргументы
            
            if command == "exit": #команды
                print("Выход из эмулятора.")
                break
            elif command == "ls":
                cmd_ls(arguments)
            elif command == "cd":
                cmd_cd(arguments)
            else:
                print(f"Ошибка: команда '{command}' не найдена.")

        except Exception as e:
            #обработка всех прочих ошибок
            print(f"Произошла ошибка: {e}")

#проверка запущен ли файл
if __name__ == "__main__":
    main()