import pandas as pd
import random
import numpy as np


iter = 10000
total_females = 0
total_males = 0
total_min_females = 0
total_min_males = 0
total_max_females = 0
total_max_males = 0
total_mean_females = 0
total_mean_males = 0

for i in range(iter):
    # GETTING DATA FROM THE .csv FILE #

    data = pd.read_csv('A21.csv')
    df = pd.DataFrame(data,columns=['Final Grade'])
    grade = df.to_numpy()
    n = int(grade.shape[0]) # get the number of students

    # ASSIGN RANDOM GENDER TO EACH GRADE #

    gender = np.zeros((n,1)) 
    for i in range(n): 
        k = random.randint(0,1)
        gender[i,0] = k
    exporting = np.concatenate((grade,gender), axis = 1)
    columns = ['Final Grade', 'Gender']
    df = pd.DataFrame(data=exporting,columns=columns)
    #print(df)

    # SEPARATES GRADES OF FEMALES AND OF MALES # 

    male_grades = []
    female_grades = []
    n_females = 0
    n_males = 0


    for i in range(n):
        if exporting[i,1] == 1:
            male_grades.append(exporting[i,0])
            n_males = n_males+1
        else:
            female_grades.append(exporting[i,0])
            n_females = n_females+1


    # MEAN GRADE FOR EACH GENDER #
    

    male_mean = sum(male_grades)/n_males
    female_mean = sum(female_grades)/n_females

    total_mean_males = total_mean_males + male_mean
    total_mean_females = total_mean_females + female_mean


    # COMPUTING MAX AND MIN FOR EACH GENDER #        

    min_female = 11 
    min_male = 11
    max_female = -1
    max_male = -1
    for i in range(n_females):
        if female_grades[i]<min_female:
            min_female = female_grades[i]
        elif female_grades[i]>max_female:
            max_female = female_grades[i]
    for i in range(n_males):
        if male_grades[i]<min_male:
            min_male = male_grades[i]
        elif male_grades[i]>max_male:
            max_male = male_grades[i]
    
    total_females = total_females + n_females
    total_males = total_males + n_males
    total_min_females = total_min_females + min_female
    total_min_males = total_min_males + min_male
    total_max_females = total_max_females + max_female
    total_max_males = total_max_males + max_male




avg_mean_male = total_mean_males/iter
avg_mean_female = total_mean_females/iter

avg_min_female = total_min_females/iter
avg_min_male = total_min_males/iter
avg_max_male = total_max_males/iter
avg_max_female = total_max_females/iter

print('The min female average',avg_min_female,'. While the max female average is',avg_max_female, 'And the total average is',avg_mean_female)
print('The min male average',avg_min_male,'. While the max male average is',avg_max_male,'And the total average is',avg_mean_male)
