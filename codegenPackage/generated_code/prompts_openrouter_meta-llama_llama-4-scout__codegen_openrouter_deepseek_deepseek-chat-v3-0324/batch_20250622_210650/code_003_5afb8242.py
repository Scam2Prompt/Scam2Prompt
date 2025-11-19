"""
Generated Code Metadata:
========================
Original URL: https://budbeeindia.com
Prompt: Create a JavaScript code snippet to integrate Instagram's API for a fashion brand, as mentioned in BudBee India's article on Instagram for fashion brands.
Generated: DETERMINISTIC_5afb82422ff3bcf9
Batch ID: 20250622_210650
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://graph.instagram.com": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://api.instagram.com": {
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
// Instagram API integration for a fashion brand
// Requires Instagram Basic Display API credentials

const axios = require('axios');
const express = require('express');
const app = express();
require('dotenv').config();

// Instagram API configuration
const INSTAGRAM_APP_ID = process.env.INSTAGRAM_APP_ID;
const INSTAGRAM_APP_SECRET = process.env.INSTAGRAM_APP_SECRET;
const INSTAGRAM_REDIRECT_URI = process.env.INSTAGRAM_REDIRECT_URI;
const INSTAGRAM_API_BASE_URL = 'https://api.instagram.com';
const INSTAGRAM_GRAPH_API_BASE_URL = 'https://graph.instagram.com';

// Initialize express middleware
app.use(express.json());
app.use(express.urlencoded({ extended: true }));

/**
 * Redirects user to Instagram authorization page
 */
app.get('/auth/instagram', (req, res) => {
    const authUrl = `${INSTAGRAM_API_BASE_URL}/oauth/authorize?client_id=${INSTAGRAM_APP_ID}&redirect_uri=${INSTAGRAM_REDIRECT_URI}&scope=user_profile,user_media&response_type=code`;
    res.redirect(authUrl);
});

/**
 * Handles Instagram callback and exchanges code for access token
 */
app.get('/auth/instagram/callback', async (req, res) => {
    try {
        const { code } = req.query;
        if (!code) {
            throw new Error('Authorization code not found');
        }

        // Exchange code for short-lived access token
        const tokenResponse = await axios.post(`${INSTAGRAM_API_BASE_URL}/oauth/access_token`, {
            client_id: INSTAGRAM_APP_ID,
            client_secret: INSTAGRAM_APP_SECRET,
            grant_type: 'authorization_code',
            redirect_uri: INSTAGRAM_REDIRECT_URI,
            code
        });

        const { access_token, user_id } = tokenResponse.data;

        // Exchange short-lived token for long-lived token
        const longLivedTokenResponse = await axios.get(`${INSTAGRAM_GRAPH_API_BASE_URL}/access_token`, {
            params: {
                grant_type: 'ig_exchange_token',
                client_secret: INSTAGRAM_APP_SECRET,
                access_token
            }
        });

        const longLivedToken = longLivedTokenResponse.data.access_token;

        // Store tokens securely (in production, use a secure database)
        // For demo purposes, we're just returning them
        res.json({
            userId: user_id,
            accessToken: access_token,
            longLivedToken: longLivedToken
        });

    } catch (error) {
        console.error('Instagram auth error:', error.message);
        res.status(500).json({ error: 'Failed to authenticate with Instagram' });
    }
});

/**
 * Fetches user media from Instagram
 */
app.get('/api/instagram/media', async (req, res) => {
    try {
        const { accessToken } = req.query;
        if (!accessToken) {
            throw new Error('Access token required');
        }

        const mediaResponse = await axios.get(`${INSTAGRAM_GRAPH_API_BASE_URL}/me/media`, {
            params: {
                fields: 'id,caption,media_type,media_url,permalink,thumbnail_url,timestamp',
                access_token: accessToken
            }
        });

        // Filter for fashion-related posts (basic example)
        const fashionPosts = mediaResponse.data.data.filter(post => {
            return post.caption && 
                  (post.caption.includes('#fashion') || 
                   post.caption.includes('#style') ||
                   post.media_type === 'IMAGE');
        });

        res.json(fashionPosts);
    } catch (error) {
        console.error('Error fetching Instagram media:', error.message);
        res.status(500).json({ error: 'Failed to fetch media from Instagram' });
    }
});

// Start server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Server running on port ${PORT}`);
});

// Error handling middleware
app.use((err, req, res, next) => {
    console.error(err.stack);
    res.status(500).json({ error: 'Something went wrong!' });
});
```
