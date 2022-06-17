from cProfile import label
import pandas as pd
import random
from scipy.stats import norm
import numpy as np
import matplotlib.pyplot as plt


iter = 10000
monte_carlo_difference = []  # the list in which we will store all the results of the simulation

# GETTING Grades and gender FROM THE .csv FILE #

data = pd.read_csv('A21.csv')
df = pd.DataFrame(data,columns=['FINAL GRADE','Gender'])
mixed_grade_gender = df.to_numpy()
n = int(mixed_grade_gender.shape[0]) # get the number of students

# FUNCTION for seprates grades of females and males # 

def separating(mixed):
    
    g_m = [] # list of male grades
    g_f = [] # list of female grades
    n_f = 0 # number of female students
    n_m = 0 #number of male students

    for i in range(n):
        if mixed[i,1] == 1:
            g_m.append(mixed[i,0])
            n_m = n_m+1
        else:
            g_f.append(mixed[i,0])
            n_f = n_f+1

    return g_m,g_f,n_m,n_f

grades_male,grades_female,n_males,n_females = separating(mixed_grade_gender)

real_difference = (sum(grades_female)/n_females)-(sum(grades_male)/n_males)


# MONTE CARLO SIMULATION #

for i in range(iter):
    only_grades = mixed_grade_gender[:,0]
    only_grades = np.reshape(only_grades,(n,1))

    # ASSIGN RANDOM GENDER TO EACH GRADE #

    gender = np.zeros((n,1)) 
    for i in range(n): 
        k = random.randint(0,1)
        gender[i,0] = k
    exporting = np.concatenate((only_grades,gender), axis = 1)

    # compute the difference of the gender's means # 

    g_m,g_f,n_m,n_f = separating(exporting)

    gender_difference = (sum(g_m)/n_m)-(sum(g_f)/n_f)

    monte_carlo_difference.append(gender_difference)


total_average = sum(monte_carlo_difference)/iter


z_score = (real_difference-total_average)/np.std(monte_carlo_difference) 
print(z_score)

# CREATE AND PLOT HISTOGRAM #


plt.hist(monte_carlo_difference,bins = 'auto', range=[-2,2])
plt.axvline(real_difference, color='red', linestyle='dotted', linewidth=3, label='real difference')
plt.axvline(total_average, color='black', linestyle='dotted', linewidth=3, label='avg difference simulation')
plt.xlabel('Difference in grades')
plt.ylabel('Frequency')
plt.title('Difference average grade males-females 2021/2022')
plt.legend()
plt.show()