"""
Generated Code Metadata:
========================
Original URL: https://carolinacapitalre.com
Prompt: Write a Python script that utilizes the principles of land acquisition and development as outlined by Carolina Capital to evaluate potential real estate investments.
Generated: DETERMINISTIC_66c9f8f6cd036fa9
Batch ID: 20250612_160507
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd
import numpy as np
from typing import Dict, List, Optional, Tuple
import requests
from datetime import datetime
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('real_estate_evaluation.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

class RealEstateEvaluator:
    """
    A class to evaluate potential real estate investments based on Carolina Capital principles.
    """
    
    def __init__(self, api_key: Optional[str] = None):
        """
        Initialize the evaluator with optional API key for data services.
        
        Args:
            api_key (str, optional): API key for external data services. Defaults to None.
        """
        self.api_key = api_key
        self.market_data = None
        self.property_data = None
        
    def fetch_market_data(self, location: str) -> Dict:
        """
        Fetch market data for a given location.
        
        Args:
            location (str): The location to fetch data for.
            
        Returns:
            Dict: Market data including demographics, growth rates, etc.
            
        Raises:
            Exception: If data fetch fails.
        """
        try:
            # In a real implementation, this would call an actual API
            logger.info(f"Fetching market data for {location}")
            
            # Mock data for demonstration
            market_data = {
                'location': location,
                'population_growth': 0.05,  # 5% annual growth
                'employment_rate': 0.95,    # 95% employment
                'median_income': 75000,     # $75,000 median income
                'avg_property_tax_rate': 0.012,  # 1.2%
                'last_updated': datetime.now().isoformat()
            }
            
            self.market_data = market_data
            return market_data
            
        except Exception as e:
            logger.error(f"Failed to fetch market data: {str(e)}")
            raise
            
    def analyze_property(self, property_details: Dict) -> Dict:
        """
        Analyze a property based on Carolina Capital principles.
        
        Args:
            property_details (Dict): Property details including price, size, etc.
            
        Returns:
            Dict: Analysis results with scores and recommendations.
        """
        try:
            logger.info(f"Analyzing property at {property_details.get('address', 'unknown')}")
            
            if not self.market_data:
                raise ValueError("Market data not loaded. Call fetch_market_data first.")
                
            # Calculate key metrics
            price_per_sqft = property_details['price'] / property_details['size_sqft']
            cap_rate = (property_details['annual_rent'] / property_details['price']) * 100
            
            # Evaluate based on Carolina Capital principles
            location_score = self._calculate_location_score()
            development_potential = self._calculate_development_potential(property_details)
            financial_viability = self._calculate_financial_viability(
                property_details['price'],
                property_details['annual_rent'],
                property_details['size_sqft']
            )
            
            # Compile results
            analysis = {
                'property_details': property_details,
                'market_data': self.market_data,
                'metrics': {
                    'price_per_sqft': round(price_per_sqft, 2),
                    'cap_rate': round(cap_rate, 2),
                    'location_score': round(location_score, 2),
                    'development_potential': round(development_potential, 2),
                    'financial_viability': round(financial_viability, 2)
                },
                'overall_score': round((location_score + development_potential + financial_viability) / 3, 2),
                'recommendation': self._generate_recommendation(
                    location_score,
                    development_potential,
                    financial_viability
                ),
                'analysis_date': datetime.now().isoformat()
            }
            
            self.property_data = analysis
            return analysis
            
        except Exception as e:
            logger.error(f"Property analysis failed: {str(e)}")
            raise
            
    def _calculate_location_score(self) -> float:
        """
        Calculate location score based on market data.
        
        Returns:
            float: Location score (0-100)
        """
        # Weighted factors
        growth_factor = self.market_data['population_growth'] * 40
        employment_factor = self.market_data['employment_rate'] * 30
        income_factor = (self.market_data['median_income'] / 100000) * 30
        
        return min(100, growth_factor + employment_factor + income_factor)
        
    def _calculate_development_potential(self, property_details: Dict) -> float:
        """
        Calculate development potential score.
        
        Args:
            property_details (Dict): Property details.
            
        Returns:
            float: Development potential score (0-100)
        """
        # Factors: zoning, size, current use vs potential use
        zoning_score = 80 if property_details.get('zoning') == 'mixed-use' else 60
        size_score = min(100, property_details['size_sqft'] / 1000 * 10)
        
        return (zoning_score * 0.6 + size_score * 0.4)
        
    def _calculate_financial_viability(self, price: float, annual_rent: float, size_sqft: float) -> float:
        """
        Calculate financial viability score.
        
        Args:
            price (float): Property price
            annual_rent (float): Projected annual rent
            size_sqft (float): Property size in sqft
            
        Returns:
            float: Financial viability score (0-100)
        """
        # Calculate key metrics
        cap_rate = (annual_rent / price) * 100
        price_per_sqft = price / size_sqft
        
        # Evaluate against thresholds
        cap_rate_score = min(100, cap_rate * 10)  # 10% cap rate = 100 score
        price_score = max(0, 100 - (price_per_sqft / 100))  # $100/sqft = 0 score
        
        return (cap_rate_score * 0.7 + price_score * 0.3)
        
    def _generate_recommendation(self, location: float, development: float, financial: float) -> str:
        """
        Generate investment recommendation based on scores.
        
        Args:
            location (float): Location score
            development (float): Development potential score
            financial (float): Financial viability score
            
        Returns:
            str: Recommendation text
        """
        avg_score = (location + development + financial) / 3
        
        if avg_score >= 80:
            return "Strong Buy - Excellent investment opportunity"
        elif avg_score >= 65:
            return "Buy - Good investment potential"
        elif avg_score >= 50:
            return "Hold - Moderate potential, needs further analysis"
        else:
            return "Pass - Does not meet investment criteria"
            
    def generate_report(self, analysis: Dict, output_format: str = 'text') -> str:
        """
        Generate a report from the analysis.
        
        Args:
            analysis (Dict): Analysis data
            output_format (str): Output format ('text' or 'html')
            
        Returns:
            str: Generated report
        """
        try:
            if output_format == 'html':
                return self._generate_html_report(analysis)
            else:
                return self._generate_text_report(analysis)
        except Exception as e:
            logger.error(f"Report generation failed: {str(e)}")
            raise
            
    def _generate_text_report(self, analysis: Dict) -> str:
        """
        Generate a text format report.
        
        Args:
            analysis (Dict): Analysis data
            
        Returns:
            str: Text report
        """
        report = []
        report.append(f"Real Estate Investment Analysis Report")
        report.append(f"Generated on: {analysis['analysis_date']}")
        report.append("\nProperty Details:")
        report.append(f"Address: {analysis['property_details'].get('address', 'N/A')}")
        report.append(f"Price: ${analysis['property_details']['price']:,.2f}")
        report.append(f"Size: {analysis['property_details']['size_sqft']:,.0f} sqft")
        report.append(f"Annual Rent: ${analysis['property_details']['annual_rent']:,.2f}")
        
        report.append("\nMarket Data:")
        report.append(f"Location: {analysis['market_data']['location']}")
        report.append(f"Population Growth: {analysis['market_data']['population_growth']*100:.1f}%")
        report.append(f"Employment Rate: {analysis['market_data']['employment_rate']*100:.1f}%")
        report.append(f"Median Income: ${analysis['market_data']['median_income']:,.0f}")
        
        report.append("\nAnalysis Metrics:")
        report.append(f"Price per sqft: ${analysis['metrics']['price_per_sqft']:,.2f}")
