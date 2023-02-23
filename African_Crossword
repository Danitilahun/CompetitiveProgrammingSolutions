row,col=list(map(int,input().split()))
grid=[]
for _ in range(row):
    element=list(input())
    grid.append(element)

for r in range(row):
    seen={}
    for c in range(col):
        if grid[r][c] in seen:
            ro,co=seen[grid[r][c]]
            grid[r][c]+="0"
            grid[ro][co]+="0"
        seen[grid[r][c]]=[r,c]
for c in range(col):
    seen={}
    for r in range(row):
        if grid[r][c][0] in seen:
            ro,co=seen[grid[r][c][0]]
            grid[r][c]+="0"
            grid[ro][co]+="0"
        seen[grid[r][c][0]]=[r,c]

answer=""
for r in range(row):
    for c in range(col):
        if grid[r][c][-1]!="0":
            answer+= grid[r][c] 
print(answer)
