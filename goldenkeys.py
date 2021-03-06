#!/usr/bin/env python

from lib.twitter_query import TwitterQuery
from lib.mailer import Mailer

"""
Creates a TwitterQuery and a Mailer.  

The TwitterQuery will hit the twitter feeds of Gearbox developers
(listed in config/following.yaml) and see if there are any SHiFT codes.

If TwitterQuery finds juicy delicious golden keys, Mailer notifies
everybody (in config/listserv.yaml) and we all login frantically to unlock
our keys!
"""
def main():
    tq = TwitterQuery()
    code_tweets = tq.query_twitter()
    if code_tweets:
        print "Found some shift codes! Sending mail..."
        mailer = Mailer()
        subject = "SHIFT CODE(S) DETECTED!"
        mailer.mail(subject, "\n".join(code_tweets))

if __name__ == '__main__':
    main()
