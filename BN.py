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
        if len(self.parents)==0:
            pos=self.prob.item(0)
            neg=1-self.prob.item(0)
            result = [neg, pos]
            return result
        elif len(self.parents)==1:
            if evid[self.parents[0]]==0:
                pos=self.prob.item(0)
                neg=1-self.prob.item(0)
                result = [neg, pos]
                return result
            elif evid[self.parents[0]]==1:
                pos=self.prob.item(1)
                neg=1-self.prob.item(1)
                result = [neg, pos]
                return result 
        elif len(self.parents)==2:
            if evid[self.parents[0]]==0 and evid[self.parents[1]]==0:
                pos=self.prob.item(0)
                neg=1-self.prob.item(0)
                result = [neg, pos]
                return result
            elif evid[self.parents[0]]==0 and evid[self.parents[1]]==1:
                pos=self.prob.item(1)
                neg=1-self.prob.item(1)
                result = [neg, pos]
                return result 
            elif evid[self.parents[0]]==1 and evid[self.parents[1]]==0:
                pos=self.prob.item(2)
                neg=1-self.prob.item(2)
                result = [neg, pos]
                return result 
            elif evid[self.parents[0]]==1 and evid[self.parents[1]]==1:
                pos=self.prob.item(3)
                neg=1-self.prob.item(3)
                result = [neg, pos]
                return result             
    
class BN():
    def __init__(self, gra, prob):
        self.gra=gra
        self.prob=prob

    def computePostProb(self, evid):
        for i in range(len(evid)):
            if evid[i]==-1:
                return 0
        
        
    def computeJointProb(self, evid):
        soma=1
        if evid!=(0,0,0,0,0):
            for i in range(len(self.prob)):
                soma*=self.prob[i].computeProb(evid)[1]
        return soma