import time
import json
from datetime import datetime

class result_structure:
    '''
    Analyze the data and generates result.
    '''
    def __init__(self, data, timestamp):
        self.data = data
        self.time_stamps = timestamp
        self.b_data = self.get_b_data()
        self.max_number = self.get_max_number()
        self.min_number = self.get_min_number()
        self.first_number = self.get_first_number()
        self.last_number = self.get_last_number()
        self.number_of_prime_numbers = self.get_number_of_prime_numbers()
        self.number_of_even_numbers, self.number_of_odd_numbers = self.get_number_of_even_and_odd_numbers()

    def get_b_data(self) -> list():
        "returns a list with value stored with 'b' key"
        new_list = []
        for i in self.data:
            new_list.append(i["b"])
        return new_list

    def get_max_number(self) -> int():
        return max(self.b_data)

    def get_min_number(self) -> int:
        return min(self.b_data)

    def get_first_number(self) -> int:
        return self.b_data[0]

    def get_last_number(self) -> int:
        return self.b_data[-1]

    def get_number_of_prime_numbers(self) -> int:
        count = 0
        for number in self.b_data:
            if self.isprime(number):
                count += 1
        return count

    def get_number_of_even_and_odd_numbers(self) -> tuple:
        count_even = 0
        count_odd = 0
        for number in self.b_data:
            if number % 2 == 0:
                count_even += 1
            else:
                count_odd +=1

        return count_even, count_odd

    def isprime(self, num) -> bool:
        "Checks if a number is prime or not."
        for n in range(2,int(num**0.5)+1):
            if num%n==0:
                return False
        return True

    def get_result(self) -> dict:
        return {
            "max_number": self.max_number,
            "min_number": self.min_number,
            "first_number": self.first_number,
            "last_number": self.last_number,
            "number_of_prime_numbers": self.number_of_prime_numbers,
            "number_of_even_numbers": self.number_of_even_numbers,
            "number_of_odd_numbers": self.number_of_odd_numbers
        }

if __name__ == "__main__":
    # A. Load data from json file to a dict
    with open('data.json', 'r') as f:
        file_data = json.load(f)
    # B. for each timestamp in the dict, analyse the data.
    for timestamp in list(file_data):
        a = result_structure(file_data[timestamp], timestamp)
        print(a.get_result())
