
def solve(s, t):
   if len(s) != len(t):
      return False
 
   temp = s + s
 
   if temp.count(t)> 0:
      return True
   return False

s = "hello"
t = "llohe"
print(solve(s, t))