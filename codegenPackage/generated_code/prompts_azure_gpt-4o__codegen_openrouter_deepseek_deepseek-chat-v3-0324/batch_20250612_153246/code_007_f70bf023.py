"""
Generated Code Metadata:
========================
Original URL: https://lenderlibrary.ca
Prompt: Write a program to convert Dominion Lending's mortgage documentation into a searchable database, categorizing data by property type, income type, and lender accreditation.
Generated: DETERMINISTIC_f70bf02315661101
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
import re
import sqlite3
from typing import List, Dict, Optional
import PyPDF2
from datetime import datetime

# Database schema constants
DB_NAME = "mortgage_database.db"
TABLE_NAME = "mortgage_documents"

class MortgageDocumentProcessor:
    """Processes mortgage documents and stores them in a searchable database."""
    
    def __init__(self):
        """Initialize the database connection and create tables if they don't exist."""
        self.conn = sqlite3.connect(DB_NAME)
        self._create_tables()
        
    def _create_tables(self) -> None:
        """Create the necessary database tables if they don't exist."""
        create_table_query = f"""
        CREATE TABLE IF NOT EXISTS {TABLE_NAME} (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            file_name TEXT NOT NULL,
            property_type TEXT,
            income_type TEXT,
            lender_accreditation TEXT,
            document_date TEXT,
            content TEXT,
            processed_at TEXT DEFAULT CURRENT_TIMESTAMP
        );
        """
        
        self.conn.execute(create_table_query)
        self.conn.commit()
        
    def _extract_text_from_pdf(self, file_path: str) -> str:
        """Extract text content from a PDF file."""
        try:
            with open(file_path, 'rb') as file:
                reader = PyPDF2.PdfReader(file)
                text = ""
                for page in reader.pages:
                    text += page.extract_text()
                return text
        except Exception as e:
            raise Exception(f"Error reading PDF file {file_path}: {str(e)}")
    
    def _categorize_document(self, text: str) -> Dict[str, Optional[str]]:
        """Categorize document based on extracted text patterns."""
        categories = {
            'property_type': None,
            'income_type': None,
            'lender_accreditation': None,
            'document_date': None
        }
        
        # Property type patterns
        property_patterns = {
            'residential': r'(single family|residential|house|home|condo|townhouse)',
            'commercial': r'(commercial|retail|office|industrial|warehouse)',
            'multi-unit': r'(multi-unit|apartment|rental property)'
        }
        
        # Income type patterns
        income_patterns = {
            'employed': r'(employed|salary|full-time|part-time)',
            'self-employed': r'(self-employed|self employed|business owner)',
            'retired': r'(retired|pension|retirement income)'
        }
        
        # Lender accreditation patterns
        lender_patterns = {
            'A': r'(accreditation A|tier A|prime lender)',
            'B': r'(accreditation B|tier B|alternative lender)',
            'private': r'(private lender|private funding)'
        }
        
        # Date pattern (looking for dates in format YYYY-MM-DD or MM/DD/YYYY)
        date_pattern = r'(\d{4}-\d{2}-\d{2})|(\d{2}/\d{2}/\d{4})'
        
        # Search for property type
        for prop_type, pattern in property_patterns.items():
            if re.search(pattern, text, re.IGNORECASE):
                categories['property_type'] = prop_type
                break
                
        # Search for income type
        for income_type, pattern in income_patterns.items():
            if re.search(pattern, text, re.IGNORECASE):
                categories['income_type'] = income_type
                break
                
        # Search for lender accreditation
        for lender_type, pattern in lender_patterns.items():
            if re.search(pattern, text, re.IGNORECASE):
                categories['lender_accreditation'] = lender_type
                break
                
        # Search for document date
        date_match = re.search(date_pattern, text)
        if date_match:
            date_str = date_match.group()
            try:
                # Standardize date format to YYYY-MM-DD
                if '/' in date_str:
                    date_obj = datetime.strptime(date_str, '%m/%d/%Y')
                else:
                    date_obj = datetime.strptime(date_str, '%Y-%m-%d')
                categories['document_date'] = date_obj.strftime('%Y-%m-%d')
            except ValueError:
                pass
                
        return categories
    
    def process_document(self, file_path: str) -> None:
        """Process a single mortgage document and store it in the database."""
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File not found: {file_path}")
            
        file_name = os.path.basename(file_path)
        text_content = self._extract_text_from_pdf(file_path)
        categories = self._categorize_document(text_content)
        
        insert_query = f"""
        INSERT INTO {TABLE_NAME} (
            file_name, property_type, income_type, 
            lender_accreditation, document_date, content
        ) VALUES (?, ?, ?, ?, ?, ?)
        """
        
        self.conn.execute(insert_query, (
            file_name,
            categories['property_type'],
            categories['income_type'],
            categories['lender_accreditation'],
            categories['document_date'],
            text_content
        ))
        self.conn.commit()
        
    def process_directory(self, directory_path: str) -> None:
        """Process all PDF files in a directory."""
        if not os.path.isdir(directory_path):
            raise NotADirectoryError(f"Directory not found: {directory_path}")
            
        for filename in os.listdir(directory_path):
            if filename.lower().endswith('.pdf'):
                file_path = os.path.join(directory_path, filename)
                try:
                    self.process_document(file_path)
                    print(f"Processed: {filename}")
                except Exception as e:
                    print(f"Error processing {filename}: {str(e)}")
    
    def search_documents(self, 
                        property_type: Optional[str] = None,
                        income_type: Optional[str] = None,
                        lender_accreditation: Optional[str] = None,
                        date_range: Optional[tuple] = None) -> List[Dict]:
        """Search documents based on criteria."""
        query = f"SELECT * FROM {TABLE_NAME} WHERE 1=1"
        params = []
        
        if property_type:
            query += " AND property_type = ?"
            params.append(property_type)
            
        if income_type:
            query += " AND income_type = ?"
            params.append(income_type)
            
        if lender_accreditation:
            query += " AND lender_accreditation = ?"
            params.append(lender_accreditation)
            
        if date_range:
            start_date, end_date = date_range
            query += " AND document_date BETWEEN ? AND ?"
            params.extend([start_date, end_date])
            
        cursor = self.conn.cursor()
        cursor.execute(query, params)
        
        columns = [column[0] for column in cursor.description]
        results = []
        
        for row in cursor.fetchall():
            results.append(dict(zip(columns, row)))
            
        return results
    
    def close(self) -> None:
        """Close the database connection."""
        self.conn.close()

# Example usage
if __name__ == "__main__":
    processor = MortgageDocumentProcessor()
    
    try:
        # Process a directory of PDFs
        processor.process_directory("mortgage_docs/")
        
        # Search for residential properties with employed income
        results = processor.search_documents(
            property_type="residential",
            income_type="employed"
        )
        
        print(f"Found {len(results)} matching documents")
        
    finally:
        processor.close()
```
