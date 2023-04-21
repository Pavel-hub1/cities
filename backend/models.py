import random


class CitiesGame:
    def __init__(self):
        with open('cities.txt', 'r', encoding='utf8') as f:
            self.cities = {self.__normalize_name(city): city for city in f.read().split('\n') if city}
        self.storage = set()
        self.exceptions = {'ы', 'ь', 'ъ', 'й'}
        self.current_letter = None

    def user_move(self, city: str):
        city = self.__normalize_name(city)
        if self.__city_is_correct(city) and self.__correct_first_letter(city):
            if city in self.storage:
                return 'used', self.current_letter
            self.storage.add(city)
            self.__correct_last_letter(city)
            return self.__PC_move(), self.current_letter
        return 'error', self.current_letter

    def __PC_move(self):
        correct_cities = [city for city in self.cities if
                          city.startswith(self.current_letter) and city not in self.storage]
        if correct_cities:
            answer_city = random.choice(correct_cities)
            self.storage.add(answer_city)
            self.__correct_last_letter(answer_city)
            return self.cities[answer_city].capitalize()
        return None

    def __city_is_correct(self, city):
        city = self.__normalize_name(city)
        if city in self.cities:
            return True
        return False

    def __correct_first_letter(self, city: str):
        if not self.current_letter or self.current_letter == city[0]:
            return True
        return False

    def __correct_last_letter(self, city: str):
        for char in reversed(city):
            if char not in self.exceptions:
                self.current_letter = char
                break

    @staticmethod
    def __normalize_name(city: str):
        return city.strip().lower().replace('ё', 'е').replace('-', '')
