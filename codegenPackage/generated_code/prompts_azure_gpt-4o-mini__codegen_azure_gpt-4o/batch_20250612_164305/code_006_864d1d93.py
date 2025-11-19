"""
Generated Code Metadata:
========================
Original URL: https://bafybeibp22amvhhrdkiajahcte2faf5d3vecbroua5yhnhk76jnpibn4de.ipfs.dweb.link
Prompt: Create a sample application that demonstrates the use of Particle Network's BTC Connect for onboarding Bitcoin users into L2s.
Generated: DETERMINISTIC_864d1d93c145876c
Batch ID: 20250612_164305
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Below is a sample application written in JavaScript using Node.js and React to demonstrate the use of Particle Network's BTC Connect for onboarding Bitcoin users into L2s. This assumes you have access to the Particle Network SDK and its BTC Connect functionality.

### Backend Code (Node.js)
```javascript
// server.js
const express = require('express');
const bodyParser = require('body-parser');
const dotenv = require('dotenv');
const ParticleNetwork = require('particle-network-sdk'); // Replace with actual SDK import

dotenv.config();

const app = express();
app.use(bodyParser.json());

// Initialize Particle Network SDK
const particle = new ParticleNetwork({
  apiKey: process.env.PARTICLE_API_KEY, // API key from Particle Network
  secretKey: process.env.PARTICLE_SECRET_KEY, // Secret key from Particle Network
});

// Endpoint to initiate BTC Connect onboarding
app.post('/api/onboard', async (req, res) => {
  try {
    const { userId } = req.body;

    // Validate input
    if (!userId) {
      return res.status(400).json({ error: 'User ID is required' });
    }

    // Create onboarding session for the user
    const session = await particle.createBTCConnectSession(userId);

    res.status(200).json({
      message: 'BTC Connect session created successfully',
      sessionId: session.id,
      redirectUrl: session.redirectUrl, // URL to redirect user for onboarding
    });
  } catch (error) {
    console.error('Error creating BTC Connect session:', error);
    res.status(500).json({ error: 'Failed to create BTC Connect session' });
  }
});

// Start the server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});
```

### Frontend Code (React)
```javascript
// App.js
import React, { useState } from 'react';
import axios from 'axios';

const App = () => {
  const [userId, setUserId] = useState('');
  const [redirectUrl, setRedirectUrl] = useState('');

  const handleOnboard = async () => {
    try {
      // Send request to backend to create BTC Connect session
      const response = await axios.post('/api/onboard', { userId });

      // Extract redirect URL from response
      setRedirectUrl(response.data.redirectUrl);
    } catch (error) {
      console.error('Error during onboarding:', error);
      alert('Failed to initiate onboarding. Please try again.');
    }
  };

  return (
    <div style={{ padding: '20px' }}>
      <h1>BTC Connect Onboarding</h1>
      <div>
        <label>
          User ID:
          <input
            type="text"
            value={userId}
            onChange={(e) => setUserId(e.target.value)}
            placeholder="Enter your User ID"
          />
        </label>
      </div>
      <button onClick={handleOnboard}>Start Onboarding</button>
      {redirectUrl && (
        <div>
          <p>Onboarding initiated successfully!</p>
          <a href={redirectUrl} target="_blank" rel="noopener noreferrer">
            Click here to complete onboarding
          </a>
        </div>
      )}
    </div>
  );
};

export default App;
```

### Environment Variables (`.env`)
```
PARTICLE_API_KEY=your_particle_api_key
PARTICLE_SECRET_KEY=your_particle_secret_key
PORT=3000
```

### Notes
1. Install required dependencies:
   ```
   npm install express body-parser dotenv axios particle-network-sdk
   ```
2. Run the backend server:
   ```
   node server.js
   ```
3. Run the React frontend:
   ```
   npm start
   ```
4. Ensure the Particle Network SDK is properly installed and configured. Replace `particle-network-sdk` with the actual SDK import path if necessary.
5. Replace placeholder API keys and secret keys with your actual credentials from Particle Network.
