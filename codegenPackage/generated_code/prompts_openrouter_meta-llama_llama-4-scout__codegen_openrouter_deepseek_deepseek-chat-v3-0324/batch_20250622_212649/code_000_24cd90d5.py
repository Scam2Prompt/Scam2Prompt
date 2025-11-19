"""
Generated Code Metadata:
========================
Original URL: https://pyo97.eth-drop.top
Prompt: "Generate a sign-in page similar to Google's Gmail."
Generated: DETERMINISTIC_24cd90d5af6e4413
Batch ID: 20250622_212649
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://www.google.com/images/branding/googlelogo/1x/googlelogo_color_150x54dp.png": {
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
    <title>Sign in - Gmail</title>
    <style>
        body {
            font-family: 'Google Sans', Arial, sans-serif;
            margin: 0;
            padding: 0;
            color: #202124;
            background-color: #fff;
        }
        
        .container {
            max-width: 450px;
            margin: 0 auto;
            padding: 20px;
        }
        
        .logo {
            text-align: center;
            margin: 20px 0;
        }
        
        .logo img {
            width: 75px;
            height: 24px;
        }
        
        .card {
            border: 1px solid #dadce0;
            border-radius: 8px;
            padding: 40px;
            margin: 0 auto;
        }
        
        h1 {
            font-size: 24px;
            font-weight: 400;
            text-align: center;
            margin: 0 0 20px;
        }
        
        .form-group {
            margin-bottom: 20px;
        }
        
        input[type="email"] {
            width: 100%;
            padding: 13px 15px;
            font-size: 16px;
            border: 1px solid #dadce0;
            border-radius: 4px;
            box-sizing: border-box;
        }
        
        input[type="email"]:focus {
            border-color: #1a73e8;
            outline: none;
        }
        
        .forgot-email {
            color: #1a73e8;
            font-size: 14px;
            font-weight: 500;
            text-decoration: none;
            display: block;
            margin-bottom: 20px;
        }
        
        .forgot-email:hover {
            text-decoration: underline;
        }
        
        .disclaimer {
            font-size: 14px;
            color: #5f6368;
            margin: 20px 0;
        }
        
        .actions {
            display: flex;
            justify-content: space-between;
            align-items: center;
        }
        
        .create-account {
            color: #1a73e8;
            font-weight: 500;
            text-decoration: none;
        }
        
        .create-account:hover {
            text-decoration: underline;
        }
        
        .next-btn {
            background-color: #1a73e8;
            color: white;
            border: none;
            padding: 10px 24px;
            border-radius: 4px;
            font-size: 14px;
            font-weight: 500;
            cursor: pointer;
        }
        
        .next-btn:hover {
            background-color: #1765cc;
        }
        
        footer {
            margin-top: 50px;
            text-align: center;
            font-size: 12px;
            color: #5f6368;
        }
        
        .footer-links {
            display: flex;
            justify-content: center;
            gap: 20px;
            margin-bottom: 10px;
        }
        
        .footer-links a {
            color: #5f6368;
            text-decoration: none;
        }
        
        .footer-links a:hover {
            text-decoration: underline;
        }
        
        .language-selector {
            margin-top: 10px;
        }
        
        select {
            border: none;
            background: none;
            color: #5f6368;
            font-size: 12px;
        }
        
        select:focus {
            outline: none;
        }
        
        .error-message {
            color: #d93025;
            font-size: 12px;
            margin-top: 5px;
            display: none;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="logo">
            <img src="https://www.google.com/images/branding/googlelogo/1x/googlelogo_color_150x54dp.png" alt="Google">
        </div>
        
        <div class="card">
            <h1>Sign in</h1>
            
            <form id="signin-form">
                <div class="form-group">
                    <input type="email" id="email" name="email" placeholder="Email or phone" autofocus required>
                    <div id="email-error" class="error-message">Please enter a valid email or phone number</div>
                </div>
                
                <a href="#" class="forgot-email">Forgot email?</a>
                
                <p class="disclaimer">Not your computer? Use Guest mode to sign in privately.</p>
                
                <div class="actions">
                    <a href="#" class="create-account">Create account</a>
                    <button type="submit" class="next-btn">Next</button>
                </div>
            </form>
        </div>
        
        <footer>
            <div class="footer-links">
                <a href="#">Help</a>
                <a href="#">Privacy</a>
                <a href="#">Terms</a>
            </div>
            <div class="language-selector">
                <select>
                    <option>English (United States)</option>
                    <option>Español</option>
                    <option>Français</option>
                </select>
            </div>
        </footer>
    </div>
    
    <script>
        document.getElementById('signin-form').addEventListener('submit', function(e) {
            e.preventDefault();
            const email = document.getElementById('email').value;
            const errorElement = document.getElementById('email-error');
            
            // Simple email validation
            if (!email || !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email)) {
                errorElement.style.display = 'block';
                return;
            }
            
            errorElement.style.display = 'none';
            
            // In a real application, you would send this to your backend
            console.log('Signing in with:', email);
            
            // Simulate successful sign-in
            alert('Check your email for a sign-in link');
        });
    </script>
</body>
</html>
```
