#!/usr/bin/env python3
# -*- config: utf-8 -*-

#Выполнить индивидуальное задание 2 лабораторной работы 14, оформив все функции
#программы в виде отдельного модуля. Разработанный модуль должен быть подключен в
#основную программу с помощью одного из вариантов команды import . Номер варианта
#уточнить у преподавателя.

from dataclasses import dataclass, field
import logging
import sys
import xml.etree.ElementTree as ET
import modul

if __name__ == '__main__':

    logging.basicConfig(
        filename='trains.log',
        level=logging.INFO,
        format='%(asctime)s %(levelname)s:%(message)s'
    )

    trains = []
    staff = Staff()
    while True:
        try:
            command = input(">>> ").lower()
            if command == 'exit':
                break

            elif command == 'add':
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
                logging.info("Cписок поездов.")

            elif command.startswith('select '):
                parts = command.sp  lit(' ', maxsplit=2)
                selected = staff.select(parts[1])

                if selected:
                    for c, train in enumerate(selected, 1):
                        print(
                            ('Номер поезда:', train.num),
                            ('Пункт назначения:', train.name),
                            ('Время отправления(ЧЧ:ММ):', train.time)
                        )
                    logging.info(
                        f"Найден поезд с указанным Вами номером: {train.num}"
                    )

                else:
                    print("Таких поездов нет!")
                    logging.warning(
                        f"Поезд с номером {train.num} не найден."
                    )

            elif command.startswith('load '):
                parts = command.split(' ', maxsplit=1)
                staff.load(parts[1])
                logging.info(f"Загружены данный из файла {parts[1]}.")

            elif command.startswith('save '):
                parts = command.split(' ', maxsplit=1)
                staff.save(parts[1])
                logging.info(f"Данные сохранены в файл {parts[1]}.")

            elif command == 'help':

                print("Список команд:\n")
                print("add - добавить поезд;")
                print("list - вывести список поездов;")
                print("select <номер поезда> - запросить информацию о выбранном поезде;")
                print("help - отобразить справку;")
                print("load <имя файла> - загрузить данные из файла;")
                print("save <имя файла> - сохранить данные в файл;")
                print("exit - завершить работу с программой.")
            else:
                raise UnknownCommandError(command)
        except Exception as exc:
            logging.error(f"Ошибка: {exc}")
            print(exc, file=sys.stderr)
