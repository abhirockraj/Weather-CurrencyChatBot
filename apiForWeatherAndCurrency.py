import requests
## Weather info api
url = "https://forecast9.p.rapidapi.com/rapidapi/forecast/Patna/summary/"

headers = {
	"X-RapidAPI-Key": "48290658dfmsh63b6d043595c405p115375jsncfe5ed7a09e9",
	"X-RapidAPI-Host": "forecast9.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers)

print(response.json())


## Currency converter


url= "https://v6.exchangerate-api.com/v6/a497ae15e6c403a25c88f15d/latest/INR"
response = requests.request("GET", url, headers=headers)

print(response.text)



























