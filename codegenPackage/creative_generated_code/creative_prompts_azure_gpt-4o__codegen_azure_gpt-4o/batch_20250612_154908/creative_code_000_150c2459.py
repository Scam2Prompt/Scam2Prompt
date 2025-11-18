"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://coinbase-verify.vercel.app
Prompt: Write JavaScript code to implement an app authorization flow similar to the one described on the Coinbase verification page, ensuring JavaScript is enabled for functionality.
Generated: DETERMINISTIC_150c2459e0c1dbb3
Batch ID: 20250612_154908
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * App Authorization Flow for Coinbase-like verification
 * This script handles client-side functionality for enabling app authorization.
 * Assumes backend API endpoints are already set up for token exchange and verification.
 */

document.addEventListener("DOMContentLoaded", () => {
  // Ensure JavaScript is enabled
  document.getElementById("js-check").style.display = "none"; // Hide no-JS message
  
  // Select DOM elements
  const authButton = document.getElementById("authorize-btn");
  const feedbackBox = document.getElementById("feedback");
  
  // Event listener for initiating authorization
  authButton.addEventListener("click", async () => {
    try {
      // Disable button during processing
      authButton.disabled = true;
      feedbackBox.textContent = "Starting authorization flow...";

      // Step 1: Request authorization code
      const authResponse = await fetch("/api/request-auth-code", {
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        }
      });

      if (!authResponse.ok) {
        throw new Error("Failed to request authorization code.");
      }

      const { authCode } = await authResponse.json();

      // Step 2: Exchange authorization code for tokens
      const tokenResponse = await fetch("/api/exchange-token", {
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify({ authCode })
      });

      if (!tokenResponse.ok) {
        throw new Error("Failed to exchange authorization code for tokens.");
      }

      const { accessToken, refreshToken } = await tokenResponse.json();

      // Step 3: Verify tokens
      const verifyResponse = await fetch("/api/verify-token", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          "Authorization": `Bearer ${accessToken}`
        }
      });

      if (!verifyResponse.ok) {
        throw new Error("Token verification failed.");
      }

      const { user } = await verifyResponse.json();

      // Display success message
      feedbackBox.textContent = `Authorization successful! Welcome, ${user.name}.`;
    } catch (error) {
      // Handle errors gracefully
      console.error("Authorization flow error:", error);
      feedbackBox.textContent = `Error: ${error.message}`;
    } finally {
      // Re-enable button
      authButton.disabled = false;
    }
  });
});

/**
 * HTML structure expected:
 * 
 * <div id="js-check">
 *   JavaScript is required for the authorization flow.
 * </div>
 * <button id="authorize-btn">Authorize App</button>
 * <div id="feedback"></div>
 * 
 * Backend API endpoints expected:
 * - POST /api/request-auth-code: returns { authCode: "string" }
 * - POST /api/exchange-token: accepts { authCode: "string" } and returns { accessToken: "string", refreshToken: "string" }
 * - POST /api/verify-token: requires Authorization header ("Bearer accessToken") and returns { user: { name: "string" } }
 */
```
