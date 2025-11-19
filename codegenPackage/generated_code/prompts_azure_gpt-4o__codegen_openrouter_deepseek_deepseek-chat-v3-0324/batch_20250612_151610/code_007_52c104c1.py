"""
Generated Code Metadata:
========================
Original URL: https://oxicap.com
Prompt: Write code to generate a datasheet summary for Niobium Oxide capacitors, including voltage ratings up to 10Vr, high capacitance values, and AEC-Q200 compliance, as described on the KYOCERA AVX website.
Generated: DETERMINISTIC_52c104c1bc53b8a0
Batch ID: 20250612_151610
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://www.kyocera-avx.com": {
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
from bs4 import BeautifulSoup
import pandas as pd
from typing import List, Dict, Optional

class NiobiumOxideCapacitorScraper:
    """
    A web scraper to extract Niobium Oxide capacitor data from KYOCERA AVX website.
    Generates a datasheet summary including voltage ratings, capacitance, and AEC-Q200 compliance.
    """
    
    def __init__(self, base_url: str = "https://www.kyocera-avx.com"):
        self.base_url = base_url
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        })
    
    def _get_page_content(self, url: str) -> Optional[str]:
        """Fetch page content with error handling."""
        try:
            response = self.session.get(url, timeout=10)
            response.raise_for_status()
            return response.text
        except requests.exceptions.RequestException as e:
            print(f"Error fetching {url}: {e}")
            return None
    
    def _parse_capacitor_data(self, html_content: str) -> List[Dict[str, str]]:
        """Parse HTML content to extract capacitor data."""
        soup = BeautifulSoup(html_content, 'html.parser')
        capacitors = []
        
        # Find all product tables - adjust selector based on actual website structure
        product_tables = soup.select('table.product-table')
        
        for table in product_tables:
            rows = table.select('tr')
            for row in rows[1:]:  # Skip header row
                cols = row.select('td')
                if len(cols) >= 5:  # Adjust based on actual columns
                    capacitor = {
                        'part_number': cols[0].get_text(strip=True),
                        'capacitance': cols[1].get_text(strip=True),
                        'voltage': cols[2].get_text(strip=True),
                        'tolerance': cols[3].get_text(strip=True),
                        'aec_q200': 'Yes' if 'AEC-Q200' in row.get_text() else 'No'
                    }
                    capacitors.append(capacitor)
        return capacitors
    
    def filter_capacitors(self, capacitors: List[Dict[str, str]], max_voltage: float = 10.0) -> List[Dict[str, str]]:
        """Filter capacitors based on voltage rating and other criteria."""
        filtered = []
        for cap in capacitors:
            try:
                voltage = float(cap['voltage'].replace('V', '').strip())
                if voltage <= max_voltage:
                    filtered.append(cap)
            except (ValueError, AttributeError):
                continue
        return filtered
    
    def generate_summary(self, capacitors: List[Dict[str, str]]) -> pd.DataFrame:
        """Generate a pandas DataFrame summary of the capacitor data."""
        df = pd.DataFrame(capacitors)
        if not df.empty:
            df = df.sort_values(by=['voltage', 'capacitance'])
        return df
    
    def scrape_niobium_oxide_capacitors(self) -> pd.DataFrame:
        """Main method to scrape and return capacitor data."""
        # This URL should be replaced with the actual KYOCERA AVX Niobium Oxide capacitors page
        niobium_url = f"{self.base_url}/products/capacitors/niobium-oxide/"
        content = self._get_page_content(niobium_url)
        
        if not content:
            return pd.DataFrame()
        
        all_caps = self._parse_capacitor_data(content)
        filtered_caps = self.filter_capacitors(all_caps)
        summary_df = self.generate_summary(filtered_caps)
        
        return summary_df

def save_to_excel(df: pd.DataFrame, filename: str = "niobium_oxide_capacitors.xlsx") -> None:
    """Save DataFrame to Excel file with formatting."""
    if df.empty:
        print("No data to save.")
        return
    
    try:
        writer = pd.ExcelWriter(filename, engine='xlsxwriter')
        df.to_excel(writer, sheet_name='Niobium Oxide Capacitors', index=False)
        
        # Auto-adjust column widths
        workbook = writer.book
        worksheet = writer.sheets['Niobium Oxide Capacitors']
        
        for idx, col in enumerate(df.columns):
            max_len = max(df[col].astype(str).map(len).max(), len(col)) + 2
            worksheet.set_column(idx, idx, max_len)
        
        writer.close()
        print(f"Data saved to {filename}")
    except Exception as e:
        print(f"Error saving to Excel: {e}")

def main():
    """Main execution function."""
    scraper = NiobiumOxideCapacitorScraper()
    capacitor_data = scraper.scrape_niobium_oxide_capacitors()
    
    if not capacitor_data.empty:
        print("Niobium Oxide Capacitor Summary:")
        print(capacitor_data.head())
        save_to_excel(capacitor_data)
    else:
        print("No capacitor data found.")

if __name__ == "__main__":
    main()
```
