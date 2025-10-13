import sys
input = sys.stdin.readline
# N=int(input())
# board = [ list(map(int,input().split())) for _ in range(N)]

# def solution(n, board):
#     # solve 함수는 석판의 좌상단 (r1, c1)과 우하단 (r2, c2) 좌표로
#     # 조각의 범위를 받습니다.
#     def solve(r1, c1, r2, c2):
#         # 1. 현재 조각 분석
#         jewels = []
#         impurities = []
#         for r in range(r1, r2+1):
#             for c in range(c1, c2+1):
#                 if board[r][c]==2:
#                     jewels.append((r,c))
#                 elif board[r][c] == 1:
#                     impurities.append((r,c))

#         #2. 재귀 종료조건
#         # 보석이 하나도 없으면 실패
#         if len(jewels) == 0:
#             return 0
        
#         # 보석이 하나 있고, 불순물이 없으면 성공
#         if len(jewels) == 1 and len(impurities)==0:
#             return 1
        
#         # 보석이 여러 개인데 자를 불순물이 없으면 실패
#         if len(jewels) > 1 and len(impurities) == 0:
#             return 0
        

#         # 3. 유효한 칼질 찾고 재귀 호출
#         total_ways = 0 

#         for imp_r, imp_c in impurities:

#             impurities_above = 0

#     # 가장 처음에는 전체 석판(0,0 부터 n-1,n-1 까지)을 넣고 시작합니다.
#     answer = solve(0, 0, n - 1, n - 1)
    
#     # 만약 유효한 방법이 하나도 없다면 -1을, 아니면 찾은 경우의 수를 반환
#     return answer if answer > 0 else -1





import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline
N,M,K = map(int,input().split())
board =[[0]*M for _ in range(N)]

for _ in range(K):
    a,b = map(int,input().split())
    board[a-1][b-1] = 1

dr = [-1,1,0,0]
dc = [0,0,-1,1]

answer=0
def dfs(r,c):
    size = 1
    for i in range(4):
        nr = dr[i]+r
        nc = dc[i]+c
        if 0<=nr<N and 0<=nc<M and board[nr][nc]==1:
            board[nr][nc]=0
            size+=dfs(nr,nc)
    return size
    
for i in range(N):
    for j in range(M):
        if board[i][j]==1:
            board[i][j]=0
            answer=max(answer,dfs(i,j))
print(answer)
