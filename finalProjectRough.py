import json, requests

#App id from openweathermap.org
api_key = '5e1051ac4db40ae05990d8f9dfc4dffa'


#format of url when zipcode is given
def url_with_zip(zipcode):
    url = 'http://api.openweathermap.org/data/2.5/weather?zip=%s&units=imperial&appid=%s' % (zipcode, api_key)
    return url


#format of url when city is given
def url_with_city(city):
    url = 'http://api.openweathermap.org/data/2.5/weather?q=%s&units=imperial&appid=%s' % (city, api_key)
    return url


def primary():

    #Ask the user for zip code or city
    user_input = input('Enter zip code or city: ')

    #Get the correct url based on input
    if user_input.isdecimal():
        url = url_with_zip(user_input)
    else:
        url = url_with_city(user_input)

    server_response = requests.get(url)

    #Check if connection was established or not
    try:
        server_response.raise_for_status()
        print('Connection was successful')
    except:
        print('Connection was not succesful')

    weather_report = server_response.json()
    #if statment to check the status of json file
    if weather_report["cod"] != "404":
        #attaching the json file to various variables
        temp = weather_report["main"]["temp"]
        found_city = weather_report["name"]
        skies = weather_report["weather"][0]["main"]

        #Display the weather information to the user
        print('This weather is for the city of : {}'.format(found_city))
        print('The skies will be : {}'.format(skies))
        print('Current Temperature : {} degrees fahrenheit'.format(temp))
    else:
        print("city not found ")


cont = True
#loop to allow the user to run more than once.
while cont == True:

    primary()
    x = input('Would you like to enter another city? Y/N\n')
    if x.upper() == 'Y':
        cont = True
    else:
      print("Goodbye")
      cont = False
