
def findTheClosure(attr, list):  # { A->B, A->C,A->D, B->E,B->F, AG->F }

    closure = [attr]
    closureChanged = True
    while closureChanged:
        for x in list:
            f = x.split("->")
            if f[0] == attr or f[0] in closure:
                newAttr = f[1]
                closure.append(newAttr)
                closureChanged = True
            else:
                closureChanged = False

    print("The closure of {0} is: {1}".format(attr, closure))
    return 1


list = ["A->B", "A->C", "A->D", "B->E", "B->F", "AG->F"]
attr = "A"
findTheClosure(attr, list)
list2 = ["A->B", "A->C", "A->D", "B->E", "B->F"]
attr = "A"
findTheClosure(attr, list2)
