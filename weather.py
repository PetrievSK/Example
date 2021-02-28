import requests,datetime

APPID = "85390c0d34a1288f66e6a8224c8596b1"
URL_BASE = "https://api.openweathermap.org/data/2.5/"

def weather_onecall(lat: float = 55.45, lon: float = 37.37, appid: str = APPID,exclude: list=['minutely','hourly','alerts'],units : str ="metric",lang : str ="ru") -> dict:
    """https://openweathermap.org/api/one-call-api"""
    return requests.get(URL_BASE + "onecall", params=locals()).json()

if __name__ == "__main__":
    weather=weather_onecall()
    count=0
    print('Для города: ' + weather['timezone'])
    for i in weather['daily']:
        if count<5:
            print(datetime.datetime.fromtimestamp(i['dt']).date(), 'Средняя темп =',((i['temp']['day']+i['temp'][
                'eve'])/2),'Темп утром =',
                  i['temp']['morn'])
            count+=1
        else: break
