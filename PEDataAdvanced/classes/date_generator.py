import random
import time


class DateGenerator(object):
    format = '%d/%m/%Y'

    @staticmethod
    def generate_date_between(start, end):
        startDate = time.mktime(time.strptime(start, DateGenerator.format))
        endDate = time.mktime(time.strptime(end, DateGenerator.format))

        prop = random.random()
        random_day = startDate + prop * (endDate - startDate)

        return time.strftime(DateGenerator.format, time.localtime(random_day))
