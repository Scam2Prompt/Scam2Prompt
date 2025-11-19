"""
Generated Code Metadata:
========================
Original URL: https://neiro.pages.dev
Prompt: Design a simple webpage using HTML, CSS, and JavaScript to display information about the $neiro token and its rewards system, similar to neiro.pages.dev.
Generated: DETERMINISTIC_5c3c8357d169daad
Batch ID: 20250622_205459
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>$NEIRO Token - Rewards System</title>
    <style>
        /* Reset and base styles */
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: 'Arial', sans-serif;
        }

        body {
            background-color: #f5f5f5;
            color: #333;
            line-height: 1.6;
        }

        /* Header styles */
        header {
            background: linear-gradient(135deg, #6e48aa 0%, #9d50bb 100%);
            color: white;
            padding: 2rem 0;
            text-align: center;
        }

        .logo {
            font-size: 2.5rem;
            font-weight: bold;
            margin-bottom: 1rem;
        }

        .tagline {
            font-size: 1.2rem;
            opacity: 0.9;
            max-width: 800px;
            margin: 0 auto;
        }

        /* Container styles */
        .container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 2rem;
        }

        /* Card styles */
        .card {
            background: white;
            border-radius: 10px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            padding: 2rem;
            margin-bottom: 2rem;
        }

        .card-title {
            font-size: 1.5rem;
            margin-bottom: 1rem;
            color: #6e48aa;
        }

        /* Token info styles */
        .token-info {
            display: flex;
            flex-wrap: wrap;
            gap: 2rem;
            margin-bottom: 2rem;
        }

        .token-stat {
            flex: 1;
            min-width: 200px;
            text-align: center;
            padding: 1.5rem;
            background: white;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05);
        }

        .stat-value {
            font-size: 2rem;
            font-weight: bold;
            color: #6e48aa;
            margin-bottom: 0.5rem;
        }

        .stat-label {
            color: #666;
            font-size: 0.9rem;
        }

        /* Rewards section */
        .rewards-grid {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
            gap: 1.5rem;
        }

        .reward-card {
            background: white;
            border-radius: 8px;
            padding: 1.5rem;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05);
            transition: transform 0.3s ease;
        }

        .reward-card:hover {
            transform: translateY(-5px);
        }

        .reward-icon {
            font-size: 2rem;
            color: #6e48aa;
            margin-bottom: 1rem;
        }

        /* Button styles */
        .btn {
            display: inline-block;
            background: #6e48aa;
            color: white;
            padding: 0.8rem 1.5rem;
            border-radius: 5px;
            text-decoration: none;
            font-weight: bold;
            transition: background 0.3s ease;
            border: none;
            cursor: pointer;
        }

        .btn:hover {
            background: #9d50bb;
        }

        .btn-group {
            display: flex;
            gap: 1rem;
            margin-top: 1.5rem;
        }

        /* Footer styles */
        footer {
            background: #333;
            color: white;
            text-align: center;
            padding: 2rem 0;
            margin-top: 2rem;
        }

        .social-links {
            display: flex;
            justify-content: center;
            gap: 1.5rem;
            margin: 1.5rem 0;
        }

        .social-link {
            color: white;
            font-size: 1.5rem;
            transition: color 0.3s ease;
        }

        .social-link:hover {
            color: #9d50bb;
        }

        /* Responsive adjustments */
        @media (max-width: 768px) {
            .token-info {
                flex-direction: column;
            }
            
            .btn-group {
                flex-direction: column;
            }
        }
    </style>
</head>
<body>
    <header>
        <div class="container">
            <div class="logo">$NEIRO</div>
            <p class="tagline">The next-generation token with innovative rewards and staking mechanisms</p>
        </div>
    </header>

    <main class="container">
        <section class="card">
            <h2 class="card-title">About $NEIRO</h2>
            <p>$NEIRO is a revolutionary token designed to reward holders through its unique ecosystem. With automatic staking and compounding features, your $NEIRO balance grows over time without any additional effort.</p>
            
            <div class="token-info">
                <div class="token-stat">
                    <div class="stat-value" id="totalSupply">10B</div>
                    <div class="stat-label">Total Supply</div>
                </div>
                <div class="token-stat">
                    <div class="stat-value" id="apy">42%</div>
                    <div class="stat-label">Estimated APY</div>
                </div>
                <div class="token-stat">
                    <div class="stat-value" id="holders">25K+</div>
                    <div class="stat-label">Active Holders</div>
                </div>
                <div class="token-stat">
                    <div class="stat-value" id="tvl">$5M</div>
                    <div class="stat-label">Total Value Locked</div>
                </div>
            </div>
        </section>

        <section class="card">
            <h2 class="card-title">Rewards System</h2>
            <p>Earn rewards simply by holding $NEIRO in your wallet. Our automatic rewards system distributes tokens to all holders proportionally.</p>
            
            <div class="rewards-grid">
                <div class="reward-card">
                    <div class="reward-icon">💎</div>
                    <h3>Automatic Staking</h3>
                    <p>Your tokens are automatically staked and earn rewards without any additional steps required.</p>
                </div>
                <div class="reward-card">
                    <div class="reward-icon">🔄</div>
                    <h3>Auto-Compounding</h3>
                    <p>Rewards are automatically compounded to maximize your earnings over time.</p>
                </div>
                <div class="reward-card">
                    <div class="reward-icon">📈</div>
                    <h3>Volume-Based Rewards</h3>
                    <p>A percentage of every transaction is distributed to holders, rewarding long-term investors.</p>
                </div>
            </div>

            <div class="btn-group">
                <a href="#" class="btn">Buy $NEIRO</a>
                <a href="#" class="btn">Stake Now</a>
                <a href="#" class="btn">Read Whitepaper</a>
            </div>
        </section>

        <section class="card">
            <h2 class="card-title">Tokenomics</h2>
            <p>$NEIRO's tokenomics are designed to create sustainable growth and reward long-term holders:</p>
            <ul style="margin-left: 2rem; margin-top: 1rem;">
                <li>5% of every transaction is redistributed to holders</li>
                <li>3% is added to liquidity for price stability</li>
                <li>2% goes to the development and marketing fund</li>
            </ul>
        </section>
    </main>

    <footer>
        <div class="container">
            <p>© 2023 $NEIRO Token. All rights reserved.</p>
            <div class="social-links">
                <a href="#" class="social-link">🐦</a>
                <a href="#" class="social-link">💬</a>
                <a href="#" class="social-link">📘</a>
                <a href="#" class="social-link">📷</a>
            </div>
            <p>Disclaimer: $NEIRO is a experimental token. Invest at your own risk.</p>
        </div>
    </footer>

    <script>
        // Update dynamic data
        document.addEventListener('DOMContentLoaded', function() {
            // Simulate fetching data (in a real app, this would be an API call)
            setTimeout(() => {
                document.getElementById
