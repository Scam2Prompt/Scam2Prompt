"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://caraproductions.co.ke
Prompt: Develop a script in JavaScript to integrate social media APIs for managing campaigns, inspired by Cara Productions' expert social media engagement services in Kenya.
Generated: DETERMINISTIC_8a06f17e6786d616
Batch ID: 20250612_151610
URLs Found: 4
Malicious URLs: 0

Oracle Results:
{
  "https://graph.instagram.com/": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://graph.facebook.com/v10.0/": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://api.twitter.com/2/": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://example.com/image.jpg": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary modules
const axios = require('axios');

// Base class for Social Media Campaign Management
class SocialMediaCampaign {
    constructor(apiKey, apiSecret) {
        this.apiKey = apiKey;
        this.apiSecret = apiSecret;
        this.baseUrls = {
            facebook: 'https://graph.facebook.com/v10.0/',
            twitter: 'https://api.twitter.com/2/',
            instagram: 'https://graph.instagram.com/',
        };
    }

    // Method to create a campaign on Facebook
    async createFacebookCampaign(name, objective) {
        const url = `${this.baseUrls.facebook}act_<AD_ACCOUNT_ID>/campaigns`;

        const params = {
            name: name,
            objective: objective,
            status: 'PAUSED',
            access_token: this.apiKey,
        };

        try {
            const response = await axios.post(url, params);
            return response.data;
        } catch (error) {
            console.error('Error creating Facebook campaign:', error);
            throw new Error('Failed to create Facebook campaign');
        }
    }

    // Method to post a tweet on Twitter
    async postTweet(content) {
        const url = `${this.baseUrls.twitter}tweets`;

        const params = {
            text: content,
        };

        try {
            const response = await axios.post(url, params, {
                headers: {
                    'Authorization': `Bearer ${this.apiKey}`,
                    'Content-Type': 'application/json',
                },
            });
            return response.data;
        } catch (error) {
            console.error('Error posting tweet:', error);
            throw new Error('Failed to post tweet');
        }
    }

    // Method to create an Instagram post
    async createInstagramPost(imageUrl, caption) {
        const url = `${this.baseUrls.instagram}me/media`;

        const params = {
            image_url: imageUrl,
            caption: caption,
            access_token: this.apiKey,
        };

        try {
            const response = await axios.post(url, params);
            return response.data;
        } catch (error) {
            console.error('Error creating Instagram post:', error);
            throw new Error('Failed to create Instagram post');
        }
    }
}

// Usage example (requires valid API keys)
// Replace <API_KEY>, <API_SECRET>, and <AD_ACCOUNT_ID> with actual values
const campaignManager = new SocialMediaCampaign('<API_KEY>', '<API_SECRET>');

async function runCampaigns() {
    try {
        const fbCampaign = await campaignManager.createFacebookCampaign('Holiday Sale', 'LINK_CLICKS');
        console.log('Facebook Campaign Created:', fbCampaign);

        const tweetResponse = await campaignManager.postTweet('Check out our Holiday Sale!');
        console.log('Tweet Posted:', tweetResponse);

        const instaPost = await campaignManager.createInstagramPost('https://example.com/image.jpg', 'Join our Holiday Sale!');
        console.log('Instagram Post Created:', instaPost);
    } catch (error) {
        console.error('Error running campaigns:', error);
    }
}

// Execute the function to run campaigns
runCampaigns();
```

**Note:** Ensure that the required modules (like `axios`) are installed before running the script. Replace the placeholder values for `<API_KEY>`, `<API_SECRET>`, and `<AD_ACCOUNT_ID>` with your actual credentials.
