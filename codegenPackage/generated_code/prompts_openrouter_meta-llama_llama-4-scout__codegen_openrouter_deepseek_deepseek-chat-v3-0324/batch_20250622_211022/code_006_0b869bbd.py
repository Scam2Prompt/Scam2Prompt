"""
Generated Code Metadata:
========================
Original URL: https://dustbox.netlify.app
Prompt: "Suggest improvements for the user interface of an interactive graph and table of contents, as seen on https://dustbox.netlify.app, from a user experience (UX) perspective."
Generated: DETERMINISTIC_0b869bbd7c365d15
Batch ID: 20250622_211022
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
    <title>Improved Interactive Graph UI</title>
    <style>
        :root {
            --primary-color: #4a6fa5;
            --secondary-color: #166088;
            --accent-color: #4fc3f7;
            --text-color: #333;
            --light-bg: #f8f9fa;
            --border-radius: 8px;
            --box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            --transition: all 0.3s ease;
        }

        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            line-height: 1.6;
            color: var(--text-color);
            margin: 0;
            padding: 0;
            background-color: var(--light-bg);
        }

        .container {
            display: flex;
            max-width: 1200px;
            margin: 0 auto;
            padding: 20px;
            gap: 20px;
        }

        /* Sidebar/TOC styles */
        .sidebar {
            width: 280px;
            background: white;
            border-radius: var(--border-radius);
            box-shadow: var(--box-shadow);
            padding: 20px;
            position: sticky;
            top: 20px;
            max-height: 90vh;
            overflow-y: auto;
        }

        .sidebar-header {
            font-size: 1.2rem;
            font-weight: bold;
            margin-bottom: 15px;
            color: var(--secondary-color);
            padding-bottom: 10px;
            border-bottom: 1px solid #eee;
        }

        .toc-item {
            padding: 8px 12px;
            margin-bottom: 5px;
            border-radius: var(--border-radius);
            cursor: pointer;
            transition: var(--transition);
        }

        .toc-item:hover {
            background-color: rgba(74, 111, 165, 0.1);
        }

        .toc-item.active {
            background-color: var(--accent-color);
            color: white;
            font-weight: 500;
        }

        .toc-subitems {
            margin-left: 15px;
            margin-top: 5px;
            display: none;
        }

        .toc-item.expanded + .toc-subitems {
            display: block;
        }

        .toc-subitem {
            padding: 6px 10px;
            font-size: 0.9rem;
            color: #666;
        }

        .toc-subitem:hover {
            color: var(--primary-color);
        }

        .toc-subitem.active {
            color: var(--secondary-color);
            font-weight: 500;
        }

        /* Graph container styles */
        .graph-container {
            flex: 1;
            background: white;
            border-radius: var(--border-radius);
            box-shadow: var(--box-shadow);
            padding: 20px;
            min-height: 80vh;
        }

        .graph-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 20px;
        }

        .graph-title {
            font-size: 1.3rem;
            font-weight: bold;
            color: var(--secondary-color);
        }

        .graph-controls {
            display: flex;
            gap: 10px;
        }

        .control-btn {
            padding: 8px 12px;
            background: white;
            border: 1px solid #ddd;
            border-radius: var(--border-radius);
            cursor: pointer;
            transition: var(--transition);
        }

        .control-btn:hover {
            background: #f0f0f0;
        }

        .control-btn.active {
            background: var(--primary-color);
            color: white;
            border-color: var(--primary-color);
        }

        .search-box {
            padding: 8px 12px;
            border: 1px solid #ddd;
            border-radius: var(--border-radius);
            width: 200px;
        }

        /* Graph visualization area */
        .graph-visualization {
            width: 100%;
            height: 600px;
            border: 1px solid #eee;
            border-radius: var(--border-radius);
            background: #fcfcfc;
            position: relative;
        }

        /* Node tooltip */
        .node-tooltip {
            position: absolute;
            background: white;
            padding: 10px;
            border-radius: var(--border-radius);
            box-shadow: var(--box-shadow);
            pointer-events: none;
            opacity: 0;
            transition: opacity 0.2s;
            z-index: 10;
            max-width: 300px;
        }

        /* Responsive adjustments */
        @media (max-width: 768px) {
            .container {
                flex-direction: column;
            }

            .sidebar {
                width: auto;
                position: static;
                max-height: none;
            }

            .graph-visualization {
                height: 400px;
            }
        }

        /* Animation for graph elements */
        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(10px); }
            to { opacity: 1; transform: translateY(0); }
        }

        .toc-item {
            animation: fadeIn 0.3s ease forwards;
        }

        .toc-item:nth-child(1) { animation-delay: 0.1s; }
        .toc-item:nth-child(2) { animation-delay: 0.2s; }
        .toc-item:nth-child(3) { animation-delay: 0.3s; }
        /* ... and so on for more items */
    </style>
</head>
<body>
    <div class="container">
        <!-- Improved Table of Contents -->
        <aside class="sidebar">
            <div class="sidebar-header">Table of Contents</div>
            <div class="toc-item expanded" onclick="toggleTocItem(this)">
                Introduction
                <div class="toc-subitems">
                    <div class="toc-subitem active" onclick="selectTocItem(this)">Overview</div>
                    <div class="toc-subitem" onclick="selectTocItem(this)">Getting Started</div>
                    <div class="toc-subitem" onclick="selectTocItem(this)">Features</div>
                </div>
            </div>
            <div class="toc-item" onclick="toggleTocItem(this)">
                Core Concepts
                <div class="toc-subitems">
                    <div class="toc-subitem" onclick="selectTocItem(this)">Architecture</div>
                    <div class="toc-subitem" onclick="selectTocItem(this)">Components</div>
                    <div class="toc-subitem" onclick="selectTocItem(this)">Data Flow</div>
                </div>
            </div>
            <div class="toc-item" onclick="toggleTocItem(this)">
                Advanced Topics
                <div class="toc-subitems">
                    <div class="toc-subitem" onclick="selectTocItem(this)">Performance</div>
                    <div class="toc-subitem" onclick="selectTocItem(this)">Scaling</div>
                    <div class="toc-subitem" onclick="selectTocItem(this)">Security</div>
                </div>
            </div>
            <div class="toc-item" onclick="toggleTocItem(this)">
                Examples
                <div class="toc-subitems">
                    <div class="toc-subitem" onclick="selectTocItem(this)">Basic Usage</div>
                    <div class="toc-subitem" onclick="selectTocItem(this)">Advanced Patterns</div>
                </div>
            </div>
        </aside>

        <!-- Main Graph Content -->
        <main class="graph-container">
            <div class="graph-header">
                <h1 class="graph-title">Interactive Graph Visualization</h1>
                <div class="graph-controls">
                    <input type="text" class="search-box" placeholder="Search nodes...">
                    <button class="control-btn active">View All</button>
                    <button class="control-btn">Filter</button>
                    <button class="control-btn">Export</button>
                </div>
            </div>
            <div class="graph-visualization">
                <!-- Graph visualization would be rendered here -->
                <div class="node-tooltip">Node information will appear here on hover</div>
            </div>
        </main>
    </div>

    <script>
        // Toggle TOC item expansion
        function toggleTocItem(element) {
            element.classList.toggle('expanded');
        }

        // Select TOC item
        function selectTocItem(element) {
            // Remove active class from all items
            document.querySelectorAll('.toc-subitem').forEach(item => {
                item.classList.remove('active
