#!/usr/bin/python

"""TCP sender.

You need to implement SendDataOverNetwork and PacketFromReceiver functions to do:
-- ACK
-- Retry
-- Handle out of order packets, etc.

"""

class Sender(object):

  def __init__(self, network_simulator):
    self.network_simulator = network_simulator

  def ApplicationSend(self, data):
    """Called by application. No need to do change anything here."""
    print 'SENDER: Application sending data %s' % data
    self.SendDataOverNetwork(data)

  def SendPacketToReceiver(self, packet):
    """Call this function when you need to send this packet to receiver.

    No need to do change anything here.
    """
    self.network_simulator.SendToReceiver(packet)

  def SendDataOverNetwork(self, data):
    print 'SENDER: Sending data %s over network' % data
    # TODO: Implement TCP here.
    self.network_simulator.Send(data)

  def PacketFromReceiver(self, packet):
    """This function is called when receiver sends a packet to you."""
    # TODO: Implement TCP here.
    pass