"""
For investments over $1M it can be typically assumed that they will return 5% forever.
Using the [2022 - 2023 JMU Cost of Attendance](https://www.jmu.edu/financialaid/learn/cost-of-attendance-undergrad.shtml),
calculate how much a rich alumnus would have to give to pay for one full year (all costs) for an in-state student
and an out-of-state student. Store your final answer in the variables: "in_state_gift" and "out_state_gift".

JMU 2022-2023 Annual:
In-state total cost: 30792 USD
Out-of-state total cost: 47882 USD

Note: this problem does not require the "compounding interest" formula from the previous problem.

"""

### Your code here ###
#Define the anual cost of attendance for both in-state and out-of-state students.
in_state_cost = 30792 
out_state_cost = 47882

#Calculate the size of the gift needed to cover both costs. (Works because gift * 0.05 must = annual cost, solve for gift)
in_state_gift = in_state_cost / 0.05
out_state_gift = out_state_cost / 0.05


#Print findings to terminal. 
print(f"in state gift needed is: ${in_state_gift}")
print(f"out of state gift needed is: ${out_state_gift}")