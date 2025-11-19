"""
Generated Code Metadata:
========================
Original URL: https://trade.exploreearn.com
Prompt: Design a simple user interface for a trading dashboard inspired by Explore Earn's platform, using HTML and CSS.
Generated: DETERMINISTIC_eb5fd7729bd375be
Batch ID: 20250622_212046
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
    <title>Trading Dashboard</title>
    <style>
        /* Reset and Base Styles */
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        }

        body {
            background-color: #f5f5f5;
            color: #333;
            line-height: 1.6;
        }

        /* Container Layout */
        .dashboard {
            display: grid;
            grid-template-columns: 250px 1fr;
            grid-template-rows: 60px 1fr;
            grid-template-areas:
                "sidebar header"
                "sidebar main";
            height: 100vh;
        }

        /* Header Styles */
        .header {
            grid-area: header;
            background-color: #fff;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
            display: flex;
            align-items: center;
            padding: 0 20px;
            justify-content: space-between;
        }

        .logo {
            font-size: 1.5rem;
            font-weight: bold;
            color: #2a52be;
        }

        .user-profile {
            display: flex;
            align-items: center;
            gap: 10px;
        }

        .user-avatar {
            width: 36px;
            height: 36px;
            border-radius: 50%;
            background-color: #e0e0e0;
            display: flex;
            align-items: center;
            justify-content: center;
            font-weight: bold;
        }

        /* Sidebar Styles */
        .sidebar {
            grid-area: sidebar;
            background-color: #2a52be;
            color: white;
            padding: 20px 0;
        }

        .sidebar-menu {
            list-style: none;
            margin-top: 20px;
        }

        .sidebar-menu li {
            padding: 12px 20px;
            cursor: pointer;
            transition: background-color 0.2s;
        }

        .sidebar-menu li:hover {
            background-color: rgba(255, 255, 255, 0.1);
        }

        .sidebar-menu li.active {
            background-color: rgba(255, 255, 255, 0.2);
            border-left: 3px solid white;
        }

        .sidebar-menu li i {
            margin-right: 10px;
        }

        /* Main Content Styles */
        .main-content {
            grid-area: main;
            padding: 20px;
            overflow-y: auto;
        }

        .card {
            background-color: white;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
            padding: 20px;
            margin-bottom: 20px;
        }

        .card-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 15px;
        }

        .card-title {
            font-size: 1.2rem;
            font-weight: 600;
        }

        /* Market Data Grid */
        .market-grid {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
            gap: 20px;
        }

        .market-card {
            padding: 15px;
            border-radius: 6px;
            background-color: #f9f9f9;
            transition: transform 0.2s;
        }

        .market-card:hover {
            transform: translateY(-2px);
        }

        .asset-name {
            font-weight: 600;
            margin-bottom: 5px;
        }

        .asset-price {
            font-size: 1.3rem;
            font-weight: bold;
            margin-bottom: 5px;
        }

        .price-change {
            display: inline-block;
            padding: 3px 8px;
            border-radius: 4px;
            font-size: 0.9rem;
        }

        .positive {
            background-color: #e6f7ee;
            color: #00a854;
        }

        .negative {
            background-color: #fff1f0;
            color: #f5222d;
        }

        /* Trading Widget */
        .trading-widget {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 20px;
        }

        .trade-form {
            display: flex;
            flex-direction: column;
            gap: 15px;
        }

        .form-group {
            display: flex;
            flex-direction: column;
            gap: 5px;
        }

        .form-group label {
            font-weight: 500;
            font-size: 0.9rem;
        }

        .form-control {
            padding: 10px;
            border: 1px solid #ddd;
            border-radius: 4px;
            font-size: 1rem;
        }

        .btn {
            padding: 10px 15px;
            border: none;
            border-radius: 4px;
            cursor: pointer;
            font-weight: 500;
            transition: opacity 0.2s;
        }

        .btn:hover {
            opacity: 0.9;
        }

        .btn-primary {
            background-color: #2a52be;
            color: white;
        }

        .btn-secondary {
            background-color: #f0f0f0;
            color: #333;
        }

        /* Responsive Adjustments */
        @media (max-width: 768px) {
            .dashboard {
                grid-template-columns: 1fr;
                grid-template-rows: 60px auto 1fr;
                grid-template-areas:
                    "header"
                    "sidebar"
                    "main";
            }

            .sidebar {
                padding: 10px 0;
            }

            .sidebar-menu {
                display: flex;
                overflow-x: auto;
                margin-top: 0;
            }

            .sidebar-menu li {
                white-space: nowrap;
                border-left: none;
                border-bottom: 3px solid transparent;
            }

            .sidebar-menu li.active {
                border-left: none;
                border-bottom: 3px solid white;
            }

            .trading-widget {
                grid-template-columns: 1fr;
            }
        }
    </style>
</head>
<body>
    <div class="dashboard">
        <!-- Header Section -->
        <header class="header">
            <div class="logo">TradeDash</div>
            <div class="user-profile">
                <span>John Doe</span>
                <div class="user-avatar">JD</div>
            </div>
        </header>

        <!-- Sidebar Navigation -->
        <nav class="sidebar">
            <ul class="sidebar-menu">
                <li class="active">
                    <i>📊</i> Dashboard
                </li>
                <li>
                    <i>💰</i> Portfolio
                </li>
                <li>
                    <i>📈</i> Markets
                </li>
                <li>
                    <i>🔄</i> Transactions
                </li>
                <li>
                    <i>⚙️</i> Settings
                </li>
            </ul>
        </nav>

        <!-- Main Content Area -->
        <main class="main-content">
            <!-- Summary Cards -->
            <div class="card">
                <div class="card-header">
                    <h2 class="card-title">Market Overview</h2>
                </div>
                <div class="market-grid">
                    <div class="market-card">
                        <div class="asset-name">Bitcoin (BTC)</div>
                        <div class="asset-price">$42,356.78</div>
                        <span class="price-change positive">+2.45%</span>
                    </div>
                    <div class="market-card">
                        <div class="asset-name">Ethereum (ETH)</div>
                        <div class="asset-price">$2,345.67</div>
                        <span class="price-change positive">+1.23%</span>
                    </div>
                    <div class="market-card">
                        <div class="asset-name">Solana (SOL)</div>
                        <div class="asset-price">$98.76</div>
                        <span class="price-change negative">-0.78%</span>
                    </div>
                    <div class="market-card">
                        <div class="asset-name">Cardano (ADA)</div>
                        <div class="asset-price">$0.56</div>
                        <span class="price-change positive">+0.34%</span>
                    </div>
                </div>
            </div>

            <!-- Trading Widget -->
            <div class="card">
                <div class="card-header">
                    <h2 class="card-title">Trade</h2>
                </div>
                <div class="trading-widget">
                    <
