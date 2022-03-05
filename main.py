from bia import Data_Analytic

inputs = {
    'firm_name': 'Python Zero 2 Hero!',
    'data_route': './data/db.csv'
}

### MAIN FUNCTION ###

def main():
    #1. initialize class...
    DA = Data_Analytic(inputs)

    #print previus database...
    #print(DA.data)

    #add new record...
    #DA.add_record()

    #show report...
    DA.graph_analytics()

if __name__ == '__main__':
    main()