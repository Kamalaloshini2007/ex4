import set_module
A=map(int,input("enter set A number:").split())
A=set(A)
B=map(int,input("enter set B number:").split())
B=set(B)
print("union:",set_module.sunion(A,B))
print("intersection:",set_module.sintersection(A,B))
print("difference:",set_module.sdifference(A,B))
print("symmetric:",set_module.ssymmetric(A,B))
