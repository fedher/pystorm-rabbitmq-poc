from __future__ import absolute_import, print_function, unicode_literals

import itertools
from streamparse.spout import Spout

from pika import BlockingConnection, ConnectionParameters
from pika.exceptions import ConnectionClosed


class WordSpout(Spout):

    def initialize(self, stormconf, context):
        self.m2m_conn = BlockingConnection(
            ConnectionParameters(
                host='127.0.0.1',
                port=5672))
        self.channel = self.m2m_conn.channel()
        #self.channel.basic_qos(prefetch_count=1)
        self.channel.queue_bind(exchange="Test", queue="test.queue", routing_key="test.route")

    def next_tuple(self):

        def callback(ch, method, properties, body):
            print (" [x] %r:%r" % (method.routing_key, body,))
            self.log(body)
            self.emit([body])

        try:
            self.channel.basic_consume(callback, queue="test.queue", no_ack=True)

        except ConnectionClosed, e:
            pass