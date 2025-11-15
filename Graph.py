#pandas - reads excel files
import pandas as pd
#matplotlib creates graph (used in class)
import matplotlib.pyplot as plt

excel = pd.read_csv('Nat_Gas.csv')

def find_price(date):
    l = len(date)
    day = date[l-5:l-3]
    month = date[:l-6]
    year = date[l-2:]
    found = False
    for x in range(len(excel)):
        if excel["Dates"][x] == date:
            price = excel["Prices"][x]
            found = True
            msg = "On " + date + " the price was: " + str(price)
            return msg
            
    if found == False:
        for y in range(len(excel)-1):
            curr_date = excel["Dates"][y]
            w = len(curr_date)
            curr_day = int(curr_date[w-5:w-3])
            curr_month = int(curr_date[:w-6])
            curr_year = int(curr_date[w-2:])

            next_date = excel["Dates"][y+1]
            v = len(next_date)
            next_day = int(next_date[v-5:v-3])
            next_month = int(next_date[:v-6])
            next_year = int(next_date[v-2:])

            if int(month) in (4,6,9,11):
                depth = int(day)/30
            elif int(month) == 2:
                if int(year) % 4 == 0:
                    depth = int(day)/29
                else:
                    depth = int(day)/28
            else:
                depth = int(day)/31
            if (int(year) == curr_year or int(year) == next_year) and int(month) == next_month: #and curr_month <= int(month) < next_month:   
                price = excel["Prices"][y] - (depth*(excel["Prices"][y]-excel["Prices"][y+1]))
                msg = "On " + date + " the price was: " + str(price)
                return msg
                
def june2025():
    total = 0
    jun = {}
    for x in range(1,5):
        jun[x] = excel["Prices"][(12*x-4)]
    inc = {}
    for x in range(1,4):
        inc[x] = jun[x+1]/jun[x]
    for y in range(1,4):
        total += inc[y]
    total = total/3
    prediction = total*jun[4]
    return prediction
def sept2025():
    total = 0
    sep = {}
    for x in range(1,5):
        sep[x] = excel["Prices"][(12*x-1)]
    inc = {}
    for x in range(1,4):
        inc[x] = sep[x+1]/sep[x]
    for y in range(1,4):
        total += inc[y]
    total = total/3
    prediction = total*sep[4]
    return prediction
def jan2025():
    total = 0
    jan = {}
    for x in range(1,5):
        jan[x] = excel["Prices"][(12*x-9)]
    inc1 = {}
    for x in range(1,4):
        inc1[x] = jan[x+1]/jan[x]
    for y in range(1,4):
        total += inc1[y]
    total = total/3
    prediction = total*jan[4]
    return prediction
def feb2025():
    total = 0
    feb = {}
    for x in range(1,5):
        feb[x] = excel["Prices"][(12*x-8)]
    inc = {}
    for x in range(1,4):
        inc[x] = feb[x+1]/feb[x]
    for y in range(1,4):
        total += inc[y]
    total = total/3
    prediction = total*feb[4]
    return prediction    
def mar2025():
    total = 0
    mar = {}
    for x in range(1,5):
        mar[x] = excel["Prices"][(12*x-7)]
    inc = {}
    for x in range(1,4):
        inc[x] = mar[x+1]/mar[x]
    for y in range(1,4):
        total += inc[y]
    total = total/3
    prediction = total*mar[4]
    return prediction    
def apr2025():
    total = 0
    apr = {}
    for x in range(1,5):
        apr[x] = excel["Prices"][(12*x-6)]
    inc = {}
    for x in range(1,4):
        inc[x] = apr[x+1]/apr[x]
    for y in range(1,4):
        total += inc[y]
    total = total/3
    prediction = total*apr[4]
    return prediction
def may2025():
    total = 0
    may = {}
    for x in range(1,5):
        may[x] = excel["Prices"][(12*x-5)]
    inc = {}
    for x in range(1,4):
        inc[x] = may[x+1]/may[x]
    for y in range(1,4):
        total += inc[y]
    total = total/3
    prediction = total*may[4]
    return prediction
def jul2025():
    total = 0
    jul = {}
    for x in range(1,5):
        jul[x] = excel["Prices"][(12*x-3)]
    inc = {}
    for x in range(1,4):
        inc[x] = jul[x+1]/jul[x]
    for y in range(1,4):
        total += inc[y]
    total = total/3
    prediction = total*jul[4]
    return prediction
def aug2025():
    total = 0
    aug = {}
    for x in range(1,5):
        aug[x] = excel["Prices"][(12*x-2)]
    inc = {}
    for x in range(1,4):
        inc[x] = aug[x+1]/aug[x]
    for y in range(1,4):
        total += inc[y]
    total = total/3
    prediction = total*aug[4]
    return prediction
def oct2024():
    total = 0
    oct = {}
    for x in range(1,5):
        oct[x] = excel["Prices"][(12*x-12)]
    inc = {}
    for x in range(1,4):
        inc[x] = oct[x+1]/oct[x]
    for y in range(1,4):
        total += inc[y]
    total = total/3
    prediction = total*oct[4]
    return prediction
def nov2024():
    total = 0
    nov = {}
    for x in range(1,5):
        nov[x] = excel["Prices"][(12*x-11)]
    inc = {}
    for x in range(1,4):
        inc[x] = nov[x+1]/nov[x]
    for y in range(1,4):
        total += inc[y]
    total = total/3
    prediction = total*nov[4]
    return prediction
def dec2024():
    total = 0
    dec = {}
    for x in range(1,5):
        dec[x] = excel["Prices"][(12*x-10)]
    inc = {}
    for x in range(1,4):
        inc[x] = dec[x+1]/dec[x]
    for y in range(1,4):
        total += inc[y]
    total = total/3
    prediction = total*dec[4]
    return prediction

june = {"Dates":"6/30/25","Prices":float(june2025())}
september = {"Dates":"9/30/25","Prices":float(sept2025())}
janruary = {"Dates":"1/31/25","Prices":float(jan2025())}
february = {"Dates":"2/28/25","Prices":float(feb2025())}
march = {"Dates":"3/31/25","Prices":float(mar2025())}
april = {"Dates":"4/30/25","Prices":float(apr2025())}
may = {"Dates":"5/31/25","Prices":float(may2025())}
july = {"Dates":"7/31/25","Prices":float(jul2025())}
august = {"Dates":"8/30/25","Prices":float(aug2025())}
october = {"Dates":"10/31/25","Prices":float(oct2024())}
november = {"Dates":"11/30/25","Prices":float(nov2024())}
december = {"Dates":"12/31/25","Prices":float(dec2024())}

new_rows =  [october,november,december,janruary,february,march,april,may,june,july,august,september]
new_df = pd.DataFrame(new_rows)
excel = pd.concat([excel,new_df], ignore_index=True)

i = input("Enter date (in (m)m/dd/yy): ")
print(find_price(i))

plt.figure(figsize=(18,7))
plt.plot(excel["Dates"], excel["Prices"])
plt.xlabel("Dates")
plt.ylabel("Prices")
plt.margins(x=0)
plt.title("natural gas price over time")
plt.grid(True)
plt.xticks(rotation =70, ha ="right", rotation_mode = "anchor")
plt.show()