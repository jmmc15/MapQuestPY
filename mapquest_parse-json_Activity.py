import urllib.parse
import requests


main_api = "https://www.mapquestapi.com/directions/v2/route?"
key = "BfmYEhKkmUCzybpkWfMwuqZa6bDBdonD"

while True:
    orig = input("Starting Location: ")
    if orig == "quit" or orig == "q":
        break
    dest = input("Destination: ")
    if dest == "quit" or dest == "q":
        break

    Metrics = input("What metrics do you choose? Press M for miles and gallons, Press K for kilometers and liters: ")
    if Metrics != "m" and Metrics != "k" and Metrics != "M" and Metrics != "K":
        print("Please choose either M or K")
        print("=============TERMINATING PROGRAM=============")
        break
    url = main_api + urllib.parse.urlencode({"key":key, "from":orig, "to":dest})
    print("URL: " + (url))
    json_data = requests.get(url).json()
    json_status = json_data["info"]["statuscode"]
    if json_status == 0:
        print("API Status: " + str(json_status) + " = A successful route call.\n")
        print("=============================================")
        print("Directions from " + (orig) + " to " + (dest))
        print("Trip Duration:   " + (json_data["route"]["formattedTime"]))
        if Metrics == "M" or Metrics == "m":
            print("Miles:      " + str("{:.2f}".format((json_data["route"]["distance"]))))
        elif Metrics == "K" or Metrics == "k":
            print("Kilometers:      " + str("{:.2f}".format((json_data["route"]["distance"])*1.61)))
        if Metrics == "M" or Metrics == "m":
            print("Fuel Used (Gal): " + str("{:.2f}".format((json_data["route"]["fuelUsed"]))))
        elif Metrics == "K" or Metrics == "k":
            print("Fuel Used (Ltr): " + str("{:.2f}".format((json_data["route"]["fuelUsed"])*3.78)))
        print("=============================================")
        count = 1
        for each in json_data["route"]["legs"][0]["maneuvers"]:
            if Metrics == "M" or Metrics == "m":
                print(count, ": ", end='')
                print((each["narrative"]) + " (" + str("{:.2f}".format((each["distance"])) + " miles)"))
                count = count + 1
            elif Metrics == "K" or Metrics == "k":
                print(count, ": ", end='')
                print((each["narrative"]) + " (" + str("{:.2f}".format((each["distance"])*1.61) + " km)"))
                count = count + 1
        print("=============================================\n")
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