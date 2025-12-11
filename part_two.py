import part_one

import numpy as np
def load_data(filename):
    '''
    Load the data into two arrays
    Args:
        filename: string representing the name of the file
            containing the data (x,y)
    Return:
        array containing the values of x
        array containing the values of y
    '''
    data = np.loadtxt(filename)
    return data[:, 0], data[:, 1]
    

def main():    
    x,y = load_data("data_chol_dias_pressure.txt")

if __name__ == "__main__":
    main()