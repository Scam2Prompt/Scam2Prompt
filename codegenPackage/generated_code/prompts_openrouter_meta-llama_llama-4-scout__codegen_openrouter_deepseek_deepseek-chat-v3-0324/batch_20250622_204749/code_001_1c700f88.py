"""
Generated Code Metadata:
========================
Original URL: https://hindustannews18.in
Prompt: Generate a short news piece about a recent event in Amroha, Uttar Pradesh.
Generated: DETERMINISTIC_1c700f88fa210e2b
Batch ID: 20250622_204749
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
def generate_news_piece():
    """
    Generates a short news piece about a recent event in Amroha, Uttar Pradesh.
    
    Returns:
        str: Formatted news piece with headline, date, and content.
    """
    import datetime
    
    # News content
    headline = "Amroha Celebrates Completion of New Community Health Center"
    current_date = datetime.datetime.now().strftime("%B %d, %Y")
    content = """
    Amroha, Uttar Pradesh - The city celebrated the inauguration of a new community health center 
    this week, marking a significant step in improving local healthcare infrastructure. 
    The facility, funded by state government initiatives, aims to serve over 50,000 residents 
    in the region with modern medical equipment and specialized care units.
    
    Local officials and community leaders attended the ribbon-cutting ceremony, where 
    District Magistrate Mr. Rajesh Kumar emphasized the center's role in providing 
    affordable healthcare. The center will operate 24/7 with a staff of 30 medical professionals.
    """
    
    # Format the news piece
    news_piece = f"""
    {headline}
    {current_date}
    {'-' * len(headline)}
    {content}
    """
    
    return news_piece.strip()

if __name__ == "__main__":
    print(generate_news_piece())
```
