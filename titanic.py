import csv
with open(r'C:\Users\agogo\Downloads\archive (3)\Titanic-Dataset.csv'\
, mode='r',encoding='utf-8') as file:
    csv_reader = csv.reader(file)
    header = next(csv_reader)
    rows = []
    for row in csv_reader:
        rows.append(row)

#survival rate
def survival_rate(rows):
    total = 0
    survivors = 0
    for r in rows:
        total += 1
        if r[1] == '1' and total > 0:
            survivors +=1
    survival_rate = (survivors/total)*100
    print(f'Overall survival rate: {survival_rate:.1f}%')


def survival_rate_by_gender(rows):
    total_female = 0
    total_male = 0
    survivors_female = 0
    survivors_male = 0
    for r in rows:
        if r[4] == 'female':
            total_female += 1
        else:
            total_male += 1
        if r[1] == '1' and r[4] == 'female':
            survivors_female +=1
        elif r[1] == '1' and r[4] == 'male':
            survivors_male +=1
    Women = (survivors_female/total_female)*100
    Men = (survivors_male/total_male)*100
    print(f'Women: {Women:.1f}% | Men: {Men:.1f}%')


def survival_rate_by_class(rows):
    total_passengers_class1 = 0
    total_passengers_class2 = 0
    total_passengers_class3 = 0
    survivors_class1 = 0
    survivors_class2 = 0
    survivors_class3 = 0
    for r in rows:
        if r[2] == '1':
            total_passengers_class1 += 1
            if r[1] == '1':
                survivors_class1 +=1
        elif r[2] == '2':
            total_passengers_class2 += 1
            if r[1] == '1':
                survivors_class2 +=1
        elif r[2] == '3':
            total_passengers_class3 += 1
            if r[1] == '1':
                survivors_class3 +=1
        
    first_class = (survivors_class1/total_passengers_class1)*100
    second_class = (survivors_class2/total_passengers_class2)*100
    third_class = (survivors_class3/total_passengers_class3)*100
    print(f'1st class: {first_class:.1f}% | 2nd class: {second_class:.1f}% | 3rd class: {third_class:.1f}%' )

def survival_rate_by_age(rows):
    total_children = 0
    total_adults = 0
    total_elders = 0
    survivors_children = 0
    survivors_adults = 0
    survivors_elders = 0
    for r in rows:
        if r[5] == '':
            continue
        else:
            age = float(r[5])
            if age < 18:
                total_children +=1
                if r[1] == '1':
                    survivors_children +=1
            elif age >= 18 and age < 60:
                total_adults +=1
                if r[1] == '1':
                    survivors_adults +=1
            elif age >= 60:
                total_elders +=1
                if r[1] == '1':
                    survivors_elders +=1
    children = (survivors_children/total_children)*100
    adults = (survivors_adults/total_adults)*100
    elders = (survivors_elders/total_elders)*100
    print(f'Children: {children:.1f}% | Adults: {adults:.1f}% | Elders: {elders:.1f}%' )
    

print("=== TITANNIC SUVIVAL ANALYSIS ===")
survival_rate(rows),
survival_rate_by_gender(rows),
survival_rate_by_class(rows)
survival_rate_by_age(rows)

