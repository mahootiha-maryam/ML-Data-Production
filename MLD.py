
"""
its graphic is by tkinter
"""
import tkinter as tk
from tkinter import TOP,LEFT,X,BOTTOM
import tkinter.font as tkFont
from tkinter import messagebox 
import random
import time
import pandas as pd
from datetime import datetime
"""
these two functions are for time generation between two date
"""
def strTimeProp(start, end, format, prop):
    """Get a time at a proportion of a range of two formatted times.

        start and end should be strings specifying times formated in the
        given format (strftime-style), giving an interval [start, end].
        prop specifies how a proportion of the interval to be taken after
        start.  The returned time will be in the specified format.
        """

    stime = time.mktime(time.strptime(start, format))
    etime = time.mktime(time.strptime(end, format))
    ptime = stime + prop * (etime - stime)
    """
    if the hour of date is not in worktime hour,it replaced randomly with 
    worktime hour between 8 to 16
    """
    xx=time.strftime(format, time.localtime(ptime))
    datee = datetime.strptime(xx, '%Y/%m/%d %H:%M')
    hours=datee.hour
    if hours<8 or hours>15:
        newhour=random.randrange(8,16)
        newdate = datee.replace(hour=newhour)
    else:
        newdate =datee
    return newdate
def randomDate(start, end, prop):
    return strTimeProp(start, end, '%Y/%m/%d %H:%M', prop)
###############################################################################
"""
this function is for spliting money to persons
"""
def split(x, n): 
  
    # If we cannot split the  
    # number into exactly 'N' parts 
    if(x < n):  
        print(-1) 
  
    # If x % n == 0 then the minimum  
    # difference is 0 and all  
    # numbers are x / n 
    elif (x % n == 0): 
        for i in range(n): 
            yx=x//n
            forth.append(yx)
    else: 
        # upto n-(x % n) the values  
        # will be x / n  
        # after that the values  
        # will be x / n + 1 
        zp = n - (x % n) 
        pp = x//n 
        for i in range(n): 
            if(i>= zp):
                zx=pp+1
                forth.append(zx)
            else:
                forth.append(pp)
###############################################################################               
"""
this function is for rule1.rule1 is about a person who split a big money to 
shorter money and give shorter money to many people.

"""                
def rule1(person1,startt,endt,moneyl,money,first,second,third,forth,fifth,sixth,seventh,mm1,mm2):
                    


    """
       theresholds for data generation
        """
    """
    for source and destination id generation
    """
    """
    for type of banking work,label of fraud and type of fraud
    """
    prule1=random.randrange(person1,30)

    idvariz=random.randrange(1, 100001)
    mm1.append(idvariz)
    for j in range(0,prule1):
        idgirande=random.randrange(1, 100001)
        first.append("cash-in")
        second.append(idvariz)
        mm2.append(idgirande)
        third.append(idgirande)
        sixth.append("1")
        seventh.append("type1")
           
    """
    for amount of money generation
    """
    numberofmoney=random.randrange(money,moneyl)
    split(numberofmoney,prule1)
    
    """
    for date and time generation randomly between two dates
    """
    for k in range(0,prule1):
        final=randomDate(startt,endt, random.random())
        fifth.append(final)
    return (first,second,third,forth,fifth,sixth,seventh,mm1,mm2)
###############################################################################
"""
this function is for rule2.rule2 is about a some person who  transfer money 
sequentially in a range of time

"""
def rule2(person2,startt,endt,moneyl2,money2,first,forth,sixth,seventh,bb1,bb2,bb3):
    """
    theresholds for data generation
    """
    global miani1
    miani1=[]
    global miani2
    miani2=[]
    global sort
    sort=[]
    """
    for source and destination id generation
    """
    """
    for type of banking work,label of fraud and type of fraud
    """
    prule2=random.randrange(person2,25)

    for s in range(0,prule2):
        if s!=0:
            ids=random.randrange(1, 100001)
            first.append("transfer")
            miani1.append(miani2[s-1])
            miani2.append(ids)
            bb2.append(ids)
            sixth.append("1")
            seventh.append("type2")
        if s==0 :
            ids1=random.randrange(1, 100001)
            ids2=random.randrange(1, 100001)
            first.append("transfer")        
            miani1.append(ids1)
            bb1.append(ids1)
            miani2.append(ids2)
            sixth.append("1")
            seventh.append("type2")
        if s==prule2-1:
           bb3.append(ids)

    """
    for amount of money generation
    """
    numberofmoney2=random.randrange(money2,moneyl2)
    for e in range(0,prule2):
        forth.append(numberofmoney2)
    """
    for date and time generation randomly between two dates
    """
    for m in range(0,prule2):
        final2=randomDate(startt,endt, random.random())
        sort.append(final2)
    return (first,forth,sixth,seventh,bb1,bb2,bb3)
###############################################################################
"""
this function is for rule3.rule3 is about many person who transfer short money to 
one person and sum of these transfers is big.


"""
def rule3(person1,startt,endt,moneyl2,money2,first,second,third,forth,fifth,sixth,seventh,aa1,aa2):
    """
       theresholds for data generation
    """
    
    """
    for source and destination id generation
    """
    """
    for type of banking work,label of fraud and type of fraud
    """
    
    idvariz2=random.randrange(1, 100001)
    aa1.append(idvariz2)
    prule3=random.randrange(person1,30)

    for n in range(0,prule3):
        idgirande2=random.randrange(1, 100001)
        aa2.append(idgirande2)
        first.append("transfer")
        third.append(idvariz2)
        second.append(idgirande2)
        sixth.append("1")
        seventh.append("type3")
    """
    for amount of money generation
    """
    numberofmoney3=random.randrange(money2, moneyl2)
    split(numberofmoney3,prule3)
    
    """
    for date and time generation randomly between two dates
    """
    for h in range(0,prule3):
        final=randomDate(startt,endt, random.random())
        fifth.append(final)
    return (first,second,third,forth,fifth,sixth,seventh,aa1,aa2)

"""
this function is for generation of cashing in data that is not fraud action.
 
""" 
def normal1(startt,endt,money,first,second,third,forth,fifth,sixth,seventh,ff1,ff2,mm1,mm2):
                    
    """
    for source and destination id generation
    """
    """
    for type of banking work,label of fraud and type of fraud
    """
    
    idvariz=random.randrange(1, 100001)
    idgirande=random.randrange(1, 100001)
    first.append("cash-in")
    ff1.append(idvariz)
    ff2.append(idgirande)
    second.append(idvariz)
    third.append(idgirande)
    sixth.append("0")
    seventh.append("none")
           
    """
    for amount of money generation
    """
    numberofmoney=random.randrange(50000,money)
    forth.append(numberofmoney)
    
    """
    for date and time generation randomly between two dates
    """
    final=randomDate(startt,endt, random.random())
    fifth.append(final)
    return (first,second,third,forth,fifth,sixth,seventh,ff1,ff2)

"""
this function is for generation of cashing in data that is not fraud action.
 
"""                
def normal12(startt,endt,money,first,second,third,forth,fifth,sixth,seventh,ff1,ff2,mm1,mm2):
                    
    """
    for source and destination id generation
    """
    """
    for type of banking work,label of fraud and type of fraud
    """
    
    idvariz=random.choice(ff1)
    idgirande=random.choice(ff2)
    first.append("cash-in")
    second.append(idvariz)
    third.append(idgirande)
    sixth.append("0")
    seventh.append("none")
           
    """
    for amount of money generation
    """
    numberofmoney=random.randrange(50000,money)
    forth.append(numberofmoney)
    
    """
    for date and time generation randomly between two dates
    """
    final=randomDate(startt,endt, random.random())
    fifth.append(final)
    return (first,second,third,forth,fifth,sixth,seventh)
"""
this function is for generation of cashing in data that is not fraud action.

"""                
def normal13(startt,endt,money,first,second,third,forth,fifth,sixth,seventh,ff1,ff2,mm1,mm2):
                    
    """
    for source and destination id generation
    """
    """
    for type of banking work,label of fraud and type of fraud
    """
    
    idvariz=random.choice(ff1)
    idgirande=random.choice(ff1)
    first.append("cash-in")
    second.append(idvariz)
    third.append(idgirande)
    sixth.append("0")
    seventh.append("none")
           
    """
    for amount of money generation
    """
    numberofmoney=random.randrange(50000,money)
    forth.append(numberofmoney)
    
    """
    for date and time generation randomly between two dates
    """
    final=randomDate(startt,endt, random.random())
    fifth.append(final)
    return (first,second,third,forth,fifth,sixth,seventh)
"""
this function is for generation of cashing in data that is not fraud action.

"""                
def normal14(startt,endt,money,first,second,third,forth,fifth,sixth,seventh,ff1,ff2,mm1,mm2):
                    
    """
    for source and destination id generation
    """
    """
    for type of banking work,label of fraud and type of fraud
    """
    
    idvariz=random.choice(ff2)
    idgirande=random.choice(ff1)
    first.append("cash-in")
    second.append(idvariz)
    third.append(idgirande)
    sixth.append("0")
    seventh.append("none")
           
    """
    for amount of money generation
    """
    numberofmoney=random.randrange(50000,money)
    forth.append(numberofmoney)
    
    """
    for date and time generation randomly between two dates
    """
    final=randomDate(startt,endt, random.random())
    fifth.append(final)
    return (first,second,third,forth,fifth,sixth,seventh)
"""
this function is for generation of cashing in data that is not fraud action.
 
"""                
def normal15(startt,endt,money,first,second,third,forth,fifth,sixth,seventh,ff1,ff2,mm1,mm2):
                    
    """
    for source and destination id generation
    """
    """
    for type of banking work,label of fraud and type of fraud
    """
    
    idvariz=random.choice(ff2)
    idgirande=random.choice(ff2)
    first.append("cash-in")
    second.append(idvariz)
    third.append(idgirande)
    sixth.append("0")
    seventh.append("none")
           
    """
    for amount of money generation
    """
    numberofmoney=random.randrange(50000,money)
    forth.append(numberofmoney)
    
    """
    for date and time generation randomly between two dates
    """
    final=randomDate(startt,endt, random.random())
    fifth.append(final)
    return (first,second,third,forth,fifth,sixth,seventh)

"""
this function is for generation of cashing in data that is not fraud action.

"""                
def normal16(startt,endt,money,first,second,third,forth,fifth,sixth,seventh,ff1,ff2,mm1,mm2):
                    
    """
    for source and destination id generation
    """
    """
    for type of banking work,label of fraud and type of fraud
    """
    
    idvariz=random.choice(ff2)
    idgirande=random.choice(mm1)
    first.append("cash-in")
    second.append(idvariz)
    third.append(idgirande)
    sixth.append("0")
    seventh.append("none")
           
    """
    for amount of money generation
    """
    numberofmoney=random.randrange(50000,money)
    forth.append(numberofmoney)
    
    """
    for date and time generation randomly between two dates
    """
    final=randomDate(startt,endt, random.random())
    fifth.append(final)
    return (first,second,third,forth,fifth,sixth,seventh)

"""
this function is for generation of cashing in data that is not fraud action.

"""                
def normal17(startt,endt,money,first,second,third,forth,fifth,sixth,seventh,ff1,ff2,mm1,mm2):
                    
    """
    for source and destination id generation
    """
    """
    for type of banking work,label of fraud and type of fraud
    """
    
    idvariz=random.choice(ff1)
    idgirande=random.choice(mm1)
    first.append("cash-in")
    second.append(idvariz)
    third.append(idgirande)
    sixth.append("0")
    seventh.append("none")
           
    """
    for amount of money generation
    """
    numberofmoney=random.randrange(50000,money)
    forth.append(numberofmoney)
    
    """
    for date and time generation randomly between two dates
    """
    final=randomDate(startt,endt, random.random())
    fifth.append(final)
    return (first,second,third,forth,fifth,sixth,seventh)

"""
this function is for generation of cashing in data that is not fraud action.

"""                
def normal18(startt,endt,money,first,second,third,forth,fifth,sixth,seventh,ff1,ff2,mm1,mm2):
                    
    """
    for source and destination id generation
    """
    """
    for type of banking work,label of fraud and type of fraud
    """
    
    idvariz=random.choice(ff2)
    idgirande=random.choice(mm2)
    first.append("cash-in")
    second.append(idvariz)
    third.append(idgirande)
    sixth.append("0")
    seventh.append("none")
           
    """
    for amount of money generation
    """
    numberofmoney=random.randrange(50000,money)
    forth.append(numberofmoney)
    
    """
    for date and time generation randomly between two dates
    """
    final=randomDate(startt,endt, random.random())
    fifth.append(final)
    return (first,second,third,forth,fifth,sixth,seventh)

"""
this function is for generation of cashing in data that is not fraud action.

"""                
def normal19(startt,endt,money,first,second,third,forth,fifth,sixth,seventh,ff1,ff2,mm1,mm2):
                    
    """
    for source and destination id generation
    """
    """
    for type of banking work,label of fraud and type of fraud
    """
    
    idvariz=random.choice(ff1)
    idgirande=random.choice(mm2)
    first.append("cash-in")
    second.append(idvariz)
    third.append(idgirande)
    sixth.append("0")
    seventh.append("none")
           
    """
    for amount of money generation
    """
    numberofmoney=random.randrange(50000,money)
    forth.append(numberofmoney)
    
    """
    for date and time generation randomly between two dates
    """
    final=randomDate(startt,endt, random.random())
    fifth.append(final)
    return (first,second,third,forth,fifth,sixth,seventh)
"""
this function is for generation of cashing in data that is not fraud action.

"""                
def normal110(startt,endt,money,first,second,third,forth,fifth,sixth,seventh,ff1,ff2,mm1,mm2):
                    
    """
    for source and destination id generation
    """
    """
    for type of banking work,label of fraud and type of fraud
    """
    
    idvariz=random.choice(mm2)
    idgirande=random.choice(ff1)
    first.append("cash-in")
    second.append(idvariz)
    third.append(idgirande)
    sixth.append("0")
    seventh.append("none")
           
    """
    for amount of money generation
    """
    numberofmoney=random.randrange(50000,money)
    forth.append(numberofmoney)
    
    """
    for date and time generation randomly between two dates
    """
    final=randomDate(startt,endt, random.random())
    fifth.append(final)
    return (first,second,third,forth,fifth,sixth,seventh)
"""
this function is for generation of cashing in data that is not fraud action.

"""                
def normal111(startt,endt,money,first,second,third,forth,fifth,sixth,seventh,ff1,ff2,mm1,mm2):
                    
    """
    for source and destination id generation
    """
    """
    for type of banking work,label of fraud and type of fraud
    """
    
    idvariz=random.choice(mm2)
    idgirande=random.choice(ff2)
    first.append("cash-in")
    second.append(idvariz)
    third.append(idgirande)
    sixth.append("0")
    seventh.append("none")
           
    """
    for amount of money generation
    """
    numberofmoney=random.randrange(50000,money)
    forth.append(numberofmoney)
    
    """
    for date and time generation randomly between two dates
    """
    final=randomDate(startt,endt, random.random())
    fifth.append(final)
    return (first,second,third,forth,fifth,sixth,seventh)
"""
this function is for generation of cashing in data that is not fraud action.

"""                
def normal112(startt,endt,money,first,second,third,forth,fifth,sixth,seventh,ff1,ff2,mm1,mm2):
                    
    """
    for source and destination id generation
    """
    """
    for type of banking work,label of fraud and type of fraud
    """
    
    idvariz=random.choice(mm1)
    idgirande=random.choice(ff1)
    first.append("cash-in")
    second.append(idvariz)
    third.append(idgirande)
    sixth.append("0")
    seventh.append("none")
           
    """
    for amount of money generation
    """
    numberofmoney=random.randrange(50000,money)
    forth.append(numberofmoney)
    
    """
    for date and time generation randomly between two dates
    """
    final=randomDate(startt,endt, random.random())
    fifth.append(final)
    return (first,second,third,forth,fifth,sixth,seventh)
"""
this function is for generation of cashing in data that is not fraud action.

"""                
def normal113(startt,endt,money,first,second,third,forth,fifth,sixth,seventh,ff1,ff2,mm1,mm2):
                    
    """
    for source and destination id generation
    """
    """
    for type of banking work,label of fraud and type of fraud
    """
    
    idvariz=random.choice(mm1)
    idgirande=random.choice(ff2)
    first.append("cash-in")
    second.append(idvariz)
    third.append(idgirande)
    sixth.append("0")
    seventh.append("none")
           
    """
    for amount of money generation
    """
    numberofmoney=random.randrange(50000,money)
    forth.append(numberofmoney)
    
    """
    for date and time generation randomly between two dates
    """
    final=randomDate(startt,endt, random.random())
    fifth.append(final)
    return (first,second,third,forth,fifth,sixth,seventh)


"""
this function is for generation of cashing in data that is not fraud action.
 
""" 
def normal114(person1,startt,endt,moneyl,money,first,second,third,forth,fifth,sixth,seventh):
                    


    """
       theresholds for data generation
        """
    """
    for source and destination id generation
    """
    """
    for type of banking work,label of fraud and type of fraud
    """
    prule1=random.randrange(person1,30)
    idvariz=random.randrange(1, 100001)
    for j in range(0,prule1):
        idgirande=random.randrange(1, 100001)
        first.append("cash-in")
        second.append(idvariz)
        third.append(idgirande)
        sixth.append("0")
        seventh.append("none")
           
    """
    for amount of money generation
    """
    numberofmoney=random.randrange(5000,money)
    split(numberofmoney,prule1)
    
    """
    for date and time generation randomly between two dates
    """
    for k in range(0,prule1):
        final=randomDate(startt,endt, random.random())
        fifth.append(final)
    return (first,second,third,forth,fifth,sixth,seventh)

"""
this function is for generation of transfering data that is not fraud action.
 
"""                
def normal2(startt,endt,money2,first,second,third,forth,fifth,sixth,seventh,zz1,zz2):
                    

    """
    for source and destination id generation
    """
    """
    for type of banking work,label of fraud and type of fraud
    """
    
    idvariz=random.randrange(1, 100001)
    idgirande=random.randrange(1, 100001)
    zz1.append(idvariz)
    zz2.append(idgirande)
    first.append("transfer")
    second.append(idvariz)
    third.append(idgirande)
    sixth.append("0")
    seventh.append("none")
           
    """
    for amount of money generation
    """
    numberofmoney=random.randrange(50000,money2)
    forth.append(numberofmoney)
    
    """
    for date and time generation randomly between two dates
    """
    final=randomDate(startt,endt, random.random())
    fifth.append(final)
    return (first,second,third,forth,fifth,sixth,seventh,zz1,zz2)
"""
this function is for generation of transfering data that is not fraud action.

"""                
def normal21(startt,endt,money2,first,second,third,forth,fifth,sixth,seventh,zz1,zz2,bb1,bb2,bb3,aa1,aa2):
                    

    """
    for source and destination id generation
    """
    """
    for type of banking work,label of fraud and type of fraud
    """
    
    idvariz=random.choice(zz1)
    idgirande=random.choice(zz2)
    first.append("transfer")
    second.append(idvariz)
    third.append(idgirande)
    sixth.append("0")
    seventh.append("none")
           
    """
    for amount of money generation
    """
    numberofmoney=random.randrange(50000,money2)
    forth.append(numberofmoney)
    
    """
    for date and time generation randomly between two dates
    """
    final=randomDate(startt,endt, random.random())
    fifth.append(final)
    return (first,second,third,forth,fifth,sixth,seventh)
"""
this function is for generation of transfering data that is not fraud action.

"""                
def normal22(startt,endt,money2,first,second,third,forth,fifth,sixth,seventh,zz1,zz2,bb1,bb2,bb3,aa1,aa2):
                    

    """
    for source and destination id generation
    """
    """
    for type of banking work,label of fraud and type of fraud
    """
    
    idvariz=random.choice(zz1)
    idgirande=random.choice(zz1)
    first.append("transfer")
    second.append(idvariz)
    third.append(idgirande)
    sixth.append("0")
    seventh.append("none")
           
    """
    for amount of money generation
    """
    numberofmoney=random.randrange(50000,money2)
    forth.append(numberofmoney)
    
    """
    for date and time generation randomly between two dates
    """
    final=randomDate(startt,endt, random.random())
    fifth.append(final)
    return (first,second,third,forth,fifth,sixth,seventh)
"""
this function is for generation of transfering data that is not fraud action.

"""                
def normal23(startt,endt,money2,first,second,third,forth,fifth,sixth,seventh,zz1,zz2,bb1,bb2,bb3,aa1,aa2):
                    

    """
    for source and destination id generation
    """
    """
    for type of banking work,label of fraud and type of fraud
    """
    idvariz=random.choice(zz2)
    idgirande=random.choice(zz1)
    first.append("transfer")
    second.append(idvariz)
    third.append(idgirande)
    sixth.append("0")
    seventh.append("none")
           
    """
    for amount of money generation
    """
    numberofmoney=random.randrange(50000,money2)
    forth.append(numberofmoney)
    
    """
    for date and time generation randomly between two dates
    """
    final=randomDate(startt,endt, random.random())
    fifth.append(final)
    return (first,second,third,forth,fifth,sixth,seventh)
"""
this function is for generation of transfering data that is not fraud action.

"""                
def normal24(startt,endt,money2,first,second,third,forth,fifth,sixth,seventh,zz1,zz2,bb1,bb2,bb3,aa1,aa2):
                    

    """
    for source and destination id generation
    """
    """
    for type of banking work,label of fraud and type of fraud
    """
    
    idvariz=random.choice(zz2)
    idgirande=random.choice(zz2)
    first.append("transfer")
    second.append(idvariz)
    third.append(idgirande)
    sixth.append("0")
    seventh.append("none")
           
    """
    for amount of money generation
    """
    numberofmoney=random.randrange(50000,money2)
    forth.append(numberofmoney)
    
    """
    for date and time generation randomly between two dates
    """
    final=randomDate(startt,endt, random.random())
    fifth.append(final)
    return (first,second,third,forth,fifth,sixth,seventh)
"""
this function is for generation of transfering data that is not fraud action.

"""                
def normal25(startt,endt,money2,first,second,third,forth,fifth,sixth,seventh,zz1,zz2,bb1,bb2,bb3,aa1,aa2):
                    

    """
    for source and destination id generation
    """
    """
    for type of banking work,label of fraud and type of fraud
    """
    
    idvariz=random.choice(zz2)
    idgirande=random.choice(aa1)
    first.append("transfer")
    second.append(idvariz)
    third.append(idgirande)
    sixth.append("0")
    seventh.append("none")
           
    """
    for amount of money generation
    """
    numberofmoney=random.randrange(50000,money2)
    forth.append(numberofmoney)
    
    """
    for date and time generation randomly between two dates
    """
    final=randomDate(startt,endt, random.random())
    fifth.append(final)
    return (first,second,third,forth,fifth,sixth,seventh)
"""
this function is for generation of transfering data that is not fraud action.

"""                
def normal26(startt,endt,money2,first,second,third,forth,fifth,sixth,seventh,zz1,zz2,bb1,bb2,bb3,aa1,aa2):
                    

    """
    for source and destination id generation
    """
    """
    for type of banking work,label of fraud and type of fraud
    """
    
    idvariz=random.choice(zz1)
    idgirande=random.choice(aa1)
    first.append("transfer")
    second.append(idvariz)
    third.append(idgirande)
    sixth.append("0")
    seventh.append("none")
           
    """
    for amount of money generation
    """
    numberofmoney=random.randrange(50000,money2)
    forth.append(numberofmoney)
    
    """
    for date and time generation randomly between two dates
    """
    final=randomDate(startt,endt, random.random())
    fifth.append(final)
    return (first,second,third,forth,fifth,sixth,seventh)
"""
this function is for generation of transfering data that is not fraud action.

"""                
def normal27(startt,endt,money2,first,second,third,forth,fifth,sixth,seventh,zz1,zz2,bb1,bb2,bb3,aa1,aa2):
                    

    """
    for source and destination id generation
    """
    """
    for type of banking work,label of fraud and type of fraud
    """
    
    idvariz=random.choice(zz2)
    idgirande=random.choice(aa2)
    first.append("transfer")
    second.append(idvariz)
    third.append(idgirande)
    sixth.append("0")
    seventh.append("none")
           
    """
    for amount of money generation
    """
    numberofmoney=random.randrange(50000,money2)
    forth.append(numberofmoney)
    
    """
    for date and time generation randomly between two dates
    """
    final=randomDate(startt,endt, random.random())
    fifth.append(final)
    return (first,second,third,forth,fifth,sixth,seventh)
"""
this function is for generation of transfering data that is not fraud action.

"""                
def normal28(startt,endt,money2,first,second,third,forth,fifth,sixth,seventh,zz1,zz2,bb1,bb2,bb3,aa1,aa2):
                    

    """
    for source and destination id generation
    """
    """
    for type of banking work,label of fraud and type of fraud
    """
    
    idvariz=random.choice(zz1)
    idgirande=random.choice(aa2)
    first.append("transfer")
    second.append(idvariz)
    third.append(idgirande)
    sixth.append("0")
    seventh.append("none")
           
    """
    for amount of money generation
    """
    numberofmoney=random.randrange(50000,money2)
    forth.append(numberofmoney)
    
    """
    for date and time generation randomly between two dates
    """
    final=randomDate(startt,endt, random.random())
    fifth.append(final)
    return (first,second,third,forth,fifth,sixth,seventh)
"""
this function is for generation of transfering data that is not fraud action.

"""                
def normal29(startt,endt,money2,first,second,third,forth,fifth,sixth,seventh,zz1,zz2,bb1,bb2,bb3,aa1,aa2):
                    

    """
    for source and destination id generation
    """
    """
    for type of banking work,label of fraud and type of fraud
    """
    
    idvariz=random.choice(aa2)
    idgirande=random.choice(zz1)
    first.append("transfer")
    second.append(idvariz)
    third.append(idgirande)
    sixth.append("0")
    seventh.append("none")
           
    """
    for amount of money generation
    """
    numberofmoney=random.randrange(50000,money2)
    forth.append(numberofmoney)
    
    """
    for date and time generation randomly between two dates
    """
    final=randomDate(startt,endt, random.random())
    fifth.append(final)
    return (first,second,third,forth,fifth,sixth,seventh)
"""
this function is for generation of transfering data that is not fraud action.

"""                
def normal210(startt,endt,money2,first,second,third,forth,fifth,sixth,seventh,zz1,zz2,bb1,bb2,bb3,aa1,aa2):
                    

    """
    for source and destination id generation
    """
    """
    for type of banking work,label of fraud and type of fraud
    """
    
    idvariz=random.choice(aa2)
    idgirande=random.choice(zz2)
    first.append("transfer")
    second.append(idvariz)
    third.append(idgirande)
    sixth.append("0")
    seventh.append("none")
           
    """
    for amount of money generation
    """
    numberofmoney=random.randrange(50000,money2)
    forth.append(numberofmoney)
    
    """
    for date and time generation randomly between two dates
    """
    final=randomDate(startt,endt, random.random())
    fifth.append(final)
    return (first,second,third,forth,fifth,sixth,seventh)
"""
this function is for generation of transfering data that is not fraud action.

"""                
def normal211(startt,endt,money2,first,second,third,forth,fifth,sixth,seventh,zz1,zz2,bb1,bb2,bb3,aa1,aa2):
                    

    """
    for source and destination id generation
    """
    """
    for type of banking work,label of fraud and type of fraud
    """
    
    idvariz=random.choice(aa1)
    idgirande=random.choice(zz1)
    first.append("transfer")
    second.append(idvariz)
    third.append(idgirande)
    sixth.append("0")
    seventh.append("none")
           
    """
    for amount of money generation
    """
    numberofmoney=random.randrange(50000,money2)
    forth.append(numberofmoney)
    
    """
    for date and time generation randomly between two dates
    """
    final=randomDate(startt,endt, random.random())
    fifth.append(final)
    return (first,second,third,forth,fifth,sixth,seventh)
"""
this function is for generation of transfering data that is not fraud action.

"""                
def normal212(startt,endt,money2,first,second,third,forth,fifth,sixth,seventh,zz1,zz2,bb1,bb2,bb3,aa1,aa2):
                    

    """
    for source and destination id generation
    """
    """
    for type of banking work,label of fraud and type of fraud
    """
    
    idvariz=random.choice(aa1)
    idgirande=random.choice(zz2)
    first.append("transfer")
    second.append(idvariz)
    third.append(idgirande)
    sixth.append("0")
    seventh.append("none")
           
    """
    for amount of money generation
    """
    numberofmoney=random.randrange(50000,money2)
    forth.append(numberofmoney)
    
    """
    for date and time generation randomly between two dates
    """
    final=randomDate(startt,endt, random.random())
    fifth.append(final)
    return (first,second,third,forth,fifth,sixth,seventh)
"""
this function is for generation of transfering data that is not fraud action.

"""                
def normal213(startt,endt,money2,first,second,third,forth,fifth,sixth,seventh,zz1,zz2,bb1,bb2,bb3,aa1,aa2):
                    

    """
    for source and destination id generation
    """
    """
    for type of banking work,label of fraud and type of fraud
    """
    
    idvariz=random.choice(zz1)
    idgirande=random.choice(bb1)
    first.append("transfer")
    second.append(idvariz)
    third.append(idgirande)
    sixth.append("0")
    seventh.append("none")
           
    """
    for amount of money generation
    """
    numberofmoney=random.randrange(50000,money2)
    forth.append(numberofmoney)
    
    """
    for date and time generation randomly between two dates
    """
    final=randomDate(startt,endt, random.random())
    fifth.append(final)
    return (first,second,third,forth,fifth,sixth,seventh)
"""
this function is for generation of transfering data that is not fraud action.

"""                
def normal214(startt,endt,money2,first,second,third,forth,fifth,sixth,seventh,zz1,zz2,bb1,bb2,bb3,aa1,aa2):
                    

    """
    for source and destination id generation
    """
    """
    for type of banking work,label of fraud and type of fraud
    """
    
    idvariz=random.choice(zz1)
    idgirande=random.choice(bb3)
    first.append("transfer")
    second.append(idvariz)
    third.append(idgirande)
    sixth.append("0")
    seventh.append("none")
           
    """
    for amount of money generation
    """
    numberofmoney=random.randrange(50000,money2)
    forth.append(numberofmoney)
    
    """
    for date and time generation randomly between two dates
    """
    final=randomDate(startt,endt, random.random())
    fifth.append(final)
    return (first,second,third,forth,fifth,sixth,seventh)
"""
this function is for generation of transfering data that is not fraud action.

"""                
def normal215(startt,endt,money2,first,second,third,forth,fifth,sixth,seventh,zz1,zz2,bb1,bb2,bb3,aa1,aa2):
                    

    """
    for source and destination id generation
    """
    """
    for type of banking work,label of fraud and type of fraud
    """
    
    idvariz=random.choice(zz1)
    idgirande=random.choice(bb2)
    first.append("transfer")
    second.append(idvariz)
    third.append(idgirande)
    sixth.append("0")
    seventh.append("none")
           
    """
    for amount of money generation
    """
    numberofmoney=random.randrange(50000,money2)
    forth.append(numberofmoney)
    
    """
    for date and time generation randomly between two dates
    """
    final=randomDate(startt,endt, random.random())
    fifth.append(final)
    return (first,second,third,forth,fifth,sixth,seventh)
"""
this function is for generation of transfering data that is not fraud action.

"""                
def normal216(startt,endt,money2,first,second,third,forth,fifth,sixth,seventh,zz1,zz2,bb1,bb2,bb3,aa1,aa2):
                    

    """
    for source and destination id generation
    """
    """
    for type of banking work,label of fraud and type of fraud
    """
    
    idvariz=random.choice(zz2)
    idgirande=random.choice(bb1)
    first.append("transfer")
    second.append(idvariz)
    third.append(idgirande)
    sixth.append("0")
    seventh.append("none")
           
    """
    for amount of money generation
    """
    numberofmoney=random.randrange(50000,money2)
    forth.append(numberofmoney)
    
    """
    for date and time generation randomly between two dates
    """
    final=randomDate(startt,endt, random.random())
    fifth.append(final)
    return (first,second,third,forth,fifth,sixth,seventh)
"""
this function is for generation of transfering data that is not fraud action.

"""                
def normal217(startt,endt,money2,first,second,third,forth,fifth,sixth,seventh,zz1,zz2,bb1,bb2,bb3,aa1,aa2):
                    

    """
    for source and destination id generation
    """
    """
    for type of banking work,label of fraud and type of fraud
    """
    
    idvariz=random.choice(zz2)
    idgirande=random.choice(bb3)
    first.append("transfer")
    second.append(idvariz)
    third.append(idgirande)
    sixth.append("0")
    seventh.append("none")
           
    """
    for amount of money generation
    """
    numberofmoney=random.randrange(50000,money2)
    forth.append(numberofmoney)
    
    """
    for date and time generation randomly between two dates
    """
    final=randomDate(startt,endt, random.random())
    fifth.append(final)
    return (first,second,third,forth,fifth,sixth,seventh)
"""
this function is for generation of transfering data that is not fraud action.

"""                
def normal218(startt,endt,money2,first,second,third,forth,fifth,sixth,seventh,zz1,zz2,bb1,bb2,bb3,aa1,aa2):
                    

    """
    for source and destination id generation
    """
    """
    for type of banking work,label of fraud and type of fraud
    """
    
    idvariz=random.choice(zz2)
    idgirande=random.choice(bb2)
    first.append("transfer")
    second.append(idvariz)
    third.append(idgirande)
    sixth.append("0")
    seventh.append("none")
           
    """
    for amount of money generation
    """
    numberofmoney=random.randrange(50000,money2)
    forth.append(numberofmoney)
    
    """
    for date and time generation randomly between two dates
    """
    final=randomDate(startt,endt, random.random())
    fifth.append(final)
    return (first,second,third,forth,fifth,sixth,seventh)
"""
this function is for generation of transfering data that is not fraud action.

"""                
def normal219(startt,endt,money2,first,second,third,forth,fifth,sixth,seventh,zz1,zz2,bb1,bb2,bb3,aa1,aa2):
                    

    """
    for source and destination id generation
    """
    """
    for type of banking work,label of fraud and type of fraud
    """
    
    idvariz=random.choice(bb1)
    idgirande=random.choice(zz1)
    first.append("transfer")
    second.append(idvariz)
    third.append(idgirande)
    sixth.append("0")
    seventh.append("none")
           
    """
    for amount of money generation
    """
    numberofmoney=random.randrange(50000,money2)
    forth.append(numberofmoney)
    
    """
    for date and time generation randomly between two dates
    """
    final=randomDate(startt,endt, random.random())
    fifth.append(final)
    return (first,second,third,forth,fifth,sixth,seventh)
"""
this function is for generation of transfering data that is not fraud action.

"""                
def normal220(startt,endt,money2,first,second,third,forth,fifth,sixth,seventh,zz1,zz2,bb1,bb2,bb3,aa1,aa2):
                    

    """
    for source and destination id generation
    """
    """
    for type of banking work,label of fraud and type of fraud
    """
    
    idvariz=random.choice(bb1)
    idgirande=random.choice(zz2)
    first.append("transfer")
    second.append(idvariz)
    third.append(idgirande)
    sixth.append("0")
    seventh.append("none")
           
    """
    for amount of money generation
    """
    numberofmoney=random.randrange(50000,money2)
    forth.append(numberofmoney)
    
    """
    for date and time generation randomly between two dates
    """
    final=randomDate(startt,endt, random.random())
    fifth.append(final)
    return (first,second,third,forth,fifth,sixth,seventh)
"""
this function is for generation of transfering data that is not fraud action.

"""                
def normal221(startt,endt,money2,first,second,third,forth,fifth,sixth,seventh,zz1,zz2,bb1,bb2,bb3,aa1,aa2):
                    

    """
    for source and destination id generation
    """
    """
    for type of banking work,label of fraud and type of fraud
    """
    
    idvariz=random.choice(bb3)
    idgirande=random.choice(zz1)
    first.append("transfer")
    second.append(idvariz)
    third.append(idgirande)
    sixth.append("0")
    seventh.append("none")
           
    """
    for amount of money generation
    """
    numberofmoney=random.randrange(50000,money2)
    forth.append(numberofmoney)
    
    """
    for date and time generation randomly between two dates
    """
    final=randomDate(startt,endt, random.random())
    fifth.append(final)
    return (first,second,third,forth,fifth,sixth,seventh)
"""
this function is for generation of transfering data that is not fraud action.

"""                
def normal222(startt,endt,money2,first,second,third,forth,fifth,sixth,seventh,zz1,zz2,bb1,bb2,bb3,aa1,aa2):
                    

    """
    for source and destination id generation
    """
    """
    for type of banking work,label of fraud and type of fraud
    """
    
    idvariz=random.choice(bb3)
    idgirande=random.choice(zz2)
    first.append("transfer")
    second.append(idvariz)
    third.append(idgirande)
    sixth.append("0")
    seventh.append("none")
           
    """
    for amount of money generation
    """
    numberofmoney=random.randrange(50000,money2)
    forth.append(numberofmoney)
    
    """
    for date and time generation randomly between two dates
    """
    final=randomDate(startt,endt, random.random())
    fifth.append(final)
    return (first,second,third,forth,fifth,sixth,seventh)
"""
this function is for generation of transfering data that is not fraud action.

"""                
def normal223(startt,endt,money2,first,second,third,forth,fifth,sixth,seventh,zz1,zz2,bb1,bb2,bb3,aa1,aa2):
                    

    """
    for source and destination id generation
    """
    """
    for type of banking work,label of fraud and type of fraud
    """
    
    idvariz=random.choice(bb2)
    idgirande=random.choice(zz1)
    first.append("transfer")
    second.append(idvariz)
    third.append(idgirande)
    sixth.append("0")
    seventh.append("none")
           
    """
    for amount of money generation
    """
    numberofmoney=random.randrange(50000,money2)
    forth.append(numberofmoney)
    
    """
    for date and time generation randomly between two dates
    """
    final=randomDate(startt,endt, random.random())
    fifth.append(final)
    return (first,second,third,forth,fifth,sixth,seventh)
"""
this function is for generation of transfering data that is not fraud action.

"""                
def normal224(startt,endt,money2,first,second,third,forth,fifth,sixth,seventh,zz1,zz2,bb1,bb2,bb3,aa1,aa2):
                    

    """
    for source and destination id generation
    """
    """
    for type of banking work,label of fraud and type of fraud
    """
    
    idvariz=random.choice(bb2)
    idgirande=random.choice(zz2)
    first.append("transfer")
    second.append(idvariz)
    third.append(idgirande)
    sixth.append("0")
    seventh.append("none")
           
    """
    for amount of money generation
    """
    numberofmoney=random.randrange(50000,money2)
    forth.append(numberofmoney)
    
    """
    for date and time generation randomly between two dates
    """
    final=randomDate(startt,endt, random.random())
    fifth.append(final)
    return (first,second,third,forth,fifth,sixth,seventh)

"""
this function is for generation of cashing in data that is not fraud action.
 
""" 
def normal225(person2,startt,endt,moneyl2,money2,first,forth,sixth,seventh):
    """
    theresholds for data generation
    """
    global miani3
    miani3=[]
    global miani4
    miani4=[]
    global sort1
    sort1=[]
    """
    for source and destination id generation
    """
    """
    for type of banking work,label of fraud and type of fraud
    """
    prule2=random.randrange(person2,25)
    for s in range(0,prule2):
        if s!=0:
            ids=random.randrange(1, 100001)
            first.append("transfer")
            miani3.append(miani4[s-1])
            miani4.append(ids)
            sixth.append("0")
            seventh.append("none")
        if s==0 :
            ids1=random.randrange(1, 100001)
            ids2=random.randrange(1, 100001)
            first.append("transfer")        
            miani3.append(ids1)
            miani4.append(ids2)
            sixth.append("0")
            seventh.append("none")

    """
    for amount of money generation
    """
    numberofmoney2=random.randrange(5000,money2)
    for e in range(0,prule2):
        forth.append(numberofmoney2)
    """
    for date and time generation randomly between two dates
    """
    for m in range(0,prule2):
        final2=randomDate(startt,endt, random.random())
        sort.append(final2)
    return (first,forth,sixth,seventh)
"""
this function is for generation of cashing in data that is not fraud action.
 
""" 

def normal226(person1,startt,endt,moneyl2,money2,first,second,third,forth,fifth,sixth,seventh):
    """
       theresholds for data generation
    """
    
    """
    for source and destination id generation
    """
    """
    for type of banking work,label of fraud and type of fraud
    """
    
    idvariz2=random.randrange(1, 100001)
    prule3=random.randrange(person1,30)
    for n in range(0,prule3):
        idgirande2=random.randrange(1, 100001)
        first.append("transfer")
        third.append(idvariz2)
        second.append(idgirande2)
        sixth.append("0")
        seventh.append("none")
    """
    for amount of money generation
    """
    numberofmoney3=random.randrange(5000, money2)
    split(numberofmoney3,prule3)
    
    """
    for date and time generation randomly between two dates
    """
    for h in range(0,prule3):
        final=randomDate(startt,endt, random.random())
        fifth.append(final)
    return (first,second,third,forth,fifth,sixth,seventh)
##############################################################################
def nextpage():
   window1 =tk.Tk()
   window1.title("Money-Laundering Data Generation")
   color1='#CCFFFF'
   color2='#CCCCFF'
   color3='#FFCCE5'
   color5='#99FFCC'
   color6='#FFCC99'
   color7='#00CED1'
   color8='#87CEFA'
   global txt1
   global txt2
   global txt3
   global txt4
   global txt5
   global txt6
   global txt7
   global txt8
   global txt9
   global txt10
   global txt11
   global txt12
   global txt13
   frame=tk.Frame(window1)
   frame.pack()
   bottomframe=tk.Frame(window1)
   bottomframe.pack(side=BOTTOM)
   bottomframe1=tk.Frame(bottomframe)
   bottomframe1.pack(side=BOTTOM)
   bottomframe2=tk.Frame(bottomframe1)
   bottomframe2.pack(side=BOTTOM)
   bottomframe3=tk.Frame(bottomframe2)
   bottomframe3.pack(side=BOTTOM)
   bottomframe4=tk.Frame(bottomframe3)
   bottomframe4.pack(side=BOTTOM)
   bottomframe5=tk.Frame(bottomframe4)
   bottomframe5.pack(side=BOTTOM)
   bottomframe6=tk.Frame(bottomframe5)
   bottomframe6.pack(side=BOTTOM)
   label1= tk.Label(frame, text="number of generation of rule1",bg=color1,font=fontStyle1)
   label1.pack(side=LEFT,pady=3,fill=X)
   txt1=tk.Entry(frame,width=10,bg=color1)
   txt1.pack(side=LEFT,pady=3,fill=X)
   label2= tk.Label(frame, text="number of generation of rule2",bg=color1,font=fontStyle1)
   label2.pack(side=LEFT,pady=3)
   txt2=tk.Entry(frame,width=10,bg=color1)
   txt2.pack(side=LEFT,pady=3)
   label3= tk.Label(frame, text="number of generation of rule3",bg=color1,font=fontStyle1)
   label3.pack(side=LEFT,pady=3,fill=X)
   txt3=tk.Entry(frame,width=10,bg=color1)
   txt3.pack(side=LEFT,pady=3)
   label4= tk.Label(bottomframe, text="how much money for cashing in is money laundering crime?",bg=color2,font=fontStyle1)
   label4.pack(side=LEFT,pady=10)
   txt4=tk.Entry(bottomframe,width=15,bg=color2)
   txt4.pack(side=LEFT,pady=3)
   label5= tk.Label(bottomframe, text="how much money is suitble for cashing in crime?",bg=color2,font=fontStyle1)
   label5.pack(side=LEFT,pady=10)
   txt5=tk.Entry(bottomframe,width=15,bg=color2)
   txt5.pack(side=LEFT,pady=3)
   label6= tk.Label(bottomframe1, text="how much money for transfering is money laundering crime?",bg=color3,font=fontStyle1)
   label6.pack(side=LEFT,pady=10)
   txt6=tk.Entry(bottomframe1,width=15,bg=color3)
   txt6.pack(side=LEFT,pady=3)
   label7= tk.Label(bottomframe1, text="how much money is suitble for transfering crime?",bg=color3,font=fontStyle1)
   label7.pack(side=LEFT,pady=10)
   txt7=tk.Entry(bottomframe1,width=15,bg=color3)
   txt7.pack(side=LEFT,pady=3)
   label8= tk.Label(bottomframe2, text="enter  start time like  2019/2/20 8:13",bg=color5,font=fontStyle1)
   label8.pack(side=LEFT,pady=10)
   txt8=tk.Entry(bottomframe2,width=20,bg=color5)
   txt8.pack(side=LEFT,pady=3)
   label9= tk.Label(bottomframe2, text="enter  end time like  2019/7/20 11:3",bg=color5,font=fontStyle1)
   label9.pack(side=LEFT,pady=10)
   txt9=tk.Entry(bottomframe2,width=20,bg=color5)
   txt9.pack(side=LEFT,pady=3)
   label12= tk.Label(bottomframe4, text="How many not fraud data do you want for cashing in action(should more than 40)?",bg=color6,font=fontStyle1)
   label12.pack(side=LEFT,pady=10)
   txt12=tk.Entry(bottomframe4,width=10,bg=color6)
   txt12.pack(side=LEFT,pady=3)
   label13= tk.Label(bottomframe5, text="How many not fraud data do you want for transfering action(should more than 80)?",bg=color7,font=fontStyle1)
   label13.pack(side=LEFT,pady=10)
   txt13=tk.Entry(bottomframe5,width=10,bg=color7)
   txt13.pack(side=LEFT,pady=3)
   button=tk.Button(bottomframe6,text="DONE",command=final,font=fontStyle1,bg=color8)
   button.pack()
   window1.geometry('1000x285')
   window1.mainloop()
   
def final():
    try:
        number1=txt1.get()
        number2=txt2.get()
        number3=txt3.get()
        moneyl=txt4.get()
        money=txt5.get()
        moneyl2=txt6.get()
        money2=txt7.get()
        startt=txt8.get()
        endt=txt9.get()
        number4=txt12.get()
        number5=txt13.get()
        person1=3
        person2=3
        """
        arrays for data generation
        """
        global first
        global second
        global third
        global forth
        global fifth
        global sixth
        global seventh
        first=[]
        second=[]
        third=[]
        forth=[]
        fifth=[]
        sixth=[]
        seventh=[]
        ff1=[]
        ff2=[]
        mm1=[]
        mm2=[]
        zz1=[]
        zz2=[]
        aa1=[]
        aa2=[]
        bb1=[]
        bb2=[]
        bb3=[]
        """
        calling rule1 function
        """
        number1=int(number1)
        person1=int(person1)
        moneyl=int(moneyl)
        money=int(money)
        for f in range(0,number1):
            rule1(person1,startt,endt,moneyl,money,first,second,third,forth,fifth,sixth,seventh,mm1,mm2)
        
        """
        calling rule2 function
        """
        number2=int(number2)
        moneyl2=int(moneyl2)
        person2=int(person2)
        money2=int(money2)
        for a in range(0,number2):
            rule2(person2,startt,endt,moneyl2,money2,first,forth,sixth,seventh,bb1,bb2,bb3)
            second=second+miani1
            third=third+miani2
            fifth=fifth+sorted(sort)
        """
        calling rule3 function
        """
        number3=int(number3)
        for b in range(0,number3):
            rule3(person1,startt,endt,moneyl2,money2,first,second,third,forth,fifth,sixth,seventh,aa1,aa2)
            
        """
        calling normal1 function
        """
        number4=int(number4)
        for v in range(0,number4):
            normal1(startt,endt,money,first,second,third,forth,fifth,sixth,seventh,ff1,ff2,mm1,mm2)
        """
        calling normal12 function
        """
        number42=int(number4*(0.025))
        for v1 in range(0,number42):
            normal12(startt,endt,money,first,second,third,forth,fifth,sixth,seventh,ff1,ff2,mm1,mm2)
        """
        calling normal13 function
        """
        for v2 in range(0,number42):
            normal13(startt,endt,money,first,second,third,forth,fifth,sixth,seventh,ff1,ff2,mm1,mm2)
        """
        calling normal14 function
        """
        for v3 in range(0,number42):
            normal14(startt,endt,money,first,second,third,forth,fifth,sixth,seventh,ff1,ff2,mm1,mm2)
        """
        calling normal15 function
        """
        for v4 in range(0,number42):
            normal15(startt,endt,money,first,second,third,forth,fifth,sixth,seventh,ff1,ff2,mm1,mm2)
        """
        calling normal16 function
        """
        for v5 in range(0,number42):
            normal16(startt,endt,money,first,second,third,forth,fifth,sixth,seventh,ff1,ff2,mm1,mm2)
        """
        calling normal17 function
        """
        for v6 in range(0,number42):
            normal17(startt,endt,money,first,second,third,forth,fifth,sixth,seventh,ff1,ff2,mm1,mm2)
        """
        calling normal18 function
        """
        for v7 in range(0,number42):
            normal18(startt,endt,money,first,second,third,forth,fifth,sixth,seventh,ff1,ff2,mm1,mm2)
        """
        calling normal19 function
        """
        for v8 in range(0,number42):
            normal19(startt,endt,money,first,second,third,forth,fifth,sixth,seventh,ff1,ff2,mm1,mm2)
        """
        calling normal110 function
        """
        for v9 in range(0,number42):
            normal110(startt,endt,money,first,second,third,forth,fifth,sixth,seventh,ff1,ff2,mm1,mm2)
        """
        calling normal111 function
        """
        for v10 in range(0,number42):
            normal111(startt,endt,money,first,second,third,forth,fifth,sixth,seventh,ff1,ff2,mm1,mm2)
        """
        calling normal112 function
        """
        for v11 in range(0,number42):
            normal112(startt,endt,money,first,second,third,forth,fifth,sixth,seventh,ff1,ff2,mm1,mm2)
        """
        calling normal113 function
        """
        for v12 in range(0,number42):
            normal113(startt,endt,money,first,second,third,forth,fifth,sixth,seventh,ff1,ff2,mm1,mm2)
        """
        calling normal114 function
        """
        for v13 in range(0,number42):
            normal114(person1,startt,endt,moneyl,money,first,second,third,forth,fifth,sixth,seventh)
            
        """
        calling normal2 function
        """
        number5=int(number5)
        for v14 in range(0,number5):
            normal2(startt,endt,money2,first,second,third,forth,fifth,sixth,seventh,zz1,zz2)
        """
        calling normal21 function
        """
        number52=int(number5*(0.0125))
        for v15 in range(0,number52):
            normal21(startt,endt,money2,first,second,third,forth,fifth,sixth,seventh,zz1,zz2,bb1,bb2,bb3,aa1,aa2)
        """
        calling normal22 function
        """
        for v16 in range(0,number52):
            normal22(startt,endt,money2,first,second,third,forth,fifth,sixth,seventh,zz1,zz2,bb1,bb2,bb3,aa1,aa2)
        """
        calling normal23 function
        """
        
        for v17 in range(0,number52):
            normal23(startt,endt,money2,first,second,third,forth,fifth,sixth,seventh,zz1,zz2,bb1,bb2,bb3,aa1,aa2)
        """
        calling normal24 function
        """
        
        for v18 in range(0,number52):
            normal24(startt,endt,money2,first,second,third,forth,fifth,sixth,seventh,zz1,zz2,bb1,bb2,bb3,aa1,aa2)
        """
        calling normal25 function
        """
        
        for v19 in range(0,number52):
            normal25(startt,endt,money2,first,second,third,forth,fifth,sixth,seventh,zz1,zz2,bb1,bb2,bb3,aa1,aa2)
        """
        calling normal26 function
        """
        
        for v20 in range(0,number52):
            normal26(startt,endt,money2,first,second,third,forth,fifth,sixth,seventh,zz1,zz2,bb1,bb2,bb3,aa1,aa2)
        """
        calling normal27 function
        """
        
        for v21 in range(0,number52):
            normal27(startt,endt,money2,first,second,third,forth,fifth,sixth,seventh,zz1,zz2,bb1,bb2,bb3,aa1,aa2)
        """
        calling normal28 function
        """
        
        for v22 in range(0,number52):
            normal28(startt,endt,money2,first,second,third,forth,fifth,sixth,seventh,zz1,zz2,bb1,bb2,bb3,aa1,aa2)
        """
        calling normal29 function
        """
        
        for v23 in range(0,number52):
            normal29(startt,endt,money2,first,second,third,forth,fifth,sixth,seventh,zz1,zz2,bb1,bb2,bb3,aa1,aa2)
        """
        calling normal210 function
        """
        
        for v24 in range(0,number52):
            normal210(startt,endt,money2,first,second,third,forth,fifth,sixth,seventh,zz1,zz2,bb1,bb2,bb3,aa1,aa2)
        """
        calling normal211 function
        """
        
        for v25 in range(0,number52):
            normal211(startt,endt,money2,first,second,third,forth,fifth,sixth,seventh,zz1,zz2,bb1,bb2,bb3,aa1,aa2)
        """
        calling normal212 function
        """
        
        for v26 in range(0,number52):
            normal212(startt,endt,money2,first,second,third,forth,fifth,sixth,seventh,zz1,zz2,bb1,bb2,bb3,aa1,aa2)
        
        """
        calling normal213 function
        """
        
        for v27 in range(0,number52):
            normal213(startt,endt,money2,first,second,third,forth,fifth,sixth,seventh,zz1,zz2,bb1,bb2,bb3,aa1,aa2)
        """
        calling normal214 function
        """
        
        for v28 in range(0,number52):
            normal214(startt,endt,money2,first,second,third,forth,fifth,sixth,seventh,zz1,zz2,bb1,bb2,bb3,aa1,aa2)
        """
        calling normal215 function
        """
        
        for v29 in range(0,number52):
            normal215(startt,endt,money2,first,second,third,forth,fifth,sixth,seventh,zz1,zz2,bb1,bb2,bb3,aa1,aa2)
        """
        calling normal216 function
        """
        
        for v30 in range(0,number52):
            normal216(startt,endt,money2,first,second,third,forth,fifth,sixth,seventh,zz1,zz2,bb1,bb2,bb3,aa1,aa2)
        """
        calling normal217 function
        """
        
        for v31 in range(0,number52):
            normal217(startt,endt,money2,first,second,third,forth,fifth,sixth,seventh,zz1,zz2,bb1,bb2,bb3,aa1,aa2)
        """
        calling normal218 function
        """
        
        for v32 in range(0,number52):
            normal218(startt,endt,money2,first,second,third,forth,fifth,sixth,seventh,zz1,zz2,bb1,bb2,bb3,aa1,aa2)
        """
        calling normal219 function
        """
        
        for v33 in range(0,number52):
            normal219(startt,endt,money2,first,second,third,forth,fifth,sixth,seventh,zz1,zz2,bb1,bb2,bb3,aa1,aa2)
        """
        calling normal220 function
        """
        
        for v34 in range(0,number52):
            normal220(startt,endt,money2,first,second,third,forth,fifth,sixth,seventh,zz1,zz2,bb1,bb2,bb3,aa1,aa2)
        """
        calling normal221 function
        """
        
        for v35 in range(0,number52):
            normal221(startt,endt,money2,first,second,third,forth,fifth,sixth,seventh,zz1,zz2,bb1,bb2,bb3,aa1,aa2)
        """
        calling normal222 function
        """
        
        for v36 in range(0,number52):
            normal222(startt,endt,money2,first,second,third,forth,fifth,sixth,seventh,zz1,zz2,bb1,bb2,bb3,aa1,aa2)
        """
        calling normal223 function
        """
        
        for v37 in range(0,number52):
            normal223(startt,endt,money2,first,second,third,forth,fifth,sixth,seventh,zz1,zz2,bb1,bb2,bb3,aa1,aa2)
        """
        calling normal224 function
        """
        
        for v38 in range(0,number52):
            normal224(startt,endt,money2,first,second,third,forth,fifth,sixth,seventh,zz1,zz2,bb1,bb2,bb3,aa1,aa2)
        """
        calling normal225 function
        """
        
        for v39 in range(0,number52):
            normal225(person2,startt,endt,moneyl2,money2,first,forth,sixth,seventh)
            second=second+miani3
            third=third+miani4
            fifth=fifth+sorted(sort1)
        """
        calling normal226 function
        """
        
        for v40 in range(0,number52):
            normal226(person1,startt,endt,moneyl2,money2,first,second,third,forth,fifth,sixth,seventh)
        
        guilty=[]
        typeper=[]
        typefr=[]
        
        for lenn6,lennn6 in enumerate(mm1):
            guilty.append(lennn6)
            typeper.append("head")
            typefr.append("type1")
        
        for lenn2,lennn2 in enumerate(bb1):
            guilty.append(lennn2)
            typeper.append("head")
            typefr.append("type2")
            
        
        for lenn1,lennn1 in enumerate(aa1):
            guilty.append(lennn1)
            typeper.append("head")
            typefr.append("type3")
        
        for lenn7,lennn7 in enumerate(mm2):
            guilty.append(lennn7)
            typeper.append("colleague")
            typefr.append("type1")
        
        for lenn5,lennn5 in enumerate(bb2):
            guilty.append(lennn5)
            typeper.append("colleague")
            typefr.append("type2")
            
        for lenn3,lennn3 in enumerate(bb3):
            guilty.append(lennn3)
            typeper.append("colleague")
            typefr.append("type2")    
        
        for lenn4,lennn4 in enumerate(aa2):
            guilty.append(lennn4)
            typeper.append("colleague")
            typefr.append("type3")
            
        print(bb3)
        """
        for saving arrays to a csv file
        """
        rel=list(zip(first,second,third,forth,fifth,sixth,seventh))
        pp=pd.DataFrame(data=rel , columns=['typeofaction','sourceid','destinationid','amountofmoney','date','isfraud','typeoffraud'])
        pp.to_csv(r'D:\Ml.csv',index=False)
        
        rel1=list(zip(guilty,typeper,typefr))
        pp1=pd.DataFrame(data=rel1 , columns=['guiltyid','levelofcrime','typeofcrime'])
        pp1.to_csv(r'D:\Mlltag.csv',index=False)
        
        messagebox.showinfo("information","Your data and label of guilties are saved to D folder.Name of data is ML.csv and name of label is Mltag.csv.") 
        
    except ValueError:
        messagebox.showerror("Error", "Please enter all data and take attention to format of data")

window =tk.Tk()
window.title("Money-Laundering Data Generation")
color='#49A'
window.configure(bg=color)
fontStyle = tkFont.Font(family="Showcard Gothic", size=16)
fontStyle1 = tkFont.Font(family="Bodoni MT", size=14)
label1= tk.Label(window, text="Welcome To Money Laundering Data Generation System Written By MARYAM MAHOOTIHA",font=fontStyle)
label1.pack(side = TOP , pady = 5)
label2= tk.Label(window, text="I generate data by 3 rules.First rule is about a person who splits a big money to shorter money and",font=fontStyle1)
label2.pack(fill=X)
label3= tk.Label(window, text="give shorter money to many people.Second is about some person who  transfer money sequentially in a range of time.",font=fontStyle1)
label3.pack(fill=X)
label4= tk.Label(window, text="Third rule is about many person who transfer short money to one person and sum of these transfers is big",font=fontStyle1)
label4.pack(fill=X)
label5= tk.Label(window, text="For Generation Of Data Please enter next information.",font=fontStyle1)
label5.pack(fill=X)
color7='#00CED1'
button=tk.Button(text="NEXT",command=nextpage,font=fontStyle1,bg=color7)
button.pack(side = TOP , pady = 5)
window.geometry('1000x250')
window.mainloop()
