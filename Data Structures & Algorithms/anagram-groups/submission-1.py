# class Solution:
#     def isAnagram(self, a: str, b: str) -> bool:
#         return sorted(a) == sorted(b)

#     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
#         ans_list = list()
#         tracker = [0] * len(strs)
#         for i in range(len(strs)):
#             if tracker[i] == 1:
#                 continue
#             new_list = list()
#             new_list.append(strs[i])
#             tracker[i] = 1
#             for j in range(i+1, len(strs)):
#                 if self.isAnagram(strs[i], strs[j]):
#                     new_list.append(strs[j])
#                     tracker[j] = 1
#             ans_list.append(new_list)
#         return ans_list



from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}

        for word in strs:
            key = ''.join(sorted(word))

            if key not in groups:
                groups[key] = []

            groups[key].append(word)

        return list(groups.values())


