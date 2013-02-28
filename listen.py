#!/usr/bin/env python
# Original script written by Stuart Colville: http://muffinresearch.co.uk/archives/2010/10/15/fake-smtp-server-with-python/
"""A noddy fake smtp server."""

import smtpd
import asyncore
import time
from email.parser import Parser

class FakeSMTPServer(smtpd.SMTPServer):
    """A Fake smtp server"""

    def __init__(*args, **kwargs):
        print "Running fake smtp server on port 25"
        smtpd.SMTPServer.__init__(*args, **kwargs)

    def process_message(*args, **kwargs):
        headers = Parser().parsestr(args[4])
        mail = open("mails/"+str(time.time())+".eml", "w")
        print "New mail from " + headers['from'] + " to " + headers['to'] + " - " + headers['subject']
        mail.write(args[4])
        mail.close
        pass

if __name__ == "__main__":
    smtp_server = FakeSMTPServer(('localhost', 25), None)
    try:
        asyncore.loop()
    except KeyboardInterrupt:
        smtp_server.close()
