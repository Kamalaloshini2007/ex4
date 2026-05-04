def sunion(s1,s2):
    return s1|s2
def sintersection(s1,s2):
    return s1&s2
def sdifference(s1,s2):
    ch=input("(s1-s2/s2-s1):")
    if ch=='s1-s2':
        return s1-s2
    else:
        return s2-s1
def ssymmetric(s1,s2):
    return s1^s2
