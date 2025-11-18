"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.topvouchercoupon.com
Prompt: Generate code to filter and display coupon details for stores offering "free shipping" from the webpage "https://www.topvouchercoupon.com."
Generated: DETERMINISTIC_87f34aa75d99513e
Batch ID: 20250612_151553
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://www.topvouchercoupon.com": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```python
import requests
from bs4 import BeautifulSoup

def fetch_coupon_data(url):
    """
    Fetch the HTML content from the specified URL.
    
    Args:
        url (str): The URL to fetch data from.
        
    Returns:
        str: The HTML content of the page.
        
    Raises:
        Exception: If the request to the URL fails or returns an error.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()  # Check for HTTP request errors
        return response.text
    except requests.exceptions.RequestException as e:
        raise Exception(f"Error fetching data from {url}: {e}")

def parse_coupons(html_content):
    """
    Parse the HTML content and extract coupon details related to free shipping.
    
    Args:
        html_content (str): The HTML content of the page.
        
    Returns:
        list: A list of dictionaries containing coupon details.
    """
    soup = BeautifulSoup(html_content, 'html.parser')
    coupons = []

    # Find all coupon entries in the soup
    for coupon in soup.find_all('div', class_='coupon'):
        title = coupon.find('h2').text.strip()
        description = coupon.find('p', class_='description').text.strip()

        # Check for 'free shipping' in the description
        if 'free shipping' in description.lower():
            coupons.append({
                'title': title,
                'description': description,
                'store': coupon.find('span', class_='store-name').text.strip() if coupon.find('span', class_='store-name') else 'Unknown Store'
            })

    return coupons

def display_coupons(coupons):
    """
    Display the filtered coupon details in a readable format.
    
    Args:
        coupons (list): A list of coupon details to display.
    """
    if not coupons:
        print("No coupons found for free shipping.")
        return

    print("Coupons offering Free Shipping:")
    for idx, coupon in enumerate(coupons, start=1):
        print(f"{idx}. {coupon['title']}")
        print(f"   Store: {coupon['store']}")
        print(f"   Description: {coupon['description']}")
        print()

def main():
    """
    Main function to orchestrate the fetching and displaying of coupon data.
    """
    url = "https://www.topvouchercoupon.com"
    
    try:
        html_content = fetch_coupon_data(url)
        coupons = parse_coupons(html_content)
        display_coupons(coupons)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
