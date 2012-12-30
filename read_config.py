#!/usr/bin/env python

'''
PyASB launcher module

Concatenate processes
____________________________

This module is part of the PyASB project, 
created and maintained by Miguel Nievas [UCM].
____________________________
'''

try:
	import ephem
except:
	print 'One or more modules missing: pyephem'
	raise SystemExit

__author__ = "Miguel Nievas"
__copyright__ = "Copyright 2012, PyASB project"
__credits__ = ["Miguel Nievas"]
__license__ = "GNU GPL v3"
__shortname__ = "PyASB"
__longname__ = "Python All-Sky Brightness pipeline"
__version__ = "1.99.0"
__maintainer__ = "Miguel Nievas"
__email__ = "miguelnr89[at]gmail[dot]com"
__status__ = "Prototype" # "Prototype", "Development", or "Production"


class ConfigOptions():
	def __init__(self,config_file):
		self.FileOptions = {}
		self.read_config_file(config_file)
	
	''' Add and remove options '''
	def add_option(param,value):
		self.FileOptions.append([param,value])
	def remove_option(param,value):
		self.FileOptions.pop([param,value])
	
	def add_param_value(textline):
		line_split = raw_config[textline].split("=")
		param = line_split[0].replace(' ','')
		value = line_split[1]
		if '"' not in value and "'" not in value:
			value = value.replace(' ','')
		value = value.replace('"','')
		value = value.replace("'",'')
		value = value.replace('\r','')
		value = value.replace('\n','')
		self.add_option(param,value)
		
	def read_config_file(self,config_file):
		raw_config = open(config_file, 'r').readlines()
		for line in xrange(len(raw_config)):
			raw_config[line] = raw_config[line].replace("\n","")
			if len(raw_config[line].split("=")) == 2:
				if raw_config[line][0]!="#":
					self.add_param_value(raw_config[line])

# Setup Pyephem Observatory
def pyephem_setup(ImageInfo):
	ObsPyephem = ephem.Observer()
	ObsPyephem.pressure = 0 # Dont consider atmospheric effects for now
	ObsPyephem.elevation = 700
	ObsPyephem.lat = ImageInfo.latitude*pi/180# '40.450941' # From cielosdemadrid webpage
	ObsPyephem.lon = ImageInfo.longitude*pi/180#'-3.726065'
	return ObsPyephem
	