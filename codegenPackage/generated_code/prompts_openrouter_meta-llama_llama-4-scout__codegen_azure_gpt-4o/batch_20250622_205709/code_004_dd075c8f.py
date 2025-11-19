"""
Generated Code Metadata:
========================
Original URL: https://unitedsoftwareservices.com
Prompt: "Create a digital marketing strategy for a small business using Google Analytics, Google Ads, and social media platforms, and provide a sample code for tracking website conversions using Google Tag Manager."
Generated: DETERMINISTIC_dd075c8fc4b41a0c
Batch ID: 20250622_205709
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Sample code for tracking website conversions using Google Tag Manager (GTM)

// This script is intended to be used within Google Tag Manager as a custom HTML tag.
// It tracks conversions on a website and sends data to Google Analytics.

// Ensure GTM is properly installed on your website before using this code.
// Replace 'GA_MEASUREMENT_ID' with your actual Google Analytics Measurement ID.

// Custom HTML Tag for Conversion Tracking
<script>
  // Function to send conversion event to Google Analytics
  function trackConversion(eventCategory, eventAction, eventLabel, eventValue) {
    try {
      // Check if the gtag function is available
      if (typeof gtag === 'function') {
        // Send event data to Google Analytics
        gtag('event', 'conversion', {
          event_category: eventCategory, // Category of the event (e.g., 'Purchase')
          event_action: eventAction,    // Action performed (e.g., 'Buy Now')
          event_label: eventLabel,      // Label for the event (e.g., 'Product XYZ')
          value: eventValue             // Value associated with the event (e.g., revenue)
        });
        console.log('Conversion event tracked successfully.');
      } else {
        console.error('Google Analytics gtag function is not available.');
      }
    } catch (error) {
      console.error('Error tracking conversion event:', error);
    }
  }

  // Example usage: Track a purchase conversion
  // Replace these values with dynamic data from your website
  const eventCategory = 'Purchase';
  const eventAction = 'Buy Now';
  const eventLabel = 'Product XYZ';
  const eventValue = 49.99; // Example revenue value

  // Call the function to track the conversion
  trackConversion(eventCategory, eventAction, eventLabel, eventValue);
</script>

// Notes:
// 1. This script should be added as a Custom HTML tag in Google Tag Manager.
// 2. Configure the tag to fire on specific pages or events where conversions occur.
// 3. Ensure your Google Analytics property is set up to receive event data.
// 4. Test the implementation thoroughly using Google Tag Manager's preview mode.
```
