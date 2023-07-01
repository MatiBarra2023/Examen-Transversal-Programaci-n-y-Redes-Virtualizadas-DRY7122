import urllib.parse
import requests
import datetime
main_api = "https://www.mapquestapi.com/directions/v2/route?"
key = "UmeMH4iEK6DBdkUdhGfrBB1IjgHCvKLt"

while True:
    orig = input("Ciudad origen: ")
    if orig == "quit" or orig == "s":
        break
    dest = input("Ciudad destino: ")
    if dest == "quit" or dest == "s":
        break
    url = main_api + urllib.parse.urlencode({"key": key, "from":orig, "to":dest})
    print("URL: " + (url))
    json_data = requests.get(url).json()
    json_status = json_data["info"]["statuscode"]

    if json_status == 0:
        print("API Status: " + str(json_status) + " = A successful route call.\n")
        print("=============================================")
        print("Direcciones de " + (orig) + " a " + (dest))
        print("Duracion del viaje:   " + (json_data["route"]["formattedTime"]))
        print("Kilometros:      " + str("{:.1f}".format((json_data["route"]["distance"])*1.61)))
        print("=============================================")
        print("=============================================")
        for each in json_data["route"]["legs"][0]["maneuvers"]:
            print((each["narrative"]) + " (" + str("{:.1f}".format((each["distance"])*1.61) + " km)"))
        print("=============================================\n")