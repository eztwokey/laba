#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Вариант6
# Использовать словарь, содержащий следующие ключи: название пункта назначения; ФИО; номер
# поезда. Написать программу, выполняющую следующие действия:
# ввод с клавиатуры данных в список, состоящий из словарей заданной структуры; записи должны
# быть размещены в алфавитном порядке по названиям пунктов назначения; вывод на экран
# информации о поездах, отправляющихся после введенного с клавиатуры времени; если
# таких поездов нет, выдать на дисплей соответствующее сообщение.


import logging
import sys
import modul


if __name__ == '__main__':

    logging.basicConfig(
        filename='trains.log',
        level=logging.INFO,
        format='%(asctime)s %(levelname)s:%(message)s'
    )

    trains = []
    staff = modul.Staff()
    # Организовать бесконечный цикл запроса команд.
    while True:
        try:
            # Запросить команду из терминала.
            command = input(">>> ").lower()
            # Выполнить действие в соответствие с командой.
            if command == 'exit':
                break

            elif command == 'add':
                # Запросить данные о поезде.
                name = input("Название пункта назначения: ")
                num = input("Номер поезда: ")
                time = input("Время отправления: ")

                staff.add(name, num, time)
                logging.info(
                    f"Добавлен поезд: {num}, "
                    f"пункт назначения {name}, "
                    f"отправляющийся в {time} времени."
                )

            elif command == 'list':
                print(staff)
                logging.info("Отображен список поездов.")

            elif command.startswith('select '):
                parts = command.split(' ', maxsplit=2)
                selected = staff.select(parts[1])

                if selected:
                    for c, train in enumerate(selected, 1):
                        print(
                            ('Номер поезда:', train.num),
                            ('Пункт назначения:', train.name),
                            ('Время отправления(ЧЧ:ММ):', train.time)
                        )
                    logging.info(
                        f"Найден поезд с номером {train.num}"
                    )

                else:
                    print("Таких поездов нет!")
                    logging.warning(
                        f"Поезд с номером {train.num} не найден."
                    )

            elif command.startswith('load '):
                # Разбить команду на части для выделения имени файла.
                parts = command.split(' ', maxsplit=1)
                staff.load(parts[1])
                logging.info(f"Загружены данные из файла {parts[1]}.")

            elif command.startswith('save '):
                # Разбить команду на части для выделения имени файла.
                parts = command.split(' ', maxsplit=1)
                staff.save(parts[1])
                logging.info(f"Сохранены данные в файл {parts[1]}.")

            elif command == 'help':

                print("Список команд:\n")
                print("add - добавить поезд;")
                print("list - вывести список поездов;")
                print("select <номер поезда> - запросить информацию о выбранном времени;")
                print("help - отобразить справку;")
                print("load <имя файла> - загрузить данные из файла;")
                print("save <имя файла> - сохранить данные в файл;")
                print("exit - завершить работу с программой.")
            else:
                raise modul.UnknownCommandError(command)
        except Exception as exc:
            logging.error(f"Ошибка: {exc}")
            print(exc, file=sys.stderr)
