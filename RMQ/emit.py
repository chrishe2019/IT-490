#!/usr/bin/env python
import pika
import sys
import datetime

today = datetime.date.today;
todaystr = datetime.datetime.now().strftime("%I:%M%p on %B %d, %Y")
credentials = pika.PlainCredentials('admin','password')
connection = pika.BlockingConnection(pika.ConnectionParameters('192.168.0.8' , 5672 , "VHOST1", credentials))
channel = connection.channel()

channel.exchange_declare(exchange='logs',
                         exchange_type='fanout')

message = ' '.join(sys.argv[1:]) or "info: Hi"
channel.basic_publish(exchange='logs',
                      routing_key='',
                      body='log queue test at ' + todaystr)
print(" [x] Sent %r" % message)
connection.close()
