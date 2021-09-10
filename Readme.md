## Krypto Task Submission File

Deployed on: https://git.heroku.com/kryptotask.git

Steps to run
1. Install files from requirements.txt
2. Execute run.py

API format
Use Post Request

/alerts/create
{
"user": username
"email"emailid
"alert": price alert
}


/alerts/delete #Deletes the user
{
"user":username
}


/alerts/fetch
Send get request to show users and their alerts

Database used: Google Firebase

Email not working yet but event is triggered

Used threading instead of salery due to time constrains
 
