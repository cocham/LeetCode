from collections import deque 

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        dq = deque()

        visited = {}
        for word in wordList:
            visited[word] = False
        
        dq.append((beginWord, 1))

        while (len(dq) != 0):
            start, ans = dq.popleft()

            if (start == endWord):
                return ans
            
            for word in wordList:
                if (visited[word]):
                    continue

                correct = 0

                for i in range(len(word)):
                    if (word[i] == start[i]):
                        correct += 1

                if (correct == len(start) - 1):
                    visited[word] = True
                    dq.append((word, ans + 1))
                    

        return 0

        