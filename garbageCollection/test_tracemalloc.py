import tracemalloc
tracemalloc.start()
# ... 애플리케이션 시작 ...

snapshot1 = tracemalloc.take_snapshot()
# ... 메모리 누수 함수 호출 ...
snapshot2 = tracemalloc.take_snapshot()

top_stats = snapshot2.compare_to(snapshot1, 'lineno')

print("[ Top 10 differences ]")
for stat in top_stats[:10]:
    print(stat)
