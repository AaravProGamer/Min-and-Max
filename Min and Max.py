N, M = map(int, input().split())
mat = [list(map(int, input().split())) for _ in range(N)]
print(max([min(row) for row in mat]))
