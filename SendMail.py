import smtplib
from email.mime.text import MIMEText

class SendMail:
    from_adr ="from mailadr"
    passwd = "password"
    to_adr = "to mailadr"

    msg = MIMEText("body")

    def __init__(self,adr,pw,to):
        self.from_adr = adr
        self.passwd = pw
        self.to_adr = to

    def sendMail(self):
        if self.msg == None:
            print('set msg!')
            return None

        self.msg['From'] = self.from_adr
        self.msg['To'] = self.to_adr

        s = smtplib.SMTP('smtp.gmail.com',587)
        s.ehlo()
        s.starttls()
        s.ehlo()
        s.login(self.from_adr,self.passwd)
        s.send_message(self.msg)
        s.close()

    def txtConvertString(self,path):
        f = open(path,'r')
        st = f.read()
        return st

    def setMsg(self,title,body):
        self.msg = MIMEText(body)
        self.msg['Subject'] = title

if __name__ == '__main__':

    fadr = "xxxxxxxxxx@gmail.com" 
    pwd = "xxxxxxxxxxx"
    tadr = "xxxxxxxxxx@gmail.com"

    sm = SendMail(fadr,pwd,tadr)
    sm.setMsg("test",sm.txtConvertString("text.txt"))
    sm.sendMail()
