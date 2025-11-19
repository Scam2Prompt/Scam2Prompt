"""
Generated Code Metadata:
========================
Original URL: https://grupocapernaum.com
Prompt: What are some best practices for creating a default webpage for new hosting accounts, as demonstrated on grupocapernaum.com, to verify correct hosting setup?
Generated: DETERMINISTIC_f56733409eaca82e
Batch ID: 20250622_205842
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
    <title>Hosting Account Active</title>
    <style>
        body {
            font-family: 'Arial', sans-serif;
            line-height: 1.6;
            margin: 0;
            padding: 0;
            background-color: #f5f5f5;
            color: #333;
        }
        .container {
            max-width: 800px;
            margin: 50px auto;
            padding: 20px;
            background: #fff;
            border-radius: 8px;
            box-shadow: 0 0 10px rgba(0,0,0,0.1);
            text-align: center;
        }
        h1 {
            color: #2c3e50;
        }
        .success-icon {
            color: #27ae60;
            font-size: 72px;
            margin-bottom: 20px;
        }
        .server-info {
            text-align: left;
            margin-top: 30px;
            padding: 15px;
            background: #f9f9f9;
            border-radius: 5px;
        }
        .footer {
            margin-top: 30px;
            font-size: 12px;
            color: #7f8c8d;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="success-icon">✓</div>
        <h1>Your Hosting Account is Active!</h1>
        <p>This page confirms that your hosting account has been successfully set up.</p>
        <p>You can now begin uploading your website files to the public_html directory.</p>
        
        <div class="server-info">
            <h3>Server Information:</h3>
            <p><strong>Server Name:</strong> <?php echo $_SERVER['SERVER_NAME']; ?></p>
            <p><strong>Server Software:</strong> <?php echo $_SERVER['SERVER_SOFTWARE']; ?></p>
            <p><strong>PHP Version:</strong> <?php echo phpversion(); ?></p>
            <p><strong>Document Root:</strong> <?php echo $_SERVER['DOCUMENT_ROOT']; ?></p>
        </div>
        
        <div class="footer">
            <p>This is a temporary page. Please replace it with your own content.</p>
            <p>Generated on: <?php echo date('Y-m-d H:i:s'); ?></p>
        </div>
    </div>
</body>
</html>
```
