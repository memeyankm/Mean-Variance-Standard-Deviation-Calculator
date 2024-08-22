import numpy as np

def calculate(list):
    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")
    
    array = np.reshape(np.array([list]),(3,3))
    
    mean1 = np.mean(array, axis=0)
    mean2 = np.mean(array, axis=1)
    mean_all = np.mean(array)
    
    variance1 = np.var(array, axis=0)
    variance2 = np.var(array, axis=1)
    varaince_all = np.var(array)
    
    std1 = np.std(array, axis=0)
    std2 = np.std(array, axis=1)
    std_all = np.std(array)
    
    max1 = np.any(np.max(array, axis=0))
    max2 = np.any(np.max(array, axis=1))
    max_all = np.any(np.max(array))
    
    min1 = np.any(np.min(array, axis=0))
    min2 = np.any(np.min(array, axis=1))
    min_all = np.any(np.min(array))
    
    sum1 = np.sum(array, axis=0)
    sum2 = np.sum(array, axis=1)
    sum_all = np.sum(array)

    calculations = {}
    calculations['mean'] = [mean1, mean2, mean_all]
    calculations['variance'] = [variance1, variance2, varaince_all]
    calculations['standard deviation'] = [std1, std2, std_all]
    calculations['max'] = [max1, max2, max_all]
    calculations['min'] = [min1, min2, min_all]
    calculations['sum'] = [sum1, sum2, sum_all]

    print(calculations['min'])
    return calculations
