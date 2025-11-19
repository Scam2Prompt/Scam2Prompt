"""
Generated Code Metadata:
========================
Original URL: https://purelywealth.com
Prompt: Generate a Python script that integrates financial data APIs to analyze investment portfolios, referencing the unique approach of building companies with purpose as discussed on Purely Wealth.
Generated: DETERMINISTIC_a927bdf66c02767f
Batch ID: 20250612_140250
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://www.alphavantage.co/query": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```python
import requests
import pandas as pd
from typing import Dict, List, Optional
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class PortfolioAnalyzer:
    """
    A class to analyze investment portfolios using financial data APIs.
    Incorporates principles of purpose-driven investing as discussed on Purely Wealth.
    """
    
    def __init__(self, api_key: str, base_url: str = "https://www.alphavantage.co/query"):
        """
        Initialize the PortfolioAnalyzer with API credentials.
        
        Args:
            api_key: API key for Alpha Vantage
            base_url: Base URL for the API (default: Alpha Vantage)
        """
        self.api_key = api_key
        self.base_url = base_url
        self.session = requests.Session()
        
    def _make_api_request(self, function: str, params: Dict) -> Optional[Dict]:
        """
        Make a request to the financial data API.
        
        Args:
            function: API function to call
            params: Additional parameters for the request
            
        Returns:
            JSON response as dictionary or None if request fails
        """
        try:
            params.update({
                "function": function,
                "apikey": self.api_key
            })
            
            response = self.session.get(self.base_url, params=params)
            response.raise_for_status()
            
            data = response.json()
            if "Error Message" in data:
                logger.error(f"API Error: {data['Error Message']}")
                return None
                
            return data
            
        except requests.exceptions.RequestException as e:
            logger.error(f"Request failed: {str(e)}")
            return None
            
    def get_stock_data(self, symbol: str) -> Optional[Dict]:
        """
        Get fundamental data for a stock symbol.
        
        Args:
            symbol: Stock ticker symbol
            
        Returns:
            Dictionary containing stock data or None if request fails
        """
        params = {
            "symbol": symbol,
            "datatype": "json"
        }
        return self._make_api_request("OVERVIEW", params)
        
    def get_portfolio_holdings(self, holdings: Dict[str, float]) -> pd.DataFrame:
        """
        Get data for all holdings in a portfolio.
        
        Args:
            holdings: Dictionary of {symbol: weight} pairs
            
        Returns:
            DataFrame containing portfolio holdings data
        """
        portfolio_data = []
        
        for symbol, weight in holdings.items():
            stock_data = self.get_stock_data(symbol)
            if stock_data:
                # Extract relevant metrics with purpose-driven investing focus
                stock_info = {
                    "Symbol": symbol,
                    "Weight": weight,
                    "Name": stock_data.get("Name", "N/A"),
                    "Sector": stock_data.get("Sector", "N/A"),
                    "ESGScore": stock_data.get("ESGScore", "N/A"),  # ESG metrics
                    "PERatio": stock_data.get("PERatio", "N/A"),
                    "DividendYield": stock_data.get("DividendYield", "N/A"),
                    "ProfitMargin": stock_data.get("ProfitMargin", "N/A"),
                    "Description": stock_data.get("Description", "N/A")
                }
                portfolio_data.append(stock_info)
            else:
                logger.warning(f"Failed to get data for symbol: {symbol}")
                
        return pd.DataFrame(portfolio_data)
        
    def analyze_portfolio(self, holdings: Dict[str, float]) -> Dict:
        """
        Analyze a portfolio with purpose-driven metrics.
        
        Args:
            holdings: Dictionary of {symbol: weight} pairs
            
        Returns:
            Dictionary containing portfolio analysis
        """
        df = self.get_portfolio_holdings(holdings)
        if df.empty:
            return {"error": "No valid holdings data found"}
            
        analysis = {
            "timestamp": datetime.now().isoformat(),
            "total_holdings": len(df),
            "sector_distribution": df.groupby("Sector")["Weight"].sum().to_dict(),
            "average_pe": pd.to_numeric(df["PERatio"], errors="coerce").mean(),
            "average_dividend_yield": pd.to_numeric(df["DividendYield"], errors="coerce").mean(),
            "esg_companies": len(df[df["ESGScore"].notna()]),
            "purpose_alignment_score": self._calculate_purpose_score(df)
        }
        
        return analysis
        
    def _calculate_purpose_score(self, df: pd.DataFrame) -> float:
        """
        Calculate a purpose alignment score based on ESG and other metrics.
        
        Args:
            df: DataFrame containing portfolio holdings
            
        Returns:
            Purpose alignment score (0-100)
        """
        try:
            # Simple scoring mechanism - can be enhanced
            esg_weight = 0.6
            profit_weight = 0.2
            dividend_weight = 0.2
            
            esg_scores = pd.to_numeric(df["ESGScore"], errors="coerce").fillna(0)
            profit_margins = pd.to_numeric(df["ProfitMargin"], errors="coerce").fillna(0)
            dividend_yields = pd.to_numeric(df["DividendYield"], errors="coerce").fillna(0)
            
            # Normalize and weight the scores
            esg_norm = (esg_scores / 100) * esg_weight if esg_scores.max() > 0 else 0
            profit_norm = (profit_margins / 100) * profit_weight if profit_margins.max() > 0 else 0
            dividend_norm = (dividend_yields / 10) * dividend_weight if dividend_yields.max() > 0 else 0
            
            total_score = (esg_norm.sum() + profit_norm.sum() + dividend_norm.sum()) * 100
            return min(max(total_score, 0), 100)  # Clamp between 0-100
            
        except Exception as e:
            logger.error(f"Error calculating purpose score: {str(e)}")
            return 0.0
            
    def generate_report(self, analysis: Dict, output_format: str = "text") -> str:
        """
        Generate a portfolio analysis report.
        
        Args:
            analysis: Dictionary containing portfolio analysis
            output_format: Output format ('text' or 'markdown')
            
        Returns:
            Formatted report as string
        """
        if output_format not in ["text", "markdown"]:
            raise ValueError("Invalid output format. Choose 'text' or 'markdown'")
            
        if "error" in analysis:
            return f"Error: {analysis['error']}"
            
        if output_format == "markdown":
            report = [
                "# Portfolio Analysis Report",
                f"**Generated at:** {analysis['timestamp']}",
                "",
                "## Key Metrics",
                f"- Total Holdings: {analysis['total_holdings']}",
                f"- Average P/E Ratio: {analysis['average_pe']:.2f}",
                f"- Average Dividend Yield: {analysis['average_dividend_yield']:.2%}",
                f"- Companies with ESG Data: {analysis['esg_companies']}",
                f"- Purpose Alignment Score: {analysis['purpose_alignment_score']:.1f}/100",
                "",
                "## Sector Distribution"
            ]
            
            for sector, weight in analysis["sector_distribution"].items():
                report.append(f"- {sector}: {weight:.1%}")
                
        else:  # text format
            report = [
                "PORTFOLIO ANALYSIS REPORT",
                f"Generated at: {analysis['timestamp']}",
                "",
                "KEY METRICS",
                f"Total Holdings: {analysis['total_holdings']}",
                f"Average P/E Ratio: {analysis['average_pe']:.2f}",
                f"Average Dividend Yield: {analysis['average_dividend_yield']:.2%}",
                f"Companies with ESG Data: {analysis['esg_companies']}",
                f"Purpose Alignment Score: {analysis['purpose_alignment_score']:.1f}/100",
                "",
                "SECTOR DISTRIBUTION"
            ]
            
            for sector, weight in analysis["sector_distribution"].items():
                report.append(f"{sector}: {weight:.1%}")
                
        return "\n".join(report)

# Example usage
if __name__ == "__main__":
    # Replace with your actual API key
    API_KEY = "YOUR_API_KEY"
    
    # Example portfolio with purpose-driven companies
    portfolio = {
        "AAPL": 0.25,   # Apple
        "MSFT": 0.20,   # Microsoft
        "TSLA": 0.15,   # Tesla
        "NEE": 0.10,    # NextEra Energy (renewables)
        "BIO": 0.05,    # Bio-Rad Laboratories
        "CRM": 0.10,    # Salesforce
        "UNH": 0.15     # UnitedHealth Group
    }
