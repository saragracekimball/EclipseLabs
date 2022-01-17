import cs50
# get amount of cash
cash_entered = cs50.get_int("How much cash are you putting in? ")
total_due = 37.63

# calculate total_change
total_change = cash_entered - total_due

num_dollars = int(total_change)
print(num_dollars)
