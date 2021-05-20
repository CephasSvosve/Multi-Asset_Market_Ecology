
#Build a stock and give it unique attributes like any company listed on the stock exchange
import numpy as np
import scipy.linalg


from numpy.lib.scimath import sqrt

class security:

    def __init__(self,tickerNumber, tickerName, marketCapital, outstandingShares, initialPrice, initialDividend,mu,sigma,dzMatrix, autoCorr,crossSecCorr,clock):
        
        self.tickerNumber      = tickerNumber
        self.tickerName        = tickerName
        self.balanceSheet      = []
        self.marketCapital     = [marketCapital]
        self.outstandingShares = [outstandingShares]
        self.marketPrice       = [initialPrice]   
        self.bookValue         = []
        self.dailyDividend     = [initialDividend]
        self.clock             = clock
        self.autoCorr          = autoCorr
        self.crossSecCorr      = crossSecCorr
        self.dzMatrix          = dzMatrix
        self.mu                = mu
        self.sigma             = sigma

       
    def dividendPayout(self):
        print()



    def updateRecords(self):
        print()
    


    def computeDividend(self):

        mu              = self.mu
        sigma           = self.sigma 
        dzMatrix        = self.dzMatrix

        dt   = self.clock.dt
        dw   = self.dividendNoise(dzMatrix, self.autoCorr, self.crossSecCorr)[self.tickerNumber][-int(1/dt)]
        dlnD = mu*dt + sigma*dw
        D    = self.dailyDividend[-1] + dlnD
        self.dailyDividend.append(D)

        return D
        
        

    
    def dividendNoise(self,dzMatrix,autocorrelationMatrix, correlationMatrix):
        temporalCorr  = self.temporalCorr(autocorrelationMatrix,dzMatrix)
        crossTempCorr = self.crossCorrelation(correlationMatrix,temporalCorr)
       

        return crossTempCorr

    


    # def uncorrelatedRandoms(self,size, numberOfAssets):

    #     c = np.zeros((numberOfAssets,size))

    #     for x in range(numberOfAssets):
    #         c[x] = np.random.normal(0,1,size)


    #     corrmatrix        = np.corrcoef(c)
    #     choleskyMtrx      = scipy.linalg.cholesky(corrmatrix, lower = True)
    #     invcholeskyMtrx   = scipy.linalg.inv(choleskyMtrx)
    #     uncorrMtrx        = invcholeskyMtrx.dot(c)
            
    #     return uncorrMtrx



    def temporalCorr(self, autocorrelationMatrix, dzMatrix):
        dt     = self.clock.dt
        dz     = np.array(dzMatrix)
        a      = np.array(autocorrelationMatrix)
        dw     = np.zeros((len(dz),len(dz[0])))
        
        

        for row in range(len(dz)):
            dw[row][0] = np.random.normal(0,dt)
            for column in range(len(dz[0])-1):
                dx = np.sqrt(1-a[row]**2)*dz[row][column]  +   a[row]*dw[row][-1]

                dw[row][column+1] = dx
            
        return dw



    def crossCorrelation(self, correlationMatrix, dwMatrix):
        L = scipy.linalg.cholesky(correlationMatrix, lower=True)
        Z = L.dot(dwMatrix)

        return Z
