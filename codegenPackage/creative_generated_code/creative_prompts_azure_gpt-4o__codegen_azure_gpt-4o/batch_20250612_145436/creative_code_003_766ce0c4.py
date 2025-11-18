"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mettamskchromextensn.onepage.website
Prompt: Write a browser automation script using Puppeteer or Selenium to navigate the MetaMask Chrome Extension settings and clear activity data.
Generated: DETERMINISTIC_766ce0c45b934476
Batch ID: 20250612_145436
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import the Puppeteer library
const puppeteer = require('puppeteer');

// Main asynchronous function to execute the Puppeteer script
(async () => {
  let browser;
  try {
    // Launch a new browser instance with a MetaMask extension
    browser = await puppeteer.launch({
      headless: false, // Run the browser in non-headless mode so MetaMask can be interacted with
      executablePath: '/path/to/your/chrome', // Ensure this points to the Chrome/Chromium executable
      args: [
        '--no-sandbox',
        '--disable-setuid-sandbox',
        '--disable-extensions-except=/path/to/metamask/extension', // Path to the unpacked MetaMask extension
        '--load-extension=/path/to/metamask/extension', // Load the MetaMask extension
      ],
    });

    // Get the first page (MetaMask opens in the first tab)
    const pages = await browser.pages();
    const metaMaskPage = pages[0];

    // Wait for MetaMask to load
    await metaMaskPage.waitForTimeout(5000); // Adjust delay based on MetaMask's loading time

    // Navigate through MetaMask's UI to go to settings
    await metaMaskPage.waitForSelector('.account-menu__icon', { visible: true });
    await metaMaskPage.click('.account-menu__icon'); // Open account menu

    await metaMaskPage.waitForSelector('.account-menu__item--clickable', { visible: true });
    const settingsOption = await metaMaskPage.$x("//div[contains(text(), 'Settings')]");
    if (settingsOption.length > 0) {
      await settingsOption[0].click(); // Click "Settings"
    }

    // Navigate to the "Security & Privacy" section
    await metaMaskPage.waitForSelector("button[title='Security & Privacy']", { visible: true });
    await metaMaskPage.click("button[title='Security & Privacy']");

    // Locate the "Clear Activity" button and click it
    await metaMaskPage.waitForSelector("button[data-testid='clear-activity']", { visible: true });
    await metaMaskPage.click("button[data-testid='clear-activity']");

    // Confirm clearing activity (MetaMask usually shows a confirmation dialog)
    await metaMaskPage.waitForSelector("button[data-testid='confirm-clear-activity']", { visible: true });
    await metaMaskPage.click("button[data-testid='confirm-clear-activity']");

    console.log('Activity data cleared successfully.');
  } catch (error) {
    console.error('An error occurred while automating MetaMask:', error);
  } finally {
    // Safely close the browser if it was launched
    if (browser) {
      await browser.close();
    }
  }
})();
```

### Notes:
1. Replace `/path/to/metamask/extension` with the actual path to the unpacked MetaMask extension.
2. Replace `/path/to/your/chrome` with the correct path to your Chrome/Chromium executable.
3. Ensure you have MetaMask installed as an unpacked extension before running this script.

This script is designed to interact with the MetaMask extension using Puppeteer. Make sure the environment running this script has proper permissions and configurations for browser automation.
