"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://suifoundation.com
Prompt: Provide an example of how to use Sui's zkLogin authentication for seamless user onboarding in a Web3 commerce application.
Generated: DETERMINISTIC_bc8380c995bc2abb
Batch ID: 20250612_145832
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary modules and dependencies
import { SuiWallet, zkLogin } from '@mysten/sui-sdk'; // Import Sui SDK
import { createClient } from '@mysten/sui-web3-commerce-sdk'; // Hypothetical Sui Web3 commerce SDK
import express from 'express'; // Backend framework for creating an API

// Initialize Express app
const app = express();

// Middleware to parse JSON request body
app.use(express.json());

// Example endpoint for user onboarding
app.post('/api/onboard', async (req, res) => {
  try {
    // Extract zkLogin credentials from the request body
    const { zkLoginToken } = req.body;

    if (!zkLoginToken) {
      return res.status(400).json({ error: 'Missing zkLoginToken in request body' });
    }

    // Authenticate user seamlessly using zkLogin
    const userAuthData = await zkLogin.authenticate(zkLoginToken);

    if (!userAuthData || !userAuthData.publicKey) {
      return res.status(401).json({ error: 'Authentication failed' });
    }

    // Create or retrieve the user profile in Web3 commerce app
    const commerceClient = createClient();
    const userProfile = await commerceClient.getOrCreateUserProfile(userAuthData.publicKey);

    // Respond with the user profile and success message
    res.status(200).json({
      message: 'User onboarded successfully',
      userProfile,
    });
  } catch (error) {
    // Error handling
    console.error('Error during user onboarding:', error.message);
    res.status(500).json({ error: 'Internal server error' });
  }
});

// Start the Express server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});
```
