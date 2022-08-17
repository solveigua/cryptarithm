from re import sub
import random

def solve(q):
  try:
    n = next(i for i in q if i.isalpha())
  except StopIteration:
    return q if eval(sub(r'(^|[^0-9])0+([1-9]+)', r'\1\2', q)) else False
  else: 
    for i in (str(i) for i in range(10) if str(i) not in q):
      r = solve(q.replace(n,str(i)))
      if r:
        return r
    return False

def map_to_dictionary(q, r):
    pos_vals = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}
    letters = {"V", "I", "S", "M", "A", "P", "H", "E", "N", "L"}
    dict = {}
    for symbol in range(0, 33): # both strings (r, q) have len 33.
        dict[r[symbol]] = q[symbol]
        letters.discard(q[symbol])
        pos_vals.discard(r[symbol])
    dict[pos_vals.pop()] = letters.pop() #only one letter left 
    return dict

if __name__ == "__main__":
    print("SOLVING PUZZLE: ")
    query = "HEAVEN == AI + API + SAAS + VISMA"
    print(query)
    r = solve(query)
    print(r) if r else "No solution found."
    print("31203 = ?")
    dict = map_to_dictionary(query, r)
    number = ("31203")
    sol =""
    for num in number:
        sol += dict.get(num)
    print(sol) if sol != "" else "No solution found."
