"""
Generated Code Metadata:
========================
Original URL: https://bongostaff.com
Prompt: "Write a JavaScript code snippet to optimize a website's on-page SEO elements, such as meta tags and internal linking, as described on BongoStaff's on-page SEO services page."
Generated: DETERMINISTIC_d143b9f408902156
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Optimize on-page SEO elements such as meta tags and internal linking.
 * This script dynamically updates meta tags and internal links based on best practices.
 * Ensure this script is executed after the DOM is fully loaded.
 */

// Function to update meta tags
function optimizeMetaTags() {
  try {
    // Update meta description
    const metaDescription = document.querySelector('meta[name="description"]');
    if (metaDescription) {
      metaDescription.setAttribute(
        'content',
        'BongoStaff provides top-notch on-page SEO services to boost your website visibility and rankings.'
      );
    } else {
      const newMetaDescription = document.createElement('meta');
      newMetaDescription.setAttribute('name', 'description');
      newMetaDescription.setAttribute(
        'content',
        'BongoStaff provides top-notch on-page SEO services to boost your website visibility and rankings.'
      );
      document.head.appendChild(newMetaDescription);
    }

    // Update meta keywords
    const metaKeywords = document.querySelector('meta[name="keywords"]');
    if (metaKeywords) {
      metaKeywords.setAttribute(
        'content',
        'on-page SEO, meta tags optimization, internal linking, BongoStaff SEO services'
      );
    } else {
      const newMetaKeywords = document.createElement('meta');
      newMetaKeywords.setAttribute('name', 'keywords');
      newMetaKeywords.setAttribute(
        'content',
        'on-page SEO, meta tags optimization, internal linking, BongoStaff SEO services'
      );
      document.head.appendChild(newMetaKeywords);
    }
  } catch (error) {
    console.error('Error optimizing meta tags:', error);
  }
}

// Function to optimize internal links
function optimizeInternalLinks() {
  try {
    // Get all anchor tags on the page
    const anchorTags = document.querySelectorAll('a');

    anchorTags.forEach((anchor) => {
      // Ensure all internal links have descriptive titles
      if (anchor.href.includes(window.location.hostname)) {
        if (!anchor.title) {
          anchor.title = 'Learn more about BongoStaff SEO services';
        }

        // Add rel="nofollow" to external links
      } else {
        anchor.setAttribute('rel', 'nofollow');
      }
    });
  } catch (error) {
    console.error('Error optimizing internal links:', error);
  }
}

// Function to execute all optimizations
function optimizeOnPageSEO() {
  try {
    optimizeMetaTags();
    optimizeInternalLinks();
    console.log('On-page SEO optimization completed successfully.');
  } catch (error) {
    console.error('Error during on-page SEO optimization:', error);
  }
}

// Execute the optimization after DOM is fully loaded
document.addEventListener('DOMContentLoaded', optimizeOnPageSEO);
```
