from bia import Data_Analytic

inputs = {
    'data_route': './data/db.csv'
}

#MAIN FUNCTION
def main():
    #initialize class
    DA = Data_Analytic(inputs)
    #print previus database
    print(DA.data)
    #add new record
    DA.add_record()
    #print new database
    print(DA.data)
    #show report
    DA.graph_analytics()

if __name__ == '__main__':
    main()