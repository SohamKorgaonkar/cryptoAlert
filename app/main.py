from flask import Flask
from flask.wrappers import Request
from flask import request
from firebase import firebase
import json

Firebase=firebase.FirebaseApplication("https://kryptotest-ce994-default-rtdb.firebaseio.com/",None)

app = Flask(__name__)
 
@app.route('/')
def landing_page():
    return """<h1>Welcome to my crypto Alert API</h1>
    <p>For more info go to <a href="https://github.com/SohamKorgaonkar/cryptoAlert">https://github.com/SohamKorgaonkar/cryptoAlert</a></p>"""

@app.route('/alerts/create',methods=["POST"])
def create_alert():
    create_new=request.get_json()
    user=create_new['user']
    email=create_new['email']
    alert=create_new['alert']
    Firebase.put(user,'username',user)
    Firebase.put(user,'email',email)
    Firebase.put(user,'alert',alert)
    Firebase.put(user,'status','Not Triggered')
    return 'Alert Created'

@app.route('/alerts/delete',methods=["POST"])
def delete_alert():
    delate_user=request.get_json()
    user=delate_user['user']
    Firebase.delete("/",user)
    return 'Alert Deleted'

@app.route('/alerts/fetch')
def fetch_alerts():
    num_users=Firebase.get("/","")
    return num_users

@app.route('/alerts/reset',methods=["POST"])
def reset_alert():
    change_state=request.get_json()
    user=change_state['user']
    Firebase.put(user,'status','Not Triggered')
    return 'Alert Reset'