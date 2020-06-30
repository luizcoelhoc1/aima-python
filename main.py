# -*- coding: utf-8 -*-
"""
Created on Tue Jun 30 14:36:15 2020

@author: luizc
"""
from agents import *

#init
trivial_vacuum_env = TrivialVacuumEnvironment4Places()




#create agent
random_agent = Agent(program=RandomVacuumAgent4places())


 
#add agent on Environment
trivial_vacuum_env.add_thing(random_agent)

#runing 10 passos printing map
for _ in range(1,10):
    print("RandomVacuumAgent is located at {}.".format(random_agent.location))
    mapa = ""
    for i in range(0, 2):
        for j in range(0, 2):
            mapa += str(trivial_vacuum_env.map[i][j]) + " "
        mapa += "\n"
    print (mapa)
    trivial_vacuum_env.step()
    
print(random_agent.performance)
    