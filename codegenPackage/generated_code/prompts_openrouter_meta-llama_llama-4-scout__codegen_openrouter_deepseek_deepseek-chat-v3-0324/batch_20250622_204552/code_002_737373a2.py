"""
Generated Code Metadata:
========================
Original URL: https://ui-refactor-wallets-to-not-u.swim-ui.pages.dev
Prompt: Generate HTML code for a cryptocurrency app wallet using Swim UI guidelines.
Generated: DETERMINISTIC_737373a253385796
Batch ID: 20250622_204552
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap": {
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
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CryptoWallet | Swim UI</title>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    <style>
        :root {
            --primary: #3a86ff;
            --primary-light: #e6f0ff;
            --secondary: #8338ec;
            --success: #06d6a0;
            --danger: #ef476f;
            --warning: #ffd166;
            --dark: #1a1a2e;
            --light: #f8f9fa;
            --gray: #6c757d;
            --gray-light: #e9ecef;
        }

        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: 'Inter', sans-serif;
        }

        body {
            background-color: var(--light);
            color: var(--dark);
        }

        .container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 20px;
        }

        .header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 20px 0;
            margin-bottom: 30px;
        }

        .logo {
            font-size: 24px;
            font-weight: 700;
            color: var(--primary);
        }

        .nav {
            display: flex;
            gap: 20px;
        }

        .nav-item {
            padding: 8px 16px;
            border-radius: 8px;
            font-weight: 500;
            cursor: pointer;
            transition: all 0.2s;
        }

        .nav-item:hover {
            background-color: var(--primary-light);
            color: var(--primary);
        }

        .nav-item.active {
            background-color: var(--primary);
            color: white;
        }

        .wallet-card {
            background: white;
            border-radius: 16px;
            padding: 30px;
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.05);
            margin-bottom: 30px;
        }

        .wallet-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 20px;
        }

        .wallet-title {
            font-size: 20px;
            font-weight: 600;
        }

        .wallet-balance {
            font-size: 32px;
            font-weight: 700;
            margin-bottom: 10px;
        }

        .wallet-address {
            color: var(--gray);
            font-size: 14px;
            margin-bottom: 20px;
            word-break: break-all;
        }

        .btn {
            padding: 12px 24px;
            border-radius: 8px;
            font-weight: 600;
            cursor: pointer;
            border: none;
            transition: all 0.2s;
        }

        .btn-primary {
            background-color: var(--primary);
            color: white;
        }

        .btn-primary:hover {
            background-color: #2a75e6;
        }

        .btn-secondary {
            background-color: var(--secondary);
            color: white;
        }

        .btn-secondary:hover {
            background-color: #7229d6;
        }

        .btn-outline {
            background-color: transparent;
            border: 1px solid var(--gray-light);
            color: var(--dark);
        }

        .btn-outline:hover {
            background-color: var(--gray-light);
        }

        .btn-group {
            display: flex;
            gap: 10px;
        }

        .assets-list {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
            gap: 20px;
        }

        .asset-card {
            background: white;
            border-radius: 12px;
            padding: 20px;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.05);
            transition: all 0.2s;
        }

        .asset-card:hover {
            transform: translateY(-2px);
            box-shadow: 0 6px 16px rgba(0, 0, 0, 0.1);
        }

        .asset-header {
            display: flex;
            align-items: center;
            margin-bottom: 15px;
        }

        .asset-icon {
            width: 40px;
            height: 40px;
            margin-right: 12px;
            border-radius: 50%;
            background-color: var(--primary-light);
            display: flex;
            align-items: center;
            justify-content: center;
            font-weight: 700;
            color: var(--primary);
        }

        .asset-name {
            font-weight: 600;
        }

        .asset-symbol {
            color: var(--gray);
            font-size: 14px;
        }

        .asset-balance {
            font-size: 18px;
            font-weight: 600;
            margin-bottom: 5px;
        }

        .asset-value {
            color: var(--gray);
            font-size: 14px;
        }

        .transaction-history {
            margin-top: 40px;
        }

        .section-title {
            font-size: 20px;
            font-weight: 600;
            margin-bottom: 20px;
        }

        .transaction-table {
            width: 100%;
            border-collapse: collapse;
            background: white;
            border-radius: 12px;
            overflow: hidden;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.05);
        }

        .transaction-table th {
            text-align: left;
            padding: 16px;
            background-color: var(--primary-light);
            color: var(--primary);
            font-weight: 600;
        }

        .transaction-table td {
            padding: 16px;
            border-bottom: 1px solid var(--gray-light);
        }

        .transaction-type {
            display: inline-block;
            padding: 4px 8px;
            border-radius: 4px;
            font-size: 12px;
            font-weight: 600;
        }

        .type-receive {
            background-color: rgba(6, 214, 160, 0.1);
            color: var(--success);
        }

        .type-send {
            background-color: rgba(239, 71, 111, 0.1);
            color: var(--danger);
        }

        .transaction-amount {
            font-weight: 600;
        }

        .transaction-date {
            color: var(--gray);
            font-size: 14px;
        }

        .footer {
            text-align: center;
            padding: 30px 0;
            color: var(--gray);
            font-size: 14px;
            margin-top: 50px;
        }

        @media (max-width: 768px) {
            .header {
                flex-direction: column;
                gap: 20px;
            }

            .nav {
                width: 100%;
                justify-content: space-between;
            }

            .btn-group {
                flex-direction: column;
            }

            .assets-list {
                grid-template-columns: 1fr;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <header class="header">
            <div class="logo">CryptoWallet</div>
            <nav class="nav">
                <div class="nav-item active">Wallet</div>
                <div class="nav-item">Transactions</div>
                <div class="nav-item">Swap</div>
                <div class="nav-item">Settings</div>
            </nav>
        </header>

        <main>
            <div class="wallet-card">
                <div class="wallet-header">
                    <h2 class="wallet-title">My Wallet</h2>
                    <div class="btn-group">
                        <button class="btn btn-primary">Receive</button>
                        <button class="btn btn-secondary">Send</button>
                    </div>
                </div>
                <div class="wallet-balance">$12,345.67</div>
                <div class="wallet-address">0x71C7656EC7ab88b098defB751B7401B5f6d8976F</div>
            </div>

            <div class="section-title">Assets</div>
            <div class="assets-list">
                <div class="asset-card">
                    <div class="asset-header">
                        <div class="asset-icon">B</div>
                        <div>
                            <div class="asset-name">Bitcoin</div>
                            <div class="asset-symbol">BTC</div>
                        </div>
                    </div>
                    <div class="asset-balance">0.42 BTC</
