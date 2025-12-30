import pandas as pd

a = pd.read_csv('Task_3_and_4_Loan_Data.csv')
#lines 5-10, create the table with all %'s from debt and income
debt_percent_of_total_income = []
for x in range(len(a)):
    #add loan + debt to get total debt, then divide by income to see how debt compares to income
    value = ((a["loan_amt_outstanding"][x] + a["total_debt_outstanding"][x])/a["income"][x])*100
    value = int(value)
    debt_percent_of_total_income.append(float(value))
#print(debt_percent_of_total_income)
#splits the array above into ppl who defaulted and into ppl who didnt
default = []
didnt_default = []
for x in range(len(a)):
    if a["default"][x] == 1:
        default.append(debt_percent_of_total_income[x])
    else:
        didnt_default.append(debt_percent_of_total_income[x])
        didnt_default = sorted(didnt_default)
    
highest_nondefault = didnt_default[-1]
default_ascending = sorted(default)

#print(highest_nondefault) #31
#print(len(default)) # 1851 people defaulted total
#print(default_ascending)

def loan_percent(loan_amt_outstanding, total_debt_outstanding, income):
    a = int(((loan_amt_outstanding + total_debt_outstanding)/income)*100)
    return a

#put in a percent and returns ppl who did and didnt default who have that %
def prob(data):
    store = data
    de = 0
    for x in default: #default contains the % of ppl who defaulted
        if x == data:
            de+=1
    safe=0
    for x in didnt_default:
        if x == data:
            safe+=1
    return store, safe, de, "at " + str(store) + "%, " + str(de) + " people defaulted and " + str(safe) +" people didnt"

dict = {}
for x in range(1,50):
    #prob(x)[3]
    dict[x] = [prob(x)[1],prob(x)[2]] 
    #creates a dict w each key being a % and each key linking to an array of length 2 which has default and didnt default inside

#print(dict)

#checks what % of ppl default at 30%
def chance_default_each_percent_ofincome():
    bad = 0
    good = 0
    for x in dict: #30% is a good baseline of checking
        if x < 30:
            continue
        #print(x,dict[x])
        good += dict[x][0]
        bad += dict[x][1]
    chance_of_default_30 = float(bad/(good+bad))
    #print(chance_of_default_30)

    bad = 0
    good = 0
    for x in dict: 
        if x < 25 or x > 29:
            continue
        #print(x,dict[x])
        good += dict[x][0]
        bad += dict[x][1]
    chance_of_default_25 = float(bad/(good+bad))
    #print(chance_of_default_25)



    bad = 0
    good = 0
    for x in dict: 
        if x < 19 or x > 25:
            continue
        #print(x,dict[x])
        good += dict[x][0]
        bad += dict[x][1]
    chance_of_default_20 = float(bad/(good+bad))
    #print(chance_of_default_20)

    bad = 0
    good = 0
    for x in dict: 
        if x > 19:
            continue
        #print(x,dict[x])
        good += dict[x][0]
        bad += dict[x][1]
    chance_of_default_sub_20 = float(bad/(good+bad))
    #print(chance_of_default_sub_20)

    return chance_of_default_30, chance_of_default_25, chance_of_default_20, chance_of_default_sub_20


#looking at fico scores
ficobad =[]
ficogood = []
for x in range(len(a)):
    if a["fico_score"][x] < 600 and a["fico_score"][x] > 499: #600 is a good baseline to see whether its a good fico score
        if a["default"][x] == 1:
            ficobad.append(int(a["fico_score"][x]))
        else:
            ficogood.append(int(a["fico_score"][x]))
#find the probability of defaulting if you have a fico score of under 600
fico_default_prob_600 = len(ficobad)/(len(ficobad) + len(ficogood))

ficobad =[]
ficogood = []
for x in range(len(a)):
    if a["fico_score"][x] < 500: 
        if a["default"][x] == 1:
            ficobad.append(int(a["fico_score"][x]))
        else:
            ficogood.append(int(a["fico_score"][x]))
#find the probability of defaulting if you have a fico score of under 500
fico_default_prob_500 = len(ficobad)/(len(ficobad) + len(ficogood))

ficobad =[]
ficogood = []
for x in range(len(a)):
    if a["fico_score"][x] > 599: 
        if a["default"][x] == 1:
            ficobad.append(int(a["fico_score"][x]))
        else:
            ficogood.append(int(a["fico_score"][x]))
#find the probability of defaulting if you have a fico score of over 600
fico_default_prob_over600 = len(ficobad)/(len(ficobad) + len(ficogood))
def prob_of_default(loan_amt_outstanding,total_debt_outstanding,income,fico_score):
    debt_percent_income = loan_percent(loan_amt_outstanding,total_debt_outstanding,income)
    if debt_percent_income < 20:
        probability = chance_default_each_percent_ofincome()[3]
    elif debt_percent_income >= 20 and debt_percent_income < 25:
        probability = chance_default_each_percent_ofincome()[2]
    elif debt_percent_income >= 25 and debt_percent_income < 30:
        probability = chance_default_each_percent_ofincome()[1]
    else:
        probability = chance_default_each_percent_ofincome()[0]
    if fico_score < 600 and fico_score > 499:
        probability = probability + fico_default_prob_600 - (probability*fico_default_prob_600)
    elif fico_score < 500:
        probability = probability + fico_default_prob_500 - (probability*fico_default_prob_500)
    else:
        probability = probability * (1-fico_default_prob_over600) - (probability*(1-fico_default_prob_over600))
    
    return probability*100

loan_amt_outstanding = float(input("enter outstanding loan: "))
total_debt_outstanding = float(input("\nenter outstanding debt: "))
income = float(input("\nenter income: "))
fico_score = int(input("\nenter fico score: "))

a = prob_of_default(loan_amt_outstanding,total_debt_outstanding,income,fico_score)

def recovery(probability,loan_amt_outstanding):
    if probability>0:
        return "\nWith a recovery rate of 10%, the expected less of this loan, if its defaulted, is: " + str(loan_amt_outstanding*0.9) 

print("The probability of this person defaulting is " + str(a) + "%")
print(recovery(a,loan_amt_outstanding))
