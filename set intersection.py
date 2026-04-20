# English newspaper subscribers
_ = input() 
english_set = set(map(int, input().split()))

# French newspaper subscribers
_ = input() 
french_set = set(map(int, input().split()))

# Find students in both sets using the intersection operator
both_subscriptions = english_set & french_set

# Output the total count
print(len(both_subscriptions))
