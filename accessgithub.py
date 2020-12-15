import requests 
import json
username = 'connolr3'

# from https://github.com/user/settings/tokens
token = 'c56bcd3455453fb6d266e72b0b8611084a519edc'

# create a re-usable session object with the user creds in-built
gh_session = requests.Session()
gh_session.auth = (username, token)

# get the list of repos belonging to me
repos_url = 'https://api.github.com/user/repos'
repos = json.loads(gh_session.get(repos_url).text)

# print the repo names

i = 0
for repo in repos:
    print (repos[i]['name'])
    i+=1

# get my user details
user_url = 'https://api.github.com/user'
user = json.loads(gh_session.get(user_url).text)

print (user["name"])
print (user["login"])
print (user["url"])
print (user["bio"])
print (user["following"])
print (user["created_at"])

