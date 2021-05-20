from trader import trader
from assets import security
from underwriters import marketMaker
from marketWatch import watch
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


class market:
   

    #marketwatch
    dt             = 1/252
    clock          = watch(dt)

    #we setup a market
    periodOfTrade = 1
    marketMaker   =marketMaker(clock)
    
    marketMaker.randomGenerator(size = int(periodOfTrade/dt), numberOfAssets =2)
    

    autoCorr       = np.matrix([[0.4],
                                [0.5]])
    
    crossSecCorr   =  np.matrix([[1,0.6],
                                [0.6, 1]])



    marketMaker.setCorr(autoCorr, crossSecCorr)


    AAPL           = marketMaker.IPO(0,'AAPL', 132.5, 7547169.811,3.2,1.5,0.0038)
    JNJ            = marketMaker.IPO(1,'JNJ',95.6,10460251.05,4.32,1.9,0.0042) 

    
    



    
 


    #valueTrader123 = trader('valueTrader',63,1,100, marketMaker,clock)
    trendFollower  = trader('trendFollower',30,1,100, marketMaker,clock)
    passiveTrader  = trader('passiveTrader',63,1,100, marketMaker,clock)
    noiseTrader    = trader('noiseTrader',1,1,100, marketMaker,clock)
    Traders        = [trendFollower,passiveTrader,noiseTrader]


    
   

    marketMaker.setRiskFreeRate((1.02**(1/252))-1)








    #we generate market activity
    if __name__ == '__main__':
        clock.start()

        while clock.time() <= periodOfTrade:        #years
            qoutes = marketMaker.sendQoutes()
            Orders = 0
            for trader in Traders:
                trader.receiveQoutes(qoutes,clock.time())
                Orders += trader.respond()
                

            marketMaker.receiveOrders(Orders)

            clock.tick()

        
        
        output =marketMaker.stockPrice

        def returns(output1,Asset):
            returns= []
            for i in range(1,len(output1[Asset])-1):
                a= (output1[Asset][i+1]/output1[Asset][i])
                returns.append(np.log(a))
            return returns



        #Output
        
        plt.style.use('seaborn')
        figure, axis = plt.subplots(2, 1)
        axis[0].plot(output.loc[1:,'JNJ'], label = 'JNJ')
        axis[0].set_ylabel('Price, ($)')
        axis[0].legend(loc = 'upper left')
        axis[0].plot(output.loc[1:,'AAPL'], label = 'AAPL')
        axis[0].set_ylabel('Price, ($)')
        axis[0].legend(loc = 'upper left')
        axis[1].plot(returns(output,'AAPL') )
        axis[1].set_ylabel('JNJ')
        axis[1].set_xlabel('AAPL')
        axis[1].legend(loc = 'upper left')
        
        plt.show()

     
    




