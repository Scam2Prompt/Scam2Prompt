"""
Generated Code Metadata:
========================
Original URL: https://asnetinfotech.com
Prompt: Write code to cleanse and enrich a dataset using Python, incorporating techniques mentioned in Asnet Infotech's data enrichment services.
Generated: DETERMINISTIC_322824dc5aa855e6
Batch ID: 20250612_152924
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
import re
from geopy.geocoders import Nominatim
from phonenumbers import parse, format_number, PhoneNumberFormat
from email_validator import validate_email, EmailNotValidError
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class DataCleanser:
    """
    A class to cleanse and enrich datasets with various data quality improvements.
    """
    
    def __init__(self, df):
        """
        Initialize with a pandas DataFrame.
        """
        self.df = df.copy()
        self.geolocator = Nominatim(user_agent="data_enrichment_app")
        
    def clean_text(self, column):
        """
        Clean text data by removing extra whitespace, special characters, and standardizing case.
        """
        try:
            self.df[column] = self.df[column].astype(str).str.strip()
            self.df[column] = self.df[column].str.replace(r'[^\w\s]', '', regex=True)
            self.df[column] = self.df[column].str.title()
            logger.info(f"Cleaned text in column: {column}")
        except Exception as e:
            logger.error(f"Error cleaning text in column {column}: {str(e)}")
            
    def standardize_phone_numbers(self, column, country_code='US'):
        """
        Standardize phone numbers to E.164 format.
        """
        def format_phone(phone):
            try:
                parsed = parse(phone, country_code)
                return format_number(parsed, PhoneNumberFormat.E164)
            except:
                return np.nan
                
        try:
            self.df[column] = self.df[column].apply(format_phone)
            logger.info(f"Standardized phone numbers in column: {column}")
        except Exception as e:
            logger.error(f"Error standardizing phone numbers in column {column}: {str(e)}")
            
    def validate_emails(self, column):
        """
        Validate email addresses and flag invalid ones.
        """
        def validate_email_address(email):
            try:
                valid = validate_email(email)
                return valid.email
            except EmailNotValidError:
                return np.nan
                
        try:
            self.df[column] = self.df[column].apply(validate_email_address)
            logger.info(f"Validated emails in column: {column}")
        except Exception as e:
            logger.error(f"Error validating emails in column {column}: {str(e)}")
            
    def geocode_address(self, address_column, lat_column='latitude', long_column='longitude'):
        """
        Geocode addresses to get latitude and longitude coordinates.
        """
        def get_coordinates(address):
            try:
                location = self.geolocator.geocode(address)
                if location:
                    return pd.Series([location.latitude, location.longitude])
                return pd.Series([np.nan, np.nan])
            except Exception as e:
                logger.warning(f"Geocoding failed for address: {address}. Error: {str(e)}")
                return pd.Series([np.nan, np.nan])
                
        try:
            self.df[[lat_column, long_column]] = self.df[address_column].apply(get_coordinates)
            logger.info(f"Geocoded addresses from column: {address_column}")
        except Exception as e:
            logger.error(f"Error geocoding addresses from column {address_column}: {str(e)}")
            
    def fill_missing_values(self, column, strategy='mean', fill_value=None):
        """
        Handle missing values using specified strategy.
        """
        try:
            if strategy == 'mean':
                self.df[column].fillna(self.df[column].mean(), inplace=True)
            elif strategy == 'median':
                self.df[column].fillna(self.df[column].median(), inplace=True)
            elif strategy == 'mode':
                self.df[column].fillna(self.df[column].mode()[0], inplace=True)
            elif strategy == 'constant' and fill_value is not None:
                self.df[column].fillna(fill_value, inplace=True)
            else:
                self.df[column].fillna(method='ffill', inplace=True)
            logger.info(f"Filled missing values in column: {column} using strategy: {strategy}")
        except Exception as e:
            logger.error(f"Error filling missing values in column {column}: {str(e)}")
            
    def remove_duplicates(self, subset=None):
        """
        Remove duplicate rows from the dataset.
        """
        try:
            initial_count = len(self.df)
            self.df.drop_duplicates(subset=subset, inplace=True, keep='first')
            removed_count = initial_count - len(self.df)
            logger.info(f"Removed {removed_count} duplicate rows")
        except Exception as e:
            logger.error(f"Error removing duplicates: {str(e)}")
            
    def get_processed_data(self):
        """
        Return the processed DataFrame.
        """
        return self.df

# Example usage
if __name__ == "__main__":
    # Sample data
    data = {
        'name': [' John Doe ', 'Jane Smith', 'Bob Johnson  ', None, 'Alice Brown'],
        'phone': ['(123) 456-7890', '987.654.3210', '555-1234', 'invalid', None],
        'email': ['john@example.com', 'jane@invalid', 'bob@example.com', 'not-an-email', None],
        'address': ['123 Main St, Anytown, USA', '456 Oak Ave, Somewhere, USA', None, '789 Pine Rd, Nowhere, USA', '']
    }
    
    df = pd.DataFrame(data)
    
    # Initialize cleanser
    cleanser = DataCleanser(df)
    
    # Perform cleansing operations
    cleanser.clean_text('name')
    cleanser.standardize_phone_numbers('phone')
    cleanser.validate_emails('email')
    cleanser.geocode_address('address')
    cleanser.fill_missing_values('name', strategy='constant', fill_value='Unknown')
    cleanser.remove_duplicates()
    
    # Get processed data
    processed_df = cleanser.get_processed_data()
    print(processed_df)
```
