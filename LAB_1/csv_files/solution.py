class solution:
    def __init__(self):
        self.best = 0 # Лучшее значение (результат функции оптимизации) 
        self.bestIndividual=[] # Лучшее решение в популяции, то есть лучшая частица в колонии
        self.convergence1 = [] 
        # self.convergence2 = []
        self.objfname="" # Название исследуемой функции
        self.startTime=0 # Начало отсчета времени
        self.endTime=0
        self.executionTime=0 
        self.lb=0 # нижний порог
        self.ub=0 # верхний порог
        self.dim=0 # размерность 
        self.popnum=0 # численность популяции 
        self.maxiers=0 # максимальное кол-во итераций 
        self.objective_value = 0



        