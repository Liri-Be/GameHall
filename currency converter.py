import requests
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty, ListProperty, StringProperty
from kivymd.uix.button import MDFillRoundFlatIconButton

URL = 'https://v6.exchangerate-api.com/v6/a8ca3170d4d4b469142d72d1/latest/USD'
NAMES = ['USD', 'AED', 'AFN', 'ALL', 'AMD', 'ANG', 'AOA', 'ARS', 'AUD', 'AWG', 'AZN', 'BAM', 'BBD', 'BDT', 'BGN', 'BHD',
         'BIF', 'BMD', 'BND', 'BOB', 'BRL', 'BSD', 'BTN', 'BWP', 'BYN', 'BZD', 'CAD', 'CDF', 'CHF', 'CLP', 'CNY', 'COP',
         'CRC', 'CUC', 'CUP', 'CVE', 'CZK', 'DJF', 'DKK', 'DOP', 'DZD', 'EGP', 'ERN', 'ETB', 'EUR', 'FJD', 'FKP', 'FOK',
         'GBP', 'GEL', 'GGP', 'GHS', 'GIP', 'GMD', 'GNF', 'GTQ', 'GYD', 'HKD', 'HNL', 'HRK', 'HTG', 'HUF', 'IDR', 'ILS',
         'IMP', 'INR', 'IQD', 'IRR', 'ISK', 'JMD', 'JOD', 'JPY', 'KES', 'KGS', 'KHR', 'KID', 'KMF', 'KRW', 'KWD', 'KYD',
         'KZT', 'LAK', 'LBP', 'LKR', 'LRD', 'LSL', 'LYD', 'MAD', 'MDL', 'MGA', 'MKD', 'MMK', 'MNT', 'MOP', 'MRU', 'MUR',
         'MVR', 'MWK', 'MXN', 'MYR', 'MZN', 'NAD', 'NGN', 'NIO', 'NOK', 'NPR', 'NZD', 'OMR', 'PAB', 'PEN', 'PGK', 'PHP',
         'PKR', 'PLN', 'PYG', 'QAR', 'RON', 'RSD', 'RUB', 'RWF', 'SAR', 'SBD', 'SCR', 'SDG', 'SEK', 'SGD', 'SHP', 'SLL',
         'SOS', 'SRD', 'SSP', 'STN', 'SYP', 'SZL', 'THB', 'TJS', 'TMT', 'TND', 'TOP', 'TRY', 'TTD', 'TVD', 'TWD', 'TZS',
         'UAH', 'UGX', 'UYU', 'UZS', 'VES', 'VND', 'VUV', 'WST', 'XAF', 'XCD', 'XDR', 'XOF', 'XPF', 'YER', 'ZAR', 'ZMW']


class StartScreen(Screen):
    """
    class to handle the start screen
    """
    def __init__(self, **kw):
        """
        constructor of the class
        :param kw:
        """
        super(StartScreen, self).__init__(**kw)
        self.start_lbl = self.ids['start_lbl']

    def pressed_main(self):
        """
        if pressing the main button, switching to the main screen
        :return None:
        """
        self.manager.current = 'main'

    def pressed_inst(self):
        """
        if pressing the instruction button, switching to the instruction screen
        :return:
        """
        self.manager.current = 'inst'


class InstScreen(Screen):
    """
    class to handle the instruction screen
    """
    def __init__(self, **kw):
        """
        constructor of the class
        :param kw:
        """
        super(InstScreen, self).__init__(**kw)

    def pressed_main(self):
        """
        if pressing the main button, switching to the main screen
        :return:
        """
        self.manager.current = 'main'


class MainScreen(Screen):
    """
    class to handle the instruction screen
    """
    def __init__(self, **kw):
        """
        constructor of the class
        :param kw:
        """
        super(MainScreen, self).__init__(**kw)
        self.database = requests.get(URL).json()['conversion_rates']

    def pressed_inst(self):
        """
        if pressing the instruction button, switching to the instruction screen
        :return:
        """
        self.manager.current = 'inst'

    def pressed_conv(self):
        """
        if pressing the convert button, convert the currency using the database
        :return:
        """
        pass


def main():
    response = requests.get(URL)
    currency_dict = response.json()['conversion_rates']
    print(currency_dict)
    print(NAMES)


if __name__ == '__main__':
    main()
