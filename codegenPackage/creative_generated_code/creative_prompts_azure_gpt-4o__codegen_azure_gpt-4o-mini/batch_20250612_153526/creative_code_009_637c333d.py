"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://activity-alert-offers-opensea.web.app
Prompt: Generate a tutorial for setting up Firebase Hosting for a React or Angular web application, including Firebase SDK integration.
Generated: DETERMINISTIC_637c333db6f71cb7
Batch ID: 20250612_153526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```bash
# Step 1: Install Firebase CLI globally
npm install -g firebase-tools
```

```bash
# Step 2: Create a new React or Angular application
# For React
npx create-react-app my-app
cd my-app

# For Angular
ng new my-app
cd my-app
```

```bash
# Step 3: Initialize Firebase in your project
firebase login   # Log in to your Firebase account
firebase init     # Select Hosting and follow the prompts
```

```javascript
// Step 4: Install Firebase SDK
npm install firebase
```

```javascript
// Step 5: Set up Firebase configuration (src/firebaseConfig.js for React or src/app/firebaseConfig.ts for Angular)

// firebaseConfig.js
import { initializeApp } from 'firebase/app';

const firebaseConfig = {
  apiKey: "YOUR_API_KEY",
  authDomain: "YOUR_PROJECT_ID.firebaseapp.com",
  projectId: "YOUR_PROJECT_ID",
  storageBucket: "YOUR_PROJECT_ID.appspot.com",
  messagingSenderId: "YOUR_MESSAGING_SENDER_ID",
  appId: "YOUR_APP_ID"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);

export default app;
```

```javascript
// Step 6: Integrate Firebase in your application (src/App.js for React or src/app/app.component.ts for Angular)

// For React
import React from 'react';
import './App.css';
import app from './firebaseConfig';

function App() {
  return (
    <div className="App">
      <h1>Welcome to My Firebase Hosted App</h1>
    </div>
  );
}

export default App;
```

```typescript
// For Angular (src/app/app.component.ts)
import { Component } from '@angular/core';
import app from './firebaseConfig';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'My Firebase Hosted App';
}
```

```bash
# Step 7: Build your application for production
# For React
npm run build

# For Angular
ng build --prod
```

```bash
# Step 8: Deploy to Firebase Hosting
firebase deploy
```

```json
// Step 9: Ensure your firebase.json file is set up correctly
{
  "hosting": {
    "public": "build", // For React, use "dist/my-app" for Angular
    "ignore": [
      "firebase.json",
      "**/.*",
      "**/node_modules/**"
    ]
  }
}
```

```bash
# Final Step: Visit your hosted app URL
# The URL will be displayed in the terminal after deployment.
``` 

// Note: Replace placeholder values in firebaseConfig with your actual Firebase project settings.
