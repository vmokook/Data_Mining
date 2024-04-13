#import skfuzzy
import numpy as np
from math import pi
from scipy.special import erf
import matplotlib.pylab as plt

##______________________S-shaped transfer functions_______________________

# def s1(x):
    
#     s1=1 / (1 + np.exp(-2*x)) # Сигмоидная функция с удвоенным аргументом
    
#     return s1

def s1(x):
    # Ограничение значения x для предотвращения overflow
    s1 = np.clip(x, a_min=None, a_max=100)
    return 1 / (1 + np.exp(-2*s1))


def s2(x):
    s2 = 1 / (1 + np.exp(-x)) # Логистическая функция 
    return s2

def s3(x):
    s3=1 / (1 + np.exp(-x/3)) # Сигмоидная функция с аргументом, деленным на 3
    return s3


def s4(x):
    s4=1 / (1 + np.exp(-x/2)) # Сигмоидная функция с аргументом, деленным на 2

x = np.arange(-8, 8, 0.1) 
# x используется в этом скрипте и будет заменено на бинарный индивид (1-мерный бинарный вектор),
# когда функция передачи вызывается или импортируется в скриптах оптимизаторов

