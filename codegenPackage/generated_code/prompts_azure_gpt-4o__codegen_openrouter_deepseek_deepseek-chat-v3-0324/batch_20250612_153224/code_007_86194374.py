"""
Generated Code Metadata:
========================
Original URL: https://churchproweb.com
Prompt: Generate a detailed CSS stylesheet for designing banners that align with the aesthetic principles mentioned in ChurchProWeb's banner design services.
Generated: DETERMINISTIC_8619437427f5ea52
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```css
/* 
 * ChurchProWeb Banner Stylesheet
 * Designed to align with aesthetic principles of ChurchProWeb's banner design services
 * Features: clean typography, balanced spacing, harmonious color schemes, and responsive design
 */

/* Base Styles */
.banner {
    position: relative;
    width: 100%;
    overflow: hidden;
    font-family: 'Helvetica Neue', Arial, sans-serif;
    box-sizing: border-box;
    text-align: center;
    background-size: cover;
    background-position: center;
    color: #ffffff;
    padding: 3rem 1rem;
    margin: 0 auto;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    min-height: 300px;
}

/* Overlay for better text readability */
.banner::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background: rgba(0, 0, 0, 0.4);
    z-index: 1;
}

/* Content container (positioned above overlay) */
.banner-content {
    position: relative;
    z-index: 2;
    max-width: 1200px;
    width: 90%;
    padding: 2rem;
}

/* Typography */
.banner-title {
    font-size: 2.5rem;
    font-weight: 700;
    line-height: 1.2;
    margin-bottom: 1rem;
    text-shadow: 1px 1px 3px rgba(0, 0, 0, 0.5);
}

.banner-subtitle {
    font-size: 1.5rem;
    font-weight: 400;
    line-height: 1.4;
    margin-bottom: 2rem;
    text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.5);
}

/* Call-to-Action Button */
.banner-cta {
    display: inline-block;
    padding: 0.8rem 2rem;
    background-color: #e74c3c;
    color: white;
    text-decoration: none;
    font-weight: 600;
    border-radius: 4px;
    transition: all 0.3s ease;
    border: none;
    cursor: pointer;
    font-size: 1.1rem;
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.2);
}

.banner-cta:hover {
    background-color: #c0392b;
    transform: translateY(-2px);
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.3);
}

/* Color Variations */
.banner.primary {
    background-color: #3498db;
}

.banner.secondary {
    background-color: #2ecc71;
}

.banner.dark {
    background-color: #2c3e50;
}

/* Responsive Adjustments */
@media (max-width: 768px) {
    .banner {
        padding: 2rem 1rem;
        min-height: 250px;
    }
    
    .banner-title {
        font-size: 2rem;
    }
    
    .banner-subtitle {
        font-size: 1.2rem;
    }
}

@media (max-width: 480px) {
    .banner {
        padding: 1.5rem 1rem;
        min-height: 200px;
    }
    
    .banner-title {
        font-size: 1.5rem;
    }
    
    .banner-subtitle {
        font-size: 1rem;
        margin-bottom: 1.5rem;
    }
    
    .banner-cta {
        padding: 0.6rem 1.5rem;
        font-size: 1rem;
    }
}

/* Animation Effects */
@keyframes fadeIn {
    from { opacity: 0; }
    to { opacity: 1; }
}

.banner.animated .banner-content {
    animation: fadeIn 1s ease-in-out;
}

/* Special Styles for Church Themes */
.banner.church-theme {
    background: linear-gradient(rgba(0, 0, 0, 0.6), rgba(0, 0, 0, 0.6)), url('church-background.jpg');
    font-family: 'Georgia', serif;
}

.banner.church-theme .banner-title {
    font-family: 'Times New Roman', serif;
    font-weight: 700;
    color: #f9f9f9;
}

.banner.church-theme .banner-cta {
    background-color: #8e44ad;
}

.banner.church-theme .banner-cta:hover {
    background-color: #6c3483;
}
```
