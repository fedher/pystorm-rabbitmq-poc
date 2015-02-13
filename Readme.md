# PyStorm RabbitMQ

This is an example about using Apache Storm with Python and RabbitMQ. The example get words from RabbitMQ 
(from a spout) and count them (from a bolt). Before running the example you should publish some messages 
to RabbitMQ.


## Prerequisites

- python
- java 7 or higher
- lein 2 or higher
- streamparse

```
$ pip install streamparse
```


## Run the example

```
$ cd wordcount
$ streamparse run
```

### Streamparse doc

https://github.com/Parsely/streamparse/blob/master/doc/source/quickstart.rst


