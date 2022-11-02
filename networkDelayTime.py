class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        visit = set()
        minHeap = []
        graph = defaultdict(list)
        ans = 0

        for u, v, w in times:
            graph[u].append([w, v])
        
        visit.add(k)
        for path in graph[k]:
            heapq.heappush(minHeap, path)
        
        while minHeap:
            delay, vertex = heapq.heappop(minHeap)
            if vertex in visit:
                continue
            visit.add(vertex)
            ans = delay
            for w, v in graph[vertex]:
                heapq.heappush(minHeap, [w + delay, v])
        
        return ans if len(visit) == n else -1