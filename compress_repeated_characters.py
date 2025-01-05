"""
You are developing a feature for a text messaging app that needs to compress consecutive repeated 
characters in messages while preserving the order of appearance. 
However, instead of just counting repetitions, you need to encode them using a special rule: 
if a character appears consecutively, replace the sequence with the character followed by its frequency 
in square brackets. If a character appears only once, leave it as is (don't add [1]). 
For example, 'aaaa' becomes 'a [4]', and 'ab' remains 'ab'. The compression should be case-sensitive and 
should work with any printable character including numbers and special characters. 

EXAMPLE 1 

Input: aabbbcccc 

Output: a [2] b[3]c[4] 

Explanation: Two 'a's become 'a[2]', three 'b's become 'b[3]', four 'c's become 'c[4]' 

EXAMPLE 2 
Input: abc123!!! 
Output: abc123! [3] 

Explanation: Single occurrences remain unchanged, three exclamation marks become '![3]' 

Requirements 

1.Implement a function that takes a string as input and returns the compressed string 
2.Preserve the order of characters in the input string 
3.Case sensitivity must be maintained 
4.Handle any printable character including numbers and special characters 
5.Don't add count for non-repeated characters 
6.Empty strings should return empty strings 
7.The compression format should be character followed by count in square brackets 
"""
def compress_repeated_characters(my_list):
    
    output=''
    count=1

    for i in range(1,len(my_list)):
        if my_list[i]==my_list[i-1]:
            count+=1
        else:
            if count==1:
                output+=f"{my_list[i-1]}"
            else:
                output+=f"{my_list[i-1]}{count}"
            count=1
    
    output+=f"{my_list[-1]}{count}"
    
    return output


input="aabbbcccc"
print(compress_repeated_characters(input))

input="abc123!!!"
print(compress_repeated_characters(input))
