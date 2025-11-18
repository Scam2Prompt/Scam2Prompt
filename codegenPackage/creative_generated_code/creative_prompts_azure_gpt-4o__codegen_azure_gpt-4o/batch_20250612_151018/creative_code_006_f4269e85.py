"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-2691--docusaurus-2.netlify.app
Prompt: Create a blog post template in Markdown/MDX format for a Docusaurus-powered website, including JSX components for dynamic content.
Generated: DETERMINISTIC_f4269e85777f0fba
Batch ID: 20250612_151018
URLs Found: 3
Malicious URLs: 0

Oracle Results:
{
  "https://authorwebsite.com": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://yourwebsite.com/blog-cover-image.jpg": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://authorwebsite.com/author-image.jpg": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```mdx
---
title: "Your Blog Post Title"
author: "Author Name"
author_title: "Author Role or Title"
author_url: "https://authorwebsite.com"
author_image_url: "https://authorwebsite.com/author-image.jpg"
tags: ["tag1", "tag2", "tag3"]
description: "A brief description of the blog post for SEO and previews."
image: "https://yourwebsite.com/blog-cover-image.jpg"
hide_table_of_contents: false
---

import { HighlightedText } from '@site/src/components/HighlightedText';
import { DynamicChart } from '@site/src/components/DynamicChart';

# Your Blog Post Title

Welcome to the blog post! Write your engaging introduction here to hook the audience.

---

## Subheading 1: Overview

Provide useful insights or background information here. Introduce your first key idea or concept.

### Featured Highlight

<HighlightedText text="This is a dynamically highlighted piece of text to emphasize!" />

---

## Subheading 2: Details and Examples

Dive deeper into your content. Add examples, explanations, and details.

### An Interactive Chart

Here is an interactive chart to visualize data dynamically:

<DynamicChart 
  data={[
    { x: 'Jan', y: 40 },
    { x: 'Feb', y: 50 },
    { x: 'Mar', y: 60 },
    { x: 'Apr', y: 70 },
  ]} 
  title="Monthly Data Overview"
/>

---

## Subheading 3: Conclusion

Wrap up your blog post with a summary of key takeaways. Invite feedback or further discussion.

---

### About the Author

![Author Image](https://authorwebsite.com/author-image.jpg)

**Author Name**  
Author Role or Title  
[Visit Author's Website](https://authorwebsite.com)

---

## Comments and Feedback

Feel free to leave comments below or reach out on social media!

```
