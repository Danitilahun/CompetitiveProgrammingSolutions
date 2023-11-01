class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        
        a_values = [ord(ch) - ord('a') + 1 for ch in a]
        b_values = [ord(ch) - ord('a') + 1 for ch in b]
        
        len_a, len_b = len(a), len(b)
        
        hash_b = 0
        for i in range(len_b):
            hash_b = 26 * hash_b + b_values[i]
            
        a_power_len_b = 26 ** len_b
        
        hash_a = 0
        
        for i in range((len_b // len_a + 2) * len_a):
            hash_a = 26 * hash_a + a_values[i % len_a]
            if i >= len_b:
                hash_a -= a_values[(i - len_b) % len_a] * a_power_len_b
            if hash_a == hash_b:
                return ceil((i + 1) / len_a)
        
        return -1
