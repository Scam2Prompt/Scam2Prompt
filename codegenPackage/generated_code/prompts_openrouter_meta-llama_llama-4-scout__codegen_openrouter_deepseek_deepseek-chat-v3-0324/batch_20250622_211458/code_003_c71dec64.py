"""
Generated Code Metadata:
========================
Original URL: https://vine-pool.web.app
Prompt: How do I choose between client-side and server-side redirects for my web application, and what are the implications for SEO and user experience?
Generated: DETERMINISTIC_c71dec64981c5140
Batch ID: 20250622_211458
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# server_side_redirect.py
from flask import Flask, redirect, request, abort

app = Flask(__name__)

# Server-side redirect example (301 Permanent Redirect)
@app.route('/old-url')
def old_url():
    # Permanent redirect (301) - good for SEO when URL structure changes
    return redirect('/new-url', code=301)

# Server-side redirect example (302 Temporary Redirect)
@app.route('/temporary-redirect')
def temporary_redirect():
    # Temporary redirect (302) - use when content might return to original URL
    return redirect('/temporary-location', code=302)

if __name__ == '__main__':
    app.run(debug=True)
```

```javascript
// client_side_redirect.js
// Client-side redirect examples (using JavaScript)

// Meta refresh (not recommended for SEO)
function metaRefreshRedirect() {
    // This should be in HTML: <meta http-equiv="refresh" content="0; url=/new-url">
    console.log("Meta refresh would redirect here");
}

// JavaScript redirect (immediate)
function jsImmediateRedirect() {
    // 302-like behavior (no status code)
    window.location.href = "/new-url";
}

// JavaScript redirect with delay
function jsDelayedRedirect() {
    // Useful for showing "Redirecting..." messages
    setTimeout(() => {
        window.location.href = "/new-url";
    }, 3000);
}

// History API for SPA navigation (no full page reload)
function spaRedirect() {
    // Good for single-page applications
    history.pushState({}, "", "/new-url");
    // You would also need to update the view accordingly
}

// Handle redirect based on conditions
function conditionalRedirect() {
    if (/* some condition */ true) {
        window.location.replace("/new-url"); // replace doesn't keep original in history
    }
}
```

```python
# seo_implications.py
import requests
from bs4 import BeautifulSoup

def check_redirect_seo(url):
    """
    Check how a URL handles redirects for SEO analysis.
    Returns redirect type and final destination.
    """
    try:
        response = requests.get(url, allow_redirects=False)
        
        if 300 <= response.status_code < 400:
            redirect_type = 'Server-side'
            location = response.headers.get('Location', '')
            return {
                'type': redirect_type,
                'status_code': response.status_code,
                'destination': location,
                'message': '301 is SEO-friendly, 302 may not pass full link equity'
            }
        
        # Check for client-side redirects
        response = requests.get(url, allow_redirects=True)
        soup = BeautifulSoup(response.text, 'html.parser')
        meta_refresh = soup.find('meta', attrs={'http-equiv': 'refresh'})
        
        if meta_refresh:
            content = meta_refresh.get('content', '')
            if 'url=' in content:
                return {
                    'type': 'Client-side (Meta Refresh)',
                    'status_code': None,
                    'destination': content.split('url=')[1],
                    'message': 'Not SEO-friendly, search engines may not follow'
                }
        
        return {
            'type': 'No redirect',
            'status_code': response.status_code,
            'destination': url,
            'message': 'Direct access'
        }
        
    except requests.RequestException as e:
        return {
            'error': str(e),
            'message': 'Failed to analyze redirect'
        }
```

```python
# best_practices.py
def choose_redirect_method(scenario):
    """
    Returns recommended redirect approach based on scenario.
    """
    recommendations = {
        'permanent_url_change': {
            'recommendation': 'Server-side 301 redirect',
            'reason': 'Preserves SEO value and provides clear signal to search engines'
        },
        'temporary_outage': {
            'recommendation': 'Server-side 302 redirect',
            'reason': 'Indicates temporary change without SEO penalty'
        },
        'single_page_app': {
            'recommendation': 'Client-side routing (History API)',
            'reason': 'Provides smooth UX without full page reloads'
        },
        'legacy_browser_support': {
            'recommendation': 'Server-side redirect',
            'reason': 'Works consistently across all browsers'
        },
        'conditional_redirect': {
            'recommendation': 'Combination of server-side check with possible client-side redirect',
            'reason': 'Allows for dynamic routing decisions'
        }
    }
    
    return recommendations.get(scenario, {
        'recommendation': 'Server-side 301 redirect',
        'reason': 'Default safest choice for most scenarios'
    })
```
