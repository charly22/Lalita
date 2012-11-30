# -*- coding: utf-8 -*-
# Copyright 2009 laliputienses
# License: GPL v3
# For further info, see LICENSE file

import random

from lalita import Plugin

class Empernator(Plugin):

	def init(self, config):
		self.register(self.events.COMMAND, self.empern, ['empern'])

	def empern(self, user, channel, *args):
		auser = 'aseba'
		self.say(channel, u"I empern %s", auser)

