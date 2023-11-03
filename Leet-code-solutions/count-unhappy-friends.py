class Solution:
    def unhappyFriends(self, n: int, preferences: List[List[int]], pairs: List[List[int]]) -> int:

        order = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n - 1):
                order[i][preferences[i][j]] = j
                
        pairings = [0] * n
        for x, y in pairs:
            pairings[x] = y
            pairings[y] = x
            
        unhappy = 0
        for x in range(n):
            y = pairings[x]
            index = order[x][y]
            for i in range(index):
                u = preferences[x][i]
                v = pairings[u]
                if order[u][x] < order[u][v]:
                    unhappy += 1
                    break
                    
        return unhappy

        