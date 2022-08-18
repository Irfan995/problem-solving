class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_str = "".join(el for el in s if el.isalnum())
        clean_str = clean_str.lower()
        if len(clean_str) == 0:
            return True
        for i in range(int(len(clean_str)/2)):
            if not clean_str[i] == clean_str[len(clean_str) - i - 1]:
                return False
        return True