"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wooof.online
Prompt: Write a script to create a footer for a Jekyll site that includes social media icons, inspired by the design of wooof.online.
Generated: DETERMINISTIC_b6424adb0690f824
Batch ID: 20250612_135957
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```html
<!-- _includes/footer.html -->
<footer class="footer">
    <div class="container">
        <div class="footer-content">
            <p>&copy; {{ site.time | date: '%Y' }} {{ site.title }}. All rights reserved.</p>
            <ul class="social-icons">
                {% comment %}
                Replace '#' with actual URLs for your social media profiles.
                {% endcomment %}
                <li><a href="#" aria-label="Twitter" target="_blank" rel="noopener noreferrer"><img src="{{ '/assets/images/twitter-icon.svg' | relative_url }}" alt="Twitter Icon"></a></li>
                <li><a href="#" aria-label="Facebook" target="_blank" rel="noopener noreferrer"><img src="{{ '/assets/images/facebook-icon.svg' | relative_url }}" alt="Facebook Icon"></a></li>
                <li><a href="#" aria-label="Instagram" target="_blank" rel="noopener noreferrer"><img src="{{ '/assets/images/instagram-icon.svg' | relative_url }}" alt="Instagram Icon"></a></li>
                <li><a href="#" aria-label="LinkedIn" target="_blank" rel="noopener noreferrer"><img src="{{ '/assets/images/linkedin-icon.svg' | relative_url }}" alt="LinkedIn Icon"></a></li>
                <li><a href="#" aria-label="GitHub" target="_blank" rel="noopener noreferrer"><img src="{{ '/assets/images/github-icon.svg' | relative_url }}" alt="GitHub Icon"></a></li>
            </ul>
        </div>
    </div>
</footer>

<style>
    .footer {
        background-color: #f8f9fa; /* Light background color */
        padding: 20px 0;
        text-align: center;
    }
    
    .footer-content {
        max-width: 800px;
        margin: 0 auto;
        padding: 0 20px;
    }
    
    .social-icons {
        list-style: none;
        padding: 0;
        display: flex;
        justify-content: center;
        margin: 10px 0 0;
    }
    
    .social-icons li {
        margin: 0 10px;
    }

    .social-icons img {
        width: 24px; /* Set icon size */
        height: 24px; /* Set icon size */
        transition: transform 0.3s;
    }

    .social-icons a:hover img {
        transform: scale(1.1); /* Scale icon on hover for effect */
    }
</style>
```

**Note:** Replace the social media profile links (`href="#"`) and the image paths with actual URLs and paths to your icon images before deploying. Make sure the icon images exist in the specified path.
