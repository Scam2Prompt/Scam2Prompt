"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://activity-opensea-io.web.app
Prompt: Write code to enable HTTPS and configure caching for a web application hosted on Firebase Hosting.
Generated: DETERMINISTIC_c904f9525c782102
Batch ID: 20250612_151659
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is the code to enable HTTPS and configure caching for a web application hosted on Firebase Hosting:

```json
{
  "hosting": {
    "public": "public", // Directory containing your web application files
    "ignore": [
      "firebase.json", 
      "**/.*", 
      "**/node_modules/**"
    ],
    "headers": [
      {
        "source": "**/*.html", // Cache configuration for HTML files
        "headers": [
          {
            "key": "Cache-Control",
            "value": "no-cache" // Disable caching for HTML files to ensure fresh content
          }
        ]
      },
      {
        "source": "**/*.{js,css}", // Cache configuration for JavaScript and CSS files
        "headers": [
          {
            "key": "Cache-Control",
            "value": "public, max-age=31536000" // Cache for 1 year
          }
        ]
      },
      {
        "source": "**/*.{png,jpg,jpeg,gif,svg,ico}", // Cache configuration for images
        "headers": [
          {
            "key": "Cache-Control",
            "value": "public, max-age=31536000" // Cache for 1 year
          }
        ]
      }
    ],
    "rewrites": [
      {
        "source": "**", // Redirect all paths to your main `index.html` file (optional for single-page apps)
        "destination": "/index.html"
      }
    ],
    "cleanUrls": true, // Remove .html extensions in URLs
    "trailingSlash": false // Do not enforce trailing slashes in URLs
  }
}
```

### How to Use:
1. Ensure Firebase CLI is installed and your project is configured (`firebase init`).
2. Update the `firebase.json` file in your project directory with the code provided.
3. Place your web application files in the `public` directory.
4. Deploy your project using `firebase deploy`.

Note: HTTPS is automatically enabled for Firebase Hosting and requires no additional configuration.
