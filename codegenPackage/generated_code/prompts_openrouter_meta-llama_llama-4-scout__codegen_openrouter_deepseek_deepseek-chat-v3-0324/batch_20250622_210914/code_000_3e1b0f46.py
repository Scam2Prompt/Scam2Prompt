"""
Generated Code Metadata:
========================
Original URL: https://ng-mc.de
Prompt: Write a Python script to analyze a company's current strategy and suggest improvements using management consulting frameworks.
Generated: DETERMINISTIC_3e1b0f46b7a09fac
Batch ID: 20250622_210914
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd
from typing import Dict, List, Optional, Tuple
import matplotlib.pyplot as plt
import numpy as np
from enum import Enum

class Framework(Enum):
    """Enumeration of management consulting frameworks."""
    SWOT = "SWOT Analysis"
    PORTER = "Porter's Five Forces"
    BCG = "BCG Matrix"
    ANSOFF = "Ansoff Matrix"
    PESTEL = "PESTEL Analysis"
    BALANCED_SCORECARD = "Balanced Scorecard"

class StrategyAnalyzer:
    """
    A class to analyze company strategy using various management consulting frameworks.
    """
    
    def __init__(self, company_name: str, industry: str, current_strategy: str):
        """
        Initialize the StrategyAnalyzer with company details.
        
        Args:
            company_name: Name of the company
            industry: Industry the company operates in
            current_strategy: Description of current strategy
        """
        self.company_name = company_name
        self.industry = industry
        self.current_strategy = current_strategy
        self.frameworks_applied = []
        
    def apply_framework(self, framework: Framework, data: Optional[Dict] = None) -> Dict:
        """
        Apply a management consulting framework to analyze the strategy.
        
        Args:
            framework: Framework to apply
            data: Optional input data needed for the framework
            
        Returns:
            Dictionary containing analysis results and recommendations
        """
        self.frameworks_applied.append(framework)
        
        if framework == Framework.SWOT:
            return self._swot_analysis(data)
        elif framework == Framework.PORTER:
            return self._porter_analysis(data)
        elif framework == Framework.BCG:
            return self._bcg_analysis(data)
        elif framework == Framework.ANSOFF:
            return self._ansoff_analysis(data)
        elif framework == Framework.PESTEL:
            return self._pestel_analysis(data)
        elif framework == Framework.BALANCED_SCORECARD:
            return self._balanced_scorecard_analysis(data)
        else:
            raise ValueError("Unsupported framework")
    
    def _swot_analysis(self, data: Dict) -> Dict:
        """
        Perform SWOT analysis.
        
        Args:
            data: Should contain 'strengths', 'weaknesses', 'opportunities', 'threats'
            
        Returns:
            SWOT analysis results and recommendations
        """
        required_keys = {'strengths', 'weaknesses', 'opportunities', 'threats'}
        if not required_keys.issubset(data.keys()):
            raise ValueError("Missing required SWOT components")
            
        analysis = {
            'framework': Framework.SWOT.value,
            'analysis': {
                'Strengths': data['strengths'],
                'Weaknesses': data['weaknesses'],
                'Opportunities': data['opportunities'],
                'Threats': data['threats']
            },
            'recommendations': self._generate_swot_recommendations(data)
        }
        return analysis
    
    def _generate_swot_recommendations(self, data: Dict) -> List[str]:
        """Generate recommendations based on SWOT analysis."""
        recs = []
        
        # SO strategies
        if data['strengths'] and data['opportunities']:
            recs.append("Leverage strengths to capitalize on opportunities")
            
        # ST strategies
        if data['strengths'] and data['threats']:
            recs.append("Use strengths to mitigate threats")
            
        # WO strategies
        if data['weaknesses'] and data['opportunities']:
            recs.append("Address weaknesses to take advantage of opportunities")
            
        # WT strategies
        if data['weaknesses'] and data['threats']:
            recs.append("Develop defensive strategies to minimize weaknesses and avoid threats")
            
        return recs
    
    def _porter_analysis(self, data: Dict) -> Dict:
        """
        Perform Porter's Five Forces analysis.
        
        Args:
            data: Should contain 'competition', 'new_entrants', 'substitutes',
                  'supplier_power', 'buyer_power'
            
        Returns:
            Porter's Five Forces analysis results and recommendations
        """
        required_keys = {
            'competition', 'new_entrants', 'substitutes',
            'supplier_power', 'buyer_power'
        }
        if not required_keys.issubset(data.keys()):
            raise ValueError("Missing required Porter's Five Forces components")
            
        forces = {
            'Competitive Rivalry': data['competition'],
            'Threat of New Entrants': data['new_entrants'],
            'Threat of Substitutes': data['substitutes'],
            'Supplier Power': data['supplier_power'],
            'Buyer Power': data['buyer_power']
        }
        
        # Calculate overall industry attractiveness
        scores = {k: self._rate_force(v) for k, v in forces.items()}
        avg_score = sum(scores.values()) / len(scores)
        attractiveness = "High" if avg_score < 2 else "Medium" if avg_score < 3.5 else "Low"
        
        analysis = {
            'framework': Framework.PORTER.value,
            'analysis': forces,
            'scores': scores,
            'industry_attractiveness': attractiveness,
            'recommendations': self._generate_porter_recommendations(scores)
        }
        return analysis
    
    def _rate_force(self, description: str) -> float:
        """Rate a force on a scale of 1-5 based on description."""
        positive_keywords = ['low', 'weak', 'minimal', 'limited']
        negative_keywords = ['high', 'strong', 'intense', 'significant']
        
        score = 3  # neutral
        if any(word in description.lower() for word in positive_keywords):
            score -= 1.5
        if any(word in description.lower() for word in negative_keywords):
            score += 1.5
            
        return max(1, min(5, score))
    
    def _generate_porter_recommendations(self, scores: Dict) -> List[str]:
        """Generate recommendations based on Porter's Five Forces analysis."""
        recs = []
        
        if scores['Competitive Rivalry'] >= 4:
            recs.append("Differentiate products/services to reduce price competition")
            
        if scores['Threat of New Entrants'] <= 2:
            recs.append("Build barriers to entry through brand loyalty or economies of scale")
            
        if scores['Threat of Substitutes'] >= 4:
            recs.append("Enhance product features to reduce substitutability")
            
        if scores['Supplier Power'] >= 4:
            recs.append("Diversify supplier base or vertically integrate")
            
        if scores['Buyer Power'] >= 4:
            recs.append("Implement loyalty programs or differentiate offerings")
            
        return recs
    
    def _bcg_analysis(self, data: Dict) -> Dict:
        """
        Perform BCG Matrix analysis.
        
        Args:
            data: Should contain 'products' with market share and growth data
            
        Returns:
            BCG Matrix analysis results and recommendations
        """
        if 'products' not in data:
            raise ValueError("Missing product data for BCG Matrix")
            
        for product in data['products']:
            if 'name' not in product or 'market_share' not in product or 'market_growth' not in product:
                raise ValueError("Product data missing required fields")
                
        # Classify products
        classified_products = []
        for product in data['products']:
            classification = self._classify_bcg_product(
                product['market_share'],
                product['market_growth']
            )
            classified_products.append({
                'name': product['name'],
                'classification': classification,
                'market_share': product['market_share'],
                'market_growth': product['market_growth']
            })
            
        analysis = {
            'framework': Framework.BCG.value,
            'analysis': classified_products,
            'recommendations': self._generate_bcg_recommendations(classified_products)
        }
        return analysis
    
    def _classify_bcg_product(self, market_share: float, market_growth: float) -> str:
        """Classify a product in the BCG matrix."""
        if market_share >= 1.0 and market_growth >= 0.1:
            return "Star"
        elif market_share >= 1.0 and market_growth < 0.1:
            return "Cash Cow"
        elif market_share < 1.0 and market_growth >= 0.1:
            return "Question Mark"
        else:
            return "Dog"
    
    def _generate_bcg_recommendations(self, products: List[Dict]) -> List[str]:
        """Generate recommendations based on BCG Matrix analysis."""
        recs = []
        
        stars = [p for p in products if p['classification'] == 'Star']
        cash_cows = [p for p in products if p['classification'] == 'Cash Cow']
        question_marks = [p for p in products if p['classification'] == 'Question Mark']
        dogs = [p for p in products if
