exps = []

def load():
    try:
        f = open("exp.txt", "r")
        for l in f:
            r = l.strip().split(",")
            if len(r) == 3:
                exps.append({"name": r[0], "amt": float(r[1]), "category": r[2]})
    except:
        pass

def save():
    f=open("exp.txt", "w")
    for e in exps:
        f.write(f"{e['name']},{e['amt']},{e['category']}\n")

def add():
    n = input("Name: ")
    if not n: 
        return
    a = float(input("Amount: ")) 
    c = input("category: ")
    
    exps.append({"name": n, "amt": a, "category": c})
    save()
    print("Added your expense!")

def view():
    if not exps:
        print("Your Expenses Are Empty")
        return
    
    for i, e in enumerate(exps):
        print(f"{i+1}. {e['name']} - ₹{e['amt']} - {e['category']}")

def search():
    c = input("category: ")
    found = False
    for e in exps:
        if e["category"].lower() == c.lower():
            print(f"{e['name']} - ₹{e['amt']}")
            found = True
            
    if not found: 
        print("Given category not found.")

def total():
    t = 0
    for e in exps:
        t += e["amt"]
    print("Total: ₹", t)

def high():
    if not exps: 
        return
    h = exps[0]
    for e in exps:
        if e["amt"] > h["amt"]: 
            h = e
    print(f'Highest: {h['name']} (₹{h['amt']})')

def delete():
    view()
    if not exps: 
        return
    i = int(input('Num to delete: '))
    x = exps.pop(i - 1)
    save()
    print('Deleted', x['name'])

def cat_sum():
    sums = {}
    for e in exps:
        c = e['category']
        if c in sums:
            sums[c] += e["amt"]
        else:
            sums[c] = e["amt"]
            
    for c, t in sums.items():
        print(f"{c}: ₹{t}")

load()
c = 0
while c != 8:
    print('\n///// EXPENSE TRACKER /////')
    print("1.Add exp \n2.View exp \n3.Search category \n4.Total exp \n5.Highest exp \n6.Delete \n7.category Summary \n8.Exit")
    
    c = int(input("Choice: "))
    
    if c == 1: 
        add()
    elif c == 2:
        view()
    elif c == 3: 
        search()
    elif c == 4: 
        total()
    elif c == 5: 
        high()
    elif c == 6: 
        delete()
    elif c == 7: 
        cat_sum()
    elif c == 8: 
        print('Thank you for using expense tracker')
    else:
        print("invalid input")