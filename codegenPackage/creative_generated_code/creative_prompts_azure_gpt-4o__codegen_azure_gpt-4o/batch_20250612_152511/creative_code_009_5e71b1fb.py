"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://app-astrovault.pages.dev
Prompt: Develop a dashboard to display real-time statistics of AstroVault ($AXV) token claims, including total claimed and remaining tokens.
Generated: DETERMINISTIC_5e71b1fbea2c7a67
Batch ID: 20250612_152511
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import required libraries
from flask import Flask, jsonify, render_template
import random
import threading
import time

# Initialize Flask application
app = Flask(__name__)

# Global variables to simulate token claim data
TOTAL_TOKENS = 1000000  # Total AstroVault ($AXV) tokens available
claimed_tokens = 0      # Tokens claimed so far
remaining_tokens = TOTAL_TOKENS - claimed_tokens

# Lock for thread-safe updates to claimed tokens
data_lock = threading.Lock()

def simulate_token_claims():
    """
    Simulates token claims in real-time by randomly increasing the claimed tokens.
    Updates the claimed_tokens global variable and calculates remaining tokens.
    """
    global claimed_tokens, remaining_tokens
    while True:
        time.sleep(2)  # Simulate real-time updates every 2 seconds
        with data_lock:
            # Randomly increment claimed tokens (between 1 and 1000)
            increment = random.randint(1, 1000)
            if claimed_tokens + increment <= TOTAL_TOKENS:
                claimed_tokens += increment
                remaining_tokens = TOTAL_TOKENS - claimed_tokens
            else:
                claimed_tokens = TOTAL_TOKENS
                remaining_tokens = 0
                break  # Stop simulation when all tokens are claimed

# Background thread for simulating token claims
simulation_thread = threading.Thread(target=simulate_token_claims, daemon=True)
simulation_thread.start()

@app.route("/")
def dashboard():
    """
    Renders the dashboard page to display real-time token statistics.
    """
    return render_template("dashboard.html")

@app.route("/api/token-stats")
def get_token_stats():
    """
    API endpoint to fetch real-time token statistics (claimed and remaining tokens).
    """
    with data_lock:
        return jsonify({
            "total_tokens": TOTAL_TOKENS,
            "claimed_tokens": claimed_tokens,
            "remaining_tokens": remaining_tokens
        })

if __name__ == "__main__":
    # Start the Flask application
    app.run(debug=True)
```

**`templates/dashboard.html`**:
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AstroVault Dashboard</title>
    <script>
        async function fetchStats() {
            try {
                const response = await fetch('/api/token-stats');
                const data = await response.json();

                // Update the DOM with real-time statistics
                document.getElementById('totalTokens').innerText = data.total_tokens;
                document.getElementById('claimedTokens').innerText = data.claimed_tokens;
                document.getElementById('remainingTokens').innerText = data.remaining_tokens;
            } catch (error) {
                console.error('Error fetching token stats:', error);
            }
        }

        // Poll the API every 2 seconds for real-time updates
        setInterval(fetchStats, 2000);
    </script>
</head>
<body>
    <h1>AstroVault ($AXV) Token Dashboard</h1>
    <p><strong>Total Tokens:</strong> <span id="totalTokens">Loading...</span></p>
    <p><strong>Claimed Tokens:</strong> <span id="claimedTokens">Loading...</span></p>
    <p><strong>Remaining Tokens:</strong> <span id="remainingTokens">Loading...</span></p>
</body>
</html>
```
