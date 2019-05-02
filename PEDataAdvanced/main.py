import xlrd
import pandas as pd
import random
import matplotlib.pyplot as plt;

from PEDataAdvanced.classes.categorizer import Categorizer
from PEDataAdvanced.classes.date_generator import DateGenerator

plt.rcdefaults()
import numpy as np
import statistics


#(zien voor panda's, kan nuttiger zijn, door meer functies zoals bij grafieken en afdruk)
#moeilijkheden met file.at[i, 6] ??????
#ofwel zowel panda ans xlrd gebruiken ofwel vragen aan iemand


file = pd.read_excel("kopieOmTeTesten.xlsx")

print(file)

file = "voetbal.xlsx"
workbook = xlrd.open_workbook(file)

sheet = workbook.sheet_by_index(0)


for kolom in range(sheet.ncols):
    print(sheet.cell_value(0, kolom), end="\t\t")

# --- Opgave 2: Genereren van datums ---

print("\n")

categorie = DateGenerator.generate_date_between("1/1/2011", "1/1/2012")

print(categorie) #weergave datum

# --- Opgave 3: Categorizeren van maanden ---

month = categorie

month_digits = month[3:5]
print(month_digits) #weergave maand voor later in categorie & inzet toe te voegen

month_category = Categorizer.get_month_category(month_digits);

print(month_category) #categorie
engagement = Categorizer.get_engagement_for_category(month_category);


print(engagement) #inzet

#genereren in excel bestand, maar is dat permanent, wat als ik meerdere keren run, overschrijft dat dan
# hoe doen, gewoon array posities toekennen aan plaats in excel bestand met loop van 100


# --- Opgave 4: Grafiek genereren ---

def get_column_from_sheet(column_number):
    column = [];
    i = 0
    for cell in range(100):
        i = i + 1
        column.append(sheet.cell_value(i, column_number))
    return column


weight_column_number = 5
length_column_number = 6

weights = get_column_from_sheet(weight_column_number);
lengths = get_column_from_sheet(length_column_number);

plt.scatter(weights, lengths)
plt.show()

# --- Opgave 5: Staafdiagram ---

position_column_number = 1
goal_column_number = 2

positions = get_column_from_sheet(position_column_number)
goals = get_column_from_sheet(goal_column_number)


goalsByPosition = {
    "keeper": 0,
    "staart": 0,
    "linkervleugel": 0,
    "rechtervleugel": 0,
    "piloot": 0,
}
keepersdoelpunten = 0
staartdoelpunten = 0
linkervleugeldoelpunten = 0
rechtervleugeldoelpunten = 0
pilootdoelpunten = 0
i=0

for goaltjes in range(100):
    position = positions[i]
    goalsByPosition[position] = goalsByPosition[position] + 1
    if positions[i] == "keeper":
        keepersdoelpunten = keepersdoelpunten + goals[i]
    elif positions[i] == "staart":
        staartdoelpunten = staartdoelpunten + goals[i]
    elif positions[i] == "linkervleugel":
        linkervleugeldoelpunten = linkervleugeldoelpunten + goals[i]
    elif positions[i] == "rechtervleugel":
        rechtervleugeldoelpunten = rechtervleugeldoelpunten + goals[i]
    else:
        pilootdoelpunten = pilootdoelpunten + goals[i]

print("rechter doelpunten" + str(rechtervleugeldoelpunten))

posities = ('keeper','staart','rechtervleugel','linkervleutgel','piloot')
onderkant = np.arange(len(posities))
grafiekhoogte = [keepersdoelpunten, staartdoelpunten, linkervleugeldoelpunten, rechtervleugeldoelpunten, pilootdoelpunten]

plt.bar(onderkant, grafiekhoogte, align='center', alpha=0.5)
plt.xticks(onderkant, posities)
plt.ylabel('gescoorde doelpunten')
plt.show()


#nog opdelen in geboortecategorie puntje 5 ??????

#-----------------------------------------------------------------------------------

geheel = 0
i = 0

for goalen in range(100):
    geheel = geheel + goals[i]
    i = i + 1

gemiddelde = geheel / 100


print(gemiddelde)
print(max(goals))


#---------------------------------------------------------------------------------

eersteKwartiel = np.percentile(weights, 25)  #kwartiel 1 berekenen

print(eersteKwartiel)

standaardafwijking = statistics.stdev(weights) #standaardafwijking
print(standaardafwijking)

#--------------------------------------------------------------------------------

print("ja, hoe dieper op het veld, hoe meer goalen dat je maakt, kijk naar de staafdiagram, daaraan zie je dat keepers, geen goalen scoren, terwijl piloten veel doelpunten scoren")
#indien nodig vergelijken met met de 2 arrays (resultaat piloten scoren meer dan staart en deze op hun beurt dan keepers)

#----------------------------------------------------------------------------------
#inzet met cirkeldiagram


#--------------------------------------------------------------------------------

lvgoal = []
rvgoal = []
pilootgoal = []
i = 0

for doelpunt in range(100):
    if positions[i] == "linkervleugel":
        lvgoal.append(goals[i])
        i = i + 1
    elif positions[i] == "rechtervleugel":
        rvgoal.append(goals[i])
        i = i + 1
    elif positions[i] == "piloot":
        pilootgoal.append(goals[i])
        i = i + 1
    else: i = i + 1


plt.boxplot(lvgoal)
plt.show()
plt.boxplot(rvgoal)
plt.show()
plt.boxplot(pilootgoal)
plt.show()

#2 dingen (in een grote boxplot zetten & lv & rv hetzelfde?)




#--------------------------------------------------------------------------------
#soorten gegeven vraag 11

print("kwantitatief, discreet")       #aantal gemaakte goalen
print("kwalitatief, ordinaal")       #inzet
print("kwantitatief, continue")       #gewicht







#files Used: https://www.youtube.com/watch?v=p0DNcTnreuY
