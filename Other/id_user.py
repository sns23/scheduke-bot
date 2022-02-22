import requests

API_LINK = "https://api.telegram.org/bot5167627424:AAFGOxsZa3YH4egdKF2FjDBsrsbh37rhqRs"
updates = requests.get(API_LINK+'/getUpdates').json()

print(updates)