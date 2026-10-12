x,y=map(int,input().split())
x1,y1=map(int,input().split())
if x<=x1<=y or x<=y1<=y or x1<=x<=y1 or x1<=y<=y1:
    print('Overlap')
else:
    print('No Overlap')