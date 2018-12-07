# 	83419 - Afonso Luís  &  81583 - Joana Sesinando

# -*- coding: utf-8 -*-
"""
Created on Mon Oct 15 15:51:49 2018

@author: mlopes
"""

import copy

class Node():
    def __init__(self, prob, parents = []):
        self.parents = parents
        self.prob = prob
    
    def computeProb(self, evid):
        if len(self.parents) == 0:  # sem pais
            pos = self.prob.item(0)
            neg = 1 - pos

        elif len(self.parents) == 1:  # com 1 pai
            if evid[self.parents[0]] == 0:
                pos = self.prob.item(0)
                neg = 1 - pos

            elif evid[self.parents[0]] == 1:
                pos = self.prob.item(1)
                neg = 1 - pos

        elif len(self.parents)== 2:  # com 2 pais
            if evid[self.parents[0]] == 0:
                if evid[self.parents[1]] == 0:
                    pos = self.prob.item(0)
                    neg = 1 - pos

                elif evid[self.parents[1]] == 1:
                    pos = self.prob.item(1)
                    neg = 1 - pos

            elif evid[self.parents[0]] == 1:
                if evid[self.parents[1]] == 0:
                    pos = self.prob.item(2)
                    neg = 1 - pos

                elif evid[self.parents[1]] == 1:
                    pos = self.prob.item(3)
                    neg = 1 - pos

        return [neg, pos]


class BN():
    def __init__(self, gra, prob):
        self.gra = gra
        self.prob = prob

    def enumerateAll(self, variables, e):
        if len(variables) == 0:
            return 1.0

        Y = variables[0]
        if e[Y] != []:
            if e[Y] == 1:
                return self.prob[Y].computeProb(e)[1] * self.enumerateAll(variables[1:], e)

            elif e[Y] == 0:
                return self.prob[Y].computeProb(e)[0] * self.enumerateAll(variables[1:], e)

        else:
            probs = []
            e2 = copy.deepcopy(list(e))
            for y in [0, 1]:
                e2[Y] = y
                if y == 0:
                    probs.append(self.prob[Y].computeProb(e2)[0] * self.enumerateAll(variables[1:], e2))
                elif y == 1:
                    probs.append(self.prob[Y].computeProb(e2)[1] * self.enumerateAll(variables[1:], e2))
            return sum(probs)

    def enumerationAsk(self, X, e):
        res = []

        e = copy.deepcopy(list(e))
        e[X] = 1

        variables = []
        for i in range(len(e)):
            variables += [i]

        # enumerar
        res.append(self.enumerateAll(variables, e))
        e[X] = []
        res.append(self.enumerateAll(variables, e))

        return res[0]/res[1]


    def computePostProb(self, evid):
        for i in range(len(evid)):
            if evid[i] == -1:
                return self.enumerationAsk(i, evid)

    def computeJointProb(self, evid):
        soma = 1
        for i in range(len(evid)):
            soma *= self.prob[i].computeProb(evid)[evid[i]]
        return soma