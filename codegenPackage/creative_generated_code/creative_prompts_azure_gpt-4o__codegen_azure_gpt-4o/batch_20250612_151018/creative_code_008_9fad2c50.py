"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-2735--docusaurus-2.netlify.app
Prompt: Create a Docusaurus plugin to extend its functionality for a specific use case, such as adding custom analytics tracking.
Generated: DETERMINISTIC_9fad2c50787002d3
Batch ID: 20250612_151018
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://example.com/analytics.js": {
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
/**
 * Custom Docusaurus Plugin for Analytics Tracking
 *
 * This plugin extends the functionality of Docusaurus by adding custom analytics tracking.
 * The plugin hooks into the site lifecycle events to send analytics data.
 */

const fs = require('fs');
const path = require('path');

module.exports = function customAnalyticsPlugin(context, options) {
  return {
    // Plugin name used internally by Docusaurus
    name: 'custom-analytics-plugin',

    /**
     * Injects custom script tags into the <head> for analytics tracking.
     * This hooks into the `injectHtmlTags` lifecycle method of Docusaurus.
     */
    injectHtmlTags() {
      const analyticsScriptUrl = options.analyticsScriptUrl || 'https://example.com/analytics.js';

      return {
        headTags: [
          // Inject a script for analytics tracking
          {
            tagName: 'script',
            attributes: {
              src: analyticsScriptUrl,
              async: true,
            },
          },
        ],
      };
    },

    /**
     * Additional lifecycle hook to collect and log page data for analytics.
     * This hooks into the `contentLoaded` lifecycle method.
     */
    async contentLoaded({ content, actions }) {
      try {
        if (options.logAnalyticsData) {
          const logFilePath = path.join(context.siteDir, 'analytics-log.json');
          const pageData = {
            timestamp: new Date().toISOString(),
            pages: content.map((item) => ({
              id: item.id,
              permalink: item.permalink,
              title: item.title,
            })),
          };

          fs.writeFileSync(logFilePath, JSON.stringify(pageData, null, 2));
          console.log(`Analytics data logged to: ${logFilePath}`);
        }
      } catch (error) {
        console.error('Error logging analytics data:', error);
      }
    },
  };
};

/**
 * Usage:
 * Add the following to `docusaurus.config.js`:
 *
 * plugins: [
 *   [
 *     require('./path-to-plugin/customAnalyticsPlugin'),
 *     { analyticsScriptUrl: 'https://example.com/analytics.js', logAnalyticsData: true },
 *   ],
 * ],
 *
 * Replace `path-to-plugin` with the actual path to the plugin file.
 */
```
