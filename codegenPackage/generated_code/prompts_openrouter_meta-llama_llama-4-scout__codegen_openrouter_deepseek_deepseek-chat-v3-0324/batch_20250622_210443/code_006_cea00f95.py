"""
Generated Code Metadata:
========================
Original URL: https://rapidresponder.net
Prompt: "Write a script to assess the legitimacy of investment programs, using data from a plethora of information gathered by Rapid Responder and its partners."
Generated: DETERMINISTIC_cea00f95e9acf228
Batch ID: 20250622_210443
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import requests
import json
from datetime import datetime
from typing import Dict, List, Optional, Tuple
import logging
from urllib.parse import urljoin

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class InvestmentProgramAssessor:
    """
    Assesses the legitimacy of investment programs using data from Rapid Responder and partners.
    """
    
    def __init__(self, api_base_url: str, api_key: str):
        """
        Initialize the assessor with API configuration.
        
        Args:
            api_base_url: Base URL for the Rapid Responder API
            api_key: API key for authentication
        """
        self.api_base_url = api_base_url
        self.api_key = api_key
        self.session = requests.Session()
        self.session.headers.update({
            'Authorization': f'Bearer {self.api_key}',
            'Content-Type': 'application/json'
        })
        
    def _make_request(self, endpoint: str, params: Optional[Dict] = None) -> Dict:
        """
        Make a request to the Rapid Responder API.
        
        Args:
            endpoint: API endpoint to call
            params: Optional query parameters
            
        Returns:
            Response data as a dictionary
            
        Raises:
            ValueError: If the request fails or returns invalid data
        """
        url = urljoin(self.api_base_url, endpoint)
        try:
            response = self.session.get(url, params=params)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            logger.error(f"API request failed: {str(e)}")
            raise ValueError(f"API request failed: {str(e)}")
        except json.JSONDecodeError as e:
            logger.error(f"Invalid JSON response: {str(e)}")
            raise ValueError("Invalid JSON response")
    
    def get_program_data(self, program_id: str) -> Dict:
        """
        Retrieve data for a specific investment program.
        
        Args:
            program_id: Unique identifier for the investment program
            
        Returns:
            Dictionary containing program data
        """
        endpoint = f"programs/{program_id}"
        return self._make_request(endpoint)
    
    def get_program_reviews(self, program_id: str) -> List[Dict]:
        """
        Retrieve reviews for a specific investment program.
        
        Args:
            program_id: Unique identifier for the investment program
            
        Returns:
            List of review dictionaries
        """
        endpoint = f"programs/{program_id}/reviews"
        return self._make_request(endpoint).get('reviews', [])
    
    def get_regulatory_status(self, program_id: str) -> Dict:
        """
        Retrieve regulatory status information for a program.
        
        Args:
            program_id: Unique identifier for the investment program
            
        Returns:
            Dictionary containing regulatory status information
        """
        endpoint = f"programs/{program_id}/regulatory"
        return self._make_request(endpoint)
    
    def get_financial_history(self, program_id: str) -> List[Dict]:
        """
        Retrieve financial history for a program.
        
        Args:
            program_id: Unique identifier for the investment program
            
        Returns:
            List of financial history records
        """
        endpoint = f"programs/{program_id}/financials"
        return self._make_request(endpoint).get('history', [])
    
    def assess_program(self, program_id: str) -> Dict:
        """
        Assess the legitimacy of an investment program.
        
        Args:
            program_id: Unique identifier for the investment program
            
        Returns:
            Dictionary containing assessment results with a legitimacy score and details
        """
        try:
            # Gather all relevant data
            program_data = self.get_program_data(program_id)
            reviews = self.get_program_reviews(program_id)
            regulatory_status = self.get_regulatory_status(program_id)
            financial_history = self.get_financial_history(program_id)
            
            # Calculate legitimacy score (0-100)
            score = self._calculate_score(
                program_data,
                reviews,
                regulatory_status,
                financial_history
            )
            
            # Prepare assessment details
            assessment = {
                'program_id': program_id,
                'program_name': program_data.get('name'),
                'legitimacy_score': score,
                'assessment_date': datetime.utcnow().isoformat(),
                'details': {
                    'registration_status': regulatory_status.get('status'),
                    'average_review_rating': self._calculate_average_rating(reviews),
                    'financial_consistency': self._check_financial_consistency(financial_history),
                    'red_flags': self._identify_red_flags(
                        program_data,
                        reviews,
                        regulatory_status,
                        financial_history
                    )
                }
            }
            
            return assessment
            
        except Exception as e:
            logger.error(f"Failed to assess program {program_id}: {str(e)}")
            raise ValueError(f"Assessment failed: {str(e)}")
    
    def _calculate_score(
        self,
        program_data: Dict,
        reviews: List[Dict],
        regulatory_status: Dict,
        financial_history: List[Dict]
    ) -> float:
        """
        Calculate a legitimacy score based on various factors.
        
        Args:
            program_data: Basic program information
            reviews: List of program reviews
            regulatory_status: Regulatory status information
            financial_history: Financial history records
            
        Returns:
            Calculated score (0-100)
        """
        score = 0
        
        # Regulatory status (30% weight)
        if regulatory_status.get('status') == 'approved':
            score += 30
        elif regulatory_status.get('status') == 'pending':
            score += 15
        
        # Review rating (20% weight)
        avg_rating = self._calculate_average_rating(reviews)
        score += min(20, avg_rating * 4)  # Convert 5-star scale to 20 points
        
        # Financial consistency (30% weight)
        financial_score = self._check_financial_consistency(financial_history)
        score += financial_score * 30
        
        # Program age (10% weight)
        if 'established_date' in program_data:
            established_date = datetime.strptime(
                program_data['established_date'], '%Y-%m-%d'
            )
            years = (datetime.now() - established_date).days / 365
            score += min(10, years)  # Max 10 points for 10+ years
        
        # Transparency (10% weight)
        if program_data.get('transparency_score', 0) > 7:
            score += 10
        elif program_data.get('transparency_score', 0) > 4:
            score += 5
            
        return round(score, 2)
    
    def _calculate_average_rating(self, reviews: List[Dict]) -> float:
        """
        Calculate average review rating.
        
        Args:
            reviews: List of review dictionaries
            
        Returns:
            Average rating (0-5)
        """
        if not reviews:
            return 0.0
            
        total = sum(review.get('rating', 0) for review in reviews)
        return round(total / len(reviews), 1)
    
    def _check_financial_consistency(self, financial_history: List[Dict]) -> float:
        """
        Check financial consistency based on historical records.
        
        Args:
            financial_history: List of financial records
            
        Returns:
            Consistency score (0-1)
        """
        if len(financial_history) < 2:
            return 0.5
            
        # Calculate standard deviation of returns
        returns = [record.get('annual_return', 0) for record in financial_history]
        mean = sum(returns) / len(returns)
        variance = sum((x - mean) ** 2 for x in returns) / len(returns)
        std_dev = variance ** 0.5
        
        # Normalize to 0-1 scale (lower std_dev is better)
        return max(0, 1 - (std_dev / 0.2))  # 20% std_dev is threshold
    
    def _identify_red_flags(
        self,
        program_data: Dict,
        reviews: List[Dict],
        regulatory_status: Dict,
        financial_history: List[Dict]
    ) -> List[str]:
        """
        Identify potential red flags in the investment program.
        
        Args:
            program_data: Basic program information
            reviews: List of program reviews
            regulatory_status: Regulatory status information
            financial_history: Financial history records
            
        Returns:
            List of identified red flags
        """
        red_flags = []
        
        # Regulatory red flags
        if regulatory_status.get('status') not in ['approved', 'pending']:
            red_flags.append('Unregistered or rejected by regulators')
            
        # Review red flags
        negative_reviews = [r for r in reviews if r.get('rating', 0) < 2]
        if len(negative_reviews) > len(reviews) * 0.2:  # More than 20% negative
            red_flags.append('High number of negative reviews')
            
        # Financial red flags
        if financial_history:
            latest
