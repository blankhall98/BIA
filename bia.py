import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

class Data_Analytic:

    def __init__(self,inputs):
        self.data_route = inputs['data_route']
        self.firm_name = inputs['firm_name']
        self.data = pd.read_csv(self.data_route)

    def add_record(self):
        print('\n'+"Please answer the following questions:"+'\n')
        name = input("Name: ")
        email = input("Email: ")
        gender = input("Gender (F/M): ")
        age = input("Age: ")
        expense = input("Expense: ")
        print('\n'+"Thank you!"+'\n')
        new = [name,email,gender,age,expense]

        n = len(self.data)
        self.data.loc[n] = new
        self.data.to_csv(self.data_route,index=False)

    def linear_analysis(self,var_1,var_2):
        #Fits a linear regression for 2 given variables (var_1,var_2)
        reg = LinearRegression()
        x_axis = np.array(self.data[var_1])
        y_axis = np.array(self.data[var_2])
        reg.fit(x_axis.reshape(-1,1),y_axis)
        return reg

    def graph_analytics(self):
        #Plot analytics ----------

        #Gender
        #Who shops more? Men or Women?
        plt.figure()
        plt.title('Male vs Female Customer Count')
        sns.countplot(data=self.data,x='Gender')
        plt.show()

        #Linear regression
        age_exp_lr = self.linear_analysis('Age','Expense')

        age_range = np.arange(0,100,1)

        sales_prediction = age_exp_lr.predict(age_range.reshape(-1,1))

        #Age-Expense scatter
        #Relationship between two variables
        plt.figure()
        plt.title('Age-Expense Comparison')
        sns.scatterplot(data=self.data,x='Age',y='Expense',hue='Gender')
        plt.plot(age_range,sales_prediction,'--',label='regression')
        plt.legend()
        plt.show()

        