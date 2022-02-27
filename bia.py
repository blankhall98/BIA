import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

class Data_Analytic:

    def __init__(self,inputs):
        self.data_route = inputs['data_route']
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

    def graph_analytics(self):

        #Gender
        plt.figure()
        plt.title('Male vs Female Customer Count')
        sns.countplot(data=self.data,x='Gender')
        plt.show()

        #Age-Expense scatter
        plt.figure()
        plt.title('Age-Expense Comparison')
        sns.scatterplot(data=self.data,x='Age',y='Expense',hue='Gender')
        plt.show()