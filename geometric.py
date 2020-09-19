import math
def prob(n, p):
    return p*pow((1-p), (n-2))
def infoMeasure(n, p):
    return 0-math.log(prob(n, p), 2)

def sumProb(N, p):
    i = N
    sum = 0
    while i > 0:
        sum = sum+prob(i, p)
        i=i-1
    return sum
'''
khi N tiến tới vô cùng thì sumProb(N,p) là tổng sác xuất tất cả các biến cố của phân phối hình học
giá trị này phải tiến tới 1
'''
def approxEntropy(N, p):
    i=N
    entropy=0
    while i > 0:
     entropy=entropy+prob(i,p)*infoMeasure(i,p)
     i=i-1
    return entropy
'''
công thức tính entropy chính là công thức tính trung bình lượng tin 
khi N tiến tới vô cùng thì giá trị hàm approxEntropy xấp xỉ bằng Entropy
nguồn tin geometric thực nghiệm với giá trị p=0.5 là một người tung đồng xu đến khi được mặt ngửa thì dừng lại
Entropy của nguồn tin trên bằng approxEntropy(1000,0.5)=2.0
'''
print(approxEntropy(1000,0.5))