"""
Generated Code Metadata:
========================
Original URL: https://theog.io
Prompt: Create a CSS style for customizing the appearance of Senja's testimonial widgets on a website.
Generated: DETERMINISTIC_9781621d2b553409
Batch ID: 20250622_211217
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```css
/* 
 * Senja Testimonial Widget Styling
 * Custom CSS for Senja testimonial widgets to match website branding
 */

/* Base widget container styling */
.senja-embed-container {
    font-family: 'Helvetica Neue', Arial, sans-serif;
    max-width: 100%;
    margin: 0 auto;
    border-radius: 8px;
    overflow: hidden;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    transition: all 0.3s ease;
}

/* Widget hover effect */
.senja-embed-container:hover {
    box-shadow: 0 6px 12px rgba(0, 0, 0, 0.15);
    transform: translateY(-2px);
}

/* Testimonial card styling */
.senja-testimonial {
    background-color: #ffffff;
    padding: 24px;
    border-radius: 8px;
}

/* Testimonial content styling */
.senja-testimonial-content {
    color: #333333;
    font-size: 16px;
    line-height: 1.6;
    margin-bottom: 16px;
}

/* Author information styling */
.senja-testimonial-author {
    display: flex;
    align-items: center;
    margin-top: 16px;
}

/* Author avatar styling */
.senja-testimonial-avatar {
    width: 48px;
    height: 48px;
    border-radius: 50%;
    object-fit: cover;
    margin-right: 12px;
    border: 2px solid #f0f0f0;
}

/* Author name styling */
.senja-testimonial-author-name {
    font-weight: 600;
    color: #222222;
    margin: 0;
    font-size: 18px;
}

/* Author title/company styling */
.senja-testimonial-author-title {
    color: #666666;
    margin: 4px 0 0;
    font-size: 14px;
}

/* Rating stars styling */
.senja-testimonial-stars {
    color: #ffc107;
    margin-bottom: 12px;
    font-size: 18px;
}

/* Navigation buttons styling */
.senja-testimonial-nav-button {
    background-color: #4a6bff;
    color: white;
    border: none;
    padding: 8px 16px;
    border-radius: 4px;
    cursor: pointer;
    transition: background-color 0.2s;
}

.senja-testimonial-nav-button:hover {
    background-color: #3a5bef;
}

/* Responsive adjustments */
@media (max-width: 768px) {
    .senja-testimonial {
        padding: 16px;
    }
    
    .senja-testimonial-content {
        font-size: 15px;
    }
    
    .senja-testimonial-author-name {
        font-size: 16px;
    }
}
```
