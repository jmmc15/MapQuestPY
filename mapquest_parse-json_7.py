import urllib.parse
import requests

main_api = "https://www.mapquestapi.com/directions/v2/route?"
key = "NGO5fCSo59YyPyHEbC3q01BKlhM9knpU" 



while True:
    orig = input("Starting Location: ")
    if orig == "quit" or orig == "q":
        break
    dest = input("Destination: ")
    if dest == "quit" or dest == "q":
        break
    url = main_api + urllib.parse.urlencode({"key":key, "from":orig, "to":dest})
    print("URL: " + (url))
    json_data = requests.get(url).json()
    json_status = json_data["info"]["statuscode"]
    if json_status == 0:
        disp = input("Display data in: \n (I) Imperial System - Miles / Gallons. \n (M) Metric System - Kilometers / Liters. \n (I) or (M): ")
        if disp == "I" or disp == "i":
            print("API Status: " + str(json_status) + " = A successful route call.\n")
            print("=============================================")
            print("Directions from " + (orig) + "to " + (dest))
            print("Trip Duration:   " + (json_data["route"]["formattedTime"]))
            print("Miles:      " + str("{:.2f}".format((json_data["route"]["distance"]))))
            print("Fuel Used (gal): " + str("{:.2f}".format((json_data["route"]["fuelUsed"]))))
            print("=============================================")
            count = 1
            for each in json_data["route"]["legs"][0]["maneuvers"]:
                print(str(count) + ". " + (each["narrative"]) + " (" + str("{:.2f}".format((each["distance"])) + " miles)"))
                count += 1
            print("=============================================\n")
        
        if disp == "M" or disp == "m":
            print("API Status: " + str(json_status) + " = A successful route call.\n")
            print("=============================================")
            print("Directions from " + (orig) + "to " + (dest))
            print("Trip Duration:   " + (json_data["route"]["formattedTime"]))
            print("Kilometers:      " + str("{:.2f}".format((json_data["route"]["distance"])*1.61)))
            print("Fuel Used (Ltr): " + str("{:.2f}".format((json_data["route"]["fuelUsed"])*3.78)))
            print("=============================================")
            count = 1
            for each in json_data["route"]["legs"][0]["maneuvers"]:
                print(str(count) + ". " + (each["narrative"]) + " (" + str("{:.2f}".format((each["distance"])*1.61) + " km)"))
                count += 1
            print("=============================================\n")
            
        # print("=============================================")
        
        # count = 1
        # for each in json_data["route"]["legs"][0]["maneuvers"]:
        #     print(str(count) + ". " + (each["narrative"]) + " (" + str("{:.2f}".format((each["distance"])*1.61) + " km)"))
        #     count += 1
        # print("=============================================\n")
    elif json_status == 402:
        print("**********************************************")
        print("Status Code: " + str(json_status) + "; Invalid user inputs for one or both locations.")
        print("**********************************************\n")
    elif json_status == 611:
        print("**********************************************")
        print("Status Code: " + str(json_status) + "; Missing an entry for one or both locations.")
        print("**********************************************\n")
    else:
        print("************************************************************************")
        print("For Status Code: " + str(json_status) + "; Refer to:")
        print("https://developer.mapquest.com/documentation/directions-api/status-codes")
        print("************************************************************************\n")