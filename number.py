
def func (a = []):
    a = list(map(int, input().split()))
    N = max(a)
    S = ((1 + N)*N)/2
    S2 = sum(a)
    print (S-S2)




        

