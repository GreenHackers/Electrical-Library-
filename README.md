Electrical-Library-
===================

To simplify the electrical calculations

##### code usage
``` python
    
    from electrical import*
    a=freq(t=0.02)
    print a
    
    from electrical import*
    b=vrms(v=220) 
    print b
```
To calculate volatage, power , current, resistance value
```python
   
   from electrical import*
   v=voltage(i=5,r=10)
   print v
   
   ###### put v2 instead of  V^2
   
   from electrical import*
   p=power(v2=100,r=150)
   print p
   
   
    
    
