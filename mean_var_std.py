import numpy as np

def calculate(list):
    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")
    
    array = np.reshape(np.array([list]),(3,3))
    
    mean1 = np.mean(array, axis=0).tolist()
    mean2 = np.mean(array, axis=1).tolist()
    mean_all = np.mean(array).tolist()
    
    variance1 = np.var(array, axis=0).tolist()
    variance2 = np.var(array, axis=1).tolist()
    varaince_all = np.var(array).tolist()
    
    std1 = np.std(array, axis=0).tolist()
    std2 = np.std(array, axis=1).tolist()
    std_all = np.std(array).tolist()
    
    max1 = np.max(array, axis=0).tolist()
    max2 = np.max(array, axis=1).tolist()
    max_all = np.max(array).tolist()
    
    min1 = np.min(array, axis=0).tolist()
    min2 = np.min(array, axis=1).tolist()
    min_all = np.min(array).tolist()
    
    sum1 = np.sum(array, axis=0).tolist()
    sum2 = np.sum(array, axis=1).tolist()
    sum_all = np.sum(array).tolist()

    calculations = dict()
    calculations['mean'] = [mean1, mean2, mean_all]
    calculations['variance'] = [variance1, variance2, varaince_all]
    calculations['standard deviation'] = [std1, std2, std_all]
    calculations['max'] = [max1, max2, max_all]
    calculations['min'] = [min1, min2, min_all]
    calculations['sum'] = [sum1, sum2, sum_all]

    return calculations
