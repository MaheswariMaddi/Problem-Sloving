#Runner up program or second largest no
n = int(input())
arr = list(map(int, input().split()))
winner=arr[0]
runner_up=arr[1]
if(winner<runner_up):
        t= winner
        winner=runner_up
        runner_up=t
for i in arr[2:]:
    if(winner<i):
        runner_up=winner
        winner=i
    elif(runner_up<i and winner>i):
            runner_up=i  
    elif(runner_up==winner and i<winner):#6,6,3,4,1,0,5,2
        runner_up=i
print(runner_up)