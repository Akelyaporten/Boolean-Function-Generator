import csv 
import random



boolean_Function = []
dont_care = [0, 1, 2, 3, 4]
term = ''


def boolean_Function_Generator():
    number_of_literals = random.randint(4, 6)
    number_of_minterm = random.randint(4, (2**number_of_literals)/2)
    number_of_dontCare = random.choices(dont_care, [0.6, 0.1, 0.1, 0.1, 0.1])[0]
    
    i = 1
    
    while i < number_of_minterm + 1:
        term = 'm' + str(random.randint(0, (2**number_of_literals) + 1))
        if term in boolean_Function:
            term = ''
        else:
            boolean_Function.append(term)
            term = ''
            i = i + 1
    
    i = 0
    while i < number_of_dontCare:
        term = 'd' + str(random.randint(0, 2**number_of_literals))
        if term in boolean_Function:
            term = ''
        else:
            boolean_Function.append(term)
            i = i + 1


for i in range(10000):
    boolean_Function.clear()
    boolean_Function_Generator()
    with open('boolean_Dataset.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        
        writer.writerow(boolean_Function)
    
        
    