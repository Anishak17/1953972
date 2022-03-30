import pandas as pd
d={1:"Add grocery items to store  [name, quantity, price] :",2:"Buy grocery items from store [name, quantity] :",3:"exit"}
a,b,g={},{},{}
def dis(y,c):
    df=pd.DataFrame(y).T
    df.columns = c
    print(df)
    return pd.DataFrame(df.iloc[:,1:].to_dict(),index=df.iloc[:,0])
    
def ask():
    while(True):
        for i,j in d.items():
            print("\npress",i,"to",j)
        
        x=int(input())
        if x==1:
            get(a,b,x)
            dis(a,["name","quantity","price"]).to_excel("grocery_store.xlsx")
            
        elif x==2:
            for i in range(len(pd.read_excel("grocery_store.xlsx"))):
                l=list(pd.read_excel("grocery_store.xlsx").reset_index(drop=True).iloc[i])
                a[l[0]]=l
            get(a,b,x)
            dis(g,["name","quantity","price","total"]).to_excel("grocery_store_item_purchased.xlsx")
            dis(a,["name","remaining","price"]).to_excel("grocery_store_item_remain.xlsx")
            
        elif x==3:
            print("Thanks")
            break
    else:
        print("Wrong input")
    
def get(a,b,x):
    while(True):
        if x==2:
            dis(a, ["name","quantity","price"])
        s=input(d[x]).split()
        
        if x==1:
            a[s[0]]=s
        else:
            b[s[0]]=s
            if s[0] in a:
                g[s[0]]=[s[0],int(s[1]),a[s[0]][2],int(s[1])*int(a[s[0]][2])]
                a[s[0]]=[s[0],int(a[s[0]][1])-int(s[1]),int(a[s[0]][2])]
        
        if(input("Continue? y/n  :") not in ["y","Y"]):
            print("you can not",d[x][:28])
            del d[x]
            break 
ask()
