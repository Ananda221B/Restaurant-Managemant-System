from tkinter import*
import random
import time

root = Tk()
root.geometry("1600x800+0+0")
root.title("Mamanda's Restuarent")

text_Input= StringVar()
operator=""

Tops = Frame(root,width = 1600, height=50, bg = "powder blue", relief = SUNKEN)
Tops.pack(side=TOP)

f1 = Frame(root,width = 800, height=700, relief = SUNKEN)
f1.pack(side=LEFT)


f2 = Frame(root,width = 300, height=700, bg = "powder blue", relief = SUNKEN)
f2.pack(side=RIGHT)
#=========================================TIME======================
localtime=time.asctime(time.localtime(time.time()))
#=========================================Info======================
lblInfo = Label(Tops, font=('Edwardian Script ITC', 70), text = "Mamanda's Restaurant", fg="goldenrod", bd=10, anchor='w')
lblInfo.grid(row=0,column=0)
lblInfo = Label(Tops, font=('montserrat', 13, 'bold'), text = localtime, fg="Steel Blue", bd=10, anchor='w')
lblInfo.grid(row=2,column=0)
lblInfo = Label(Tops, font=('montserrat', 20), text ="Rules: You have to order everything in the menu", fg="Steel Blue", bd=10, anchor='w')
lblInfo.grid(row=1,column=0)
#=========================================Calc======================
def btnClick(numbers):
    global operator
    operator = operator + str(numbers)
    text_Input.set(operator)

def btnClearDisplay():
    global operator
    operator=""
    text_Input.set("")

def btnEqualsInput():
    global operator
    sumup =str(eval(operator))
    text_Input.set(sumup)
    operator = ""

def Ref():
    x=random.randint(10908, 500876)
    randomRef = str(x)
    rand.set(randomRef)

    CoF = float(Frenchfries.get())
    CoD = float(Drinks.get())
    CoDH = float(Dherosh.get())
    CoB = float(Burger.get())
    CoC = float(Chicken.get())
    CoCH = float(Cheese.get())

    CostofFrenchFries = CoF * 60
    CostofDrinks = CoD * 15
    CostofDherosh = CoDH * 50
    CostofBurger = CoB * 160
    CostofChicken = CoC * 100
    CostofCheese = CoCH * 270

    CostofMeal= "BDT", str('%.2f' % (CostofFrenchFries + CostofDrinks + CostofDherosh
                                     +CostofBurger+CostofChicken+CostofCheese ))

    PayTax =((CostofFrenchFries + CostofDrinks + CostofDherosh
                                     +CostofBurger+CostofChicken+CostofCheese) * 0.15)
    TotalCost=(CostofFrenchFries + CostofDrinks + CostofDherosh
                                     +CostofBurger+CostofChicken+CostofCheese)

    SerCharge=((CostofFrenchFries + CostofDrinks + CostofDherosh
                                     +CostofBurger+CostofChicken+CostofCheese)/99)

    Ser = "BDT", str('%.2f' % SerCharge)

    OverAllCost = "BDT", str('%.2f' % (PayTax+TotalCost+SerCharge))
    PaidTax =  "BDT", str('%.2f' % PayTax)

    Service.set(Ser)
    Cost.set(CostofMeal)
    Tax.set(PaidTax)
    SubTotal.set(CostofMeal)
    Total.set(OverAllCost)



def qExit():
    root.destroy()

def Reset():
    rand.set("")
    Frenchfries.set("")
    Burger.set("")
    Dherosh.set("")
    SubTotal.set("")
    Total.set("")
    Service.set("")
    Drinks.set("")
    Tax.set("")
    Cost.set("")
    Chicken.set("")
    Cheese.set("")



txtDisplay= Entry(f2,font=('arial', 20, 'bold'), textvariable=text_Input, bd=30, insertwidth=4,
                  bg="powder blue", justify='right')
txtDisplay.grid(columnspan=4)

btn7=Button(f2,padx=16,pady=16,bd=8, fg="black", font=('arial', 20, 'bold'),
            text='7', bg='powder blue', command=lambda: btnClick(7)).grid(row=2,column=0)

btn8=Button(f2,padx=16,pady=16,bd=8, fg="black", font=('arial', 20, 'bold'),
            text='8', bg='powder blue', command=lambda: btnClick(8)).grid(row=2,column=1)

btn9=Button(f2,padx=16,pady=16,bd=8, fg="black", font=('arial', 20, 'bold'),
            text='9', bg='powder blue', command=lambda: btnClick(9)).grid(row=2,column=2)

Addition=Button(f2,padx=16,pady=16,bd=8, fg="black", font=('arial', 20, 'bold'),
            text="+", bg='powder blue', command=lambda: btnClick("+")).grid(row=2,column=3)
#----------------------------------------------------------------------------------------------------

btn4=Button(f2,padx=16,pady=16,bd=8, fg="black", font=('arial', 20, 'bold'),
            text='4', bg='powder blue', command=lambda: btnClick(4)).grid(row=3,column=0)

btn5=Button(f2,padx=16,pady=16,bd=8, fg="black", font=('arial', 20, 'bold'),
            text='5', bg='powder blue', command=lambda: btnClick(5)).grid(row=3,column=1)

btn6=Button(f2,padx=16,pady=16,bd=8, fg="black", font=('arial', 20, 'bold'),
            text='6', bg='powder blue', command=lambda: btnClick(6)).grid(row=3,column=2)

Subtraction=Button(f2,padx=16,pady=16,bd=8, fg="black", font=('arial', 20, 'bold'),
            text="-", bg='powder blue', command=lambda: btnClick("-")).grid(row=3,column=3)
#-----------------------------------------------------------------------------------------------

btn1=Button(f2,padx=16,pady=16,bd=8, fg="black", font=('arial', 20, 'bold'),
            text='1', bg='powder blue', command=lambda: btnClick(1)).grid(row=4,column=0)

btn2=Button(f2,padx=16,pady=16,bd=8, fg="black", font=('arial', 20, 'bold'),
            text='2', bg='powder blue', command=lambda: btnClick(2)).grid(row=4,column=1)

btn3=Button(f2,padx=16,pady=16,bd=8, fg="black", font=('arial', 20, 'bold'),
            text='3', bg='powder blue', command=lambda: btnClick(3)).grid(row=4,column=2)

Multipy=Button(f2,padx=16,pady=16,bd=8, fg="black", font=('arial', 20, 'bold'),
            text="*", bg='powder blue', command=lambda: btnClick("*")).grid(row=4,column=3)
#-----------------------------------------------------------------------------------------------
btn0=Button(f2,padx=16,pady=16,bd=8, fg="black", font=('arial', 20, 'bold'),
            text='0', bg='powder blue', command=lambda: btnClick(0)).grid(row=5,column=0)

btnClear=Button(f2,padx=16,pady=16,bd=8, fg="black", font=('arial', 20, 'bold'),
            text='C', bg='powder blue', command=btnClearDisplay).grid(row=5,column=1)

btnEquals=Button(f2,padx=16,pady=16,bd=8, fg="black", font=('arial', 20, 'bold'),
            text='=', bg='powder blue',command=btnEqualsInput).grid(row=5,column=2)

Divison=Button(f2,padx=16,pady=16,bd=8, fg="black", font=('arial', 20, 'bold'),
            text="/", bg='powder blue', command=lambda: btnClick("/")).grid(row=5,column=3)
#-------------------------------------------Bam Pasher Info----------------------------------------------
rand = StringVar()
Frenchfries = StringVar()
Burger = StringVar()
Dherosh = StringVar()
SubTotal = StringVar()
Total = StringVar()
Service = StringVar()
Drinks = StringVar()
Tax = StringVar()
Cost = StringVar()
Chicken = StringVar()
Cheese = StringVar()

lblReference = Label(f1,font=('arial', 16, 'bold'), text="Reference", bd=16, anchor='w')
lblReference.grid(row=0,column=0)
txtReference=Entry(f1,font=('arial', 16, 'bold'), textvariable=rand, bd=10, insertwidth=4,
                   bg="#ffffff", justify ='right')
txtReference.grid(row=0,column=1)


lblFrenchfries = Label(f1,font=('arial', 16, 'bold'), text="Large fries", bd=16, anchor='w')
lblFrenchfries.grid(row=1,column=0)
txtFrenchfries=Entry(f1,font=('arial', 16, 'bold'), textvariable=Frenchfries, bd=10, insertwidth=4,
                   bg="#ffffff", justify ='right')
txtFrenchfries.grid(row=1,column=1)

lblBurger = Label(f1,font=('arial', 16, 'bold'), text="Burger Meal", bd=16, anchor='w')
lblBurger.grid(row=2,column=0)
txtBurger=Entry(f1,font=('arial', 16, 'bold'), textvariable=Burger, bd=10, insertwidth=4,
                   bg="#ffffff", justify ='right')
txtBurger.grid(row=2,column=1)

lblDherosh = Label(f1,font=('arial', 16, 'bold'), text="Dherosh er Haluwa", bd=16, anchor='w')
lblDherosh.grid(row=3,column=0)
txtDherosh=Entry(f1,font=('arial', 16, 'bold'), textvariable=Dherosh, bd=10, insertwidth=4,
                   bg="#ffffff", justify ='right')
txtDherosh.grid(row=3,column=1)

lblChicken = Label(f1,font=('arial', 16, 'bold'), text="Chicken Fry", bd=16, anchor='w')
lblChicken.grid(row=4,column=0)
txtChicken=Entry(f1,font=('arial', 16, 'bold'), textvariable=Chicken, bd=10, insertwidth=4,
                   bg="#ffffff", justify ='right')
txtChicken.grid(row=4,column=1)

lblCheese = Label(f1,font=('arial', 16, 'bold'), text="Cheese Box", bd=16, anchor='w')
lblCheese.grid(row=5,column=0)
txtCheese=Entry(f1,font=('arial', 16, 'bold'), textvariable=Cheese, bd=10, insertwidth=4,
                   bg="#ffffff", justify ='right')
txtCheese.grid(row=5,column=1)
#=========================================Dan Pasher Info=============================================

lblDrinks = Label(f1,font=('arial', 16, 'bold'), text="Drinks", bd=16, anchor='w')
lblDrinks.grid(row=0,column=2)
txtDrinks=Entry(f1,font=('arial', 16, 'bold'), textvariable=Drinks, bd=10, insertwidth=4,
                   bg="#ffffff", justify ='right')
txtDrinks.grid(row=0,column=3)


lblCost = Label(f1,font=('arial', 16, 'bold'), text="Cost", bd=16, anchor='w')
lblCost.grid(row=1,column=2)
txtCost=Entry(f1,font=('arial', 16, 'bold'), textvariable=Cost, bd=10, insertwidth=4,
                   bg="#ffffff", justify ='right')
txtCost.grid(row=1,column=3)

lblService = Label(f1,font=('arial', 16, 'bold'), text="Service Charge", bd=16, anchor='w')
lblService.grid(row=2,column=2)
txtService=Entry(f1,font=('arial', 16, 'bold'), textvariable=Service, bd=10, insertwidth=4,
                   bg="#ffffff", justify ='right')
txtService.grid(row=2,column=3)

lblTax = Label(f1,font=('arial', 16, 'bold'), text="Tax", bd=16, anchor='w')
lblTax.grid(row=3,column=2)
txtTax=Entry(f1,font=('arial', 16, 'bold'), textvariable=Tax, bd=10, insertwidth=4,
                   bg="#ffffff", justify ='right')
txtTax.grid(row=3,column=3)

lblSubTotal = Label(f1,font=('arial', 16, 'bold'), text="SubTotal", bd=16, anchor='w')
lblSubTotal.grid(row=4,column=2)
txtSubTotal=Entry(f1,font=('arial', 16, 'bold'), textvariable=SubTotal, bd=10, insertwidth=4,
                   bg="#ffffff", justify ='right')
txtSubTotal.grid(row=4,column=3)

lblTotal = Label(f1,font=('arial', 16, 'bold'), text="Total", bd=16, anchor='w')
lblTotal.grid(row=5,column=2)
txtTotal=Entry(f1,font=('arial', 16, 'bold'), textvariable=Total, bd=10, insertwidth=4,
                   bg="#ffffff", justify ='right')
txtTotal.grid(row=5,column=3)
#=========================================Buttons==================================
btnTotal=Button(f1,padx=16,pady=8, bd=16, fg="black",font=('arial',16,'bold'),width=10,
                text="Total", bg="powder blue", command=Ref).grid(row=7,column=1)

btnReset=Button(f1,padx=16,pady=8, bd=16, fg="black",font=('arial',16,'bold'),width=10,
                text="Reset", bg="powder blue", command=Reset).grid(row=7,column=2)

btnExit=Button(f1,padx=16,pady=8, bd=16, fg="black",font=('arial',16,'bold'),width=10,
                text="Exit", bg="powder blue", command=qExit).grid(row=7,column=3)

root.mainloop()
