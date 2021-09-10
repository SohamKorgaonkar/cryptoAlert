from app.main import app
import threading
from time import sleep
from firebase import firebase
from pycoingecko import CoinGeckoAPI

"""from Google import Create_Service
import base64
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

CLIENT_SECRET_FILE = 'client_secret.json'
API_NAME = 'gmail'
API_VERSION = 'v1'
SCOPES = ['https://mail.google.com/']

service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)"""

cg=CoinGeckoAPI()
Firebase=firebase.FirebaseApplication("https://kryptotest-ce994-default-rtdb.firebaseio.com/",None)

def get_limit():
    k=cg.get_price(ids='bitcoin',vs_currencies='usd')
    return k['bitcoin']['usd']

def send_email(email_id):
    print("Email Sent")
    pass


def test():
    while True:
        usr_det=Firebase.get('/',"")
        if(usr_det==None):
            pass
        else:
            usr_det=dict(usr_det)
            usr_list=list(usr_det.keys())
            limit=get_limit()
            for i in usr_list:
                t_alert=usr_det[i]['alert']
                check_t=usr_det[i]['status']
                emailid=usr_det[i]['email']
                if(check_t=='Not Triggered' and t_alert==limit):
                    Firebase.put(i,'status',"Triggered")
                    send_email(emailid)
        sleep(10)

                

t1=threading.Thread(target=test)
t1.start()

if __name__ == "__main__":
    app.run(port=8080)