"""
Generated Code Metadata:
========================
Original URL: https://adelanto.cl
Prompt: "Design a simple web application using HTML, CSS, and JavaScript to provide an interface for clients to access and manage their factoring services, including uploading invoices and tracking liquidity."
Generated: DETERMINISTIC_2382b37a793944ff
Batch ID: 20250622_211508
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Here's the complete code for a simple web application for factoring services:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Factoring Services Portal</title>
    <style>
        /* Reset and base styles */
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: 'Arial', sans-serif;
        }

        body {
            background-color: #f5f7fa;
            color: #333;
            line-height: 1.6;
        }

        /* Header styles */
        header {
            background-color: #2c3e50;
            color: white;
            padding: 1rem 2rem;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }

        .logo {
            font-size: 1.5rem;
            font-weight: bold;
        }

        .user-info {
            display: flex;
            align-items: center;
            gap: 1rem;
        }

        /* Main content styles */
        .container {
            max-width: 1200px;
            margin: 2rem auto;
            padding: 0 1rem;
        }

        .dashboard {
            display: grid;
            grid-template-columns: 250px 1fr;
            gap: 2rem;
        }

        /* Sidebar styles */
        .sidebar {
            background-color: white;
            border-radius: 8px;
            padding: 1.5rem;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
        }

        .sidebar nav ul {
            list-style: none;
        }

        .sidebar nav ul li {
            margin-bottom: 1rem;
        }

        .sidebar nav ul li a {
            text-decoration: none;
            color: #2c3e50;
            font-weight: 500;
            display: block;
            padding: 0.5rem;
            border-radius: 4px;
            transition: all 0.3s ease;
        }

        .sidebar nav ul li a:hover, 
        .sidebar nav ul li a.active {
            background-color: #e1f0ff;
            color: #3498db;
        }

        /* Main content area */
        .main-content {
            background-color: white;
            border-radius: 8px;
            padding: 1.5rem;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
        }

        .section-title {
            margin-bottom: 1.5rem;
            color: #2c3e50;
            font-size: 1.3rem;
            border-bottom: 1px solid #eee;
            padding-bottom: 0.5rem;
        }

        /* Card styles */
        .card {
            background-color: #f8f9fa;
            border-radius: 8px;
            padding: 1.5rem;
            margin-bottom: 1.5rem;
        }

        .card-title {
            font-size: 1.1rem;
            margin-bottom: 1rem;
            color: #3498db;
        }

        /* Form styles */
        .form-group {
            margin-bottom: 1rem;
        }

        .form-group label {
            display: block;
            margin-bottom: 0.5rem;
            font-weight: 500;
        }

        .form-group input,
        .form-group select,
        .form-group textarea {
            width: 100%;
            padding: 0.75rem;
            border: 1px solid #ddd;
            border-radius: 4px;
            font-size: 1rem;
        }

        .form-group textarea {
            min-height: 100px;
            resize: vertical;
        }

        .btn {
            background-color: #3498db;
            color: white;
            border: none;
            padding: 0.75rem 1.5rem;
            border-radius: 4px;
            cursor: pointer;
            font-size: 1rem;
            transition: background-color 0.3s ease;
        }

        .btn:hover {
            background-color: #2980b9;
        }

        /* Table styles */
        .table-responsive {
            overflow-x: auto;
        }

        table {
            width: 100%;
            border-collapse: collapse;
            margin-bottom: 1.5rem;
        }

        th, td {
            padding: 0.75rem;
            text-align: left;
            border-bottom: 1px solid #ddd;
        }

        th {
            background-color: #f2f2f2;
            font-weight: 600;
        }

        tr:hover {
            background-color: #f5f5f5;
        }

        /* Status badges */
        .badge {
            display: inline-block;
            padding: 0.25rem 0.5rem;
            border-radius: 4px;
            font-size: 0.8rem;
            font-weight: 600;
        }

        .badge.pending {
            background-color: #f39c12;
            color: white;
        }

        .badge.approved {
            background-color: #2ecc71;
            color: white;
        }

        .badge.rejected {
            background-color: #e74c3c;
            color: white;
        }

        /* File upload styles */
        .file-upload {
            border: 2px dashed #ddd;
            border-radius: 8px;
            padding: 2rem;
            text-align: center;
            margin-bottom: 1.5rem;
        }

        .file-upload input {
            display: none;
        }

        .file-upload label {
            display: block;
            cursor: pointer;
            color: #3498db;
            font-weight: 500;
        }

        .file-upload label:hover {
            text-decoration: underline;
        }

        /* Responsive adjustments */
        @media (max-width: 768px) {
            .dashboard {
                grid-template-columns: 1fr;
            }
        }
    </style>
</head>
<body>
    <header>
        <div class="logo">Factoring Services Portal</div>
        <div class="user-info">
            <span>Welcome, Client</span>
            <button class="btn" id="logoutBtn">Logout</button>
        </div>
    </header>

    <div class="container">
        <div class="dashboard">
            <aside class="sidebar">
                <nav>
                    <ul>
                        <li><a href="#" class="active" id="dashboardLink">Dashboard</a></li>
                        <li><a href="#" id="invoicesLink">Invoices</a></li>
                        <li><a href="#" id="uploadLink">Upload Invoice</a></li>
                        <li><a href="#" id="liquidityLink">Liquidity</a></li>
                        <li><a href="#" id="reportsLink">Reports</a></li>
                        <li><a href="#" id="settingsLink">Settings</a></li>
                    </ul>
                </nav>
            </aside>

            <main class="main-content">
                <!-- Dashboard Section -->
                <section id="dashboardSection">
                    <h2 class="section-title">Dashboard Overview</h2>
                    
                    <div class="card">
                        <h3 class="card-title">Quick Stats</h3>
                        <div class="stats-grid">
                            <div class="stat-item">
                                <div class="stat-value">$25,000</div>
                                <div class="stat-label">Available Credit</div>
                            </div>
                            <div class="stat-item">
                                <div class="stat-value">$12,500</div>
                                <div class="stat-label">Used Credit</div>
                            </div>
                            <div class="stat-item">
                                <div class="stat-value">5</div>
                                <div class="stat-label">Pending Invoices</div>
                            </div>
                            <div class="stat-item">
                                <div class="stat-value">12</div>
                                <div class="stat-label">Approved Invoices</div>
                            </div>
                        </div>
                    </div>

                    <div class="card">
                        <h3 class="card-title">Recent Activity</h3>
                        <div class="table-responsive">
                            <table>
                                <thead>
                                    <tr>
                                        <th>Date</th>
                                        <th>Invoice #</th>
                                        <th>Amount</th>
                                        <th>Status</th>
                                        <th>Action</th>
                                    </tr>
                                </thead>
                                <tbody>
                                    <tr>
                                        <td>2023-05-15</td>
                                        <td>INV-1001</td>
                                        <td>$2,500.00</td>
                                        <td><span class="badge approved">Approved</span></td>
                                        <td><button class="btn">View</button></td>
                                    </tr>
                                    <tr>
                                        <td>2023-05-14
