import json, os, django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "admin.settings")
django.setup()

import pika

from products.models import Product

params = pika.URLParameters('amqps://xqbyrygw:K4uJY042J_QmJQlsPlrzNYYOq73NiXTx@rat.rmq2.cloudamqp.com/xqbyrygw')
connection = pika.BlockingConnection(params)
channel = connection.channel()
channel.queue_declare(queue='admin')


def callback(ch, method, properties, body):
    print("received in admin")
    data = json.loads(body)
    print(data)
    product = Product.object.get(id=data)
    product.likes = product.likes + 1
    product.save()
    print("product likes")


channel.basic_consume(queue='admin', on_message_callback=callback, auto_ack=True)

print('started Consuming')
channel.start_consuming()

channel.close()
