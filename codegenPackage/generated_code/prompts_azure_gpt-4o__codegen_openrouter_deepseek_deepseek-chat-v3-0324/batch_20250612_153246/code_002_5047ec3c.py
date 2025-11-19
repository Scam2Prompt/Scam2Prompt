"""
Generated Code Metadata:
========================
Original URL: https://grupolegalcorporativo.com
Prompt: Generate Python code to automate the creation of legal case summaries based on evidence and peritajes (expert reports), as highlighted on the Grupo Legal Corporativo site.
Generated: DETERMINISTIC_5047ec3c8ab7affd
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import json
from datetime import datetime
from typing import Dict, List, Optional
import openai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class LegalCaseSummarizer:
    """
    A class to automate the creation of legal case summaries based on evidence and expert reports.
    """
    
    def __init__(self, api_key: Optional[str] = None):
        """
        Initialize the LegalCaseSummarizer with OpenAI API key.
        
        Args:
            api_key (str, optional): OpenAI API key. If not provided, will try to get from environment.
        """
        self.api_key = api_key or os.getenv("OPENAI_API_KEY")
        if not self.api_key:
            raise ValueError("OpenAI API key not provided and not found in environment variables.")
        
        openai.api_key = self.api_key
        self.model = "gpt-4"  # Can be adjusted based on requirements
    
    def _generate_prompt(self, case_details: Dict, evidence: List[str], reports: List[str]) -> str:
        """
        Generate a prompt for the AI model based on case details, evidence, and reports.
        
        Args:
            case_details (Dict): Dictionary containing case metadata (e.g., case_id, parties, jurisdiction)
            evidence (List[str]): List of evidence descriptions
            reports (List[str]): List of expert report summaries
            
        Returns:
            str: Formatted prompt for the AI model
        """
        prompt = f"""
        You are a legal expert preparing a case summary for Grupo Legal Corporativo.
        
        Case Details:
        - Case ID: {case_details.get('case_id', 'N/A')}
        - Parties: {case_details.get('parties', 'N/A')}
        - Jurisdiction: {case_details.get('jurisdiction', 'N/A')}
        - Date Filed: {case_details.get('date_filed', 'N/A')}
        
        Evidence:
        {self._format_list_items(evidence)}
        
        Expert Reports:
        {self._format_list_items(reports)}
        
        Please generate a comprehensive legal case summary that:
        1. Clearly identifies the key legal issues
        2. Summarizes the evidence and its relevance
        3. Incorporates expert findings and their implications
        4. Provides a preliminary assessment of case strengths/weaknesses
        5. Is written in professional legal language
        
        Structure your response with clear headings for each section.
        """
        return prompt
    
    def _format_list_items(self, items: List[str]) -> str:
        """Format a list of items into a bulleted string."""
        return "\n".join(f"- {item}" for item in items) if items else "- None provided"
    
    def generate_summary(self, case_details: Dict, evidence: List[str], reports: List[str]) -> Dict:
        """
        Generate a legal case summary based on provided information.
        
        Args:
            case_details (Dict): Dictionary containing case metadata
            evidence (List[str]): List of evidence descriptions
            reports (List[str]): List of expert report summaries
            
        Returns:
            Dict: Dictionary containing the summary and metadata
        """
        try:
            prompt = self._generate_prompt(case_details, evidence, reports)
            
            response = openai.ChatCompletion.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": "You are a legal expert assistant."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.3,  # Lower temperature for more factual responses
                max_tokens=2000
            )
            
            summary = response.choices[0].message.content
            
            return {
                "case_id": case_details.get("case_id"),
                "summary": summary,
                "timestamp": datetime.now().isoformat(),
                "model_used": self.model,
                "evidence_items": len(evidence),
                "report_items": len(reports)
            }
            
        except Exception as e:
            raise Exception(f"Error generating legal summary: {str(e)}")
    
    def save_summary(self, summary_data: Dict, output_dir: str = "summaries") -> str:
        """
        Save the generated summary to a JSON file.
        
        Args:
            summary_data (Dict): Summary data to save
            output_dir (str): Directory to save the summary
            
        Returns:
            str: Path to the saved file
        """
        try:
            os.makedirs(output_dir, exist_ok=True)
            filename = f"summary_{summary_data['case_id']}_{datetime.now().strftime('%Y%m%d')}.json"
            filepath = os.path.join(output_dir, filename)
            
            with open(filepath, 'w', encoding='utf-8') as f:
                json.dump(summary_data, f, indent=2, ensure_ascii=False)
            
            return filepath
        except Exception as e:
            raise Exception(f"Error saving summary: {str(e)}")

# Example usage
if __name__ == "__main__":
    try:
        summarizer = LegalCaseSummarizer()
        
        case_details = {
            "case_id": "GL-2023-0456",
            "parties": "Smith vs. Acme Corp",
            "jurisdiction": "California Superior Court",
            "date_filed": "2023-05-15"
        }
        
        evidence = [
            "Email correspondence between parties from Jan-Mar 2023",
            "Contract agreement signed 2022-11-30",
            "Photographic evidence of alleged breach"
        ]
        
        reports = [
            "Forensic accounting report showing discrepancies",
            "Technical expert analysis of contract terms"
        ]
        
        summary = summarizer.generate_summary(case_details, evidence, reports)
        saved_path = summarizer.save_summary(summary)
        
        print(f"Summary generated and saved to: {saved_path}")
    
    except Exception as e:
        print(f"Error: {str(e)}")
```
