#!/usr/bin/python

"""A test module to test receiver and sender.

No need of implementing anything here.
"""

import sender
import receiver
import random

class NetworkSimulator(object):

  def __init__(self, receiver):
    self.receiver = receiver
    self.datas = []

  def Send(self, data):
    self.datas.append(data)

  def Flush(self):
    random.shuffle(self.datas)
    for data in self.datas:
      self.receiver.NetworkReceived(data)


recv = receiver.Receiver()
sim = NetworkSimulator(recv)
send = sender.Sender(sim)

send.ApplicationSend(1)
send.ApplicationSend(2)
send.ApplicationSend(3)

sim.Flush()
