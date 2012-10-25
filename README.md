# GoldenKeys
GoldenKeys is a script that will fetch twitter updates from Gearbox employees,
see if the updates contain any SHiFT codes that unlock golden keys (in 
Borderlands 2), and send out a notification email to subscribed individuals.

## Setup:
* `pip install requests`
* Enter your gmail account credentials in config/sendmail.yaml
* Enter the people you wish to notify in config/listserv.yaml
* Add goldenkeys.py to the crontab
* ???
* Profit
