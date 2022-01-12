import json

import pika

from main import Product, db

params = pika.URLParameters('amqps://xqbyrygw:K4uJY042J_QmJQlsPlrzNYYOq73NiXTx@rat.rmq2.cloudamqp.com/xqbyrygw')
connection = pika.BlockingConnection(params)
channel = connection.channel()
channel.queue_declare(queue='main')


def callback(ch, method, properties, body):
    print("received in admin")
    data = json.loads(body)
    print(data)
    if properties.content_type == 'product_created':
        product = Product(id=data["id"], title=data["title"], image=data["image"])
        db.session.add(product)
        db.session.commit()
        print('product_created')
    elif properties.content_type == 'product_update':
        product = Product.query.get(data["id"])
        product.title = data["title"]
        product.image = data["image"]
        db.session.commit()
        print('product_update')

    elif properties.content_type == 'product_deleted':
        product = Product.query.get(data)
        db.session.delete(product)
        db.session.commit()
        print('product_deleted')


channel.basic_consume(queue='main', on_message_callback=callback, auto_ack=True)

print('started Consuming')
channel.start_consuming()

channel.close()
