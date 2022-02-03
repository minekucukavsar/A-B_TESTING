import itertools
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.stats.api as sms
from scipy.stats import ttest_1samp, shapiro, levene, ttest_ind, mannwhitneyu, pearsonr, spearmanr, kendalltau, f_oneway, kruskal
from statsmodels.stats.proportion import proportions_ztest

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', 10)
pd.set_option('display.float_format', lambda x: '%.5f' % x)

df_control = pd.read_excel(r"C:\Users\hp\PycharmProjects\pythonProject2\ab_testing (1).xlsx",sheet_name="Control Group")
df_test = pd.read_excel(r"C:\Users\hp\PycharmProjects\pythonProject2\ab_testing (1).xlsx",sheet_name="Test Group")

df_control.head()
df_test.head()

df_control["Purchase"].mean()
df_test["Purchase"].mean()

#What was the average earnings by purchase?
df_control.groupby("Purchase").agg({"Earning": "mean"}).sort_values(by="Earning",ascending=False)
df_test.groupby("Purchase").agg({"Earning": "mean"}).sort_values(by="Earning",ascending=False)

#What was the average earnings by number of clicks?
df_control.groupby("Click").agg({"Earning": "mean"}).sort_values(by="Earning",ascending=False)
df_test.groupby("Click").agg({"Earning": "mean"}).sort_values(by="Earning",ascending=False)

#H0:There is no significant difference between the current system that we use and the return of the new system to the company.
#H1:There is a significant difference between the current system that we use and the return of the new system to the company.
# H0 : M1=M2
# H1 : M1!=M2

########################
# Assumption of Normality:
########################
# H0:Assumption of normal distribution provided.
# H1:Assumption of normal distribution not provided.

test_stat, pvalue = shapiro(df_control["Purchase"])
print('Test Stat = %.4f, p-value = %.4f' % (test_stat, pvalue))

test_stat, pvalue = shapiro(df_test["Purchase"])
print('Test Stat = %.4f, p-value = %.4f' % (test_stat, pvalue))

########################
#Variance homogeneity assumption:
########################
# H0:Variances are Homogeneous
# H1:Variances are not Homogeneous

test_stat, pvalue = levene(df_control["Purchase"],df_test["Purchase"])
print('Test Stat = %.4f, p-value = %.4f' % (test_stat, pvalue))

#If the assumption of normality is OK and the variances are homogeneous, we use an independent two-sample t-test (parametric test).

test_stat, pvalue = ttest_ind(df_control["Purchase"],df_test["Purchase"],equal_var=True)
print('Test Stat = %.4f, p-value = %.4f' % (test_stat, pvalue))


