"""
Generated Code Metadata:
========================
Original URL: https://millennium-capital.com
Prompt: Generate a code snippet for a web application that allows users to search for available Dot COM domains and suggests creative joint venture ideas based on user input.
Generated: DETERMINISTIC_f3565923aa29da2c
Batch ID: 20250612_163350
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import requests
import whois
from datetime import datetime
import random
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# List of creative business categories for suggestions
BUSINESS_CATEGORIES = [
    "Eco-Friendly Products",
    "Tech Gadgets",
    "Online Education",
    "Health & Wellness",
    "Sustainable Fashion",
    "Digital Marketing Services",
    "Smart Home Solutions",
    "Pet Care Innovations",
    "Virtual Reality Experiences",
    "Food Delivery Services"
]

# List of business models for suggestions
BUSINESS_MODELS = [
    "Subscription Box",
    "Marketplace",
    "SaaS (Software as a Service)",
    "Freemium Model",
    "Affiliate Marketing",
    "Dropshipping",
    "Consulting Services",
    "Online Courses",
    "Mobile App",
    "Content Creation"
]

def check_domain_availability(domain_name):
    """
    Check if a .COM domain is available using WHOIS lookup.
    
    Args:
        domain_name (str): The domain name to check (without TLD)
    
    Returns:
        dict: {'available': bool, 'message': str}
    """
    full_domain = f"{domain_name.lower()}.com"
    
    try:
        # Attempt WHOIS lookup
        domain_info = whois.query(full_domain)
        
        if domain_info is None:
            return {'available': True, 'message': f'{full_domain} is available!'}
        else:
            expiry_date = domain_info.expiration_date
            days_remaining = (expiry_date - datetime.now()).days
            return {
                'available': False,
                'message': f'{full_domain} is taken (expires in {days_remaining} days)'
            }
    except Exception as e:
        return {'available': False, 'message': f'Error checking domain: {str(e)}'}

def generate_business_ideas(keywords):
    """
    Generate creative business ideas based on keywords.
    
    Args:
        keywords (str): Comma-separated keywords to base suggestions on
    
    Returns:
        list: List of suggested business ideas
    """
    keyword_list = [k.strip().lower() for k in keywords.split(',') if k.strip()]
    
    suggestions = []
    for _ in range(3):  # Generate 3 suggestions
        category = random.choice(BUSINESS_CATEGORIES)
        model = random.choice(BUSINESS_MODELS)
        
        if keyword_list:
            base = random.choice(keyword_list)
            suggestion = f"{base.capitalize()} {category} {model}"
        else:
            suggestion = f"{category} {model}"
        
        suggestions.append(suggestion)
    
    return suggestions

@app.route('/')
def home():
    """Render the homepage with search form."""
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    """Handle domain search and business idea generation."""
    data = request.get_json()
    
    if not data or 'domain' not in data:
        return jsonify({'error': 'Missing domain parameter'}), 400
    
    domain = data['domain'].strip()
    if not domain:
        return jsonify({'error': 'Domain cannot be empty'}), 400
    
    # Check domain availability
    domain_result = check_domain_availability(domain)
    
    # Generate business ideas if keywords provided
    ideas = []
    keywords = data.get('keywords', '').strip()
    if keywords:
        ideas = generate_business_ideas(keywords)
    
    return jsonify({
        'domain_result': domain_result,
        'business_ideas': ideas
    })

@app.errorhandler(404)
def not_found(e):
    """Handle 404 errors."""
    return jsonify({'error': 'Resource not found'}), 404

@app.errorhandler(500)
def server_error(e):
    """Handle 500 errors."""
    return jsonify({'error': 'Internal server error'}), 500

if __name__ == '__main__':
    app.run(debug=False)  # Set debug=False in production
```

```html
<!-- templates/index.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Domain & Business Idea Generator</title>
    <style>
        body { font-family: Arial, sans-serif; max-width: 800px; margin: 0 auto; padding: 20px; }
        .form-group { margin-bottom: 15px; }
        label { display: block; margin-bottom: 5px; font-weight: bold; }
        input, textarea { width: 100%; padding: 8px; box-sizing: border-box; }
        button { padding: 10px 15px; background: #4CAF50; color: white; border: none; cursor: pointer; }
        #results { margin-top: 20px; padding: 15px; border: 1px solid #ddd; border-radius: 4px; }
        .error { color: red; }
        .idea { margin-bottom: 10px; padding: 10px; background: #f9f9f9; }
    </style>
</head>
<body>
    <h1>Domain & Business Idea Generator</h1>
    
    <div class="form-group">
        <label for="domain">Domain Name (without .com):</label>
        <input type="text" id="domain" placeholder="myawesomebusiness" required>
    </div>
    
    <div class="form-group">
        <label for="keywords">Keywords (comma separated, optional):</label>
        <textarea id="keywords" placeholder="tech, garden, fitness"></textarea>
    </div>
    
    <button id="search-btn">Search Domain & Get Ideas</button>
    
    <div id="results"></div>
    
    <script>
        document.getElementById('search-btn').addEventListener('click', async () => {
            const domain = document.getElementById('domain').value.trim();
            const keywords = document.getElementById('keywords').value.trim();
            
            if (!domain) {
                showError('Please enter a domain name');
                return;
            }
            
            try {
                const response = await fetch('/search', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify({
                        domain: domain,
                        keywords: keywords
                    })
                });
                
                const data = await response.json();
                
                if (!response.ok) {
                    showError(data.error || 'An error occurred');
                    return;
                }
                
                displayResults(data);
            } catch (error) {
                showError('Failed to connect to server');
            }
        });
        
        function showError(message) {
            const resultsDiv = document.getElementById('results');
            resultsDiv.innerHTML = `<div class="error">${message}</div>`;
        }
        
        function displayResults(data) {
            const { domain_result, business_ideas } = data;
            const resultsDiv = document.getElementById('results');
            
            let html = `<div>
                <h3>Domain Status:</h3>
                <p>${domain_result.message}</p>
            </div>`;
            
            if (business_ideas && business_ideas.length > 0) {
                html += `<div>
                    <h3>Business Ideas:</h3>
                    ${business_ideas.map(idea => `<div class="idea">${idea}</div>`).join('')}
                </div>`;
            }
            
            resultsDiv.innerHTML = html;
        }
    </script>
</body>
</html>
```
