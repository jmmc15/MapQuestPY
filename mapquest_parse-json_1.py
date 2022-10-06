import urllib.parse
import requests

main_api = "https://www.mapquestapi.com/directions/v2/route?"
orig = "Washington, D.C."
dest = "Baltimore, Md"

# orig = "Rome, Italy"
# dest = "Frascati, Italy"
key = "NGO5fCSo59YyPyHEbC3q01BKlhM9knpU" #Replace with your MapQuest key

url = main_api + urllib.parse.urlencode({"key":key, "from":orig, "to":dest})

json_data = requests.get(url).json()
print(json_data)