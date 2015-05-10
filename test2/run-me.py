#!/usr/bin/env python

from nupic.frameworks.opf.modelfactory import ModelFactory
from nupic.swarming import permutations_runner
from nupic_output import NuPICFileOutput, NuPICPlotOutput
import shutil
import math
import  csv
import json
from numpy.random import random_integers

#model_params = permutations_runner.runWithPermutationsScript ( "permutations.py", 
#			{'maxWorkers':4, 'overwrite': True}, ".", "." )
#model = ModelFactory.create( model_params )
#exit (0)

shutil.copyfile("model_0/model_params.py", "model_params.py")

import model_params
model = ModelFactory.create( model_params.MODEL_PARAMS )

model.enableInference({"predictedField": "categoryx"})

print " === TRAIN"
for r in range(10000):
	ip =  random_integers( low=0, high=99 );
	out = "EVEN"
	if( ip % 2 ):
		out="ODD"
	res = model.run( { "letter": "A", "number": ip, "categoryx": out } )
	print "A"+str(ip), " ==> ", out,  " pred : " , res.inferences["multiStepBestPredictions"][0]
		#print res


print " === CLASSIFY"
for z in range(99):
	ip =  37 #random_integers( low=0, high=99 ) ;
	res=model.run( { "letter": "A", "number":  ip, "categoryx": None } )
	print "A"+str(ip),  res.inferences["multiStepBestPredictions"][0], res.inferences 
#  read in the real data
#for r in range(30000):
#		angle = float( r[0] )
#		sine  = float( r[1] )
# After the first 1000 steps, we feed it input back into itself
#		angle = (r*math.pi) / 50.
#		sinef = 0.9 * math.sin( angle );
#		if r < 10000:
#		sine = sinef
#
#sinef += sinef * 0.02 * normal()
#
#
#	res =model.run( { "sine": sine } )
#	f = res.inferences
#	print r, sinef, f['multiStepBestPredictions'][1], f['anomalyScore'] 
#	op2.write( angle, sine, res );
#	sine = f['multiStepBestPredictions'][1]
#
#	op.close


