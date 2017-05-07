import email
import time
import imaplib
import pyzmail
from Windows import *


last_checked = None
i = None
status = None
attachments = {}
address = None
password = None


def sign_in():
    global address, password, status, i
    address, password = read_from_database()
    try:
        i = imaplib.IMAP4_SSL("imap.gmail.com")
        a, b = i.login(address, password)
        status = True
    except:
        status = False


if "downloads" not in os.listdir(os.getcwd()):
    global i, status, address, password
    os.mkdir("downloads")
    MessageBox("Hey, thanks for using me!! \n I'll notify you of every message so you won't miss a thing!! \n \
    You can switch me off with the main window!! \n It will be available after account verification!!", "NEXT", "green")
    account = SetAccount()
    address, password = read_from_database()
    sign_in()
    while not status:
        MessageBox("Please manually sign in your gmail account and \n turn on access for less secure apps \n \
and then click next", "NEXT", "green")
        sign_in()
    m = MarkWindow( "All messages must first be marked as seen", "green", i)
    MessageBox("Thank you for using Unotify \n \
    if you face some problems with Unotify \n \
    please report to \n \
    prajapatiutxav@gmail.com \n \
    Thank you", "NEXT", "green")
    i.logout()
    f = open("switch", "w")
    f.write("True")
    f.close()
    MessageBox("Please restart your device", "NEXT", "green")


while True:
    f = open("switch")
    switch = f.read().rstrip()
    f.close()
    if switch == "True":
        if last_checked:
            if time.time()-last_checked >= 180:
                sign_in()
        else:
            last_checked = time.time()
            sign_in()
        if status:
            i.select("INBOX")
            sys, UIDS = i.search(None, '(UNSEEN)')
            for msgs in UIDS[0].split():
                sys, msg = i.fetch(msgs, "(RFC822)")
                email_msg = email.message_from_string(msg[0][1])
                pyzmail_msg = pyzmail.PyzMessage.factory(msg[0][1])
                sender = pyzmail_msg.get_addresses("from")[0]
                subject = pyzmail_msg.get_subject()
                for part in email_msg.walk():
                    if part.get_content_maintype() == "multipart":
                        continue
                    if part.get("Content-Disposition") is None:
                        continue
                    fileName = part.get_filename()
                    attachments[fileName] = part.get_payload(decode=True)
                Notification(sender, subject, attachments)
                attachments = {}
            i.logout()
            i = None
            status = None









