# -*- coding: utf-8 -*-
"""
Created on Sat Jul 20 13:36:45 2019

@author: 69018
"""

from pyspark import SparkContext

import os

os.environ['JAVA_HOME'] = 'C:\Java'

sc = SparkContext('local[2]','spark')

timedata = sc.textFile('hdfs://192.168.204.136/user/hdfspark/timeperf.csv')

timedata.take(5)

header = timedata.first()

rmhtimedata= timedata.filter(lambda x : x != header)

rmhtimedata.take(5)

timedata1 = rmhtimedata.map(lambda x: x.replace('"','')).map(lambda x:x.split(','))



this is the update
