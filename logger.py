#!/usr/bin/env python3
"""Log handler module."""

import logging
import time
import datetime

__author__ = "S. Vahid Hosseini"
__copyright__ = "Copyright 2019, IOT Module Controller"
__credits__ = ["S. Vahid Hosseini"]
__license__ = "GPL-3.0"
__version__ = "0.1"
__maintainer__ = "S. Vahid Hosseini"
__email__ = "s.vahid.h@behmerd.ir"
__status__ = "Dev"


class Log:

	def __init__(self, sender=""):
		now = datetime.datetime.now()
		logging.basicConfig(filename=("log/" + str(now.year) + str(now.month) + str(now.day) + ".log"),
		                    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)
		self.logger = logging.getLogger(__name__)