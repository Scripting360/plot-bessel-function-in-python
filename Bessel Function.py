import numpy as np  
 import matplotlib.pyplot as plt  
 from scipy.special import jv , yn  
 newparams = {'axes.labelsize': 10, 'axes.linewidth': 1.5, 'savefig.dpi':   
    1000,   
    'lines.linewidth': 2, 'figure.figsize': (12, 10),    
    'legend.frameon': True,   
    'legend.handlelength': 0.7}   
 plt.rcParams.update(newparams)   
 x= np.linspace(0,10,1000)  
 plt.subplot(1,2,1)  
 col = ['r','b','g','y']  
 for i in range(4):   
   J = jv(i,x)  
   plt.plot(x,J,c=col[i] ,label='$J_%d(x)$'%i ,markevery =None)   
 plt.legend(loc = 'best' ,prop={'size':12})   
 plt.xlabel('x')   
 plt.ylabel(r' $( J_n(x)$)')  
 plt.ylim(-1,1)  
 plt.axhline(0 , color='black')  
 plt.title("Bessel function of the first kind of order")  
 plt.grid()  
 plt.subplot(1,2,2)  
 col = ['r','b','g','y']  
 for i in range(4):   
   K = yn(i,x)  
   plt.plot(x,K,c=col[i] ,label='$Y_%d(x)$'%i ,markevery =None)   
 plt.legend(loc = 'best' ,prop={'size':12})   
 plt.xlabel('x')   
 plt.ylabel(r' $( Y_n(x)$)')  
 plt.axhline(0 , color='black')  
 plt.title("Bessel function of the second kind of order")  
 plt.ylim(-1,1)  
 plt.grid()  
 """###### Sub plot Adjusting ######"""  
 plt.subplots_adjust(left=0.1,  
           bottom=0.1,   
           right=0.9,   
           top=0.9,   
           wspace=0.4,   
           hspace=0.4)  
 plt.suptitle('Graphical Representation of Bessel Function',fontsize=18,color='b',fontstyle ="italic")   
 plt.show()   
