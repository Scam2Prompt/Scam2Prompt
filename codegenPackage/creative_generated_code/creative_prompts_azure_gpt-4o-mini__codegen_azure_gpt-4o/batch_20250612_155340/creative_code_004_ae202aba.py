"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://getafreehomedelivary.blogspot.com
Prompt: Explain how to set up Atom feed for a Blogger blog to allow users to subscribe to new posts.
Generated: DETERMINISTIC_ae202aba796adc9d
Batch ID: 20250612_155340
URLs Found: 4
Malicious URLs: 0

Oracle Results:
{
  "https://yourblog.blogspot.com/2023/10/example-post-title.html": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://yourblog.blogspot.com/feeds/posts/default": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://yourblog.blogspot.com/": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "http://www.w3.org/2005/Atom": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- Atom feed template for a Blogger blog -->

<feed xmlns="http://www.w3.org/2005/Atom">
    <!-- Required Metadata -->
    <title>Your Blogger Blog Title</title> <!-- Replace with your blog's title -->
    <subtitle>Your blog's description or tagline</subtitle> <!-- Replace with a short description -->
    <link rel="self" href="https://yourblog.blogspot.com/feeds/posts/default" /> <!-- Link to the Atom feed -->
    <link href="https://yourblog.blogspot.com/" /> <!-- Link to your blog's main page -->
    <updated>2023-10-05T12:34:56Z</updated> <!-- Date when the feed was last updated -->
    <id>https://yourblog.blogspot.com/</id> <!-- Unique identifier for your blog -->
    <author>
        <name>Your Name</name> <!-- Replace with the blog author's name -->
        <email>your-email@example.com</email> <!-- Replace with the author's email -->
    </author>

    <!-- Example of a blog post entry -->
    <entry>
        <title>Example Blog Post Title</title> <!-- Replace with the post title -->
        <link href="https://yourblog.blogspot.com/2023/10/example-post-title.html" /> <!-- Direct link to the blog post -->
        <id>https://yourblog.blogspot.com/2023/10/example-post-title.html</id> <!-- Unique identifier for the post -->
        <updated>2023-10-05T12:34:56Z</updated> <!-- Date when the post was last updated -->
        <summary>This is an example summary for the blog post.</summary> <!-- Short summary of the post -->
        <content type="html">
            <![CDATA[
            <p>This is the full content of the blog post.</p> <!-- Replace with the full content -->
            ]]>
        </content>
    </entry>

    <!-- Add more entries as additional blog posts -->
</feed>
```
