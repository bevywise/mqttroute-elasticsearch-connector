################################################################
# @Bevywise.com IOT Initiative. All rights reserved 
# www.bevywise.com Email - support@bevywise.com
#
# custom_store.py
#
# The custom data store hook for the Big Data Storage. 
# The Custom data hook can be enabled in the broker.conf 
# inside conf/ folder.
# 
# The parameter data will be in dict format and the keys are 'sender','topic', 'message', 'unixtime', 'timestamp'
#
################################################################
import os, sys, time
sys.path.append(os.getcwd()+'../extensions')
# replace the Elastic installed path with next line  
sys.path.append('/usr/local/lib/python2.7/dist-packages')
from Elastic import Elastic
global Elas_inst
confpath = "../extensions/plugin.conf"
Elas_inst = Elastic(confpath)
	
def handle_Received_Payload(data):
	#
	# Write your code here. Use your connection object to 
	#
	#
	# finish your code here.
	#
	# Send data to your data store
	result = Elas_inst.data_consumer(data)
	# if result is none then write failed
	 
	 
