#!/usr/bin/env python

from nupic.frameworks.opf.modelfactory import ModelFactory
from nupic.swarming import permutations_runner
import shutil
import math
import  csv
import json
from numpy.random import random_integers


#with open('searchDef.json') as df:
#	swarm_config = json.load(df);

#model_params = permutations_runner.runWithConfig( swarm_config, 
#	{'maxWorkers':4, 'overwrite': True}, "reports/mjh", "." )

model_params = permutations_runner.runWithPermutationsScript ( "permutations.py", 
			{'maxWorkers':4, 'overwrite': True}, ".", "." )

model = ModelFactory.create( model_params )

