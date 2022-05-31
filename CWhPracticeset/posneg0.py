a=float(input("Num: "))
if a==0:
    print ('Zero %d' %(a))
elif a>0:
    print ('Positive {}'.format(a))
elif a<0:
    print ('Negative '+str(a))
else:
    print ('What?')