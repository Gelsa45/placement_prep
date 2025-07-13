s=input("Enter the string")
char_string=[]
for char in s:
    if char.isalnum():
        char_string.append(char.lower())


left=0
right=len(char_string)-1
while left<right:
    if(char_string[left]!=char_string[right]):
          print("The given string is  not a palindrome")
          break
    left+=1
    right-=1
print("the given string is a plaindrome")  
    
    

    



