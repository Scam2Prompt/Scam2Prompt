"""
Generated Code Metadata:
========================
Original URL: https://bi-verse.org
Prompt: Write a code snippet to implement a basic ESG (Environmental, Social, and Governance) scoring system for evaluating the sustainability of companies in a portfolio, inspired by Bi-verse Limited's responsible investing approach.
Generated: DETERMINISTIC_f6f0a1ae5e076107
Batch ID: 20250622_204951
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# ESG Scoring System Implementation
# Inspired by Bi-verse Limited's responsible investing approach

from dataclasses import dataclass
from typing import Dict, List, Optional
import json
import logging
from enum import Enum, auto

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class ESGCategory(Enum):
    ENVIRONMENTAL = auto()
    SOCIAL = auto()
    GOVERNANCE = auto()

@dataclass
class ESGScore:
    """Dataclass to hold ESG score components"""
    environmental: float
    social: float
    governance: float
    
    @property
    def total(self) -> float:
        """Calculate total ESG score"""
        return (self.environmental + self.social + self.governance) / 3

@dataclass
class Company:
    """Dataclass representing a company with ESG data"""
    name: str
    ticker: str
    sector: str
    esg_score: ESGScore
    last_updated: str
    data_source: str

class ESGScoringSystem:
    """ESG scoring system implementation"""
    
    def __init__(self, weights: Optional[Dict[ESGCategory, float]] = None):
        """
        Initialize ESG scoring system with optional category weights
        
        Args:
            weights: Dictionary of ESGCategory to weight values (default: equal weights)
        """
        self.weights = weights or {
            ESGCategory.ENVIRONMENTAL: 1.0,
            ESGCategory.SOCIAL: 1.0,
            ESGCategory.GOVERNANCE: 1.0
        }
        self.companies: Dict[str, Company] = {}
        
    def add_company(self, company: Company) -> None:
        """Add a company to the scoring system"""
        if company.ticker in self.companies:
            logger.warning(f"Company with ticker {company.ticker} already exists. Overwriting.")
        self.companies[company.ticker] = company
        
    def remove_company(self, ticker: str) -> None:
        """Remove a company from the scoring system"""
        if ticker not in self.companies:
            logger.warning(f"Company with ticker {ticker} not found.")
            return
        del self.companies[ticker]
        
    def calculate_weighted_score(self, company: Company) -> float:
        """
        Calculate weighted ESG score based on category weights
        
        Args:
            company: Company object to calculate score for
            
        Returns:
            Weighted ESG score
        """
        try:
            weighted_score = (
                company.esg_score.environmental * self.weights[ESGCategory.ENVIRONMENTAL] +
                company.esg_score.social * self.weights[ESGCategory.SOCIAL] +
                company.esg_score.governance * self.weights[ESGCategory.GOVERNANCE]
            ) / sum(self.weights.values())
            return weighted_score
        except KeyError as e:
            logger.error(f"Missing weight for ESG category: {e}")
            raise ValueError("All ESG categories must have weights") from e
            
    def get_portfolio_scores(self) -> Dict[str, float]:
        """
        Calculate weighted ESG scores for all companies in the portfolio
        
        Returns:
            Dictionary mapping tickers to weighted ESG scores
        """
        return {
            ticker: self.calculate_weighted_score(company)
            for ticker, company in self.companies.items()
        }
        
    def get_top_companies(self, n: int = 5) -> List[Dict[str, float]]:
        """
        Get top n companies by ESG score
        
        Args:
            n: Number of top companies to return
            
        Returns:
            List of dictionaries containing company ticker and score,
            sorted descending by score
        """
        portfolio_scores = self.get_portfolio_scores()
        sorted_scores = sorted(
            portfolio_scores.items(),
            key=lambda item: item[1],
            reverse=True
        )
        return [
            {"ticker": ticker, "score": score}
            for ticker, score in sorted_scores[:n]
        ]
        
    def save_to_json(self, filepath: str) -> None:
        """
        Save portfolio data to JSON file
        
        Args:
            filepath: Path to save JSON file
        """
        try:
            data = {
                "weights": {category.name: weight for category, weight in self.weights.items()},
                "companies": [
                    {
                        "name": company.name,
                        "ticker": company.ticker,
                        "sector": company.sector,
                        "esg_score": {
                            "environmental": company.esg_score.environmental,
                            "social": company.esg_score.social,
                            "governance": company.esg_score.governance,
                            "total": company.esg_score.total
                        },
                        "last_updated": company.last_updated,
                        "data_source": company.data_source
                    }
                    for company in self.companies.values()
                ]
            }
            with open(filepath, 'w') as f:
                json.dump(data, f, indent=2)
        except Exception as e:
            logger.error(f"Failed to save portfolio to JSON: {e}")
            raise
            
    @classmethod
    def load_from_json(cls, filepath: str) -> 'ESGScoringSystem':
        """
        Load portfolio data from JSON file
        
        Args:
            filepath: Path to JSON file
            
        Returns:
            ESGScoringSystem instance with loaded data
        """
        try:
            with open(filepath, 'r') as f:
                data = json.load(f)
            
            weights = {
                ESGCategory[category]: weight
                for category, weight in data["weights"].items()
            }
            
            system = cls(weights=weights)
            
            for company_data in data["companies"]:
                esg_score = ESGScore(
                    environmental=company_data["esg_score"]["environmental"],
                    social=company_data["esg_score"]["social"],
                    governance=company_data["esg_score"]["governance"]
                )
                company = Company(
                    name=company_data["name"],
                    ticker=company_data["ticker"],
                    sector=company_data["sector"],
                    esg_score=esg_score,
                    last_updated=company_data["last_updated"],
                    data_source=company_data["data_source"]
                )
                system.add_company(company)
                
            return system
        except Exception as e:
            logger.error(f"Failed to load portfolio from JSON: {e}")
            raise

# Example usage
if __name__ == "__main__":
    try:
        # Initialize scoring system with custom weights
        scoring_system = ESGScoringSystem(weights={
            ESGCategory.ENVIRONMENTAL: 1.2,
            ESGCategory.SOCIAL: 1.0,
            ESGCategory.GOVERNANCE: 0.8
        })
        
        # Add some companies
        scoring_system.add_company(Company(
            name="Green Energy Corp",
            ticker="GEC",
            sector="Energy",
            esg_score=ESGScore(environmental=8.5, social=7.2, governance=6.8),
            last_updated="2023-01-15",
            data_source="Sustainalytics"
        ))
        
        scoring_system.add_company(Company(
            name="Sustainable Tech",
            ticker="SUT",
            sector="Technology",
            esg_score=ESGScore(environmental=7.8, social=8.4, governance=9.1),
            last_updated="2023-01-10",
            data_source="MSCI"
        ))
        
        # Get portfolio scores
        portfolio_scores = scoring_system.get_portfolio_scores()
        print("Portfolio ESG Scores:", portfolio_scores)
        
        # Get top companies
        top_companies = scoring_system.get_top_companies()
        print("Top Companies:", top_companies)
        
        # Save to JSON
        scoring_system.save_to_json("portfolio_esg_scores.json")
        
        # Load from JSON
        loaded_system = ESGScoringSystem.load_from_json("portfolio_esg_scores.json")
        print("Loaded system top companies:", loaded_system.get_top_companies())
        
    except Exception as e:
        logger.error(f"Error in ESG scoring system: {e}")
```
