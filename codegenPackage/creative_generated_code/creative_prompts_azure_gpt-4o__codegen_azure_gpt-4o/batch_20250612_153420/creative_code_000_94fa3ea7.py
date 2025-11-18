"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://launchpad-allybuildapp.pages.dev
Prompt: Write code to integrate Particle Auth for user authentication in a decentralized application, referencing its support for Google, Twitter, Facebook, Apple, Discord, and email login methods.
Generated: DETERMINISTIC_94fa3ea79176a1fd
Batch ID: 20250612_153420
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import required modules and libraries
const express = require('express'); // Web server framework
const bodyParser = require('body-parser'); // Middleware for parsing request bodies
const { ParticleNetwork } = require('@particle-network/auth'); // Particle Auth SDK

// Initialize the Express app
const app = express();
app.use(bodyParser.json()); // Use JSON middleware

// Particle Network configuration
const particleConfig = {
  projectId: 'YOUR_PROJECT_ID', // Replace with your Particle project ID
  clientKey: 'YOUR_CLIENT_KEY', // Replace with your Particle client key
  redirectURI: 'YOUR_REDIRECT_URI', // Replace with your redirect URI
};

// Initialize Particle Network instance
const particle = new ParticleNetwork(particleConfig);

// Endpoint to initiate login with Particle Auth
app.post('/auth/login', async (req, res) => {
  try {
    const { provider } = req.body; // Extract the provider from the request body

    // Validate provider input
    if (
      !['google', 'twitter', 'facebook', 'apple', 'discord', 'email'].includes(
        provider
      )
    ) {
      return res.status(400).json({
        error: 'Invalid provider. Supported providers: google, twitter, facebook, apple, discord, email.',
      });
    }

    // Generate login URL based on provider
    const loginUrl = particle.generateLoginUrl(provider);

    // Respond with the login URL (frontend should redirect user to this URL)
    res.status(200).json({ loginUrl });
  } catch (error) {
    console.error('Error in login route:', error.message);
    res.status(500).json({ error: 'Internal server error' });
  }
});

// Endpoint to handle Particle Auth callback after user login
app.post('/auth/callback', async (req, res) => {
  try {
    const { token } = req.body; // Extract the token from the request body

    // Validate input
    if (!token) {
      return res.status(400).json({ error: 'Token is required.' });
    }

    // Authenticate user using Particle Auth
    const user = await particle.authenticateUser(token);

    // Check if authentication was successful
    if (!user) {
      return res.status(401).json({ error: 'Authentication failed.' });
    }

    // Respond with authenticated user information
    res.status(200).json({ user });
  } catch (error) {
    console.error('Error in callback route:', error.message);
    res.status(500).json({ error: 'Internal server error' });
  }
});

// Start the Express server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}.`);
});

// Note: Replace placeholder values (YOUR_PROJECT_ID, YOUR_CLIENT_KEY, YOUR_REDIRECT_URI) with actual values from your Particle Auth setup.
// Make sure to install required dependencies (express, body-parser, @particle-network/auth) using npm or yarn.
```
