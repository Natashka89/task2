# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains
import time, unittest
import urllib, json


def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

class test_code_name(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)

    def test_code_name(self):
        success = True
        wd = self.wd
        url = "(https://www.tinkoff.ru/api/v1/currency_rates/)"
        wd.get(url)
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


    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()