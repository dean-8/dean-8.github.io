import Graph
from Graph import find_price, plot_graph, excel

def selling(injection_date,withdrawal_date,amount,months,store_cost,cost_to_inj):
    #profit pre subtractions
    base_price = float(find_price(withdrawal_date)[0]) - float(find_price(injection_date)[0])
    base_price = base_price*amount
    #used in final message
    w = find_price(withdrawal_date)[0]
    w = w*amount
    i = find_price(injection_date)[0]
    i = i*amount

    cost_of_storage = months * (store_cost/1000)
    cost_of_injection = (cost_to_inj/1000) * amount * 2
    base_price = base_price - cost_of_storage - cost_of_injection

    msg = "Buying " + str(amount) + " million MMbtu on " + injection_date + " will cost " + str(i) + " million $ and if you sell on " + withdrawal_date + " you will make " + str(w) + " million $\nSo overall the profit is: " + str(base_price) + " million $\n"
    return base_price, msg

def months_apart(injection_date,withdrawal_date):
    len1 = len(injection_date)
    month1 = injection_date[:len1-6]
    year1 = injection_date[len1-2:]
    len2 = len(withdrawal_date)
    month2 = withdrawal_date[:len2-6]
    year2 = withdrawal_date[len2-2:]
    months = 0
    a = False
    for x in range(len(excel)-1):
        cur = excel["Dates"][x]
        l = len(cur)
        month = cur[:l-6]
        year = cur[l-2:]
        if year == year1:
            if month == month1:
                a = True
        if a == True:
            months += 1
        if year == year2:
            if month == month2:
                break
    return months


injection_date = input("\nEnter injection date in (m)m/dd/yy: ")
withdrawal_date = input("\nEnter withdrawal date in (m)m/dd/yy: ")
max = float(input("\nWhats the max amount you can store (in million MMbtu)? "))
amount = float(input("\nHow many MMbtu of natural gas would you like to buy? (in millions): "))
while max < amount:
    amount = float(input("\nHow many MMbtu of natural gas would you like to buy? (in millions): "))
# price of storage will only add at the start of each month (wont increment price each day)
store_cost = int(input("\nHow much does storage cost per month (in thousands): "))
cost_to_inj = int(input("\nHow much does it cost to inject or withdraw 1 million MMbtu of natural gas (in thousands)? "))

months = months_apart(injection_date,withdrawal_date)
print(selling(injection_date,withdrawal_date,amount,months,store_cost,cost_to_inj)[1])

plot_graph()
