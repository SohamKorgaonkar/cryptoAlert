## Krypto Task Submission File

Deployed on: https://kryptodep.eu-gb.mybluemix.net

# Approach

run.py contains the initialization and threading code for polling values and setting triggers

app/main.py contains the endpoints and their functions

All credentials are to be stored as environment variables (eg. FIREBASE_URL, EMAIL_ID, EMAIL_PASSWORD)

The run.py file runs 2 threads in total, one runs the server and other polls for values and checks for changes in the database. If the value of Bitcoin comes within 50USD of the given value, and email is sent to the user alerting him about the same.


# How to use
The app currently supports only 1  alert per user, adding more than one alert will overwrite the previous one
To add an alert
1. Make a post request on /alerts/create using the given format
2. The user and the alert will be added to database and the polling thread will check if the price of bitcoin in usd matches the given price
3. When there is a match, the sendemail() function is triggered and the status is set to triggered
4. To check all alerts, send a get reqest on /alerts/fetch. It returns the user, alerts and their status
5. Making a POST request at /alerts/reset resets the status back to NotTriggered
6. Multiple requests can be made with same email id and diffierent alerts, but username must be unique.


# Steps to run
1. Install files from requirements.txt (pip install -r requirements.txt)
2. Execute run.py (python run.py)

# API format
Use Post Request

1. To Create User and Alert

    Endpoint: /alerts/create

    {
    "user": username
    "email"emailid
    "alert": price alert
    }

2. To Delete the alert (with user)

    Endpoint: /alerts/delete #Deletes the user

    {
    "user":username
    }

3. To fetch all alerts and their status

    Endpoint: /alerts/fetch

    Send get request to show users and their alerts

4. To reset alerts

    Endpoint: /alerts/reset

    {
    "user": username
    }

    Resets the status of alerts
 
