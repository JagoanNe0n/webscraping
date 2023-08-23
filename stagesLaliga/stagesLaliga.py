import requests

url = "https://prod-public-api.livescore.com/v1/api/app/stage/soccer/spain/laliga/7"

querystring = {"MD":"1","countryCode":"ID"}

payload = ""
headers = {"User-Agent": "Insomnia/2023.5.5"}

response = requests.request("GET", url, data=payload, headers=headers, params=querystring)
jsondata = response.json()

# klasemen = jsondata['Stages'][0]['LeagueTable']['L'][0]['Tables']

''''------------------------------------------------------------'''

response = requests.request("GET", url, data=payload, headers=headers, params=querystring)
jsondata = response.json()

stages = jsondata['Stages']

for stage in stages:
    klasemen = stage['Snm']
    tables = stage['LeagueTable']['L'][0]['Tables'][0]['team']
    
    for team in tables:
        ranking = team['rnk']
        club = team['Tnm']
        menang = team['win']
        kalah = team['wot']
        total = team['ptsn']
        
        print(f"klasemen {klasemen} === peringkat {ranking} {club}, Menang : {menang}, Kalah : {kalah}, Total Nilai : {total}")
