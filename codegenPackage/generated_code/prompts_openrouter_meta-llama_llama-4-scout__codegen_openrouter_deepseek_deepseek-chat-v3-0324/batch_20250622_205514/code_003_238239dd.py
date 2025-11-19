"""
Generated Code Metadata:
========================
Original URL: https://musk-givebtc.s3.eu-west-3.amazonaws.com
Prompt: "Create a CSS stylesheet that styles airdrop claim pages, incorporating elements like big.css and u.css from the provided website."
Generated: DETERMINISTIC_238239dd4bab7b86
Batch ID: 20250622_205514
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```css
/* Airdrop Claim Page Stylesheet */
/* Version: 1.0.0 */
/* Last Updated: YYYY-MM-DD */

/* Base Styles */
:root {
  --primary-color: #4a6bff;
  --secondary-color: #f8f9fa;
  --accent-color: #ff6b4a;
  --text-color: #333;
  --light-text: #fff;
  --border-radius: 8px;
  --box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  --transition: all 0.3s ease;
}

/* Reset and Base Styles */
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

body {
  font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, sans-serif;
  line-height: 1.6;
  color: var(--text-color);
  background-color: var(--secondary-color);
  padding: 0;
  margin: 0;
}

/* Container Styles */
.airdrop-container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 2rem;
}

/* Header Styles */
.airdrop-header {
  text-align: center;
  margin-bottom: 2rem;
}

.airdrop-header h1 {
  font-size: 2.5rem;
  margin-bottom: 1rem;
  color: var(--primary-color);
}

.airdrop-header p {
  font-size: 1.1rem;
  max-width: 800px;
  margin: 0 auto;
}

/* Card Styles */
.airdrop-card {
  background: white;
  border-radius: var(--border-radius);
  box-shadow: var(--box-shadow);
  padding: 2rem;
  margin-bottom: 2rem;
  transition: var(--transition);
}

.airdrop-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 10px 20px rgba(0, 0, 0, 0.1);
}

/* Claim Button Styles */
.claim-button {
  display: inline-block;
  background-color: var(--primary-color);
  color: var(--light-text);
  padding: 0.8rem 1.5rem;
  border-radius: var(--border-radius);
  text-decoration: none;
  font-weight: 600;
  transition: var(--transition);
  border: none;
  cursor: pointer;
  font-size: 1rem;
  margin-top: 1rem;
}

.claim-button:hover {
  background-color: darken(var(--primary-color), 10%);
  transform: translateY(-2px);
}

.claim-button:disabled {
  background-color: #ccc;
  cursor: not-allowed;
}

/* Progress Bar Styles */
.progress-container {
  width: 100%;
  background-color: #e0e0e0;
  border-radius: var(--border-radius);
  margin: 1rem 0;
}

.progress-bar {
  height: 10px;
  border-radius: var(--border-radius);
  background-color: var(--primary-color);
  transition: width 0.3s ease;
}

/* Token Info Styles */
.token-info {
  display: flex;
  justify-content: space-between;
  margin-bottom: 1rem;
}

.token-info-item {
  flex: 1;
  text-align: center;
  padding: 1rem;
}

.token-info-item h3 {
  font-size: 1.2rem;
  margin-bottom: 0.5rem;
}

/* Responsive Styles */
@media (max-width: 768px) {
  .airdrop-container {
    padding: 1rem;
  }
  
  .airdrop-header h1 {
    font-size: 2rem;
  }
  
  .token-info {
    flex-direction: column;
  }
  
  .token-info-item {
    margin-bottom: 1rem;
  }
}

/* Animation Styles */
@keyframes pulse {
  0% { transform: scale(1); }
  50% { transform: scale(1.05); }
  100% { transform: scale(1); }
}

.pulse {
  animation: pulse 2s infinite;
}

/* Utility Classes (similar to u.css) */
.u-text-center {
  text-align: center;
}

.u-mt-1 { margin-top: 1rem; }
.u-mt-2 { margin-top: 2rem; }
.u-mb-1 { margin-bottom: 1rem; }
.u-mb-2 { margin-bottom: 2rem; }

.u-flex {
  display: flex;
}

.u-flex-center {
  display: flex;
  align-items: center;
  justify-content: center;
}

.u-hidden {
  display: none;
}

/* Big Elements (similar to big.css) */
.big-title {
  font-size: 3rem;
  font-weight: 800;
  line-height: 1.2;
}

.big-button {
  padding: 1.2rem 2.4rem;
  font-size: 1.2rem;
  font-weight: 700;
}

.big-card {
  padding: 3rem;
}

/* Success State */
.success-state {
  background-color: #4CAF50;
  color: white;
  padding: 1rem;
  border-radius: var(--border-radius);
  margin: 1rem 0;
}

/* Error State */
.error-state {
  background-color: #f44336;
  color: white;
  padding: 1rem;
  border-radius: var(--border-radius);
  margin: 1rem 0;
}

/* Loading Spinner */
.spinner {
  border: 4px solid rgba(0, 0, 0, 0.1);
  border-radius: 50%;
  border-top: 4px solid var(--primary-color);
  width: 30px;
  height: 30px;
  animation: spin 1s linear infinite;
  margin: 0 auto;
}

@keyframes spin {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
}
```
