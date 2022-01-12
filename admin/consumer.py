import pika

params = pika.URLParameters('amqps://xqbyrygw:K4uJY042J_QmJQlsPlrzNYYOq73NiXTx@rat.rmq2.cloudamqp.com/xqbyrygw')
connection = pika.BlockingConnection(params)
channel = connection.channel()
channel.queue_declare(queue='admin')


def callback(ch, method, properties, body):
    print("received in admin")
    print(body)


channel.basic_consume(queue='admin', on_message_callback=callback,auto_ack=True)

print('started Consuming')
channel.start_consuming()

channel.close()