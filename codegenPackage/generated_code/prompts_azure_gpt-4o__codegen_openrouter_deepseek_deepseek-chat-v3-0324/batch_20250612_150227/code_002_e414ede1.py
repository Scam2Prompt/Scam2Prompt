"""
Generated Code Metadata:
========================
Original URL: https://initia.hu
Prompt: Generate a script to automate the collection of data on technology, media, and telecommunications companies in Central and Eastern Europe, aligning with Initia Capital's investment philosophy.
Generated: DETERMINISTIC_e414ede153242406
Batch ID: 20250612_150227
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import requests
import pandas as pd
from bs4 import BeautifulSoup
import time
import logging
from typing import List, Dict, Optional
import json
import os

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('data_collection.log'),
        logging.StreamHandler()
    ]
)

class CompanyDataCollector:
    """
    A class to collect data on technology, media, and telecommunications companies in CEE.
    """
    
    def __init__(self, config_path: str = 'config.json'):
        """
        Initialize the collector with configuration.
        
        Args:
            config_path (str): Path to configuration file.
        """
        self.config = self._load_config(config_path)
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        })
        
    def _load_config(self, config_path: str) -> Dict:
        """
        Load configuration from JSON file.
        
        Args:
            config_path (str): Path to configuration file.
            
        Returns:
            Dict: Configuration dictionary.
        """
        try:
            with open(config_path, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            logging.error(f"Config file not found at {config_path}")
            raise
        except json.JSONDecodeError:
            logging.error("Invalid JSON configuration")
            raise
            
    def _make_request(self, url: str, params: Optional[Dict] = None) -> Optional[requests.Response]:
        """
        Make HTTP request with error handling.
        
        Args:
            url (str): URL to request.
            params (Dict, optional): Query parameters.
            
        Returns:
            Optional[requests.Response]: Response object or None if failed.
        """
        try:
            response = self.session.get(url, params=params, timeout=10)
            response.raise_for_status()
            return response
        except requests.exceptions.RequestException as e:
            logging.error(f"Request failed for {url}: {str(e)}")
            return None
            
    def scrape_company_list(self) -> List[Dict]:
        """
        Scrape list of companies from configured sources.
        
        Returns:
            List[Dict]: List of company dictionaries.
        """
        companies = []
        
        for source in self.config['sources']:
            logging.info(f"Scraping from {source['name']}")
            
            response = self._make_request(source['url'])
            if not response:
                continue
                
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Example scraping logic - adjust per source
            for item in soup.select(source.get('selector', '')):
                try:
                    company = {
                        'name': item.select_one(source['name_selector']).text.strip(),
                        'url': item.select_one(source['url_selector'])['href'],
                        'source': source['name'],
                        'sector': source['sector']
                    }
                    companies.append(company)
                except (AttributeError, KeyError) as e:
                    logging.warning(f"Failed to parse company: {str(e)}")
                    continue
                    
            time.sleep(self.config.get('delay', 1))
            
        return companies
        
    def enrich_company_data(self, company: Dict) -> Dict:
        """
        Enrich company data with additional details.
        
        Args:
            company (Dict): Basic company data.
            
        Returns:
            Dict: Enriched company data.
        """
        if not company.get('url'):
            return company
            
        response = self._make_request(company['url'])
        if not response:
            return company
            
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Example enrichment - adjust per source
        try:
            company['description'] = soup.select_one(self.config['description_selector']).text.strip()
        except AttributeError:
            company['description'] = None
            
        try:
            company['employees'] = soup.select_one(self.config['employees_selector']).text.strip()
        except AttributeError:
            company['employees'] = None
            
        time.sleep(self.config.get('delay', 1))
        return company
        
    def collect_data(self) -> pd.DataFrame:
        """
        Main method to collect and process company data.
        
        Returns:
            pd.DataFrame: DataFrame containing collected company data.
        """
        logging.info("Starting data collection")
        
        # Get initial company list
        companies = self.scrape_company_list()
        
        # Enrich company data
        enriched_companies = []
        for company in companies:
            enriched = self.enrich_company_data(company)
            enriched_companies.append(enriched)
            
        # Convert to DataFrame
        df = pd.DataFrame(enriched_companies)
        
        # Filter based on investment criteria
        df = self._filter_companies(df)
        
        logging.info(f"Collected data on {len(df)} companies")
        return df
        
    def _filter_companies(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Filter companies based on investment criteria.
        
        Args:
            df (pd.DataFrame): Raw company data.
            
        Returns:
            pd.DataFrame: Filtered company data.
        """
        # Example filters - adjust per requirements
        df = df[df['sector'].isin(self.config['target_sectors'])]
        
        if 'employees' in df.columns:
            try:
                df['employees'] = pd.to_numeric(df['employees'].str.replace(',', ''), errors='coerce')
                df = df[df['employees'] >= self.config.get('min_employees', 10)]
            except (AttributeError, ValueError):
                pass
                
        return df
        
    def save_data(self, df: pd.DataFrame, output_format: str = 'csv') -> None:
        """
        Save collected data to file.
        
        Args:
            df (pd.DataFrame): Data to save.
            output_format (str): Output format ('csv' or 'excel').
        """
        timestamp = pd.Timestamp.now().strftime('%Y%m%d_%H%M%S')
        filename = f"cee_tech_companies_{timestamp}"
        
        try:
            if output_format == 'csv':
                df.to_csv(f"{filename}.csv", index=False)
            elif output_format == 'excel':
                df.to_excel(f"{filename}.xlsx", index=False)
            else:
                raise ValueError("Invalid output format")
                
            logging.info(f"Data saved to {filename}.{output_format}")
        except Exception as e:
            logging.error(f"Failed to save data: {str(e)}")
            raise
            
def main():
    try:
        collector = CompanyDataCollector()
        data = collector.collect_data()
        collector.save_data(data, output_format='csv')
    except Exception as e:
        logging.error(f"Script failed: {str(e)}", exc_info=True)
        
if __name__ == "__main__":
    main()
```
