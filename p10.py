x,y,x1,y2=map(int,input().split())
if (x==x1 and y!=y2) or (y==y2 and x!=x1):
    print('YES')
else:
    print('NO')