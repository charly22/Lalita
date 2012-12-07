# -*- coding: utf-8 -*-
# Copyright 2012 Sebastian Alvarez <sebastianmalvarez@gmail.com>
# License: GPL v3
# For further info, see LICENSE file

import re
import unicodedata

from random import choice

from lalita import Plugin

class Bardator(Plugin):

	def init(self, config):
		self.users = dict()
		self.register(self.events.COMMAND, self.bard, ['bard'])
		self.register(self.events.PRIVATE_MESSAGE, self.private_bard)
		self.bards = [
			u"muchachooo hay que tener cuidadín",
			u"VIRGEN!",
			u"que ágil",
			u"que tipo de mierda",
		]
		self.specific_bards = {
			u"UG": u"ULTRA GAAAY! http://bit.ly/11RY2CF",
			u"G": u"GAAAAAAY http://bit.ly/127JH4n",
			u"UN": u"ULTRA NEEEERD http://bit.ly/VCfgDn",
			u"AHH": u"AHHHHHHHHHHHHHHHHHHHHHHHHHHHH!!!! http://bit.ly/Uje2WI",
			u"E": u"Entendiiiido http://bit.ly/Uje2WI",
			u"D": u"http://bit.ly/QNdTzb",
		}

	def bard(self, user, channel, command, *args):
		if len(args) > 1:
			user = args[0]
			if len(args) == 2:
				# @bard olapic jorgemudry AHH
				command = args[1]
				self.param_bard(channel, user, command)
			else:
				# @bard olapic jorgemudry
				self.random_bard(channel, user)
		else:
			for user in args:
				self.random_bard(channel, user)
	
	def random_bard(self, channel, user):
		bard = choice(self.bards)
		self.say(channel, u"%s %s", user, bard)


	def private_bard(self, user, message):
		regex = re.compile('^\@bard\s(?P<channel>[\w]+)\s(?P<user>[a-zA-Z0-9\-\_]+)\s?(?:(?P<command>[\w]+))?$')
		r = regex.search(message.strip())
		if r.groupdict():
			channel = r.groupdict()['channel']
			if not channel.startswith("#"):
				channel = "#"+channel
			channel = unicodedata.normalize('NFKD', channel).encode('ascii','ignore')
			user = r.groupdict()['user']
			command = r.groupdict()['command']
			if command:
				self.param_bard(channel, user, command)
			else:
				self.random_bard(channel, user)
	
	def param_bard(self, channel, user, command):
		if command in self.specific_bards:
			bard = self.specific_bards[command]
			self.say(channel, u"%s %s", user, bard)
