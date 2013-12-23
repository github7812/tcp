#!/usr/bin/python

"""A test module to test receiver and sender.

No need of implementing anything here.
"""

import sender
import receiver
import random

class NetworkSimulator(object):

  def __init__(self):
    self.recv = None
    self.send = None
    self.datas = []

  def Send(self, data):
    self.datas.append(data)

  def Flush(self):
    random.shuffle(self.datas)
    for data in self.datas:
      self.recv.NetworkReceived(data)

  def SendToSender(self, packet):
    self.send.PacketFromReceiver(packet)

  def SendToReceiver(self, packet):
    self.recv.PacketFromSender(packet)


sim = NetworkSimulator()
recv = receiver.Receiver(sim)
send = sender.Sender(sim)
sim.recv = recv
sim.send = send

send.ApplicationSend('a string')
send.ApplicationSend(2)
send.ApplicationSend(True)

sim.Flush()
