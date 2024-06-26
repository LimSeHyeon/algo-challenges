import sys
sys.setrecursionlimit(10**6)

m,n,k=map(int,input().split())
graph=[[0]*n for _ in range(m)]

for _ in range(k):
    x1,y1,x2,y2=map(int,input().split())
    for i in range(x1,x2):
        for j in range(y1,y2):
            graph[j][i]=1

dx=[-1,1,0,0]
dy=[0,0,-1,1]

def dfs(x,y):
    graph[x][y]=1
    global cnt
    cnt+=1

    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]

        if 0<=nx<m and 0<=ny<n and graph[nx][ny]==0:
            dfs(nx,ny)

area=[]
for i in range(m):
    for j in range(n):
        if graph[i][j]==0:
            cnt=0
            dfs(i,j)
            area.append(cnt)

area.sort()
print(len(area))
for a in area:
    print(a, end=" ")