import requests

print('\nPlease type a word to see its synonyms...')
inputWord = input('Type: ')

url = f"https://wordsapiv1.p.rapidapi.com/words/{inputWord}/synonyms"

headers = {
	"X-RapidAPI-Key": # "TYPE HERE YOUR OWN API KEY",
	"X-RapidAPI-Host": "wordsapiv1.p.rapidapi.com"
}

response = requests.get(url, headers=headers)

print(response.json())