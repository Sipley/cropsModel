import random
import numpy
import math

class Soil(object):
    '''This is my soil class used to monitor important properties related to the soil health.
    '''
    def __init__(self, basicType, P, K):
        self.basicType = basicType
        self.P = P
        self.K = K

    def getPvalue(self):
        return self.P

    def getKvalue(self):
        return self.K

    def fertilize(self, Pfert, Kfert, amount):
        '''Increase the predicted amount of P and K in the soil based on the fertilizer applied.
        PFERT: float, percentage of P in fertilizer
        KFERT: float, percentage of K in fertilizer
        AMOUNT: float, lbs of fertilizer per acre
        '''
        self.P = int(self.getPvalue()) + int(Pfert * amount)
        self.K = int(self.getKvalue()) + int(Kfert + amount)

    def checkMinimum(self):
        '''Determine if soil is at minimum level for crop growth.  
        Minimum P: 120
        Mimimum K: 80
        '''
        if self.getPvalue() >= 120:
       	    print "P levels are adequate.  Current level: " + str(self.getPvalue())
        else:
            print "P levels are low.  Current level: " + str(self.getPvalue())

        if self.getKvalue() >= 80:
   	    print "K levels are adequate.  Current level: " + str(self.getKvalue())
        else:
   	    print "K levels are low.  Current level: " + str(self.getKvalue())

    def rainPerMonth(self):
        self.rainPerMo = math.log10(random.lognormvariate(10,3))
	
    def monthlyLoss(self):
        '''Calculate the monthly loss based on rainfall.  Assume a 2 point loss for every inch of rain for K and a 0.25 point loss for every inch of rain for 
        '''
        self.rainPerMonth()
        
        self.K = int(self.getKvalue()) - (0.25 * self.rainPerMo)
        self.P = int(self.getPvalue()) - (0.08 * self.rainPerMo)
	
	if self.K < 0:
	    self.K == 0
	if self.P < 0:
	    self.P == 0
	    	
    def yearlyLoss(self):
        for month in range(12):
            self.monthlyLoss()

	    	
# for i in range(10000):

field7 = Soil('clay', '100', '50')
field8 = Soil('clay', '100', '100')

def populateSoil():
    kList = []
    pList = []
    
    for time in range(10000):
        fieldInfo = Soil('clay', '100', '50')
        fieldInfo.yearlyLoss()
        kList.append(fieldInfo.K)
        pList.append(fieldInfo.P)
    
    return kList, pList
        
populateSoil()