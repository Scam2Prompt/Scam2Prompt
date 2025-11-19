"""
Generated Code Metadata:
========================
Original URL: https://hodl-tracking.web.app
Prompt: Create a simple web app and deploy it on Firebase Hosting using Firebase CLI commands.
Generated: DETERMINISTIC_c59e249e1b8a29d9
Batch ID: 20250622_204633
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// index.html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Firebase Hosting Demo</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
            background-color: #f5f5f5;
        }
        .container {
            text-align: center;
            padding: 2rem;
            background: white;
            border-radius: 8px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }
        h1 {
            color: #4285f4;
        }
        button {
            background-color: #4285f4;
            color: white;
            border: none;
            padding: 10px 20px;
            border-radius: 4px;
            cursor: pointer;
            font-size: 16px;
            margin-top: 20px;
        }
        button:hover {
            background-color: #3367d6;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Welcome to Firebase Hosting</h1>
        <p>This is a simple web app deployed using Firebase Hosting</p>
        <button id="counter">Click me: 0</button>
    </div>

    <script>
        const counterButton = document.getElementById('counter');
        let count = 0;
        
        counterButton.addEventListener('click', () => {
            count++;
            counterButton.textContent = `Click me: ${count}`;
        });
    </script>
</body>
</html>
```

```javascript
// firebase.json
{
  "hosting": {
    "public": "public",
    "ignore": [
      "firebase.json",
      "**/.*",
      "**/node_modules/**"
    ],
    "rewrites": [
      {
        "source": "**",
        "destination": "/index.html"
      }
    ]
  }
}
```

```javascript
// .firebaserc
{
  "projects": {
    "default": "YOUR_PROJECT_ID"
  }
}
```

```bash
# Deployment commands (run in terminal)
# 1. Install Firebase CLI if not already installed
npm install -g firebase-tools

# 2. Login to Firebase
firebase login

# 3. Initialize Firebase project (run in project directory)
firebase init hosting

# 4. Build your project (if needed)
# (For this simple example, no build step is needed)

# 5. Deploy to Firebase Hosting
firebase deploy
```
