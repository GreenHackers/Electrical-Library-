Electrical-Library-
===================

To simplify the electrical calculations. lot of areas to cover, electrical machines, electronic circuits, control systems etc...

##### contribution
More formulas to add. 

##### frequency formula with TimePeriod

<img src = "https://raw.githubusercontent.com/bhaskar4n/Electrical-Library-/master/images/images.jpg"/>

##### code usage
``` python
    
    from electrical import*
    a=freq(t=0.02)
    print a
```
#### frequency formula with L and C

<img src = "https://raw.githubusercontent.com/bhaskar4n/Electrical-Library-/master/images/images%20(1).jpg"/>

##### code usage
``` python
    from electrical import*
    d=freq(l=0.001,c=0.001)
    print d
```
##### Vrms and Irms formula
``` python
    from electrical import*
    b=vrms(v=220) 
    print b
    
    i=irms(i=10)
    print i
    
```
####To calculate volatage, power , current, resistance value

<img src="https://raw.githubusercontent.com/bhaskar4n/Electrical-Library-/master/images/FormulaWheelElectronics.gif"/>

##### code usage ()


```python
   
   from electrical import*
   # To calculate voltage (v=i*r)
   v=voltage(i=5,r=10)
   print v
   
   ###### put v2 instead of  V^2 and put i2 instead of i^2
   
   from electrical import*
   #To calulate power value (p=(V^2)/r)
   p=power(v2=100,r=150)
   print p
```
##### installation
```
    setup.py install
```   
    
    
