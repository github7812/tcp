#!/usr/bin/python

"""TCP sender.

You need to implement SendDataOverNetwork function to do:
-- ACK
-- Retry
-- Handle out of order packets, etc.

"""

class Sender(object):

  def __init__(self, network_simulator):
    self.network_simulator = network_simulator

  def ApplicationSend(self, data):
    print 'SENDER: Application sending data %s' % data
    self.SendDataOverNetwork(data)

  def SendDataOverNetwork(self, data):
    print 'SENDER: Sending data %s over network' % data
    # TODO: Implement TCP here.
    self.network_simulator.Send(data)
