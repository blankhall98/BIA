import pandas as pd

class Data_Analytic:

    def __init__(self,inputs):
        self.data_route = inputs['data_route']
        self.data = pd.read_csv(self.data_route)
        