a = float(input("Informe o valor de a: "))
b = float(input("Informe o valor de b: "))
c = float(input("Informe o valor de c: "))
delta=b*b-4*a*c
rdelta=delta**(1/2)
x1=(-b+rdelta)/2*a
x1_form="{:.2f}".format(x1)
x2=(-b-rdelta)/2*a
x2_form="{:.2f}".format(x2)
print("A primeira raiz é", x1)
print("A segunda raiz é", x2)