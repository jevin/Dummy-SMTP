#!/usr/bin/env python
"""Dummy-SMPT - A noddy fake smtp server

Usage:
  listen.py
  listen.py [--ip=127.0.0.1] [--port=25]
  listen.py (-h | --help)

Options:
  -h --help             Show this screen
  --ip=IP               IP to listen to [default: localhost]
  --port=PORT           Port to bind to [default: 25]

"""

import smtpd
import asyncore
import time
import socket
from email.parser import Parser
from docopt import docopt

class FakeSMTPServer(smtpd.SMTPServer):
    """A Fake smtp server"""

    def __init__(*args, **kwargs):
        smtpd.SMTPServer.__init__(*args, **kwargs)

    def process_message(*args, **kwargs):
        headers = Parser().parsestr(args[4])
        mail = open("mails/"+str(time.time())+".eml", "w")
        print "New mail from " + headers['from'] + " to " + headers['to'] + " - " + headers['subject']
        mail.write(args[4])
        mail.close
        pass

if __name__ == "__main__":
    arguments = docopt(__doc__, version='Dummy-SMTP')

    try:
        smtp_server = FakeSMTPServer((arguments['--ip'], int(arguments['--port'])), None)
        print "Running dummy SMTP server on " + arguments['--ip'] + ":" + arguments['--port']
    except socket.error:
        print "Permission denied to " + arguments['--ip'] + ":" + arguments['--port'] + ". Try using sudo to run this script."

    try:
        asyncore.loop()
    except KeyboardInterrupt:
        smtp_server.close()
