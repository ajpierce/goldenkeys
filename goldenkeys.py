#!/usr/bin/env python

#from lib.twitter_query import TwitterQuery
from lib.mailer import Mailer

"""
Creates a TwitterQuery and a Mailer.  

The TwitterQuery will hit the API
of Gearbox Devs (listed in config/following.yaml) and see if there are any
SHiFT codes.

If TwitterQuery finds juicy delicious golden keys, Mailer notifies
everybody (in config/listserv.yaml) and we all login frantically to try and
get more keys.
"""
def main():
    #tq = TwitterQuery()
    mailer = Mailer()
    mailer.mail(
        'Test Subject',
        'Look, you just got a test email from piercebot!'
    )

if __name__ == '__main__':
    main()
