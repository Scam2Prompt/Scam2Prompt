"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wpcontrol.be
Prompt: Generate JavaScript code to dynamically switch between WPControl themes on a WordPress site.
Generated: DETERMINISTIC_21a8eee7ea711da4
Batch ID: 20250612_152405
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Dynamically switch between WPControl themes on a WordPress site.
 * This script uses the WordPress REST API to update the active theme.
 * Ensure the user has sufficient permissions to change the theme.
 */

// Function to switch themes
async function switchTheme(newThemeSlug) {
  // WordPress REST API endpoint for updating themes
  const endpoint = '/wp-json/wp/v2/themes';

  // Data payload
  const payload = {
    theme: newThemeSlug, // Slug of the theme to activate
  };

  try {
    // Send a PUT request to switch the theme
    const response = await fetch(endpoint, {
      method: 'PUT',
      headers: {
        'Content-Type': 'application/json', // Specify JSON request format
        'X-WP-Nonce': wpApiSettings.nonce, // WordPress nonce for secure requests
      },
      body: JSON.stringify(payload), // Convert payload to JSON
    });

    // Check if the response is successful
    if (!response.ok) {
      throw new Error(`Failed to switch theme. Status: ${response.status}`);
    }

    // Parse the JSON response
    const data = await response.json();

    // Confirm the theme has been switched
    console.log(`Theme successfully switched to: ${data.theme}`);
    alert(`Theme switched to: ${data.theme}`); // Alert user of successful switch
  } catch (error) {
    // Handle errors gracefully
    console.error('Error switching theme:', error);
    alert(`An error occurred while switching themes: ${error.message}`);
  }
}

// Example usage: Switch to a theme with slug 'my-new-theme'
switchTheme('my-new-theme');
```

> **Important Notes:**
> - Ensure the WordPress site has the REST API enabled.
> - The `wpApiSettings.nonce` must be available and passed securely to authenticate the request.
> - Users need sufficient permissions to change themes; typically, this requires administrative privileges.
