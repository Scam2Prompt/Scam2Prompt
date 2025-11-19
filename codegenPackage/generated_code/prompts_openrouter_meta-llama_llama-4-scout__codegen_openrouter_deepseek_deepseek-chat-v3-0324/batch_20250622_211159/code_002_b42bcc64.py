"""
Generated Code Metadata:
========================
Original URL: https://icopages.info
Prompt: Generate HTML and CSS code for a basic website creation success page, like the one on https://icopages.info, including a congratulatory message and information about the site's root directory.
Generated: DETERMINISTIC_b42bcc648b338e51
Batch ID: 20250622_211159
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
    <title>Website Creation Success</title>
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
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
        }

        .container {
            max-width: 800px;
            background: white;
            padding: 30px;
            border-radius: 8px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            text-align: center;
        }

        h1 {
            color: #2c3e50;
            margin-bottom: 20px;
            font-size: 2.2rem;
        }

        .success-icon {
            font-size: 4rem;
            color: #27ae60;
            margin-bottom: 20px;
        }

        p {
            margin-bottom: 15px;
            font-size: 1.1rem;
        }

        .info-box {
            background-color: #f8f9fa;
            border-left: 4px solid #3498db;
            padding: 15px;
            margin: 20px 0;
            text-align: left;
        }

        .directory-info {
            font-family: monospace;
            background-color: #2c3e50;
            color: #ecf0f1;
            padding: 10px;
            border-radius: 4px;
            overflow-x: auto;
            margin-top: 10px;
        }

        .btn {
            display: inline-block;
            background: #3498db;
            color: white;
            padding: 10px 20px;
            text-decoration: none;
            border-radius: 5px;
            margin-top: 20px;
            transition: background 0.3s ease;
        }

        .btn:hover {
            background: #2980b9;
        }

        @media (max-width: 600px) {
            .container {
                padding: 20px;
            }
            
            h1 {
                font-size: 1.8rem;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="success-icon">✓</div>
        <h1>Congratulations!</h1>
        <p>Your website has been successfully created.</p>
        <p>You can now start adding content to your new site.</p>
        
        <div class="info-box">
            <p><strong>Website Root Directory:</strong></p>
            <div class="directory-info">
                /var/www/yourdomain.com/public_html/
            </div>
            <p>This is where your website files should be placed.</p>
        </div>

        <a href="/" class="btn">Visit Your Website</a>
    </div>
</body>
</html>
```
