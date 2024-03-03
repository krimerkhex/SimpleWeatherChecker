import requests
from bs4 import BeautifulSoup


def get_ipv4():
    return input("Input ip-address: ")


def check_ip_valid(ip):
    divided_list = list(map(int, list(ip.split('.'))))
    checked = list(filter(lambda x: not x, list(map(lambda x: 0 < x < 2 ** 8, divided_list))))
    return not len(checked)


def country_definition(ip):
    r = requests.get(f"http://ip-api.com/json/{ip}")
    if r.status_code == 200:
        print(f"IP: {ip} country is: {r.json()['country']}")
    else:
        print(f"Bad status code {r.status_code}")


def get_weather():
    s_city = "Kazan,RU"
    try:
        res = requests.get("http://api.openweathermap.org/data/2.5/forecast",
                           params={'q': s_city, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
        data = res.json()
        for i in data['list']:
            print(i['dt_txt'], '{0:+3.0f}'.format(i['main']['temp']), i['weather'][0]['description'])
    except Exception as e:
        print("Exception (forecast):", e)
        pass


if __name__ == '__main__':
    choise = int(input("Part 1 or 2? "))
    if choise == 1:
        ip = get_ipv4()
        if check_ip_valid(ip):
            country_definition(ip)
        else:
            print("You gived not valid ip address")
    elif choise == 2:
        get_weather()
    else:
        print("Gived uncorrect value")
