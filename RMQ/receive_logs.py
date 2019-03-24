import pika
credentials = pika.PlainCredentials('admin','password')
connection = pika.BlockingConnection(pika.ConnectionParameters('192.168.0.8' , 5672 , "VHOST1", credentials))
channel = connection.channel()

channel.exchange_declare(exchange='logs',
			exchange_type='fanout')

##result = channel.queue_declare(exclusive=True)

channel.queue_declare(queue='logqueue')


##queue_name = result.method.queue

channel.queue_bind(exchange='logs',
			queue='logqueue')

print(' [*] Waiting for logs. To exit press CTRL+C')

def callback(ch, method, properties, body):
	print(" [x] %r" % body)

channel.basic_consume(callback,
			queue='logqueue',
			no_ack=True)

channel.start_consuming()
 

