"""
Generated Code Metadata:
========================
Original URL: https://co-djs.com
Prompt: Create a JavaScript code example that enables guests to send song requests to a DJ booth via a mobile-friendly web app, similar to the online request system mentioned on the site.
Generated: DETERMINISTIC_52db35dbd7901429
Batch ID: 20250612_155332
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://www.gstatic.com/firebasejs/8.10.0/firebase-app.js": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://www.gstatic.com/firebasejs/8.10.0/firebase-database.js": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```javascript
// Song Request Web App for DJ Booth
// Frontend: HTML, CSS, JavaScript
// Backend: Firebase Realtime Database (for simplicity)

// HTML Structure (embedded in JavaScript for simplicity)
const html = `
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>DJ Song Request</title>
    <style>
        * {
            box-sizing: border-box;
            font-family: 'Arial', sans-serif;
        }
        body {
            margin: 0;
            padding: 20px;
            background-color: #121212;
            color: white;
        }
        .container {
            max-width: 500px;
            margin: 0 auto;
            padding: 20px;
            background-color: #1e1e1e;
            border-radius: 10px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
        }
        h1 {
            text-align: center;
            color: #1db954;
        }
        .form-group {
            margin-bottom: 15px;
        }
        label {
            display: block;
            margin-bottom: 5px;
            font-weight: bold;
        }
        input, textarea {
            width: 100%;
            padding: 10px;
            border: 1px solid #333;
            border-radius: 5px;
            background-color: #2d2d2d;
            color: white;
        }
        button {
            width: 100%;
            padding: 12px;
            background-color: #1db954;
            color: white;
            border: none;
            border-radius: 5px;
            font-weight: bold;
            cursor: pointer;
            transition: background-color 0.3s;
        }
        button:hover {
            background-color: #1ed760;
        }
        button:disabled {
            background-color: #535353;
            cursor: not-allowed;
        }
        .success-message {
            color: #1db954;
            text-align: center;
            margin-top: 15px;
            display: none;
        }
        .error-message {
            color: #ff4d4d;
            text-align: center;
            margin-top: 15px;
            display: none;
        }
        .loading {
            text-align: center;
            display: none;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Request a Song</h1>
        
        <form id="songRequestForm">
            <div class="form-group">
                <label for="songTitle">Song Title*</label>
                <input type="text" id="songTitle" required placeholder="e.g., Bohemian Rhapsody">
            </div>
            
            <div class="form-group">
                <label for="artist">Artist*</label>
                <input type="text" id="artist" required placeholder="e.g., Queen">
            </div>
            
            <div class="form-group">
                <label for="guestName">Your Name (optional)</label>
                <input type="text" id="guestName" placeholder="e.g., John">
            </div>
            
            <div class="form-group">
                <label for="message">Special Message (optional)</label>
                <textarea id="message" rows="3" placeholder="e.g., Play this for my birthday!"></textarea>
            </div>
            
            <button type="submit" id="submitBtn">Send Request</button>
        </form>
        
        <div class="success-message" id="successMessage">
            Your song request has been sent to the DJ!
        </div>
        
        <div class="error-message" id="errorMessage">
            There was an error sending your request. Please try again.
        </div>
        
        <div class="loading" id="loading">
            Sending your request...
        </div>
    </div>

    <!-- Firebase SDK -->
    <script src="https://www.gstatic.com/firebasejs/8.10.0/firebase-app.js"></script>
    <script src="https://www.gstatic.com/firebasejs/8.10.0/firebase-database.js"></script>
    
    <script>
        // Your web app's Firebase configuration
        const firebaseConfig = {
            apiKey: "YOUR_API_KEY",
            authDomain: "YOUR_AUTH_DOMAIN",
            databaseURL: "YOUR_DATABASE_URL",
            projectId: "YOUR_PROJECT_ID",
            storageBucket: "YOUR_STORAGE_BUCKET",
            messagingSenderId: "YOUR_SENDER_ID",
            appId: "YOUR_APP_ID"
        };

        // Initialize Firebase
        firebase.initializeApp(firebaseConfig);
        const database = firebase.database();
        
        // DOM Elements
        const form = document.getElementById('songRequestForm');
        const submitBtn = document.getElementById('submitBtn');
        const successMessage = document.getElementById('successMessage');
        const errorMessage = document.getElementById('errorMessage');
        const loading = document.getElementById('loading');
        
        // Form submission handler
        form.addEventListener('submit', async (e) => {
            e.preventDefault();
            
            // Get form values
            const songTitle = document.getElementById('songTitle').value.trim();
            const artist = document.getElementById('artist').value.trim();
            const guestName = document.getElementById('guestName').value.trim() || 'Anonymous';
            const message = document.getElementById('message').value.trim();
            
            // Validate required fields
            if (!songTitle || !artist) {
                showError('Please fill in all required fields');
                return;
            }
            
            // Show loading state
            submitBtn.disabled = true;
            loading.style.display = 'block';
            errorMessage.style.display = 'none';
            
            try {
                // Create request object
                const request = {
                    songTitle,
                    artist,
                    guestName,
                    message,
                    timestamp: firebase.database.ServerValue.TIMESTAMP,
                    status: 'pending'
                };
                
                // Save to Firebase
                const requestsRef = database.ref('songRequests');
                await requestsRef.push(request);
                
                // Show success
                successMessage.style.display = 'block';
                form.reset();
                
                // Hide success after 5 seconds
                setTimeout(() => {
                    successMessage.style.display = 'none';
                }, 5000);
            } catch (error) {
                console.error('Error submitting request:', error);
                showError('Failed to send request. Please try again.');
            } finally {
                submitBtn.disabled = false;
                loading.style.display = 'none';
            }
        });
        
        // Helper function to show error message
        function showError(msg) {
            errorMessage.textContent = msg;
            errorMessage.style.display = 'block';
            
            // Hide error after 5 seconds
            setTimeout(() => {
                errorMessage.style.display = 'none';
            }, 5000);
        }
    </script>
</body>
</html>
`;

// For Node.js environment, you would typically separate this into HTML, CSS, and JS files
// This is a simplified version combining everything for demonstration purposes
console.log(html);
```
