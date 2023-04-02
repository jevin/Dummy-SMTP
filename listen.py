#!/usr/bin/env python
# Original script written by Stuart Colville: http://muffinresearch.co.uk/archives/2010/10/15/fake-smtp-server-with-python/
"""A noddy fake smtp server."""
import os
import sys
import smtpd
import asyncore
import time

class FakeSMTPServer(smtpd.SMTPServer):
    """A Fake smtp server"""

    def __init__(*args, **kwargs):
        print "Running fake smtp server on smtp://" + str(locals()['args'][1][0]) + ":" + str(locals()['args'][1][1])
        smtpd.SMTPServer.__init__(*args, **kwargs)

    def process_message(*args, **kwargs):
        fileLoc = os.path.dirname(__file__)+"/mails/"+str(time.time())+".eml"
        mail = open(fileLoc, "w")
        print "New mail from " + args[2] + " => " + fileLoc
        mail.write(args[4])
        mail.close
        pass

if __name__ == "__main__":
    port = 25
    if len(sys.argv) == 2:
        try:
            port = int(sys.argv[1])
        except:
            print("port must be integer, unknown value("+sys.argv[1]+") provided. default port 25 will be used")

    smtp_server = FakeSMTPServer(('localhost', port), None)
    try:
        asyncore.loop()
    except KeyboardInterrupt:
        smtp_server.close()
