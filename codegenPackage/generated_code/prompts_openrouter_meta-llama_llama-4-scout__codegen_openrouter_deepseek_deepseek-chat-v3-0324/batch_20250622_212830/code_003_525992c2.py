"""
Generated Code Metadata:
========================
Original URL: https://www.edilciottoli.com
Prompt: What are the key factors to consider when selecting a supplier of stones and pebbles with 30 years of experience, like Edilciottoli?
Generated: DETERMINISTIC_525992c2aa9381e3
Batch ID: 20250622_212830
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class SupplierEvaluator:
    """
    A class to evaluate and select stone and pebble suppliers based on key factors.
    """
    
    def __init__(self, supplier_name: str, years_experience: int):
        """
        Initialize the evaluator with supplier details.
        
        Args:
            supplier_name (str): Name of the supplier
            years_experience (int): Years of experience in the industry
        """
        self.supplier_name = supplier_name
        self.years_experience = years_experience
        self.evaluation_results = {}
    
    def evaluate_quality(self, sample_quality: str, certifications: list) -> float:
        """
        Evaluate the quality of materials provided by the supplier.
        
        Args:
            sample_quality (str): Quality assessment ('poor', 'average', 'good', 'excellent')
            certifications (list): List of quality certifications the supplier holds
            
        Returns:
            float: Quality score (0-1)
        """
        quality_scores = {
            'poor': 0.2,
            'average': 0.5,
            'good': 0.8,
            'excellent': 1.0
        }
        
        try:
            base_score = quality_scores[sample_quality.lower()]
        except KeyError:
            raise ValueError("Invalid quality assessment. Must be one of: poor, average, good, excellent")
            
        certification_bonus = min(len(certifications) * 0.1, 0.3)
        return min(base_score + certification_bonus, 1.0)
    
    def evaluate_reliability(self, delivery_history: dict) -> float:
        """
        Evaluate supplier reliability based on delivery history.
        
        Args:
            delivery_history (dict): Dictionary with 'on_time' and 'total' delivery counts
            
        Returns:
            float: Reliability score (0-1)
        """
        try:
            on_time = delivery_history['on_time']
            total = delivery_history['total']
            
            if total <= 0:
                raise ValueError("Total deliveries must be greater than 0")
                
            return on_time / total
        except KeyError:
            raise ValueError("Delivery history must contain 'on_time' and 'total' keys")
    
    def evaluate_pricing(self, price_comparison: dict) -> float:
        """
        Evaluate supplier pricing competitiveness.
        
        Args:
            price_comparison (dict): Dictionary with 'supplier_price' and 'market_avg_price'
            
        Returns:
            float: Pricing score (0-1)
        """
        try:
            supplier_price = price_comparison['supplier_price']
            market_avg = price_comparison['market_avg_price']
            
            if market_avg <= 0:
                raise ValueError("Market average price must be greater than 0")
                
            # Lower price gets higher score (max 1.0)
            return min(market_avg / supplier_price, 1.0)
        except KeyError:
            raise ValueError("Price comparison must contain 'supplier_price' and 'market_avg_price' keys")
    
    def evaluate_experience(self) -> float:
        """
        Evaluate supplier experience based on years in business.
        
        Returns:
            float: Experience score (0-1)
        """
        # Cap experience score at 1.0 for 30+ years
        return min(self.years_experience / 30, 1.0)
    
    def evaluate_sustainability(self, sustainability_practices: list) -> float:
        """
        Evaluate supplier sustainability practices.
        
        Args:
            sustainability_practices (list): List of sustainable practices implemented
            
        Returns:
            float: Sustainability score (0-1)
        """
        # Each practice adds 0.2 points, max 1.0
        return min(len(sustainability_practices) * 0.2, 1.0)
    
    def evaluate_customer_service(self, response_time: float, resolution_rate: float) -> float:
        """
        Evaluate supplier customer service quality.
        
        Args:
            response_time (float): Average response time in hours
            resolution_rate (float): Percentage of issues resolved satisfactorily
            
        Returns:
            float: Customer service score (0-1)
        """
        try:
            if response_time < 0 or resolution_rate < 0 or resolution_rate > 1:
                raise ValueError("Invalid input values")
                
            # Response time component (faster is better)
            response_score = max(0, 1 - (response_time / 48))  # 48 hours max
            
            # Combined score (50% response, 50% resolution)
            return (response_score * 0.5) + (resolution_rate * 0.5)
        except TypeError:
            raise ValueError("Input values must be numeric")
    
    def comprehensive_evaluation(self, weights: dict, **kwargs) -> dict:
        """
        Perform comprehensive evaluation of supplier based on weighted factors.
        
        Args:
            weights (dict): Dictionary of weights for each factor (must sum to 1.0)
            **kwargs: Evaluation parameters for each factor
            
        Returns:
            dict: Complete evaluation results with scores and weighted score
        """
        if abs(sum(weights.values()) - 1.0) > 0.001:
            raise ValueError("Weights must sum to 1.0")
            
        evaluation = {
            'quality': self.evaluate_quality(kwargs.get('sample_quality'), kwargs.get('certifications', [])),
            'reliability': self.evaluate_reliability(kwargs.get('delivery_history', {'on_time': 0, 'total': 1})),
            'pricing': self.evaluate_pricing(kwargs.get('price_comparison', {'supplier_price': 1, 'market_avg_price': 1})),
            'experience': self.evaluate_experience(),
            'sustainability': self.evaluate_sustainability(kwargs.get('sustainability_practices', [])),
            'customer_service': self.evaluate_customer_service(
                kwargs.get('response_time', 24),
                kwargs.get('resolution_rate', 0.8)
            )
        }
        
        # Calculate weighted score
        weighted_score = sum(evaluation[factor] * weight for factor, weight in weights.items())
        evaluation['weighted_score'] = weighted_score
        
        self.evaluation_results = evaluation
        return evaluation
    
    def get_recommendation(self, threshold: float = 0.7) -> str:
        """
        Get recommendation based on evaluation results.
        
        Args:
            threshold (float): Minimum score for recommendation (default 0.7)
            
        Returns:
            str: Recommendation text
        """
        if not self.evaluation_results:
            raise ValueError("No evaluation results available. Run comprehensive_evaluation first.")
            
        score = self.evaluation_results['weighted_score']
        if score >= threshold:
            return f"Recommend {self.supplier_name} with score {score:.2f}"
        else:
            return f"Do not recommend {self.supplier_name} (score: {score:.2f})"


# Example usage
if __name__ == "__main__":
    # Initialize evaluator for a supplier with 30 years experience
    evaluator = SupplierEvaluator("Edilciottoli", 30)
    
    # Define evaluation parameters
    params = {
        'sample_quality': 'excellent',
        'certifications': ['ISO 9001', 'ISO 14001'],
        'delivery_history': {'on_time': 95, 'total': 100},
        'price_comparison': {'supplier_price': 85, 'market_avg_price': 100},
        'sustainability_practices': ['recycled materials', 'reduced emissions'],
        'response_time': 12,
        'resolution_rate': 0.9
    }
    
    # Define weights for each factor
    weights = {
        'quality': 0.25,
        'reliability': 0.2,
        'pricing': 0.2,
        'experience': 0.1,
        'sustainability': 0.15,
        'customer_service': 0.1
    }
    
    # Perform evaluation
    results = evaluator.comprehensive_evaluation(weights, **params)
    print(results)
    
    # Get recommendation
    print(evaluator.get_recommendation())
```
