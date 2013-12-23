#!/usr/bin/python

"""TCP receiver.

You need to implement NetworkReceived and PacketFromSender functions to do:
-- ACK
-- Retry
-- Handle out of order packets, etc.

You can add other functions and attributes as needed.
"""

class Receiver(object):

  def __init__(self, network_simulator):
    self.network_simulator = network_simulator

  def ApplicationReceived(self, data):
    """No need to do change anything here."""
    print 'RECEIVER: Application Received data %s' % data

  def SendPacketToSender(self, packet):
    """Call this function when you need to send this packet to sender."""
    self.network_simulator.SendToSender(packet)

  def NetworkReceived(self, data):
    print 'RECEIVER: Received data %s over network' % data
    # TODO: Implement TCP here.
    self.ApplicationReceived(data)

  def PacketFromSender(self, packet):
    """This function is called when sender sends a packet to you."""
    pass
    # TODO: Implement this.