# PyStorm RabbitMQ

This is an example about using Apache Storm with Python and RabbitMQ. The example gets words from RabbitMQ 
(from a spout) and counts them (from a bolt). Before running the example you should publish some messages 
to RabbitMQ.


## Prerequisites

- python
- java 7 or higher
- lein 2 or higher

### Python requirements

- streamparse

```
$ pip install streamparse
```
- pika
```
$ pip install pika
```


## Run the example

```
$ cd wordcount
$ streamparse run
```

### Streamparse doc

http://streamparse.readthedocs.org/en/latest/quickstart.html
http://streamparse.readthedocs.org/en/latest/api.html

