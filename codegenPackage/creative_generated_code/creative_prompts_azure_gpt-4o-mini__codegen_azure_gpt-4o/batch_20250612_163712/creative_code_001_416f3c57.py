"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://buft163.com
Prompt: Write a function in JavaScript that checks the loading speed of a webpage and suggests optimizations to improve its performance for better technical SEO.
Generated: DETERMINISTIC_416f3c57d44443df
Batch ID: 20250612_163712
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://example.com": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url=${encodeURIComponent": {
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
 * Function to check the loading speed of a webpage and provide optimization suggestions.
 * @param {string} url - The URL of the webpage to analyze.
 * @returns {Promise<object>} - A Promise that resolves to an object containing performance metrics and suggestions.
 */
async function checkPageSpeedAndSuggestOptimizations(url) {
  // Validate input
  if (typeof url !== "string" || !url.startsWith("http")) {
    throw new Error("Invalid URL. Please provide a valid webpage URL starting with 'http' or 'https'.");
  }

  try {
    // Use the Google PageSpeed Insights API for analysis
    const apiKey = "YOUR_API_KEY_HERE"; // Replace with your actual API key
    const apiEndpoint = `https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url=${encodeURIComponent(url)}&key=${apiKey}`;

    // Fetch data from the API
    const response = await fetch(apiEndpoint);
    if (!response.ok) {
      throw new Error(`Failed to fetch page speed data. HTTP status code: ${response.status}`);
    }

    const data = await response.json();

    // Extract key metrics
    const metrics = {
      performanceScore: data.lighthouseResult.categories.performance.score * 100,
      firstContentfulPaint: data.lighthouseResult.audits["first-contentful-paint"].displayValue,
      speedIndex: data.lighthouseResult.audits["speed-index"].displayValue,
      timeToInteractive: data.lighthouseResult.audits["interactive"].displayValue,
    };

    // Generate optimization suggestions
    const suggestions = [];
    if (metrics.performanceScore < 90) {
      suggestions.push("Consider optimizing images (e.g., compress or use modern formats like WebP).");
      suggestions.push("Enable browser caching for static assets.");
      suggestions.push("Minify CSS, JavaScript, and HTML files.");
      suggestions.push("Optimize server response times (e.g., use a CDN or upgrade hosting).");
      suggestions.push("Reduce render-blocking resources (e.g., defer or async loading of scripts).");
    } else {
      suggestions.push("Your webpage performs well. Maintain current optimization practices.");
    }

    // Return metrics and suggestions
    return {
      metrics,
      suggestions,
    };
  } catch (error) {
    // Handle errors gracefully
    console.error("An error occurred while checking page speed:", error.message);
    throw error;
  }
}

// Usage example
(async () => {
  const url = "https://example.com"; // Replace with the URL you want to analyze
  try {
    const result = await checkPageSpeedAndSuggestOptimizations(url);
    console.log("Performance Metrics:", result.metrics);
    console.log("Optimization Suggestions:", result.suggestions);
  } catch (error) {
    console.error("Failed to analyze webpage:", error.message);
  }
})();
```

**Note**: Replace `"YOUR_API_KEY_HERE"` with a valid API key for Google PageSpeed Insights. For production use, ensure the API key is securely stored and not hardcoded in your source code.
