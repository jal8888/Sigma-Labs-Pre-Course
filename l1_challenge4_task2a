class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        
        word_grouped = {}
        for word in words:
            if word in word_grouped:
              word_grouped[word] += 1
            else:
              word_grouped[word] = 1

        sortmessage = []

        order1 = [(value, key) for key, value in word_grouped.items()]

        for x in range(k):

           sortmessage.insert(1,max(order1))
           leader = max(order1)
           order1.remove(leader)
           sorted_data = sorted(sortmessage, key=lambda x: (-x[0], x[1]))
        answer=[]
        for y in sorted_data:
            answer.append(y[1])

        return answer
