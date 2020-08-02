from Calculator import Calculator
from Mean import mean
from Median import median
from Variance import variance
from Standard_Deviation import standard_deviation



class Statistics(Calculator):

    data = []

    def __init__(self):
        super().__init__()

    def get_mean(self, data):
        self.result = mean(data)
        return self.result

    def get_median(self, data):
        self.result = median(data)
        return self.result

    def get_standard_deviation(self, data):
        self.result = standard_deviation(data)
        return self.result

    def get_variance(self, data):
        self.result = variance(data)
        return self.result


