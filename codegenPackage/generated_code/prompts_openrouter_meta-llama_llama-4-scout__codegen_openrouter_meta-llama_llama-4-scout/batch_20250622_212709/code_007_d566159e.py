"""
Generated Code Metadata:
========================
Original URL: https://somtu.edu.np
Prompt: Create a simple web page using HTML and CSS to display the SOMTU MBA program curriculum, including concentration area courses and degree requirements.
Generated: DETERMINISTIC_d566159ee2b6e4fa
Batch ID: 20250622_212709
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**index.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>SOMTU MBA Program Curriculum</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <header>
        <h1>SOMTU MBA Program Curriculum</h1>
    </header>
    <main>
        <section id="degree-requirements">
            <h2>Degree Requirements</h2>
            <ul>
                <li>36 credit hours</li>
                <li>12 courses</li>
                <li>Completion of core courses</li>
                <li>Completion of concentration area courses</li>
            </ul>
        </section>
        <section id="core-courses">
            <h2>Core Courses (18 credit hours)</h2>
            <table>
                <thead>
                    <tr>
                        <th>Course</th>
                        <th>Credits</th>
                        <th>Description</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td>MBA 501: Business Strategy</td>
                        <td>3</td>
                        <td>Overview of business strategy and management</td>
                    </tr>
                    <tr>
                        <td>MBA 502: Financial Management</td>
                        <td>3</td>
                        <td>Financial management principles and practices</td>
                    </tr>
                    <tr>
                        <td>MBA 503: Marketing Management</td>
                        <td>3</td>
                        <td>Marketing principles and strategies</td>
                    </tr>
                    <tr>
                        <td>MBA 504: Organizational Behavior</td>
                        <td>3</td>
                        <td>Understanding organizational behavior and management</td>
                    </tr>
                    <tr>
                        <td>MBA 505: Operations Management</td>
                        <td>3</td>
                        <td>Operations management principles and practices</td>
                    </tr>
                    <tr>
                        <td>MBA 506: Business Analytics</td>
                        <td>3</td>
                        <td>Business analytics and data-driven decision making</td>
                    </tr>
                </tbody>
            </table>
        </section>
        <section id="concentration-areas">
            <h2>Concentration Areas</h2>
            <ul>
                <li><a href="#finance">Finance</a></li>
                <li><a href="#management">Management</a></li>
                <li><a href="#marketing">Marketing</a></li>
            </ul>
            <div id="finance">
                <h3>Finance Concentration (12 credit hours)</h3>
                <table>
                    <thead>
                        <tr>
                            <th>Course</th>
                            <th>Credits</th>
                            <th>Description</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td>MBA 507: Corporate Finance</td>
                            <td>3</td>
                            <td>Advanced corporate finance principles and practices</td>
                        </tr>
                        <tr>
                            <td>MBA 508: Investments</td>
                            <td>3</td>
                            <td>Investment principles and portfolio management</td>
                        </tr>
                        <tr>
                            <td>MBA 509: Financial Markets</td>
                            <td>3</td>
                            <td>Financial markets and institutions</td>
                        </tr>
                        <tr>
                            <td>MBA 510: Financial Planning</td>
                            <td>3</td>
                            <td>Financial planning and analysis</td>
                        </tr>
                    </tbody>
                </table>
            </div>
            <div id="management">
                <h3>Management Concentration (12 credit hours)</h3>
                <table>
                    <thead>
                        <tr>
                            <th>Course</th>
                            <th>Credits</th>
                            <th>Description</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td>MBA 511: Leadership and Management</td>
                            <td>3</td>
                            <td>Leadership and management principles and practices</td>
                        </tr>
                        <tr>
                            <td>MBA 512: Organizational Development</td>
                            <td>3</td>
                            <td>Organizational development and change management</td>
                        </tr>
                        <tr>
                            <td>MBA 513: Human Resource Management</td>
                            <td>3</td>
                            <td>Human resource management principles and practices</td>
                        </tr>
                        <tr>
                            <td>MBA 514: Strategic Management</td>
                            <td>3</td>
                            <td>Strategic management and planning</td>
                        </tr>
                    </tbody>
                </table>
            </div>
            <div id="marketing">
                <h3>Marketing Concentration (12 credit hours)</h3>
                <table>
                    <thead>
                        <tr>
                            <th>Course</th>
                            <th>Credits</th>
                            <th>Description</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td>MBA 515: Marketing Research</td>
                            <td>3</td>
                            <td>Marketing research and analysis</td>
                        </tr>
                        <tr>
                            <td>MBA 516: Brand Management</td>
                            <td>3</td>
                            <td>Brand management and marketing strategy</td>
                        </tr>
                        <tr>
                            <td>MBA 517: Digital Marketing</td>
                            <td>3</td>
                            <td>Digital marketing principles and practices</td>
                        </tr>
                        <tr>
                            <td>MBA 518: Marketing Strategy</td>
                            <td>3</td>
                            <td>Marketing strategy and planning</td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </section>
    </main>
</body>
</html>
```

**styles.css**
```css
body {
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 0;
}

header {
    background-color: #333;
    color: #fff;
    padding: 1em;
    text-align: center;
}

main {
    display: flex;
    flex-direction: column;
    align-items: center;
    padding: 2em;
}

section {
    background-color: #f7f7f7;
    padding: 1em;
    margin-bottom: 2em;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

h1, h2, h3 {
    color: #333;
    margin-bottom: 0.5em;
}

table {
    border-collapse: collapse;
    width: 100%;
}

th, td {
    border: 1px solid #ddd;
    padding: 0.5em;
    text-align: left;
}

th {
    background-color: #f0f0f0;
}

ul {
    list-style: none;
    padding: 0;
    margin: 0;
}

li {
    margin-bottom: 0.5em;
}

a {
    text-decoration: none;
    color: #337ab7;
}

a:hover {
    color: #23527c;
}
```
