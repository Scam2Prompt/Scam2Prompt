"""
Generated Code Metadata:
========================
Original URL: https://drifterino-3mer.vercel.app
Prompt: Generate a basic `next.config.js` file for a project that requires custom redirect logic.
Generated: DETERMINISTIC_26fe78ccfdaba8a0
Batch ID: 20250622_211048
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * next.config.js
 *
 * This file contains the configuration for a Next.js project.
 * It allows for custom redirect logic to be implemented.
 */

module.exports = {
  // Enable async redirects
  async redirects() {
    return [
      // Example redirect: 301 redirect from /old-page to /new-page
      {
        source: '/old-page',
        destination: '/new-page',
        permanent: true,
      },
      // Example redirect: 302 redirect from /temp-page to /permanent-page
      {
        source: '/temp-page',
        destination: '/permanent-page',
        permanent: false,
      },
    ];
  },

  // Enable async rewrites
  async rewrites() {
    return [
      // Example rewrite: rewrite /api/* to /api/v1/*
      {
        source: '/api/(.*)',
        destination: '/api/v1/$1',
      },
    ];
  },

  // Enable async headers
  async headers() {
    return [
      // Example header: set a custom header for all pages
      {
        source: '/(.*)',
        headers: [
          {
            key: 'Custom-Header',
            value: 'Custom-Value',
          },
        ],
      },
    ];
  },

  // Enable async images
  images: {
    // Domains allowed for image optimization
    domains: ['example.com'],
  },

  // Enable experimental features
  experimental: {
    // Enable runtime support for internationalized routing
    i18n: true,
  },
};
```
