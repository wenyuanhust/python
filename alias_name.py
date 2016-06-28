try:

	import cStringIO as cStringIO
except ImportError:
	import StringIO

try:
	import json
except ImportError:
	import simplejson as json

def _private_1(name):
	return 'Hello, %s' % name

def greeting(name):
	if len(name) > 3:
		return _private_1(name)
	else:
		pass