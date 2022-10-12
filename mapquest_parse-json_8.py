import urllib.parse
import requests
import colorama
from colorama import Fore, Back, Style

colorama.init(autoreset=True)

main_api = "https://www.mapquestapi.com/directions/v2/route?"
key = "NGO5fCSo59YyPyHEbC3q01BKlhM9knpU" 



while True:
    orig = input(Fore.CYAN + "Starting Location: ")
    if orig == "quit" or orig == "q":
        break
    dest = input(Fore.CYAN + "Destination: ")
    if dest == "quit" or dest == "q":
        break
    url = main_api + urllib.parse.urlencode({"key":key, "from":orig, "to":dest})
    print(Fore.GREEN + "URL: " + (url))
    json_data = requests.get(url).json()
    json_status = json_data["info"]["statuscode"]
    if json_status == 0:
        print(Fore.GREEN + "API Status: " + str(json_status) + " = A successful route call.\n")
        print("=============================================")
        print(Fore.BLUE + "Directions from " + (orig) + " to " + (dest))
        print(Fore.BLUE + "Trip Duration:   " + (json_data["route"]["formattedTime"]))
        print(Fore.BLUE + "Kilometers:      " + str("{:.2f}".format((json_data["route"]["distance"])*1.61)))
        print(Fore.BLUE + "Fuel Used (Ltr): " + str("{:.2f}".format((json_data["route"]["fuelUsed"])*3.78)))
        #function to check if there is toll road
        def myFunction(): 
            if json_data["route"]["hasTollRoad"] == 1:
                return Fore.BLUE + "Yes"
            else:
                return Fore.BLUE + "No"
        print(Fore.BLUE + "Has Toll Road:  ",myFunction())
        
        print("=============================================")
        for each in json_data["route"]["legs"][0]["maneuvers"]:
            print((Fore.CYAN + each["narrative"]) + " (" + str("{:.2f}".format((each[ "distance"])*1.61) + " km)"))
        print("=============================================\n")
    elif json_status == 402:
        print("**********************************************")
        print(Fore.RED + "Status Code: " + str(json_status) + "; Invalid user inputs for one or both locations.")
        print("**********************************************\n")
    elif json_status == 611:
        print("**********************************************")
        print(Fore.RED + "Status Code: " + str(json_status) + "; Missing an entry for one or both locations.")
        print("**********************************************\n")
    else:
        print("************************************************************************")
        print(Fore.RED + "For Status Code: " + str(json_status) + "; Refer to:")
        print("https://developer.mapquest.com/documentation/directions-api/status-codes")
        print("************************************************************************\n")