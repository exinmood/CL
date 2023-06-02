from tkinter import *




window=Tk()
window.geometry('200x303')
window.minsize()
window.maxsize()
window.title('CL')

a=[0,0]
i=0
cl=''
temp=''
fu=()


#entry
javab = Label(window,bd='6',font='tahoma 20',width=10)



#main app for calculate
def insertnumber(num):
    global a
    global i
    global temp
    if (i<2):
        temp=temp+str(num)
        javab.config(text=temp)
        a[i]=a[i]*10+num

def insertcl(num):
    global i
    global cl
    global temp
    cl = num
    temp=temp+str(cl)
    javab.config(text=temp)
    i+=1

def insertequal():
    global a
    global i
    global temp
    global cl
    if (cl==('+')):
        a[0]=a[0]+a[1]
    elif (cl==('–')):
        a[0]=a[0]-a[1]
    elif (cl==('×')):
        a[0]=a[0]*a[1]
    elif (cl==('÷')):
        a[0]=a[0]/a[1]
    

    a[1]=0
    javab.config(text=a[0])
    i=0



def insertclean(labl):
    global fuck
    javab.config(text=fu)
    javab.update()
    
    





#one to nine
btn1=Button(window,text='1',font='tahoma 15',padx=10 , pady=10 , bd='4',command=lambda:insertnumber(1))
btn2=Button(window,text='2',font='tahoma 15',padx=10 , pady=10 , bd='4',command=lambda:insertnumber(2))
btn3=Button(window,text='3',font='tahoma 15',padx=10 , pady=10 , bd='4',command=lambda:insertnumber(3))
btn4=Button(window,text='4',font='tahoma 15',padx=10 , pady=10 , bd='4',command=lambda:insertnumber(4))
btn5=Button(window,text='5',font='tahoma 15',padx=10 , pady=10 , bd='4',command=lambda:insertnumber(5))
btn6=Button(window,text='6',font='tahoma 15',padx=10 , pady=10 , bd='4',command=lambda:insertnumber(6))
btn7=Button(window,text='7',font='tahoma 15',padx=10 , pady=10 , bd='4',command=lambda:insertnumber(7))
btn8=Button(window,text='8',font='tahoma 15',padx=10 , pady=10 , bd='4',command=lambda:insertnumber(8))
btn9=Button(window,text='9',font='tahoma 15',padx=10 , pady=10 , bd='4',command=lambda:insertnumber(9))

#ziro number
btn0=Button(window,text='0',font='tahoma 15',padx=10 , pady=10 , bd='4',command=lambda:insertnumber(0))
#clean button
btncl=Button(window,text='‹',font='tahoma 15',padx=11.4 ,fg='red', pady=10 , bd='4',command=lambda:insertclean(javab))
#equal button 
btnequal=Button(window,text='=',font='tahoma 15',padx=8 , pady=10 , bd='4',command=lambda:insertequal())
#Total button
btntotal=Button(window,text='+',font='tahoma 15',padx=8 ,fg='gray', pady=10 , bd='4',command=lambda:insertcl('+'))
#subtraction button
btnsub=Button(window,text='–',font='tahoma 15',padx=10.2 ,fg='gray', pady=10 , bd='4',command=lambda:insertcl('–'))
#multi button
btnmulti=Button(window,text='×',font='tahoma 15',padx=8 ,fg='gray', pady=10 , bd='4',command=lambda:insertcl('×'))
#division button
btndiv=Button(window,text='÷',font='tahoma 15',padx=8 ,fg='gray', pady=10 , bd='4',command=lambda:insertcl('÷'))





btn1.grid(row=2,column=2)
btn2.grid(row=2,column=3)
btn3.grid(row=2,column=4)

btn4.grid(row=3,column=2)
btn5.grid(row=3,column=3)
btn6.grid(row=3,column=4)

btn7.grid(row=4,column=2)
btn8.grid(row=4,column=3)
btn9.grid(row=4,column=4)

btn0.grid(row=5,column=3)

btncl.grid(row=5,column=2)

btnequal.grid(row=5,column=4)

btntotal.grid(row=2,column=5)

btnsub.grid(row=3,column=5)

btnmulti.grid(row=4,column=5)

btndiv.grid(row=5,column=5)

javab.grid(row=0,column=0,columnspan=6)


mainloop()