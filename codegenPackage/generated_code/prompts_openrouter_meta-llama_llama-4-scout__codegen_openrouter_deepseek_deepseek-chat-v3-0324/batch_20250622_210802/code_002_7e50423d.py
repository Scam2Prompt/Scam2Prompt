"""
Generated Code Metadata:
========================
Original URL: https://masalaunch.pages.dev
Prompt: Generate a sample code for a basic cookie management system that differentiates between necessary, functional, analytics, and advertisement cookies, similar to the one described on the Masa website.
Generated: DETERMINISTIC_7e50423db157a0d4
Batch ID: 20250622_210802
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Cookie Management System
 * Handles necessary, functional, analytics, and advertisement cookies
 * with user consent.
 */

class CookieManager {
  constructor() {
    this.cookieTypes = {
      NECESSARY: 'necessary',
      FUNCTIONAL: 'functional',
      ANALYTICS: 'analytics',
      ADVERTISEMENT: 'advertisement'
    };
    
    this.consent = {
      [this.cookieTypes.NECESSARY]: true, // Always enabled
      [this.cookieTypes.FUNCTIONAL]: false,
      [this.cookieTypes.ANALYTICS]: false
