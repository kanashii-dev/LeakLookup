# LeakCheck Lookup
# Checks to see if your password has been leaked by recent breaches and what info was made available.
# Make sure you have a LeakCheck account, and your IP is binded to the API.

import os, requests, json, sys

api_key = "" #Enter your api key from leakcheck here :)

def Lookup(data, data_type):
    if api_type == "public" or api_type == "Public":
        url = f" https://leakcheck.net/api/public?key={api_key}&check={data}"
    elif api_type == "extended" or api_type == "Extended":
        url = f"https://leakcheck.net/api?key={api_key}&check={data}&type={data_type}"

    lookup_start = requests.get(url)
    if lookup_start.status_code == 429:
        print("Searching too fast!")
    else:
        json_data = lookup_start.text #Initializing JSON data.
        obj = json.loads(json_data) #Creating Python object from JSON data.
        json_formatted_str = json.dumps(obj, indent=2)
        print(json_formatted_str) #Print pretty JSON response :)

if __name__ == "__main__":
    os.system("clear")
    api_type = input("[?] API TYPES [?]\n[+] Public\n[+] Extended\n[?] Choose API Type: ")
    os.system("clear")

    data_type_selection1 = "[*] Please select one of the data types below: \n[-] Email\n[-] Username\n[-] Minecraft Username\n[-] Phone Number\n[-] Auto (Auto Detects Input)"
    data_type_selection2 = "[*] Please select one of the data types below: \n[-] Email\n[-] Username\n[-] Email By Hash"

    if api_type == "public" or api_type == "Public":
        print(data_type_selection2) #returns selections for the Public API
    if api_type == "extended" or api_type == "Extended":
        print(data_type_selection1) #returns selections for the Extended API

    data_type = input(str("[?] Select a Data Type: "))
    os.system("clear")

    data = input(str(f"[?] Enter {data_type}: "))
    Lookup(data, data_type)