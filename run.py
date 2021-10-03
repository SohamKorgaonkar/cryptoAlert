from app.main import app
import threading
from time import sleep
from firebase import firebase
from pycoingecko import CoinGeckoAPI
import os
import smtplib

email_id=str(os.getenv("EMAIL_ID"))
password=str(os.getenv("EMAIL_PASSWORD"))
print(email_id)
print(password)
cg=CoinGeckoAPI()
Firebase=firebase.FirebaseApplication(str(os.getenv('FIREBASE_URL')),None)
port = int( os.getenv( 'PORT', 8000 ) )

def get_limit():
    k=cg.get_price(ids='bitcoin',vs_currencies='usd')
    return k['bitcoin']['usd']

def send_email(email_id1,limit):
    with smtplib.SMTP('smtp.gmail.com',587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()
        smtp.login(email_id,password)
        subject="Crypto API Alert Triggered"
        body="The value of bitcoin has reached near the specified value of "+str(limit)+" USD"
        msg=f'Subject: {subject}\n\n{body}'
        smtp.sendmail(email_id,email_id1,msg)
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
            print(limit)
            for i in usr_list:
                t_alert=usr_det[i]['alert']
                check_t=usr_det[i]['status']
                emailid=usr_det[i]['email']
                if(check_t=='Not Triggered' and (int(t_alert)<=limit+50 and int(t_alert)>=limit-50)):
                    Firebase.put(i,'status',"Triggered")
                    send_email(emailid,limit)
        sleep(10)

                

t1=threading.Thread(target=test)
t1.start()

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=port)