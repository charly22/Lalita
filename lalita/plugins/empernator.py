# -*- coding: utf-8 -*-
# Copyright 2009 laliputienses
# License: GPL v3
# For further info, see LICENSE file

from random import choice

from lalita import Plugin

class Empernator(Plugin):

	def init(self, config):
		self.users = dict()
		self.register(self.events.COMMAND, self.empern, ['empern'])
		self.register(self.events.PUBLIC_MESSAGE, self.add_user)
		self.register(self.events.JOIN, self.add_user)
		self.register(self.events.LEFT, self.rm_user)
		self.register(self.events.ACTION, self.add_user)

	def empern(self, user, channel, *args):
		if not self.users or not self.users[channel]:
			self.say(channel, u"I have no people to empern")
		else:
			auser = choice(self.users[channel])
			self.say(channel, u"I empern %s", auser)
	
	def rm_user(self, user, channel, *args):
		if channel in self.users:
			if user in self.users[channel]:
				self.users[channel].pop(self.users[channel].index(user))

	def add_user(self, user, channel, *args):
		if channel in self.users:
			if not user in self.users[channel]:
				self.users[channel].append(user)
		else:
			self.users[channel] = list()
			self.users[channel].append(user)
