import pprint               #for printing every value of a dictionary in new line
def china(hrs,cap,chin,units,key,d):
    i=len(key)-1
    count=0
    cost=0
    d["machines"]=[]
    d["region"]="China"
    while(i>=0):
        if(chin[key[i]] is not None):
            if(cap>=units[key[i]]):
                count=cap//units[key[i]]
                cap=int(cap%units[key[i]])
                cost=cost+count*(chin[key[i]])
                v=(key[i],count)
                d["machines"].append(v)
        i=i-1
    cost="$"+str(cost*hrs)
    d["total_cost"]=cost
    return d
def india(hrs,cap,ind,units,key,d):
    i=len(key)-1
    count=0
    cost=0
    d["machines"]=[]
    d["region"]="India"
    while(i>=0):
        if(ind[key[i]] is not None):
            if(cap>=units[key[i]]):
                count=cap//units[key[i]]
                cap=int(cap%units[key[i]])
                cost=cost+count*(ind[key[i]])
                v=(key[i],count)
                d["machines"].append(v)
        i=i-1
    cost="$"+str(cost*hrs)
    d["total_cost"]=cost
    return d
def newyork(hrs,cap,ny,units,key,d):
    i=len(key)-1
    count=0
    cost=0
    d["region"]="New York"
    while(i>=0):
        if(ny[key[i]] is not None):
            if(cap>=units[key[i]]):
                count=cap//units[key[i]]
                cap=int(cap%units[key[i]])
                cost=cost+count*(ny[key[i]])
                v=(key[i],count)
                d["machines"].append(v)
        i=i-1
    cost="$"+str(cost*hrs)
    d["total_cost"]=cost
    return d
def main(hrs,cap):
    ny={"large":120,"xlarge":230,"2xlarge":450,"4xlarge":774,"8xlarge":1400}
    ind={"large":140,"xlarge":None,"2xlarge":413,"4xlarge":826,"8xlarge":1300}
    chin={"large":110,"xlarge":200,"2xlarge":None,"4xlarge":670,"8xlarge":1180}
    units={"large":10,"xlarge":20,"2xlarge":40,"4xlarge":80,"8xlarge":160}
    d={"region":None,"total_cost":None,"machines":[]}
    key=list(units.keys())
    sol={}
    a={}
    a.update(newyork(hrs,cap,ny,units,key,d))
    b={}
    b.update(india(hrs,cap,ind,units,key,d))
    c={}
    c.update(china(hrs,cap,chin,units,key,d))
    sol["Output"]=[a,b,c]
    pprint.pprint(sol,compact=True,sort_dicts=False,width=50,indent=2)
if __name__=="__main__":
    hrs=int(input("Enter total hours:"))
    cap=int(input("Enter total capacity:"))
    main(hrs,cap)
    
#Note:- The alignment of the answers may not be same as of the sample output shown, but answer is correct and I want to inform Techtinium Technologies that in the sample output given by Techtinium Technologies is wrong for Region- China as the total cost is 8570 not 8580, please check it and rectify it.
#Test case1: Enter total hours: 1
############ Enter total capacity: 1150

#Test case2: Enter total hours: 5
############ Enter total capacity: 230

# Test case3: Enter total hours: 24
############# Enter total capacity: 100

#Test case4: Enter total hours: 12
############ Enter total capacity: 1100
