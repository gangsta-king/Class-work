n=int(input())
print('Armstrong number' if sum(int(i)**3 for i in str(n))==n else 'Not an Armstrong number')