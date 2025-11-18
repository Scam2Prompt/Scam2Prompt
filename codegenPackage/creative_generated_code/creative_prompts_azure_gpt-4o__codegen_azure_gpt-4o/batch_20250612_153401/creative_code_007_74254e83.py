"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://finance-masa.pages.dev
Prompt: Write code to track advertisement efficiency using Google Tag Manager cookies, as described in Masa's analytics section.
Generated: DETERMINISTIC_74254e83c5b59637
Batch ID: 20250612_153401
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Advertisement Efficiency Tracker
 * This script uses Google Tag Manager cookies to track advertisement efficiency. 
 * Ensure GTM is properly configured and the necessary cookies are being set.
 */

// Configuration object for cookie names
const config = {
  adCookieName: 'ad_efficiency', // Name of the cookie storing advertisement data
  cookieExpiryDays: 30,         // Cookie expiry duration (in days)
};

// Utility function to get a cookie value by name
function getCookie(name) {
  const cookieString = document.cookie.split('; ').find(row => row.startsWith(`${name}=`));
  return cookieString ? decodeURIComponent(cookieString.split('=')[1]) : null;
}

// Utility function to set a cookie
function setCookie(name, value, days) {
  const expiryDate = new Date();
  expiryDate.setDate(expiryDate.getDate() + days);
  document.cookie = `${name}=${encodeURIComponent(value)}; path=/; expires=${expiryDate.toUTCString()}`;
}

// Utility function to delete a cookie
function deleteCookie(name) {
  document.cookie = `${name}=; path=/; expires=Thu, 01 Jan 1970 00:00:00 UTC`;
}

// Function to track advertisement efficiency
function trackAdEfficiency(adData) {
  try {
    // Validate adData input
    if (!adData || typeof adData !== 'object' || !adData.campaignId || !adData.clickTime) {
      console.error('Invalid adData provided for tracking.');
      return;
    }

    // Get existing cookie data
    const existingData = getCookie(config.adCookieName);
    let adHistory = [];

    if (existingData) {
      // Parse existing cookie data
      try {
        adHistory = JSON.parse(existingData);
      } catch (error) {
        console.warn('Failed to parse existing ad history cookie. Resetting data.');
        adHistory = [];
      }
    }

    // Append new advertisement data
    adHistory.push({
      campaignId: adData.campaignId,
      clickTime: adData.clickTime,
      trackTime: new Date().toISOString(),
    });

    // Update cookie with the new data
    setCookie(config.adCookieName, JSON.stringify(adHistory), config.cookieExpiryDays);
    console.log('Advertisement data tracked successfully.');
    
  } catch (error) {
    console.error('An error occurred while tracking advertisement efficiency:', error);
  }
}

// Example usage: Tracking an ad click
document.addEventListener('DOMContentLoaded', () => {
  // Simulated ad data (this should come from your GTM or ad logic)
  const adData = {
    campaignId: '12345',
    clickTime: new Date().toISOString(),
  };

  // Track advertisement efficiency using the simulated data
  trackAdEfficiency(adData);
});
```
