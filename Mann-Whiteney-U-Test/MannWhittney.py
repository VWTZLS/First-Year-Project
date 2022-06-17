import numpy as np
import math
import scipy
from scipy.stats import mannwhitneyu
from numpy import genfromtxt
import matplotlib.pyplot as plt
import scipy.stats as stats

"""2019-2020"""
Females2019 = genfromtxt('/content/2019 females.csv', delimiter=',')
Males2019 = genfromtxt('/content/2019 males.csv', delimiter=',')
medianmales19 = np.median(Males2019)
medianfemales19 = np.median(Females2019)
u_males2019 ,p_males2019 =scipy.stats.mannwhitneyu(Males2019, Females2019, False, 'greater')
u_females2019, p_females2019 =scipy.stats.mannwhitneyu(Females2019, Males2019, False, 'greater')
print('males: median-',medianmales19,', p value-', p_males2019,', U value-', u_males2019,'comparisons',(len(Females2019)*len(Males2019)))
print('females: median-',medianfemales19, ', p value-', p_females2019,', U value-', u_females2019,)
plt.hist(Males2019, bins = 20)
plt.hist(Females2019, bins = 20)

"""2020-2021"""

Females2020 = genfromtxt('/content/2020 females.csv', delimiter=',')
Males2020 = genfromtxt('/content/2020 males.csv', delimiter=',')
medianmales20 = np.median(Males2020)
medianfemales20 = np.median(Females2020)
u_males2020 ,p_males2020 =scipy.stats.mannwhitneyu(Males2020, Females2020, False, 'greater')
u_females2020, p_females2020 =scipy.stats.mannwhitneyu(Females2020, Males2020, False, 'greater')
print('males: median-',medianmales20,', p value-', p_males2020,', U value-', u_males2020,'comparisons',(len(Females2020)*len(Males2020)))
print('females: median-',medianfemales20, ', p value-', p_females2020,', U value-', u_females2020,)
plt.hist(Males2020, bins = 20)
plt.hist(Females2020, bins = 20)

"""2021-2022"""

Females2021 = genfromtxt('/content/2021 females.csv', delimiter=',')
Males2021 = genfromtxt('/content/2021 males.csv', delimiter=',')
medianmales21 = np.median(Males2021)
medianfemales21 = np.median(Females2021)
u_males2021 ,p_males2021 =scipy.stats.mannwhitneyu(Males2021, Females2021, False, 'greater')
u_females2021, p_females2021 =scipy.stats.mannwhitneyu(Females2021, Males2021, False, 'greater')
print('males: median-',medianmales21,', p value-', p_males2021,', U value-', u_males2021,'comparisons',(len(Females2021)*len(Males2021)))
print('females: median-',medianfemales21, ', p value-', p_females2021,', U value-', u_females2021,)
plt.hist(Males2021, bins = 20)
plt.legend(["Males", "Females"])
plt.hist(Females2021, bins = 20)
plt.legend(["Males", "Females"])
plt.xlabel('Number of students')
plt.ylabel('Grade')
plt.title('Statistics class 2021/2022')
