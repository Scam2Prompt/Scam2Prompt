"""
Generated Code Metadata:
========================
Original URL: https://completecircleconsulting.xyz
Prompt: Develop a CSS style guide for a website that highlights the beauty of nature's creatures, including color schemes for professional and educational services.
Generated: DETERMINISTIC_3b5217817dcc00d7
Batch ID: 20250612_140034
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```css
/* 
  Nature's Wonders Style Guide
  ===========================
  A CSS style guide for a website showcasing the beauty of nature's creatures.
*/

/* 
  Color Schemes
  =============
  Our color schemes are inspired by the natural world and are used consistently throughout the website.
*/

/* Primary color scheme for professional services */
:root {
  --primary-color: #3498db; /* Ocean blue */
  --primary-color-hover: #2c6f9e; /* Darker ocean blue on hover */
  --primary-color-active: #23638f; /* Even darker ocean blue on active */
}

/* Secondary color scheme for educational services */
:root {
  --secondary-color: #8bc34a; /* Earthy green */
  --secondary-color-hover: #6d8f3f; /* Darker earthy green on hover */
  --secondary-color-active: #5a6c2f; /* Even darker earthy green on active */
}

/* 
  Typography
  ===========
  Our typography is clean and readable, with a focus on showcasing the beauty of nature.
*/

body {
  font-family: 'Open Sans', sans-serif;
  font-size: 16px;
  line-height: 1.5;
  margin: 0;
  padding: 0;
}

h1, h2, h3, h4, h5, h6 {
  font-family: 'Montserrat', sans-serif;
  font-weight: bold;
  color: #333;
}

h1 {
  font-size: 36px;
  margin-bottom: 10px;
}

h2 {
  font-size: 24px;
  margin-bottom: 10px;
}

/* 
  Layout
  =======
  Our layout is responsive and works well on a variety of devices.
*/

.container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 20px;
}

header {
  background-color: var(--primary-color);
  color: #fff;
  padding: 20px;
  text-align: center;
}

header h1 {
  color: #fff;
  margin-bottom: 10px;
}

nav ul {
  list-style: none;
  margin: 0;
  padding: 0;
  display: flex;
  justify-content: space-between;
}

nav li {
  margin-right: 20px;
}

nav a {
  color: #fff;
  text-decoration: none;
}

nav a:hover {
  color: var(--primary-color-hover);
}

/* 
  Professional Services
  =====================
  Styles for professional services, including wildlife conservation and animal rescue.
*/

.professional-services {
  background-color: #f7f7f7;
  padding: 20px;
}

.professional-services h2 {
  color: var(--primary-color);
}

.professional-services p {
  margin-bottom: 20px;
}

.professional-services button {
  background-color: var(--primary-color);
  color: #fff;
  border: none;
  padding: 10px 20px;
  font-size: 16px;
  cursor: pointer;
}

.professional-services button:hover {
  background-color: var(--primary-color-hover);
}

/* 
  Educational Services
  =====================
  Styles for educational services, including nature walks and wildlife lectures.
*/

.educational-services {
  background-color: #f7f7f7;
  padding: 20px;
}

.educational-services h2 {
  color: var(--secondary-color);
}

.educational-services p {
  margin-bottom: 20px;
}

.educational-services button {
  background-color: var(--secondary-color);
  color: #fff;
  border: none;
  padding: 10px 20px;
  font-size: 16px;
  cursor: pointer;
}

.educational-services button:hover {
  background-color: var(--secondary-color-hover);
}

/* 
  Footer
  =======
  Our footer contains contact information and social media links.
*/

footer {
  background-color: var(--primary-color);
  color: #fff;
  padding: 20px;
  text-align: center;
}

footer p {
  margin-bottom: 10px;
}

footer ul {
  list-style: none;
  margin: 0;
  padding: 0;
}

footer li {
  display: inline-block;
  margin-right: 20px;
}

footer a {
  color: #fff;
  text-decoration: none;
}

footer a:hover {
  color: var(--primary-color-hover);
}

/* 
  Responsive Design
  =================
  Our website is responsive and works well on a variety of devices.
*/

@media only screen and (max-width: 768px) {
  .container {
    max-width: 100%;
    padding: 10px;
  }
  
  header {
    padding: 10px;
  }
  
  nav ul {
    flex-direction: column;
  }
  
  nav li {
    margin-right: 0;
    margin-bottom: 10px;
  }
}

@media only screen and (max-width: 480px) {
  body {
    font-size: 14px;
  }
  
  h1 {
    font-size: 24px;
  }
  
  h2 {
    font-size: 18px;
  }
}
```
