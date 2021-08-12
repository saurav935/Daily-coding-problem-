
class Solution:

    def longestKSubstr(self, s, k):
        hashmap = {}
        i = j = 0
        res = 0

        while j < len(s):
            if s[j] in hashmap:
                hashmap[s[j]] += 1
            else:
                hashmap[s[j]] = 1

            if len(hashmap) < k:
                j += 1

            elif len(hashmap) == k:
                res = max(res ,( j - i +1))
                j += 1

            elif len(hashmap) > k:
                while len(hashmap) > k:
                    if s[i] in hashmap:
                        hashmap[s[i]] -= 1
                        if hashmap[s[i]] == 0:
                            del hashmap[s[i]]
                    i += 1
                j += 1

        return res if res != 0 else -1