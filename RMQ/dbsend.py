#!/usr/bin/env python
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='logqueue')

channel.basic_publish(exchange='',
                      routing_key='logqueue',
                      body='Log queue test')
print(" FrontEnd Sent 'Request'")

connection.close()
