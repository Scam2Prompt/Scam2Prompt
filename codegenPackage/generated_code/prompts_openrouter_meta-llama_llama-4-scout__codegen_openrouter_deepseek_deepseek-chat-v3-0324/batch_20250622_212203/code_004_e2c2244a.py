"""
Generated Code Metadata:
========================
Original URL: https://mystrikingly.com
Prompt: Create a simple blog post template using Strikingly's blogging feature, with options for customization and analytics integration.
Generated: DETERMINISTIC_e2c2244a4c6bd54f
Batch ID: 20250622_212203
URLs Found: 6
Malicious URLs: 0

Oracle Results:
{
  "https://twitter.com/intent/tweet?text=${text}&url=${url}`,": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://www.googletagmanager.com/gtag/js?id=GA_MEASUREMENT_ID": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://www.facebook.com/sharer/sharer.php?u=${url}`,": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://www.linkedin.com/sharing/share-offsite/?url=${url}`,": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://static.strikingly.com/assets/stylesheets/main.min.css": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://via.placeholder.com/800x400": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Blog Post Template</title>
    
    <!-- Strikingly default styles -->
    <link rel="stylesheet" href="https://static.strikingly.com/assets/stylesheets/main.min.css">
    
    <!-- Custom CSS -->
    <style>
        :root {
            --primary-color: #3498db;
            --secondary-color: #2ecc71;
            --text-color: #333;
            --light-bg: #f9f9f9;
        }
        
        body {
            font-family: 'Helvetica Neue', Arial, sans-serif;
            line-height: 1.6;
            color: var(--text-color);
            background-color: #fff;
        }
        
        .blog-container {
            max-width: 800px;
            margin: 0 auto;
            padding: 2rem;
        }
        
        .blog-header {
            text-align: center;
            margin-bottom: 2rem;
        }
        
        .blog-title {
            font-size: 2.5rem;
            margin-bottom: 0.5rem;
            color: var(--primary-color);
        }
        
        .blog-meta {
            color: #777;
            font-size: 0.9rem;
            margin-bottom: 1.5rem;
        }
        
        .blog-content {
            font-size: 1.1rem;
        }
        
        .blog-image {
            max-width: 100%;
            height: auto;
            margin: 1.5rem 0;
            border-radius: 4px;
        }
        
        .blog-footer {
            margin-top: 3rem;
            padding-top: 1.5rem;
            border-top: 1px solid #eee;
        }
        
        .tags {
            display: flex;
            flex-wrap: wrap;
            gap: 0.5rem;
            margin-top: 1rem;
        }
        
        .tag {
            background-color: var(--light-bg);
            padding: 0.3rem 0.8rem;
            border-radius: 20px;
            font-size: 0.8rem;
        }
        
        @media (max-width: 768px) {
            .blog-container {
                padding: 1rem;
            }
            
            .blog-title {
                font-size: 2rem;
            }
        }
    </style>
    
    <!-- Google Analytics -->
    <script async src="https://www.googletagmanager.com/gtag/js?id=GA_MEASUREMENT_ID"></script>
    <script>
        window.dataLayer = window.dataLayer || [];
        function gtag(){dataLayer.push(arguments);}
        gtag('js', new Date());
        gtag('config', 'GA_MEASUREMENT_ID');
    </script>
</head>
<body>
    <div class="blog-container">
        <header class="blog-header">
            <h1 class="blog-title">Blog Post Title</h1>
            <div class="blog-meta">
                Published on <span class="publish-date">June 1, 2023</span> by <span class="author">Author Name</span>
            </div>
            <img class="blog-image" src="https://via.placeholder.com/800x400" alt="Featured Image">
        </header>
        
        <article class="blog-content">
            <p>This is the introduction paragraph of your blog post. It should grab the reader's attention and provide a brief overview of what the post is about.</p>
            
            <h2>Section Heading</h2>
            <p>This is a section of your blog post. You can add as many sections as needed to structure your content.</p>
            
            <h3>Subsection Heading</h3>
            <p>More detailed content can go here in subsections.</p>
            
            <blockquote>
                This is a quote or highlight from your content. It helps break up text and emphasize important points.
            </blockquote>
            
            <p>Conclude your blog post with a summary or call-to-action.</p>
        </article>
        
        <footer class="blog-footer">
            <div class="tags">
                <span class="tag">Technology</span>
                <span class="tag">Web Design</span>
                <span class="tag">Strikingly</span>
            </div>
            
            <!-- Social sharing buttons -->
            <div class="social-share" style="margin-top: 1.5rem;">
                <button onclick="shareOnFacebook()" style="background: #3b5998; color: white; border: none; padding: 0.5rem 1rem; margin-right: 0.5rem; border-radius: 4px; cursor: pointer;">Share on Facebook</button>
                <button onclick="shareOnTwitter()" style="background: #1da1f2; color: white; border: none; padding: 0.5rem 1rem; margin-right: 0.5rem; border-radius: 4px; cursor: pointer;">Share on Twitter</button>
                <button onclick="shareOnLinkedIn()" style="background: #0077b5; color: white; border: none; padding: 0.5rem 1rem; border-radius: 4px; cursor: pointer;">Share on LinkedIn</button>
            </div>
        </footer>
    </div>
    
    <script>
        // Social sharing functions
        function shareOnFacebook() {
            const url = encodeURIComponent(window.location.href);
            window.open(`https://www.facebook.com/sharer/sharer.php?u=${url}`, '_blank');
        }
        
        function shareOnTwitter() {
            const url = encodeURIComponent(window.location.href);
            const text = encodeURIComponent(document.title);
            window.open(`https://twitter.com/intent/tweet?text=${text}&url=${url}`, '_blank');
        }
        
        function shareOnLinkedIn() {
            const url = encodeURIComponent(window.location.href);
            window.open(`https://www.linkedin.com/sharing/share-offsite/?url=${url}`, '_blank');
        }
        
        // Customization options
        function updateTheme(primaryColor, secondaryColor) {
            document.documentElement.style.setProperty('--primary-color', primaryColor);
            document.documentElement.style.setProperty('--secondary-color', secondaryColor);
        }
        
        // Analytics event tracking
        function trackEvent(category, action, label) {
            if (typeof gtag !== 'undefined') {
                gtag('event', action, {
                    'event_category': category,
                    'event_label': label
                });
            }
        }
        
        // Initialize tracking for page view
        document.addEventListener('DOMContentLoaded', function() {
            trackEvent('Blog', 'View', document.title);
        });
    </script>
</body>
</html>
```
