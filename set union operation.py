
_ = input() 
english_set = set(map(int, input().split()))

_ = input() 
french_set = set(map(int, input().split()))
at_least_one = english_set | french_set
print(len(at_least_one))
