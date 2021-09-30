#Proble set - 2b
#name -Sheetal kumari
#time spent - 5 hours



def Compute_deriv(poly):
    deriv=()
    for i in poly:
        if(poly.index(i))>0:
            deriv= deriv+(((poly.index(i))*i),)
    return deriv
        
                
poly=(-13.39, 0.0, 17.5, 3.0, 1.0)
print(Compute_deriv(poly))
                
