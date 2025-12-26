class MetricCalculator:
    def __init__(self):
        self.results = []
    
    def calculate_mean(self, data):
        """
        修复：
        1. 处理空列表，防止除以零错误
        2. 检查数据类型，确保都是数字
        """
        if not data:
            return 0.0
        
        if not all(isinstance(x, (int, float)) for x in data):
            raise ValueError("Data list must contain numbers")
            
        return sum(data) / len(data)
    
    def calculate_accuracy(self, y_true, y_pred):
        """
        修复：
        1. 检查两个列表长度是否一致
        2. 处理空列表
        """
        if len(y_true) != len(y_pred):
            return 0.0

        if not y_true:
            return 0.0

        correct = sum(1 for t, p in zip(y_true, y_pred) if t == p)

        return correct / len(y_true)

    
    def add_metric(self, name, value):
        """
        修复：
        1. 验证 name 必须是字符串
        2. 验证 value 必须是数字
        """
        if not isinstance(name, str):
            raise ValueError("Metric name must be a string")
        if not isinstance(value, (int, float)):
            raise ValueError("Metric value must be a number")
            
        self.results.append((name, value))
    
    def get_results(self):
        return self.results
