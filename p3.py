n1,n2,n3=map(int,input().split())
print('Maximum =',max(n1,n2,n3))
print('Minimum =',min(n1,n2,n3))
print('Middle =',n1+n2+n3-max(n1,n2,n3)-min(n1,n2,n3))