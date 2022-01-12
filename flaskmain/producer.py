# amqps://xqbyrygw:K4uJY042J_QmJQlsPlrzNYYOq73NiXTx@rat.rmq2.cloudamqp.com/xqbyrygw
import json

import pika

params = pika.URLParameters('amqps://xqbyrygw:K4uJY042J_QmJQlsPlrzNYYOq73NiXTx@rat.rmq2.cloudamqp.com/xqbyrygw')
connection = pika.BlockingConnection(params)
channel = connection.channel()


def publish(method, body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange='', routing_key='admin', body=json.dumps(body),properties=properties)
