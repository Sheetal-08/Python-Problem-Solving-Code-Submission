#Proble set - 2
#name -Sheetal kumari
#time spent - 6 hours

def evaluate_poly(poly, x):
    result=0
    for i in poly:
        result+=(poly[poly.index(i)]) * (x**(poly.index(i)))
    return result
    Equation=Tuple(poly)
    result=Equation[0]
    for i in range(1,length(Equation)):
        result+=Equation[i](x*1)
        print(Equation[i],result)
        print(float(result))
        print (evaluate_poly(poly,-13))
poly =(0.0, 0.0, 5.0, 9.3, 7.0)
x=-13
print(evaluate_poly(poly,x))

def Compute_deriv(poly):
    deriv=()
    for i in poly:
        if(poly.index(i))>0:
            deriv= deriv+(((poly.index(i))*i),)
    return deriv
        
                
poly=(-13.39, 0.0, 17.5, 3.0, 1.0)
print(Compute_deriv(poly))

def Compute_root(poly, x_0, epsilon):
    root=x_0
    count=1
    deriv=Compute_deriv(poly)
    while (abs(evaluate_poly(poly,root))>epsilon):
        root=root-(evaluate_poly(poly,root)/(evaluate_poly(Compute_deriv(poly),root)))
        count+=1
    return (root,count)
poly = (-13.39, 0.0, 17.5, 3.0, 1.0)
x_0 = 0.1
epsilon = .0001
print(Compute_root(poly, x_0, epsilon))

    
    
                
