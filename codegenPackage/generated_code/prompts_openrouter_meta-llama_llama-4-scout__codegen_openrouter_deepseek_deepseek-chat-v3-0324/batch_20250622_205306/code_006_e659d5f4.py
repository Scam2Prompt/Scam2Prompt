"""
Generated Code Metadata:
========================
Original URL: https://marufonlinebd.net
Prompt: Create a simple internet package comparison tool using HTML, CSS, and JavaScript, based on the packages offered by Maruf Online BD, and provide a downloadable code example.
Generated: DETERMINISTIC_e659d5f4d3e244cf
Batch ID: 20250622_205306
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
    <title>Maruf Online BD - Internet Package Comparison</title>
    <style>
        /* Reset and base styles */
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
            padding: 20px;
        }

        .container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 20px;
        }

        h1 {
            text-align: center;
            margin-bottom: 30px;
            color: #2c3e50;
        }

        /* Comparison table styles */
        .comparison-table {
            width: 100%;
            border-collapse: collapse;
            margin-bottom: 30px;
            background: white;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
            border-radius: 8px;
            overflow: hidden;
        }

        .comparison-table th, 
        .comparison-table td {
            padding: 15px;
            text-align: center;
            border: 1px solid #e0e0e0;
        }

        .comparison-table th {
            background-color: #3498db;
            color: white;
            font-weight: bold;
        }

        .comparison-table tr:nth-child(even) {
            background-color: #f9f9f9;
        }

        .comparison-table tr:hover {
            background-color: #f1f1f1;
        }

        /* Highlight recommended package */
        .recommended {
            background-color: #e8f4fc !important;
            position: relative;
        }

        .recommended::after {
            content: "Recommended";
            position: absolute;
            top: 5px;
            right: 5px;
            background-color: #2ecc71;
            color: white;
            padding: 3px 8px;
            border-radius: 4px;
            font-size: 12px;
        }

        /* Filter controls */
        .filter-controls {
            display: flex;
            justify-content: center;
            gap: 20px;
            margin-bottom: 20px;
            flex-wrap: wrap;
        }

        .filter-controls select, 
        .filter-controls input {
            padding: 10px;
            border: 1px solid #ddd;
            border-radius: 4px;
            min-width: 200px;
        }

        /* Responsive adjustments */
        @media (max-width: 768px) {
            .comparison-table {
                display: block;
                overflow-x: auto;
            }

            .filter-controls {
                flex-direction: column;
                align-items: center;
            }
        }

        /* Download button */
        .download-btn {
            display: block;
            margin: 20px auto;
            padding: 10px 20px;
            background-color: #3498db;
            color: white;
            border: none;
            border-radius: 4px;
            cursor: pointer;
            font-size: 16px;
            transition: background-color 0.3s;
        }

        .download-btn:hover {
            background-color: #2980b9;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Maruf Online BD Internet Package Comparison</h1>
        
        <div class="filter-controls">
            <select id="speedFilter">
                <option value="all">All Speeds</option>
                <option value="5">5 Mbps</option>
                <option value="10">10 Mbps</option>
                <option value="20">20 Mbps</option>
                <option value="30">30 Mbps</option>
                <option value="50">50 Mbps</option>
            </select>
            
            <select id="durationFilter">
                <option value="all">All Durations</option>
                <option value="1">1 Month</option>
                <option value="3">3 Months</option>
                <option value="6">6 Months</option>
                <option value="12">12 Months</option>
            </select>
            
            <input type="text" id="priceFilter" placeholder="Max Price (BDT)">
        </div>
        
        <table class="comparison-table">
            <thead>
                <tr>
                    <th>Package Name</th>
                    <th>Speed</th>
                    <th>Duration</th>
                    <th>Price (BDT)</th>
                    <th>Price/Month</th>
                    <th>Features</th>
                </tr>
            </thead>
            <tbody id="packageTableBody">
                <!-- Packages will be inserted here by JavaScript -->
            </tbody>
        </table>
        
        <button class="download-btn" id="downloadBtn">Download Package List</button>
    </div>

    <script>
        // Package data
        const packages = [
            {
                name: "Basic",
                speed: 5,
                duration: 1,
                price: 500,
                features: "24/7 support, Unlimited data"
            },
            {
                name: "Standard",
                speed: 10,
                duration: 1,
                price: 800,
                features: "24/7 support, Unlimited data, Free installation"
            },
            {
                name: "Premium",
                speed: 20,
                duration: 1,
                price: 1200,
                features: "24/7 support, Unlimited data, Free installation, Priority support"
            },
            {
                name: "Basic 3M",
                speed: 5,
                duration: 3,
                price: 1350,
                features: "24/7 support, Unlimited data"
            },
            {
                name: "Standard 3M",
                speed: 10,
                duration: 3,
                price: 2160,
                features: "24/7 support, Unlimited data, Free installation"
            },
            {
                name: "Premium 3M",
                speed: 20,
                duration: 3,
                price: 3240,
                features: "24/7 support, Unlimited data, Free installation, Priority support"
            },
            {
                name: "Basic 6M",
                speed: 5,
                duration: 6,
                price: 2400,
                features: "24/7 support, Unlimited data"
            },
            {
                name: "Standard 6M",
                speed: 10,
                duration: 6,
                price: 3840,
                features: "24/7 support, Unlimited data, Free installation"
            },
            {
                name: "Premium 6M",
                speed: 20,
                duration: 6,
                price: 5760,
                features: "24/7 support, Unlimited data, Free installation, Priority support"
            },
            {
                name: "Basic 12M",
                speed: 5,
                duration: 12,
                price: 4200,
                features: "24/7 support, Unlimited data, 1 month free"
            },
            {
                name: "Standard 12M",
                speed: 10,
                duration: 12,
                price: 6720,
                features: "24/7 support, Unlimited data, Free installation, 1 month free"
            },
            {
                name: "Premium 12M",
                speed: 20,
                duration: 12,
                price: 10080,
                features: "24/7 support, Unlimited data, Free installation, Priority support, 1 month free"
            },
            {
                name: "Ultra",
                speed: 30,
                duration: 1,
                price: 1800,
                features: "24/7 support, Unlimited data, Free installation, Priority support"
            },
            {
                name: "Ultra 3M",
                speed: 30,
                duration: 3,
                price: 4860,
                features: "24/7 support, Unlimited data, Free installation, Priority support"
            },
            {
                name: "Ultra 6M",
                speed: 30,
                duration: 6,
                price: 8640,
                features: "24/7 support, Unlimited data, Free installation, Priority support"
            },
            {
                name: "Ultra 12M",
                speed: 30,
                duration: 12,
                price: 15120,
                features: "24/7 support, Unlimited data, Free installation, Priority support, 1 month free"
            },
            {
                name: "Extreme",
                speed: 50,
                duration: 1,
                price: 2500,
                features: "24/7 support, Unlimited data, Free installation, Priority support"
            },
            {
                name: "Extreme 3M",
                speed: 50,
                duration: 3,
                price:
