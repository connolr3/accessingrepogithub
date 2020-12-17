import requests 
import json
username = 'connolr3'

# from https://github.com/user/settings/tokens
# authentication to GitHub when using the GitHub API
token = '4522a920d8697c0bf680ebe7fe50ccbd96f2df05'

# create a re-usable session object with the user creds in-built
gh_session = requests.Session()
gh_session.auth = (username, token)

# get the list of repos belonging to me
repos_url = 'https://api.github.com/user/repos'
repos = json.loads(gh_session.get(repos_url).text)

# print the repo names
print ("Repo Names")
i = 0
for repo in repos:
    print (repos[i]['name'])
    i+=1

# get my user details
user_url = 'https://api.github.com/user'
user = json.loads(gh_session.get(user_url).text)

#PRINT USER DETAILS
print ("Name: "+user["name"])
print ("Username: "+user["login"])
print ("URL: "+user["url"])
print ("Bio: "+user["bio"])
print ("Following (no. accounts):" + str(user["following"]))
print ("Creation Date: "+user["created_at"])

