# -*- coding: utf-8 -*-
# Copyright 2012 Sebastian Alvarez <sebastianmalvarez@gmail.com>
# License: GPL v3
# For further info, see LICENSE file

from random import choice

from lalita import Plugin

class Bardator(Plugin):

	def init(self, config):
		self.users = dict()
		self.register(self.events.COMMAND, self.bard, ['bard'])
		self.bards = [
			u"muchachooo hay que tener cuidadín",
			u"VIRGEN!",
			u"que ágil",
			u"que tipo de mierda",
		]

	def bard(self, user, channel, command, *args):
		for user in args:
			bard = choice(self.bards)
			self.say(channel, u"%s %s", user, bard)
