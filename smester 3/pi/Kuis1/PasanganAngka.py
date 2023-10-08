N = int(input())
results = []
for _ in range(N):
    A, B = map(int, input().split())
    if str(A) in str(B) and 2 * B > A ** 2:
        results.append("Ya")
    else:
        results.append("Tidak")

for result in results:
    print(result)
