# GoldenKeys
GoldenKeys is a script that will fetch twitter updates from Gearbox employees,
see if the updates contain any SHiFT codes that unlock golden keys (in 
Borderlands 2), and send out a notification email to subscribed individuals.

## I'm doing it the wrong way
Listen, I know that this does a lot of redundant parsing, that it should
subscribe to a feed rather than keep hitting the same user over and over, but
this is an emergency!

## Setup:
* Enter your gmail account credentials in config/sendmail.yaml
* Enter the people you wish to notify in config/listserv.yaml
* Add goldenkeys.py to the crontab
* ???
* Profit
