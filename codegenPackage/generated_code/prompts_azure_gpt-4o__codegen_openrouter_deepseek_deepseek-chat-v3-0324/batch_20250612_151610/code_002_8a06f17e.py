"""
Generated Code Metadata:
========================
Original URL: https://caraproductions.co.ke
Prompt: Develop a script in JavaScript to integrate social media APIs for managing campaigns, inspired by Cara Productions' expert social media engagement services in Kenya.
Generated: DETERMINISTIC_8a06f17e6786d616
Batch ID: 20250612_151610
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://graph.facebook.com": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://api.twitter.com/2": {
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
/**
 * Social Media Campaign Manager
 * Integrates with Facebook, Twitter, and Instagram APIs to manage campaigns
 * Inspired by Cara Productions' social media engagement services
 */

const axios = require('axios');
const { OAuth2Client } = require('google-auth-library');

// Configuration for social media APIs
const config = {
  facebook: {
    apiVersion: 'v12.0',
    baseUrl: 'https://graph.facebook.com',
    pageId: process.env.FACEBOOK_PAGE_ID,
    accessToken: process.env.FACEBOOK_ACCESS_TOKEN
  },
  twitter: {
    baseUrl: 'https://api.twitter.com/2',
    bearerToken: process.env.TWITTER_BEARER_TOKEN
  },
  instagram: {
    baseUrl: 'https://graph.facebook.com',
    apiVersion: 'v12.0',
    accessToken: process.env.INSTAGRAM_ACCESS_TOKEN
  }
};

class SocialMediaManager {
  constructor() {
    this.facebookClient = this._createFacebookClient();
    this.twitterClient = this._createTwitterClient();
    this.instagramClient = this._createInstagramClient();
  }

  _createFacebookClient() {
    return axios.create({
      baseURL: `${config.facebook.baseUrl}/${config.facebook.apiVersion}`,
      headers: {
        'Authorization': `Bearer ${config.facebook.accessToken}`,
        'Content-Type': 'application/json'
      }
    });
  }

  _createTwitterClient() {
    return axios.create({
      baseURL: config.twitter.baseUrl,
      headers: {
        'Authorization': `Bearer ${config.twitter.bearerToken}`,
        'Content-Type': 'application/json'
      }
    });
  }

  _createInstagramClient() {
    return axios.create({
      baseURL: `${config.instagram.baseUrl}/${config.instagram.apiVersion}`,
      headers: {
        'Authorization': `Bearer ${config.instagram.accessToken}`,
        'Content-Type': 'application/json'
      }
    });
  }

  /**
   * Post content to Facebook
   * @param {string} message - The post content
   * @param {string} [link] - Optional link to include
   * @returns {Promise<Object>} API response
   */
  async postToFacebook(message, link = null) {
    try {
      const postData = {
        message,
        access_token: config.facebook.accessToken
      };

      if (link) {
        postData.link = link;
      }

      const response = await this.facebookClient.post(
        `/${config.facebook.pageId}/feed`,
        postData
      );
      return response.data;
    } catch (error) {
      console.error('Facebook post error:', error.response?.data || error.message);
      throw new Error('Failed to post to Facebook');
    }
  }

  /**
   * Tweet content to Twitter
   * @param {string} text - The tweet content
   * @returns {Promise<Object>} API response
   */
  async postToTwitter(text) {
    try {
      const response = await this.twitterClient.post('/tweets', {
        text
      });
      return response.data;
    } catch (error) {
      console.error('Twitter post error:', error.response?.data || error.message);
      throw new Error('Failed to post to Twitter');
    }
  }

  /**
   * Post content to Instagram
   * @param {string} imageUrl - URL of the image to post
   * @param {string} caption - The post caption
   * @returns {Promise<Object>} API response
   */
  async postToInstagram(imageUrl, caption) {
    try {
      // First create the media container
      const mediaResponse = await this.instagramClient.post(
        `${config.instagram.businessAccountId}/media`,
        {
          image_url: imageUrl,
          caption,
          access_token: config.instagram.accessToken
        }
      );

      // Then publish the container
      const publishResponse = await this.instagramClient.post(
        `${config.instagram.businessAccountId}/media_publish`,
        {
          creation_id: mediaResponse.data.id,
          access_token: config.instagram.accessToken
        }
      );

      return publishResponse.data;
    } catch (error) {
      console.error('Instagram post error:', error.response?.data || error.message);
      throw new Error('Failed to post to Instagram');
    }
  }

  /**
   * Schedule a post across multiple platforms
   * @param {Object} content - Content to post
   * @param {Date} scheduleTime - When to post
   * @param {Array<string>} platforms - Platforms to post to
   * @returns {Promise<Array<Object>>} Array of responses
   */
  async schedulePost(content, scheduleTime, platforms) {
    try {
      const now = new Date();
      const delay = scheduleTime.getTime() - now.getTime();

      if (delay < 0) {
        throw new Error('Schedule time must be in the future');
      }

      return new Promise((resolve) => {
        setTimeout(async () => {
          const results = [];
          for (const platform of platforms) {
            try {
              let result;
              switch (platform.toLowerCase()) {
                case 'facebook':
                  result = await this.postToFacebook(content.message, content.link);
                  break;
                case 'twitter':
                  result = await this.postToTwitter(content.text);
                  break;
                case 'instagram':
                  result = await this.postToInstagram(content.imageUrl, content.caption);
                  break;
                default:
                  throw new Error(`Unsupported platform: ${platform}`);
              }
              results.push({ platform, result });
            } catch (error) {
              results.push({ platform, error: error.message });
            }
          }
          resolve(results);
        }, delay);
      });
    } catch (error) {
      console.error('Scheduling error:', error.message);
      throw new Error('Failed to schedule post');
    }
  }

  /**
   * Get analytics for a campaign
   * @param {string} platform - Social media platform
   * @param {string} postId - ID of the post
   * @param {string} [metric] - Specific metric to retrieve
   * @returns {Promise<Object>} Analytics data
   */
  async getAnalytics(platform, postId, metric = null) {
    try {
      let response;
      switch (platform.toLowerCase()) {
        case 'facebook':
          response = await this.facebookClient.get(
            `/${postId}/insights${metric ? `/${metric}` : ''}`
          );
          break;
        case 'twitter':
          response = await this.twitterClient.get(
            `/tweets/${postId}${metric ? `?tweet.fields=${metric}` : ''}`
          );
          break;
        case 'instagram':
          response = await this.instagramClient.get(
            `/${postId}/insights${metric ? `?metric=${metric}` : ''}`
          );
          break;
        default:
          throw new Error(`Unsupported platform: ${platform}`);
      }
      return response.data;
    } catch (error) {
      console.error('Analytics error:', error.response?.data || error.message);
      throw new Error(`Failed to get ${platform} analytics`);
    }
  }
}

module.exports = SocialMediaManager;
```
