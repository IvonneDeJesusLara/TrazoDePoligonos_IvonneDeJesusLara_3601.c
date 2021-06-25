import matplotlib.pyplot as plt
def GraficarBresen(x1,y1,x2,y2,x3,y3):
    print("METODO BRESENHAMS")
    #x1=1 y1=1 x2=6 y2=1 x3=3 y3=6
    a=y1
    c=x1
    b=y3
    xx1=x1
    xx2=x2
    s=1
    dx1= abs(x2 - x1)   #6-1= 5
    dy1 =abs(y2 -y1)    #1-1=0
    p= (2 * dy1) -dx1   #2 * 0 = 0 - 5 = -5
    dx2= abs(x3 - x1)   # 3 - 1= 2
    dy2 =abs(y3 -y1)    #6 - 1= 5
    p2= (2 * dy2) -dx2  #2 * 5 =10 -2 = 8
     #X1 A X2 ABAJO
    while xx1 <= (xx2 + (xx2-2)):   #1 <= 6
        xx1= xx1 + 1
        d= (xx1 % 2)
        if  d == 0:
            plt.plot(round(xx1+ s),round(y1), marker="s", color="black")
            print("DERECHA",xx1,' , ',y1)
            if p < 0:
                p= p + (2 * dy1)
            else:
                p= p + (2 * dy1) - (2 * dx1)
                y1= y1 + 1
    #X1 A X2 izquierda
    while x1 <= (x2-1):   #1 <= 6
        plt.plot(round(y1),round(a), marker="s", color="black")
        x1= x1 + 1
        a= a + 1
        if p2 < 0:
            p2= p2 + (2 * dy2)    # -5=-5 +(2*0)= 
        else:
            p2= p2 + (2 * dy2) - (2 * dx2)
            y1= y1 + 1
        print("IZQUIERDO",y1,' , ',a)
    while c<= (x3 + 2):   #3 <= 6
        plt.plot(round(b),round(y3), marker="s", color="black")
        y3=y3-1
        c=c+1 
        b= b + 1
        if p2 < 0:
            p2= p2 + (2 * dy2)    # -5=-5 +(2*0)= 
        else:
            p2= p2 + (2 * dy2) - (2 * dx2)
            y1= y1 + 1
        print("DERECHO",  b,' , ',y3)
    


def DDA(x1,y1,x2,y2,x3,y3):
    print("METODO DDA")
    a=x1
    c=x1
    xx1=x1
    xx2=y3
    b=y3
    s=0
    dx1= abs(x2-x1)
    dy1= abs(y2-y1)
    dx2= abs(x3-x1)
    dy2= abs(y3-y1)
    if dx1 > dy1:
        steps= dx1
    else:
        steps= dy1

    if dx2 > dy2:
        steps= dx2
    else:
        steps= dy2
    incx= dx1/steps
    incy= dy1/steps
    incx2= dx2/steps
    incy2= dy2/steps
    while x1 <= (x2 + (x2-4)):   #1 <= 6
        x1= x1 + 1
        d= (x1 % 2)
        if  d == 0:
            plt.plot(round(x1+ s),round(y1), marker="s", color="black")
            print("ABAJO",x1,' , ',y1)
            #INCREMENTAMOS LAS POSICIONES 
            x1= x1+incx
            y1= y1+incy     
    #X1 A X2 izquierda
    while xx1 <= (x2-1):   #1 <= 6
        plt.plot(round(xx1),round(a), marker="s", color="black")
        xx1= xx1+incx2
        a= a+incy2
        print("IZQUIERDO",y1,' , ',a)
    while c <= (x3 + 6):   #1 <= 3+3 = 6
        plt.plot(round(b),round(y3+3), marker="s", color="black") # 6, 6
        y3=y3-1 # 6 6 - 2
        b= b + incx2
        c=c+1      
        print("DERECHO",  b,' , ',y3)
    return 0

def error():
   print ("Opcion Invalida")

def menu():
   print("----------- METODO -----------")
   print("1. DDA")
   print("2. BRESENHAMS")
   print("-----------------------------------")
   
def switch(case, a, b):
    if case == 1:
        #DEFINIMOS LOS PUNTOS (1,1)
        x1 = 1
        y1 = 1
        #DETERMINAMOS LOS VALORES A PARTIR DE LOS PUNTOS ANTERIORES
        x2= 6
        y2= 1
        x3= 3
        y3= 6
        #ENVIAMOS LOS PARAMETROS PARA GRAFICARLOS
        DDA(x1,y1,x2,y2,x3,y3)
    elif case == 2:
        #DEFINIMOS LOS PUNTOS (1,1)
        x1 = 1
        y1 = 1
        #DETERMINAMOS LOS VALORES A PARTIR DE LOS PUNTOS ANTERIORES
        x2= 6
        y2= 1
        x3= 3
        y3= 6
        #ENVIAMOS LOS PARAMETROS PARA GRAFICARLOS
        GraficarBresen(x1,y1,x2,y2,x3,y3)
    else:
        return error()

if __name__=='__main__':
   a=1
   b=1
   menu()
   case=0
   case = int(input("SELECCIONE EL METODO: ")) 
   switch(case, a, b)
   plt.show()
   print("FIN")