from __future__ import unicode_literals

import logging

FORMAT = '%(asctime)-15s %(level)s %(message)s'
logging.basicConfig(format=FORMAT)
logger = logging.getLogger()
logger.setLevel(logging.INFO)
