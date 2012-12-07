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
			u"UG": u"http://i2.kym-cdn.com/entries/icons/original/000/008/910/ultra-gay.png",
			u"G": u"http://media.tumblr.com/tumblr_m9g64idfjp1qbnggp.jpg",
			u"UN": u"http://cdn.memegenerator.net/instances/400x/23940800.jpg",
			u"AHH": u"http://www.youtube.com/watch?v=xCoD-TELD0A",
		}

	def bard(self, user, channel, command, *args):
		if(len(args) > 1):
			# @bard olapic jorgemudry AHH
			channel = args[0]
			user = args[1]
			command = args[2]
			self.param_bard(channel, user, command)
		else:
			for user in args:
				self.random_bard(channel, user)
	
	def random_bard(self, channel, user):
		bard = choice(self.bards)
		channel = unicodedata.normalize('NFKD', channel).encode('ascii','ignore')
		self.say(channel, u"%s %s", user, bard)

	
	def private_bard(self, user, message):
		regex = re.compile('^\@bard\s(?P<channel>[\w]+)\s(?P<user>[a-zA-Z0-9\-\_]+)\s?(?:(?P<command>[\w]+))?$')
		r = regex.search(message.strip())
		if r.groupdict():
			channel = r.groupdict()['channel']
			if not channel.startswith("#"):
				channel = "#"+channel
			user = r.groupdict()['user']
			command = r.groupdict()['command']
			if command:
				self.param_bard(channel, user, command)
			else:
				self.random_bard(channel, user)
	
	def param_bard(self, channel, user, command):
		if command in self.specific_bards:
			bard = self.specific_bards[command]
			channel = unicodedata.normalize('NFKD', channel).encode('ascii','ignore')
			self.say(channel, u"%s %s", user, bard)
