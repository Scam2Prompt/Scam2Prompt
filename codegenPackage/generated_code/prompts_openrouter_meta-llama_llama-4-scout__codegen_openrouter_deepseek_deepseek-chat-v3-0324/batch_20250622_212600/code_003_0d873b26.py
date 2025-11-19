"""
Generated Code Metadata:
========================
Original URL: https://swiftrealisticevm.com
Prompt: How can I generate a custom error page for a suspended website using HTML, CSS, and JavaScript, similar to the one on swiftrealisticevm.com?
Generated: DETERMINISTIC_0d873b26c8272bc2
Batch ID: 20250622_212600
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
    <title>Website Suspended</title>
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
            display: flex;
            flex-direction: column;
            min-height: 100vh;
            text-align: center;
        }
        
        /* Main container */
        .container {
            max-width: 800px;
            margin: 0 auto;
            padding: 2rem;
            flex: 1;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
        }
        
        /* Header styles */
        .header {
            margin-bottom: 2rem;
        }
        
        .header h1 {
            font-size: 2.5rem;
            color: #d9534f;
            margin-bottom: 1rem;
        }
        
        /* Content styles */
        .content {
            background-color: white;
            padding: 2rem;
            border-radius: 8px;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
            margin-bottom: 2rem;
            width: 100%;
        }
        
        .content p {
            margin-bottom: 1.5rem;
            font-size: 1.1rem;
        }
        
        /* Button styles */
        .btn {
            display: inline-block;
            padding: 0.8rem 1.5rem;
            background-color: #d9534f;
            color: white;
            text-decoration: none;
            border-radius: 4px;
            font-weight: bold;
            transition: background-color 0.3s;
            border: none;
            cursor: pointer;
            font-size: 1rem;
        }
        
        .btn:hover {
            background-color: #c9302c;
        }
        
        /* Footer styles */
        .footer {
            margin-top: 2rem;
            font-size: 0.9rem;
            color: #777;
        }
        
        /* Responsive adjustments */
        @media (max-width: 600px) {
            .container {
                padding: 1rem;
            }
            
            .header h1 {
                font-size: 2rem;
            }
            
            .content {
                padding: 1.5rem;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>Website Suspended</h1>
        </div>
        
        <div class="content">
            <p>This website has been suspended due to non-payment or violation of terms of service.</p>
            <p>If you are the owner of this website, please contact our support team to resolve this issue.</p>
            
            <button class="btn" id="contactBtn">Contact Support</button>
        </div>
        
        <div class="footer">
            <p>&copy; 2023 Hosting Provider. All rights reserved.</p>
        </div>
    </div>

    <script>
        document.addEventListener('DOMContentLoaded', function() {
            // Handle contact button click
            const contactBtn = document.getElementById('contactBtn');
            
            contactBtn.addEventListener('click', function() {
                // Replace with your actual support email
                window.location.href = 'mailto:support@example.com?subject=Website Suspension Inquiry';
            });
            
            // Additional functionality can be added here
            console.log('Suspended page loaded');
        });
    </script>
</body>
</html>
```
