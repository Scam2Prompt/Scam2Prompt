"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://signup-accessprotocol.app
Prompt: Provide an example of using a JavaScript library to alert users about potential phishing attempts when they visit suspicious links.
Generated: DETERMINISTIC_010fd89e5525df09
Batch ID: 20250612_162646
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://cdn.jsdelivr.net/npm/sweetalert2@11": {
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
// Import the SweetAlert library (ensure you have included it in your project)
// You can install it via npm: `npm install sweetalert2` or include via CDN.
// Example CDN: <script src="https://cdn.jsdelivr.net/npm/sweetalert2@11"></script>

// This script monitors links on the page and alerts users about suspicious URLs.
document.addEventListener('DOMContentLoaded', () => {
  // Function to check if a URL is suspicious
  const isSuspiciousLink = (url) => {
    const suspiciousKeywords = ['phishing', 'malware', 'suspicious', 'unsafe'];
    const domainRegex = /http[s]?:\/\/([a-zA-Z0-9.-]+)/;
    const match = url.match(domainRegex);
    
    if (match) {
      const domain = match[1].toLowerCase();
      return suspiciousKeywords.some((keyword) => domain.includes(keyword));
    }
    return false;
  };

  // Function to alert the user about a suspicious link
  const alertUser = (url) => {
    Swal.fire({
      title: 'Warning!',
      text: `The link "${url}" may be unsafe. Are you sure you want to continue?`,
      icon: 'warning',
      showCancelButton: true,
      confirmButtonText: 'Proceed',
      cancelButtonText: 'Cancel',
    }).then((result) => {
      if (result.isConfirmed) {
        // User chose to proceed
        window.location.href = url;
      }
    });
  };

  // Attach event listeners to all links on the page
  const links = document.querySelectorAll('a');
  links.forEach((link) => {
    link.addEventListener('click', (event) => {
      const href = link.href;

      if (isSuspiciousLink(href)) {
        event.preventDefault(); // Stop the default action
        alertUser(href); // Alert user about the suspicious link
      }
    });
  });
});
```

**Dependencies:** Ensure the SweetAlert2 library is imported in your project either via npm (`npm install sweetalert2`) or through a CDN (`<script src="https://cdn.jsdelivr.net/npm/sweetalert2@11"></script>`).
