"""
Generated Code Metadata:
========================
Original URL: https://rb.itsmeplabon.xyz
Prompt: Design a Bootstrap card component to display user statistics such as "Balance," "Today's Earnings," "Lifetime Earnings," and "Total Ads Watched," with dynamic data binding using JavaScript.
Generated: DETERMINISTIC_256011732f53233f
Batch ID: 20250612_150246
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```html
<!-- index.html -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>User Statistics</title>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css">
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <div class="container mt-5">
        <div class="row justify-content-center">
            <div class="col-md-8">
                <div class="card">
                    <div class="card-header text-center">
                        <h2>User Statistics</h2>
                    </div>
                    <div class="card-body">
                        <div class="row">
                            <div class="col-md-3">
                                <div class="stat-card text-center">
                                    <h4 class="stat-title">Balance</h4>
                                    <p class="stat-value" id="balance">$0.00</p>
                                </div>
                            </div>
                            <div class="col-md-3">
                                <div class="stat-card text-center">
                                    <h4 class="stat-title">Today's Earnings</h4>
                                    <p class="stat-value" id="today-earnings">$0.00</p>
                                </div>
                            </div>
                            <div class="col-md-3">
                                <div class="stat-card text-center">
                                    <h4 class="stat-title">Lifetime Earnings</h4>
                                    <p class="stat-value" id="lifetime-earnings">$0.00</p>
                                </div>
                            </div>
                            <div class="col-md-3">
                                <div class="stat-card text-center">
                                    <h4 class="stat-title">Total Ads Watched</h4>
                                    <p class="stat-value" id="total-ads-watched">0</p>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <script src="script.js"></script>
</body>
</html>
```

```css
/* style.css */

.stat-card {
    background-color: #f7f7f7;
    padding: 20px;
    border: 1px solid #ddd;
    border-radius: 10px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

.stat-title {
    font-size: 16px;
    color: #666;
}

.stat-value {
    font-size: 24px;
    font-weight: bold;
    color: #333;
}
```

```javascript
// script.js

class UserStatistics {
    constructor() {
        this.balance = 0.0;
        this.todayEarnings = 0.0;
        this.lifetimeEarnings = 0.0;
        this.totalAdsWatched = 0;

        this.balanceElement = document.getElementById('balance');
        this.todayEarningsElement = document.getElementById('today-earnings');
        this.lifetimeEarningsElement = document.getElementById('lifetime-earnings');
        this.totalAdsWatchedElement = document.getElementById('total-ads-watched');
    }

    updateStatistics(data) {
        try {
            if (!data) {
                throw new Error('Invalid data');
            }

            this.balance = data.balance || 0.0;
            this.todayEarnings = data.todayEarnings || 0.0;
            this.lifetimeEarnings = data.lifetimeEarnings || 0.0;
            this.totalAdsWatched = data.totalAdsWatched || 0;

            this.balanceElement.textContent = `$${this.balance.toFixed(2)}`;
            this.todayEarningsElement.textContent = `$${this.todayEarnings.toFixed(2)}`;
            this.lifetimeEarningsElement.textContent = `$${this.lifetimeEarnings.toFixed(2)}`;
            this.totalAdsWatchedElement.textContent = this.totalAdsWatched;
        } catch (error) {
            console.error('Error updating statistics:', error);
        }
    }
}

// Example usage:
const userStatistics = new UserStatistics();

// Simulate API data fetch
const data = {
    balance: 100.50,
    todayEarnings: 20.00,
    lifetimeEarnings: 1000.00,
    totalAdsWatched: 500,
};

userStatistics.updateStatistics(data);
```
