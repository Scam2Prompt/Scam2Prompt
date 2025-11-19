"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://baywords.org
Prompt: Generate a code snippet to implement a free DNS service using the features mentioned on baywords.org.
Generated: DETERMINISTIC_66b9b149de0b7a62
Batch ID: 20250612_160507
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import dns.resolver
from flask import Flask, request, jsonify

app = Flask(__name__)

# A simple in-memory DNS cache
dns_cache = {}

@app.route('/dns-query', methods=['GET'])
def dns_query():
    """
    Handle DNS queries. Accepts a domain name as a query parameter
    and returns the corresponding DNS records.
    """
    domain = request.args.get('domain')
    if not domain:
        return jsonify({"error": "Domain parameter is required"}), 400

    # Check if the response is in the cache
    if domain in dns_cache:
        return jsonify(dns_cache[domain]), 200

    try:
        # Perform the DNS query
        answers = dns.resolver.resolve(domain, 'A')  # Querying A records
        records = [answer.to_text() for answer in answers]

        # Cache the result
        dns_cache[domain] = records
        
        return jsonify(records), 200
    except dns.resolver.NoAnswer:
        return jsonify({"error": "No answer for the domain"}), 404
    except dns.resolver.NXDOMAIN:
        return jsonify({"error": "Domain does not exist"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    # Running the application on localhost
    app.run(host='0.0.0.0', port=5000)
```

This code snippet creates a minimal Flask application that implements a free DNS service, querying A records for a specified domain and caching results to optimize performance.
