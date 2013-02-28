Dummy-SMTP
==========

A dummy Linux SMTP server that drops emails to a folder, instead of sending them.

Allows optional options from the command line:

Usage:

  listen.py
  
  listen.py [--ip=127.0.0.1] [--port=25]
  
  listen.py (-h | --help)

Options:

  -h --help             Show this screen
  
  --ip=IP               IP to listen to [default: localhost]
  
  --port=PORT           Port to bind to [default: 25]
