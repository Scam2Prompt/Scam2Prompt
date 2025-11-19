"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://arbitrum-dao-fork.vercel.app
Prompt: How can I modify the "Welcome to Astro" message in the src/pages directory of my Astro project?
Generated: DETERMINISTIC_502e6b874c42622b
Batch ID: 20250612_135417
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// src/pages/index.astro

---
import { Layout } from '../components/Layout.astro';

// Define the welcome message
const welcomeMessage = "Welcome to Astro! Explore the universe of possibilities.";

// Define a layout for the page
const pageTitle = "Home Page";
---

<!-- Page layout with a welcome message -->
<Layout title={pageTitle}>
  <main>
    <h1>{welcomeMessage}</h1>
    <p>Get started with building your static site using Astro!</p>
  </main>
</Layout>
```
