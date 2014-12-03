yodasms
=======

Translates a message to Yoda and sms them to your friends

To install.

1. create a new virtual env and install the requirements.txt
example
virtualenv yodasmsenv
pip install -r /path/to/yodasms/requirements.txt

2. create a folder next to yodasms called 'conf', this is where the configuration file will go
fill in the empty 'apimashupconf.ini with your information and place in this folder

3. Run server with
python manage.py runserver
now navigate your browser to 127.0.0.1:8000 and start sending messages!