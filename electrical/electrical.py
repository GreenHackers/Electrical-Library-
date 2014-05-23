from math import*

# Basic Electrical

    #calculating frequency
def freq(t=0,l=0,c=0):
    if t!=0:
        f=(1/t)
        return f
    if (l and c )!= 0:
        lc=sqrt(l*c)
        f=(1)/(2*pi*lc)
        return f
        
 # power , voltage , current calculation
def power(i=0,v=0,v2=0,i2=0,r=0,):
    if (v2 and r)!=0:
        p=(pow(v2,2)/(r))
        return p
    elif(i and v)!=0:
        p=i*v
        return p
    elif(i2 and r)!=0:
        p=(pow(i2,2)*r)
        return p
def current(p=0,r=0,v=0):
    if (p and r)!=0:
        i=sqrt(p/r)
        return i
    elif (p and v)!=0:
        i=p/v
        return i
    elif (v and r)!=0:
        i=v/r
        return i
def resistance(v=0,v2=0,i=0,i2=0,p=0):
     if (v and i)!=0:
         r=v/i
         return r
     elif(p and i2)!=0:
         r=p/i2
         return r
     elif(v2 and p)!=0:
         r=v2/p
         return r
def voltage(p=0,i=0,r=0):
    if (p and r)!=0:
        v=sqrt(p*r)
        return v
    elif(p and i)!=0:
        v=p/i
        return v
    elif(i and r)!=0:
        v=i*r
        return v
#vrms and irms calculation
def vrms(v):
    vrms=(v/sqrt(2))
    return vrms
def irms(i):
    irms=(i/sqrt(2))
    return irms

#energy stored in capacitor
def cap_energy(c,v):
    energy=((c)*pow(v,2))/2
    return energy

        
    
   
            
    
        
    
    

    
        
        
    
        
