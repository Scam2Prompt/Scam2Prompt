"""
Generated Code Metadata:
========================
Original URL: https://connectnetwork.lojavirtualnuvem.com.br
Prompt: Create a function to highlight product categories using customizable banners, inspired by the "Banners de categorias" feature on the Connect Network website.
Generated: DETERMINISTIC_1bcbf47273b23bd3
Batch ID: 20250612_152306
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
from typing import Dict, Optional
from dataclasses import dataclass
from enum import Enum

class BannerStyle(Enum):
    """Enum for different banner styling options"""
    DEFAULT = "default"
    PROMO = "promo"
    NEW = "new"
    FEATURED = "featured"

@dataclass
class CategoryBanner:
    """Data class representing a category banner"""
    category_id: str
    title: str
    description: str
    style: BannerStyle = BannerStyle.DEFAULT
    image_url: Optional[str] = None
    link_url: Optional[str] = None
    is_active: bool = True

class CategoryBannerManager:
    """Manager class for handling category banners"""
    
    def __init__(self):
        self.banners: Dict[str, CategoryBanner] = {}
    
    def add_banner(self, banner: CategoryBanner) -> None:
        """Add a new banner to the manager"""
        if not banner.is_active:
            return
            
        if banner.category_id in self.banners:
            raise ValueError(f"Banner for category {banner.category_id} already exists")
            
        self.banners[banner.category_id] = banner
    
    def get_banner(self, category_id: str) -> Optional[CategoryBanner]:
        """Retrieve a banner by category ID"""
        return self.banners.get(category_id)
    
    def remove_banner(self, category_id: str) -> None:
        """Remove a banner by category ID"""
        if category_id in self.banners:
            del self.banners[category_id]
    
    def generate_html(self, category_id: str) -> str:
        """Generate HTML for a specific banner"""
        banner = self.get_banner(category_id)
        if not banner:
            return ""
        
        style_class = f"banner-{banner.style.value}"
        image_html = f'<img src="{banner.image_url}" alt="{banner.title}">' if banner.image_url else ""
        link_start = f'<a href="{banner.link_url}">' if banner.link_url else ""
        link_end = "</a>" if banner.link_url else ""
        
        return f"""
        <div class="category-banner {style_class}">
            {link_start}
                {image_html}
                <div class="banner-content">
                    <h3>{banner.title}</h3>
                    <p>{banner.description}</p>
                </div>
            {link_end}
        </div>
        """
    
    def generate_css(self) -> str:
        """Generate basic CSS styles for the banners"""
        return """
        .category-banner {
            padding: 20px;
            margin: 15px 0;
            border-radius: 8px;
            display: flex;
            align-items: center;
            text-decoration: none;
            color: inherit;
        }
        
        .banner-default {
            background-color: #f0f0f0;
            border-left: 5px solid #ccc;
        }
        
        .banner-promo {
            background-color: #fff8e6;
            border-left: 5px solid #ffcc00;
        }
        
        .banner-new {
            background-color: #e6f7ff;
            border-left: 5px solid #0099ff;
        }
        
        .banner-featured {
            background-color: #f0ffe6;
            border-left: 5px solid #66cc33;
        }
        
        .banner-content {
            margin-left: 15px;
        }
        
        .banner-content h3 {
            margin: 0 0 5px 0;
            font-size: 1.2em;
        }
        
        .banner-content p {
            margin: 0;
            font-size: 0.9em;
            color: #666;
        }
        
        .category-banner img {
            max-height: 80px;
            width: auto;
            border-radius: 4px;
        }
        """

def example_usage():
    """Example usage of the CategoryBannerManager"""
    manager = CategoryBannerManager()
    
    # Add some banners
    manager.add_banner(CategoryBanner(
        category_id="electronics",
        title="Electronics Sale",
        description="Up to 30% off on all electronics",
        style=BannerStyle.PROMO,
        image_url="/images/electronics.jpg",
        link_url="/categories/electronics"
    ))
    
    manager.add_banner(CategoryBanner(
        category_id="books",
        title="New Arrivals",
        description="Discover our latest book collection",
        style=BannerStyle.NEW,
        image_url="/images/books.jpg"
    ))
    
    # Generate HTML for a category
    print(manager.generate_html("electronics"))
    
    # Output the CSS
    print(f"<style>{manager.generate_css()}</style>")

if __name__ == "__main__":
    example_usage()
```
