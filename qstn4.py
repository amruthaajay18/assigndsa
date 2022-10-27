def FirstNonRepeat(s):
 
    for i in s:
 
        if (s.find(i, (s.find(i)+1))) == -1:
 
            print("First non-repeating character is", i)
 
            break
 
    return
 
 
 
s = 'aaabcccddd'
 
FirstNonRepeat(s)