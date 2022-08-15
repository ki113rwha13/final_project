'''
Cory Thomaier
8/14/2022
CIS245-T305 Introduction to Programming (2227-1)

Class Project
For your class project, we will be creating an application to interacts with a webservice in order to obtain data. Your program will use all of the information you’ve learned in the class in order to create a useful application.
Your program must prompt the user for their city or zip code and request weather forecast data from openweathermap.org. Your program must display the weather information in an READABLE format to the user.
Requirements: 
Create a Python Application which asks the user for their zip code or city.
Use the zip code or city name in order to obtain weather forecast data from: http://openweathermap.org/
Display the weather forecast in a readable format to the user.
Use comments within the application where appropriate in order to document what the program is doing.
Use functions including a main function.
Allow the user to run the program multiple times.
Validate whether the user entered valid data. If valid data isn’t presented, notify the user.
Use the Requests library in order to request data from the webservice.
Use Python 3.
Use try blocks when establishing connections to the webservice. You must print a message to the user indicating whether or not the connection was successful.
'''
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
