"""
Generated Code Metadata:
========================
Original URL: https://immediatebyte.org
Prompt: Write a CSS code snippet to style a blog list page with a fixed-width left sidebar and a fluid full-width content area, using the PRESTIGE-DATTES template as a reference.
Generated: DETERMINISTIC_de70d765c2f9ac2f
Batch ID: 20250622_211310
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```css
/* Blog List Page Layout Styles */
/* PRESTIGE-DATTES Template Reference */

/* Base Styles */
body {
    margin: 0;
    padding: 0;
    font-family: 'Helvetica Neue', Arial, sans-serif;
    line-height: 1.6;
    color: #333;
    background-color: #f9f9f9;
}

/* Layout Container */
.container {
    display: flex;
    min-height: 100vh;
}

/* Fixed-width Sidebar */
.sidebar {
    width: 300px;
    background-color: #2c3e50;
    color: #ecf0f1;
    padding: 2rem;
    position: fixed;
    height: 100%;
    overflow-y: auto;
    box-shadow: 2px 0 5px rgba(0, 0, 0, 0.1);
}

/* Main Content Area */
.main-content {
    flex: 1;
    margin-left: 300px; /* Matches sidebar width */
    padding: 2rem;
    background-color: #fff;
}

/* Blog List Styling */
.blog-list {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
    gap: 2rem;
    margin-top: 2rem;
}

.blog-card {
    background: #fff;
    border-radius: 8px;
    overflow: hidden;
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
    transition: transform 0.3s ease;
}

.blog-card:hover {
    transform: translateY(-5px);
}

.blog-card img {
    width: 100%;
    height: 200px;
    object-fit: cover;
}

.blog-card-content {
    padding: 1.5rem;
}

.blog-card h3 {
    margin: 0 0 0.5rem;
    font-size: 1.25rem;
}

.blog-card p {
    margin: 0 0 1rem;
    color: #666;
}

.blog-card .meta {
    font-size: 0.875rem;
    color: #999;
}

/* Responsive Adjustments */
@media (max-width: 768px) {
    .container {
        flex-direction: column;
    }

    .sidebar {
        width: 100%;
        position: relative;
        height: auto;
    }

    .main-content {
        margin-left: 0;
    }

    .blog-list {
        grid-template-columns: 1fr;
    }
}

/* Utility Classes */
.text-center {
    text-align: center;
}

.mb-2 {
    margin-bottom: 2rem;
}

/* Link Styles */
a {
    color: #3498db;
    text-decoration: none;
}

a:hover {
    text-decoration: underline;
}
```
