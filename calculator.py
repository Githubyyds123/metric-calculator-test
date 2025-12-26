class MetricCalculator:
    def __init__(self):
        self.results = []
    
    def calculate_mean(self, data):
        if not data:
            return 0.0
        
        if not all(isinstance(x, (int, float)) for x in data):
            raise ValueError("Data list must contain numbers")
            
        return sum(data) / len(data)
    
    def calculate_accuracy(self, y_true, y_pred):
        if len(y_true) != len(y_pred):
            return 0.0

        if not y_true:
            return 0.0

        correct = sum(1 for t, p in zip(y_true, y_pred) if t == p)
        return correct / len(y_true)

    
    def add_metric(self, name, value):
        if not isinstance(name, str):
            raise ValueError("Metric name must be a string")
        if not isinstance(value, (int, float)):
            raise ValueError("Metric value must be a number")
            
        self.results.append((name, value))
    
    def get_results(self):
        return self.results
