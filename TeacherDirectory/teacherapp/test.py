with open('F:/details.txt','r') as rd:
    l=rd.readlines()
    output= ' '.join(l)
    print(set(output.split()))
    
    