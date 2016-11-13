# -*- coding: utf-8 -*-
# Заадание 2
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains
import time, unittest
import urllib, json

class test_code_name(unittest.TestCase):
    def test_code_name(self):
        url = "(https://www.tinkoff.ru/api/v1/currency_rates/)"
        response = urllib.urlopen(url)
        data = json.loads(response.read())
        for stroka in data["rates"]):
            if (stroka["fromCurrency"]["code"] == '643' and stroka["fromCurrency"]["name"] == 'RUB'):
                if (stroka["toCurrency"]["code"] == '840' and stroka["fromCurrency"]["name"] == 'USD'):
                    pass
                elif (stroka["toCurrency"]["code"] == '978' and stroka["fromCurrency"]["name"] == 'EUR'):
                    pass
                elif (stroka["toCurrency"]["code"] == '826' and stroka["fromCurrency"]["name"] == 'GBP'):
                    pass
                else:
                    print("Ошибка:%stroka")
            elif (stroka["fromCurrency"]["code"] == '840' and stroka["fromCurrency"]["name"] == 'USD'):
                if (stroka["toCurrency"]["code"] == '643' and stroka["fromCurrency"]["name"] == 'RUB'):
                    pass
                elif (stroka["toCurrency"]["code"] == '978' and stroka["fromCurrency"]["name"] == 'EUR'):
                    pass
                elif (stroka["toCurrency"]["code"] == '826' and stroka["fromCurrency"]["name"] == 'GBP'):
                    pass
                else:
                    print("Ошибка:%stroka")
            elif (stroka["fromCurrency"]["code"] == '978' and stroka["fromCurrency"]["name"] == 'EUR'):
                if (stroka["toCurrency"]["code"] == '643' and stroka["fromCurrency"]["name"] == 'RUB'):
                    pass
                elif (stroka["toCurrency"]["code"] == '840' and stroka["fromCurrency"]["name"] == 'USD'):
                    pass
                elif (stroka["toCurrency"]["code"] == '826' and stroka["fromCurrency"]["name"] == 'GBP'):
                    pass
                else:
                    print("Ошибка:%stroka")
            elif (stroka["fromCurrency"]["code"] == '826' and stroka["fromCurrency"]["name"] == 'GBP'):
                 if (stroka["toCurrency"]["code"] == '840' and stroka["fromCurrency"]["name"] == 'USD'):
                    pass
                elif (stroka["toCurrency"]["code"] == '978' and stroka["fromCurrency"]["name"] == 'EUR'):
                    pass
                elif (stroka["toCurrency"]["code"] == '643' and stroka["fromCurrency"]["name"] == 'BGP'):
                    pass
                else:
                    print("Ошибка:%stroka")
            else:
                print("Ошибка:%stroka")

if __name__ == '__main__':
    unittest.main()