import csv
import logging
import homework.logs as logs
import homework.validators as validators

path = "data.csv"

class Patient:
    first_name = validators.NotRen()
    last_name = validators.NotRen()
    birth_date = validators.Date()
    phone = validators.Phone()
    document_type = validators.DocType()
    document_id = validators.DocId()

    def __init__(self, *args):
        self.logger_inf = logging.getLogger("inf")
        self.logger_err = logging.getLogger("err")
        self.first_name = args[0]
        self.last_name = args[1]
        self.birth_date = args[2]
        self.phone = args[3]
        self.document_type = args[4]
        self.document_id = args[5]

        self.logger_inf.info('Создан новый пациент')

    @ staticmethod
    def create(fname, lname, bdate, number, doc_type, doc_id):
        return Patient(fname, lname, bdate, number, doc_type, doc_id)

    def save(self):
        myData = [str(self).split(",")]

        myFile = open(path, 'a', newline="")
        with myFile:
            writer = csv.writer(myFile)
            writer.writerows(myData)
            self.logger_inf.info('Запись о новом пациенте сохранена')

    def __str__(self):
        return f"{self.first_name}, {self.last_name}, {self.birth_date}, {self.phone}, {self.document_type}, {self.document_id}"


class PatientCollection:
    def __init__(self, path):
        self.path = path
        self.cursor = 0
        self.count = -1

    def __iter__(self):
        return self

    def limit(self, n):
        self.count = n
        return self.__iter__()

    def __next__(self):
        with open(self.path, 'r') as File:
            File.seek(self.cursor)
            data = File.readline()
            self.cursor = File.tell()

        if not data or not self.count:
            raise StopIteration
        self.count -= 1
        return Patient(*data.split(','))
