#!/usr/bin/env python3
"""Login module file. Authorizing valid users"""

import time
import logging
import datetime

from dbhelper import DBHelper

__author__ = "S. Vahid Hosseini"
__copyright__ = "Copyright 2019, IOT Module Controller"
__credits__ = ["S. Vahid Hosseini"]
__license__ = "GPL-3.0"
__version__ = "0.1"
__maintainer__ = "S. Vahid Hosseini"
__email__ = "s.vahid.h@behmerd.ir"
__status__ = "Dev"


class Login:

	def __init__(self):
		self.database = DBHelper()

	def login(self, user, password):
		account = database.get_user(user["id"])
		if account is None:
			return None
		elif account["password"] == password:
			


	def status(self, user):
		pass