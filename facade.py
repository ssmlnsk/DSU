from DataBase import DataBase
from dsu import DSU
import re


class Facade:
    """
    Класс фасада
    """
    def __init__(self, name='dsu_DB.db'):
        """
        Создание объекта Базы Данных, структуры данных.
        :param name: имя БД
        """
        self.DB = DataBase(name)
        self.dsu = DSU()
        self.build()

    def build(self):
        """
        Функция, добавляющая данные в таблицу
        :return: None
        """
        data = self.DB.get_data_db()
        print(data)
        if data == '':
            data = []
        else:
            if type(data) != int:
                print('Выгрузка данных: ', data)
                if data is not None:
                    data = data.split(', ')
                    for i in data:
                        i = int(i)
                        self.dsu.push(i)
                        self.dsu.make_set()
                    print(data)
            else:
                data = str(data)
                print('Выгрузка данных: ', data)
                if data is not None:
                    data = data.split(', ')
                    for i in data:
                        i = int(i)
                        self.dsu.push(i)
                        self.dsu.make_set()
                    print(data)

    def make_set(self):
        """
        Функция, создающая список из добавленных в структуру элементов
        :return: None
        """
        self.dsu.make_set()

    def union(self, a, b):
        """
        Функция, объединяющая два элемента в одно множество
        :param a: первый элемент
        :param b: второй элемент
        :return: None
        """
        self.dsu.union(a, b)

    def find(self, k):
        """
        Функция, осуществляющая поиск родителя элемента
        :param k: элемент, родителя которого нужно найти
        :return:
        """
        return self.dsu.find(k)

    def push(self, item):
        """
        Функция, добавляющая новый элемент в структуру данных
        :param item: добавляемы элемент
        :return: None
        """
        self.dsu.push(item)

    def print_sets(self):
        """
        Функция, отображающая список элементов
        :return:
        """
        printset = []
        print = str(self.dsu.print_sets())
        if print is not None:
            nums = print[2:-2].split(',')
            if nums != '':
                for num in nums:
                    printset.append(int(num))
        return printset

    def saveDB(self):
        """
        Функция сохраняющая данные в БД
        :return: None
        """
        value = self.dsu.print_sets()
        self.DB.insert(value)

    def loadDB(self):
        """
        Функция загружающая данные из Базы Данных
        :return: None
        """
        self.dsu.universe.clear()
        loadlist = []
        load2 = []
        integer = 0
        load3 = self.DB.load_last()
        p = re.compile(r"\b\d+\b")
        for i in load3:
            if type(i) != type(integer):
                m = p.findall(i)
                for j in m:
                    if j != '':
                        load2.append(int(j))
            else:
                load2.append(i)
        if load2 != None:
            if len(load2) > 1:
                if load2 is not None:
                    load2 = str(load2)
                    nums = load2[1:-1].split(',')
                    if nums != ['']:
                        for num in nums:
                            loadlist.append(int(num))
                            self.dsu.universe.append(int(num))
                return loadlist

            elif len(load2) == 1:
                nums = load2
                if nums != ['']:
                    for num in nums:
                        loadlist.append(int(num))
                        self.dsu.universe.append(int(num))
                return loadlist
        else:
            loadlist = []
            return loadlist

    def deleteDB(self):
        """
        Функция, очищающая Базу Данных от записанных в неё элементов
        :return: None
        """
        self.DB.del_all()
        self.dsu.universe.clear()
