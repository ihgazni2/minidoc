#__init__(self,**kwargs)
from qtable.qtable import *
qtbl = Qtable(index=['a','c','d','a','e'],columns=['one', 'two', 'three','one','four'])
qtbl 

qtbl = Qtable(mat= np.arange(25).reshape((5,5)),index=['a','c','d','a','e'],columns=['one', 'two', 'three','one','four'])
qtbl 

#__getitem__(self,*args)
from qtable.qtable import *
qtbl = Qtable(mat= np.arange(25).reshape((5,5)),index=['a','c','d','a','e'],columns=['one', 'two', 'three','one','four'])
qtbl 
qtbl['a','one']
qtbl['a','one',0,1]


qtbl = Qtable(allow_duplicates=False,mat= np.arange(25).reshape((5,5)),index=['a','b','c','d','e'],columns=['one', 'two', 'three','four','five'])
qtbl 
qtbl['a','one']
