import matplotlib.pyplot as plt

class AnalyticsDashboard:
    def __init__(self):
        self.data = []
    
    def add_data(self, key, value):
        self.data.append((key, value))
    
    def visualize_data(self):
        keys, values = zip(*self.data)
        plt.bar(keys, values)
        plt.show()
