# -*- coding: utf-8 -*-

import datetime
import itertools
import random

from celery import Celery


def random_failover_strategy(servers):
    it = list(servers)  # don't modify callers list
    print "Shuffling"
    random.shuffle(it)
    for i in itertools.cycle(it):
        print "Looping", i
        yield i


BROKER_URL = [
    'amqp://admin:admin@localhost:5672',
    'amqp://admin:admin@localhost:6672',
    'amqp://admin:admin@localhost:7672',
]

app = Celery('tasks', broker=BROKER_URL)


# app.conf.BROKER_FAILOVER_STRATEGY = 'shuffle'
app.conf.BROKER_FAILOVER_STRATEGY = random_failover_strategy
app.conf.CELERY_DEFAULT_QUEUE = "celery-%s" % datetime.datetime.now()
