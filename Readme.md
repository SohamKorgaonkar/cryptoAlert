## Krypto Task Submission File

Deployed on: https://kryptodep.eu-gb.mybluemix.net    #Not working properly but deploys on localhost

# Approach
Used flask to setup the endpoints. Couldnt setup celery due to time constrains but used threading instead to poll for values. Email service not working hence code is commented, tried using gmail api.

Firebase was used as the database to store user credentials and other info.

The venv folder contains the working environment for python.

run.py contains the initialization and threading code for polling values and setting triggers

app/main.py contains the endpoints and their functions

# How to use
The app currently supports only 1  alert per user, adding more than one alert will overwrite the previous one
To add an alert
1. Make a post request on /alerts/create using the given format
2. The user and the alert will be added to database and the polling thread will check if the price of bitcoin in usd matches the given price
3. When there is a match, the sendemail() function is triggered (Does nothing for now) and the status is set to triggered
4. To check all alerts, send a get reqest on /alerts/fetch. It returns the user, alerts and their status
5. Making a POST request at /alerts/reset resets the status back to NotTriggered


# Steps to run
1. Install files from requirements.txt
2. Execute run.py

# API format
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

/alerts/reset

{
"user": username
}

Resets the status of alerts
 
