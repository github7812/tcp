#!/usr/bin/python

"""TCP receiver.

You need to implement NetworkReceived function to do:
-- ACK
-- Retry
-- Handle out of order packets, etc.

You can add other functions and attributes as needed.
"""

class Receiver(object):

  def __init__(self):
    pass

  def NetworkReceived(self, data):
    print 'RECEIVER: Received data %s over network' % data
    # TODO: Implement TCP here.
    self.ApplicationReceived(data)

  def ApplicationReceived(self, data):
    print 'RECEIVER: Application Received data %s' % data
