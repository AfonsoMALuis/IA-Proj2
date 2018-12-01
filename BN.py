# -*- coding: utf-8 -*-
"""
Created on Mon Oct 15 15:51:49 2018

@author: mlopes
"""

import numpy as np

class Node():
    def __init__(self, prob, parents = []):
        self.parents=parents
        self.prob=prob
    
    def computeProb(self, evid):
        if len(self.parents)<2:
            pos=self.prob
            neg=1-self.prob
            result = [neg[0], pos[0]]
            return result
        else:
            
            return 0
    
class BN():
    def __init__(self, gra, prob):
        pass

    def computePostProb(self, evid):
        pass
               
        return 0
        
        
    def computeJointProb(self, evid):
        pass
        
        return 0