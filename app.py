import requests
import json

with open("keys.json", "r") as f:
	keys = json.load(f)
	AUTH = { "api_key": keys["tmdb"] }

def getShow(id):
	def populate(show):
		for i in range(len(show["seasons"])):
			show["seasons"][i] = json.loads(requests.get("https://api.themoviedb.org/3/tv/" + str(show["id"]) + "/season/" + str(show["seasons"][i]["season_number"]), data=AUTH).text)
		return show

	r = requests.get("https://api.themoviedb.org/3/tv/" + id, data=AUTH)
	return populate(json.loads(r.text))

def getStructure(show):
	return { season["season_number"]: [episode["name"] for episode in season["episodes"]] for season in show["seasons"] }

with open("structure.out", "w") as f:
	json.dump(getStructure(getShow("60572")), f, indent=2)
