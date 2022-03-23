def shuffle(l1,l2):
    s=[]
    if len(l1)!= 0 and len(l2)!=0:
        for i in range(min(len(l1),len(l2))):
            s.append(l1[i])
            s.append(l2[i])
        for i in range(min(len(l1),len(l2)),max(len(l1),len(l2))):
            if len(l1)>len(l2):
                s.append(l1[i])
            else:
                s.append(l2[i])
    else:
        s.extend(l1[0:] or l2[0:])   
    return s
print(shuffle([1,2,3],[3,4,5]))