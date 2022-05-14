input_a = input("ひらがなで入力")
input_b = input("ひらがなで入力")
la = len(input_a)
lb = len(input_b)

# dp[i][j]=(inpt_aのi文字目、input_bのj文字目までみた時の最長共通部分列の長さ)
dp = [[0] * (lb+1) for i in range(la+1)]
dp[0][0] = 0

for i in range(1, la+1):
    for j in range(1, lb+1):
        if input_a[i-1] == input_b[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1]) 
        
#復元
i = la  
j = lb
 
ans = ''
while i > 0 and j > 0:
    if input_a[i-1] == input_b[j-1]:
        ans = input_a[i-1] + ans
        i -= 1
        j -= 1
    else:
        if dp[i-1][j] > dp[i][j-1]:
            i -= 1
        else:
            j -= 1

print(ans)
