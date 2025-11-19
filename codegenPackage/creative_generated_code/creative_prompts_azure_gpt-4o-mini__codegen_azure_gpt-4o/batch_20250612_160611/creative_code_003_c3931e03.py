"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://opti.lol
Prompt: Create a JavaScript function that alerts users when they exceed a certain amount of time spent on social media, based on the themes of addiction highlighted on https://opti.lol.
Generated: DETERMINISTIC_c3931e03e62c2f2e
Batch ID: 20250612_160611
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Function to monitor and alert users when they exceed a specified time limit
 * on social media usage. 
 * This function uses local storage to track usage time across sessions.
 * 
 * @param {number} timeLimit - Maximum allowable time on social media in minutes.
 */
function monitorSocialMediaUsage(timeLimit) {
    // Validate input
    if (!Number.isFinite(timeLimit) || timeLimit <= 0) {
        throw new Error('Invalid time limit. Please provide a positive number.');
    }

    // Constants
    const CHECK_INTERVAL = 1000 * 60; // Check every minute
    const SOCIAL_MEDIA_DOMAINS = ['facebook.com', 'instagram.com', 'twitter.com']; // Add more domains as needed

    // Helper: Check if the current domain is a social media domain
    function isSocialMediaDomain() {
        const currentDomain = window.location.hostname;
        return SOCIAL_MEDIA_DOMAINS.some(domain => currentDomain.includes(domain));
    }

    // Helper: Get or set usage time in local storage
    function getUsageTime() {
        const usage = localStorage.getItem('socialMediaUsageTime');
        return usage ? parseInt(usage, 10) : 0;
    }

    function setUsageTime(minutes) {
        localStorage.setItem('socialMediaUsageTime', minutes);
    }

    // Monitor usage
    if (isSocialMediaDomain()) {
        // Initial load: Increment usage time
        let usageTime = getUsageTime();
        setUsageTime(usageTime + 1);

        // Alert if time limit is exceeded
        if (usageTime >= timeLimit) {
            alert(
                `You've exceeded your daily social media usage limit of ${timeLimit} minutes. Consider taking a break!`
            );
        }

        // Set an interval to continue tracking usage
        setInterval(() => {
            usageTime = getUsageTime(); // Fetch current usage
            setUsageTime(usageTime + 1); // Increment usage by 1 minute

            if (usageTime >= timeLimit) {
                alert(
                    `You've exceeded your daily social media usage limit of ${timeLimit} minutes. Consider taking a break!`
                );
            }
        }, CHECK_INTERVAL);
    } else {
        console.log('Not a social media domain. Monitoring is inactive.');
    }
}

// Example usage:
// Monitor social media usage with a 60-minute daily limit
try {
    monitorSocialMediaUsage(60);
} catch (error) {
    console.error('Error initializing social media monitor:', error.message);
}
```
