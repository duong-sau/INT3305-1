import math
def tinhgiaithua(n):
    giai_thua = 1;
    if (n == 0 or n == 1):
        return giai_thua;
    else:
        for i in range(2, n + 1):
            giai_thua = giai_thua * i;
        return giai_thua;
def tinhchinhhop(n,k):
    chinh_hop=1;
    chinh_hop=chinh_hop*tinhgiaithua(n)/tinhgiaithua(k)/tinhgiaithua(n-k)
    return chinh_hop
def prob(n, p, r):
    return tinhchinhhop((n-1), (r-1))*pow(p,r)*pow((1-p),(n-r))
def infoMeasure(n, p, r):
    return 0-math.log(prob(n, p,r), 2)

def sumProb(N, p,r):
    i = N
    sum = 0
    while i > 0:
        sum = sum+prob(i, p, r)
        i=i-1
    return sum
'''
khi N tiến tới vô cùng thì sumProb(N,p) là tổng sác xuất tất cả các biến cố của phân phối nhị thức âm
giá trị này phải tiến tới 1
'''
def approxEntropy(N, p,r):
    i=N
    entropy=0
    while i > 0:
        entropy=entropy+prob(i, p, r)*infoMeasure(i, p, r)
        i=i-1
    return entropy
'''
công thức tính entropy chính là công thức tính trung bình lượng tin 
khi N tiến tới vô cùng thì giá trị hàm approxEntropy xấp xỉ bằng Entropy
nguồn tin geometric thực nghiệm với giá trị p=0.5 là một người tung đồng xu lần được đúng 1 lần ngửa
Entropy của nguồn tin trên bằng approxEntropy(100,0.5)
'''
print(approxEntropy(100, 0.5,1))
