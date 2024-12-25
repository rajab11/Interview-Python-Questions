"""
Given an array of strings arr[], the task is to return the longest common prefix among each and every strings present in the array. If there’s no prefix common in all the strings, return “”.

Examples:

Input: arr[] = [“geeksforgeeks”, “geeks”, “geek”, “geezer”]
Output: “gee”
Explanation: “gee” is the longest common prefix in all the given strings: “geeksforgeeks”, “geeks”, “geeks” and “geezer”.

Input: arr[] = [“apple”, “ape”, “april”]
Output : “ap”
Explanation: “ap” is the longest common prefix in all the given strings: “apple”, “ape” and “april”.

Input: arr[] = [“hello”, “world”]
Output: “”
Explanation: There’s no common prefix in the given strings.
"""
def longestCommonPrefix(arr):
    arr.sort()
    first=arr[0]
    last=arr[-1]

    minlength=min(len(first),len(last))

    i=0
    while i<minlength and first[i]==last[i]:
        i+=1
    return first[:i]
    

if __name__=="__main__":
    arr=["geeksforgeeks", "geeks", "geek", "geezer"]
    print(longestCommonPrefix(arr))
