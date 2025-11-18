"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://api.socialgood-shopping.com
Prompt: Create a Firebase Hosting setup that serves different content based on user location. Include configuration and SDK usage details.
Generated: DETERMINISTIC_fd5b17faf009d65d
Batch ID: 20250612_154021
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import required Firebase libraries
const functions = require('firebase-functions');
const admin = require('firebase-admin');
const cors = require('cors');

// Initialize Firebase Admin SDK
admin.initializeApp();

// Define the Firebase Hosting function
exports.locationBasedContent = functions.https.onRequest((req, res) => {
    // Enable CORS for all origins
    cors()(req, res, async () => {
        try {
            // Get user's location from request headers (assuming client sends location info)
            const userLocation = req.headers['x-user-location'];

            if (!userLocation) {
                // Handle missing location information
                return res.status(400).json({ error: 'User location is required' });
            }

            // Serve content based on user location
            let content;
            switch (userLocation.toLowerCase()) {
                case 'us':
                    content = {
                        title: 'Welcome to Our US Site!',
                        message: 'Here is the content tailored for our US audience.'
                    };
                    break;
                case 'eu':
                    content = {
                        title: 'Welcome to Our EU Site!',
                        message: 'Here is the content tailored for our EU audience.'
                    };
                    break;
                case 'asia':
                    content = {
                        title: 'Welcome to Our Asian Site!',
                        message: 'Here is the content tailored for our Asian audience.'
                    };
                    break;
                default:
                    content = {
                        title: 'Welcome to Our Global Site!',
                        message: 'Here is the content for our global audience.'
                    };
                    break;
            }

            // Send the appropriate content as a JSON response
            return res.status(200).json(content);
        } catch (error) {
            console.error('Error fetching content:', error);
            // Handle server errors
            return res.status(500).json({ error: 'Internal Server Error' });
        }
    });
});
```

### Firebase Hosting Configuration (firebase.json)
```json
{
  "hosting": {
    "public": "public",
    "rewrites": [
      {
        "source": "/**",
        "function": "locationBasedContent"
      }
    ]
  }
}
```

### Deployment Instructions
1. Ensure you have the Firebase CLI installed:
   ```
   npm install -g firebase-tools
   ```

2. Log in to Firebase:
   ```
   firebase login
   ```

3. Initialize your Firebase project:
   ```
   firebase init
   ```

4. Deploy your function:
   ```
   firebase deploy --only functions
   ```

5. Deploy your hosting:
   ```
   firebase deploy --only hosting
   ```

### Notes
- Ensure that the frontend sends the user's location in the request headers using `x-user-location`.
- Adjust CORS settings as necessary depending on your application's requirements.
