for i in range(1,10):
    for j in range(1,10):
        s=i*j
        print("%d*"%i,"%d="%j,"%-4d"%s,end="    ")
    print("")