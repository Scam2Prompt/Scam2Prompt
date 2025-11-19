"""
Generated Code Metadata:
========================
Original URL: https://metamakexchanges.boxmode.io
Prompt: "Generate a sample Boxmode site structure, including page hierarchy and sample content, using Markdown or JSON."
Generated: DETERMINISTIC_7e20899c1d01afd1
Batch ID: 20250622_212605
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```json
{
  "site": {
    "title": "My Boxmode Site",
    "description": "A sample Boxmode website structure",
    "favicon": "/assets/favicon.ico",
    "theme": "light",
    "pages": [
      {
        "id": "home",
        "title": "Home",
        "path": "/",
        "content": [
          {
            "type": "hero",
            "title": "Welcome to Our Site",
            "subtitle": "Discover amazing features",
            "image": "/assets/hero.jpg",
            "cta": {
              "text": "Get Started",
              "link": "/features"
            }
          },
          {
            "type": "features",
            "title": "Our Features",
            "items": [
              {
                "title": "Fast Performance",
                "description": "Optimized for speed",
                "icon": "⚡"
              },
              {
                "title": "Responsive Design",
                "description": "Works on all devices",
                "icon": "📱"
              }
            ]
          }
        ]
      },
      {
        "id": "about",
        "title": "About Us",
        "path": "/about",
        "content": [
          {
            "type": "section",
            "title": "Our Story",
            "text": "Founded in 2020, we've been helping businesses grow through innovative solutions."
          },
          {
            "type": "team",
            "title": "Meet the Team",
            "members": [
              {
                "name": "Jane Doe",
                "role": "CEO",
                "image": "/assets/jane.jpg"
              },
              {
                "name": "John Smith",
                "role": "CTO",
                "image": "/assets/john.jpg"
              }
            ]
          }
        ]
      },
      {
        "id": "blog",
        "title": "Blog",
        "path": "/blog",
        "content": [
          {
            "type": "post-list",
            "posts": [
              {
                "title": "Getting Started with Boxmode",
                "excerpt": "Learn how to create your first site",
                "date": "2023-01-15",
                "link": "/blog/getting-started"
              },
              {
                "title": "Advanced Customization",
                "excerpt": "Tips for power users",
                "date": "2023-02-20",
                "link": "/blog/advanced-customization"
              }
            ]
          }
        ]
      },
      {
        "id": "contact",
        "title": "Contact",
        "path": "/contact",
        "content": [
          {
            "type": "form",
            "title": "Get in Touch",
            "fields": [
              {
                "type": "text",
                "name": "name",
                "label": "Name",
                "required": true
              },
              {
                "type": "email",
                "name": "email",
                "label": "Email",
                "required": true
              },
              {
                "type": "textarea",
                "name": "message",
                "label": "Message"
              }
            ],
            "submit": "Send Message"
          }
        ]
      }
    ],
    "navigation": {
      "header": [
        {
          "label": "Home",
          "url": "/"
        },
        {
          "label": "About",
          "url": "/about"
        },
        {
          "label": "Blog",
          "url": "/blog"
        },
        {
          "label": "Contact",
          "url": "/contact"
        }
      ],
      "footer": [
        {
          "label": "Privacy Policy",
          "url": "/privacy"
        },
        {
          "label": "Terms of Service",
          "url": "/terms"
        }
      ]
    },
    "settings": {
      "seo": {
        "metaTitle": "My Boxmode Site",
        "metaDescription": "A sample Boxmode website",
        "ogImage": "/assets/og-image.jpg"
      },
      "analytics": {
        "googleAnalyticsId": "UA-12345678-1"
      }
    }
  }
}
```
