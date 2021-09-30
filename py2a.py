#Proble set - 2a
#name -Sheetal kumari
#time spent - 4 hours


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
