import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from bia import Data_Analytic

inputs = {
    'data_route': './data/db.csv'
}

#MAIN FUNCTION
def main():
    DA = Data_Analytic(inputs)
    print(DA.data)

if __name__ == '__main__':
    main()