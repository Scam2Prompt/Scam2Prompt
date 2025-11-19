"""
Generated Code Metadata:
========================
Original URL: https://proofoftalk.pages.dev
Prompt: Write code to generate a PDF report summarizing the AI-driven evaluation of a Web3 startup, including sections for business model analysis, market size, and competitive landscape, as described in the Proof of Pitch competition.
Generated: DETERMINISTIC_57911784894faa6d
Batch ID: 20250612_153606
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
from datetime import datetime
from fpdf import FPDF
import json
from typing import Dict, Any, Optional

class StartupEvaluationPDF:
    """
    Generates a PDF report for a Web3 startup evaluation based on the Proof of Pitch competition criteria.
    """
    
    def __init__(self, startup_data: Dict[str, Any], output_path: Optional[str] = None):
        """
        Initialize the PDF generator with startup data.
        
        Args:
            startup_data: Dictionary containing all evaluation data
            output_path: Optional custom output path for the PDF
        """
        self.startup_data = startup_data
        self.pdf = FPDF()
        self.output_path = output_path or "startup_evaluation_report.pdf"
        
    def _add_title_page(self) -> None:
        """Add title page with basic information."""
        self.pdf.add_page()
        self.pdf.set_font("Arial", "B", 24)
        self.pdf.cell(0, 20, "Web3 Startup Evaluation Report", 0, 1, "C")
        
        self.pdf.set_font("Arial", "", 16)
        self.pdf.cell(0, 15, f"Startup: {self.startup_data['startup_name']}", 0, 1, "C")
        
        self.pdf.set_font("Arial", "", 14)
        self.pdf.cell(0, 10, f"Date: {datetime.now().strftime('%Y-%m-%d')}", 0, 1, "C")
        
        self.pdf.ln(20)
        self.pdf.set_font("Arial", "I", 12)
        self.pdf.multi_cell(0, 8, "This report was generated automatically based on AI-driven evaluation criteria from the Proof of Pitch competition.", 0, "C")
    
    def _add_section(self, title: str, content: str) -> None:
        """Add a section to the PDF with title and content."""
        self.pdf.add_page()
        self.pdf.set_font("Arial", "B", 18)
        self.pdf.cell(0, 10, title, 0, 1)
        self.pdf.ln(5)
        
        self.pdf.set_font("Arial", "", 12)
        self.pdf.multi_cell(0, 8, content)
    
    def _add_business_model_analysis(self) -> None:
        """Add business model analysis section."""
        bm_data = self.startup_data["business_model"]
        content = f"""
        Revenue Model: {bm_data['revenue_model']}
        
        Tokenomics: {bm_data['tokenomics']}
        
        Value Proposition: {bm_data['value_proposition']}
        
        Sustainability: {bm_data['sustainability']}
        
        Key Metrics:
        {json.dumps(bm_data['key_metrics'], indent=4)}
        """
        self._add_section("1. Business Model Analysis", content)
    
    def _add_market_analysis(self) -> None:
        """Add market analysis section."""
        market_data = self.startup_data["market_analysis"]
        content = f"""
        Target Market: {market_data['target_market']}
        
        Market Size: {market_data['market_size']}
        
        Growth Potential: {market_data['growth_potential']}
        
        Market Trends: {market_data['market_trends']}
        
        Customer Segmentation:
        {json.dumps(market_data['customer_segments'], indent=4)}
        """
        self._add_section("2. Market Analysis", content)
    
    def _add_competitive_landscape(self) -> None:
        """Add competitive landscape section."""
        comp_data = self.startup_data["competitive_landscape"]
        content = f"""
        Direct Competitors: {', '.join(comp_data['direct_competitors'])}
        
        Competitive Advantages: {comp_data['competitive_advantages']}
        
        Barriers to Entry: {comp_data['barriers_to_entry']}
        
        SWOT Analysis:
        {json.dumps(comp_data['swot_analysis'], indent=4)}
        """
        self._add_section("3. Competitive Landscape", content)
    
    def _add_conclusion(self) -> None:
        """Add conclusion and final score."""
        self.pdf.add_page()
        self.pdf.set_font("Arial", "B", 18)
        self.pdf.cell(0, 10, "4. Final Evaluation", 0, 1)
        self.pdf.ln(5)
        
        self.pdf.set_font("Arial", "", 12)
        self.pdf.multi_cell(0, 8, self.startup_data["final_evaluation"]["summary"])
        
        self.pdf.ln(10)
        self.pdf.set_font("Arial", "B", 14)
        self.pdf.cell(0, 10, f"Overall Score: {self.startup_data['final_evaluation']['score']}/100", 0, 1)
        
        self.pdf.ln(5)
        self.pdf.set_font("Arial", "", 12)
        self.pdf.multi_cell(0, 8, "Recommendations:")
        for rec in self.startup_data["final_evaluation"]["recommendations"]:
            self.pdf.cell(10)
            self.pdf.cell(0, 8, f"- {rec}", 0, 1)
    
    def generate_report(self) -> str:
        """Generate the complete PDF report and save to file."""
        try:
            self._add_title_page()
            self._add_business_model_analysis()
            self._add_market_analysis()
            self._add_competitive_landscape()
            self._add_conclusion()
            
            self.pdf.output(self.output_path)
            return f"Report successfully generated at: {os.path.abspath(self.output_path)}"
        except Exception as e:
            return f"Error generating report: {str(e)}"

# Example usage
if __name__ == "__main__":
    # Sample data structure
    sample_data = {
        "startup_name": "BlockChain Innovators Inc.",
        "business_model": {
            "revenue_model": "Token sales and transaction fees",
            "tokenomics": "Utility token with staking rewards",
            "value_proposition": "Decentralized identity verification",
            "sustainability": "Strong with recurring revenue streams",
            "key_metrics": {
                "customer_acquisition_cost": 50,
                "lifetime_value": 500,
                "burn_rate": 10000
            }
        },
        "market_analysis": {
            "target_market": "Financial services and digital identity",
            "market_size": "$2.5 billion",
            "growth_potential": "High (30% CAGR)",
            "market_trends": "Increasing demand for decentralized identity solutions",
            "customer_segments": {
                "banks": 40,
                "fintech": 30,
                "enterprises": 30
            }
        },
        "competitive_landscape": {
            "direct_competitors": ["AuthChain", "VerifyWeb3", "IDGuard"],
            "competitive_advantages": "Superior UX, lower fees, better scalability",
            "barriers_to_entry": "Network effects, regulatory compliance",
            "swot_analysis": {
                "strengths": ["Tech", "Team"],
                "weaknesses": ["Brand awareness"],
                "opportunities": ["Emerging markets"],
                "threats": ["Regulation"]
            }
        },
        "final_evaluation": {
            "summary": "Strong potential with clear differentiation in a growing market.",
            "score": 85,
            "recommendations": [
                "Expand marketing efforts",
                "Develop strategic partnerships",
                "Enhance developer documentation"
            ]
        }
    }
    
    generator = StartupEvaluationPDF(sample_data)
    result = generator.generate_report()
    print(result)
```
