"""
Generated Code Metadata:
========================
Original URL: https://metamark.lt
Prompt: Create a CSS stylesheet to ensure a website design aligns with a unique company style, as described in Metamark's approach to custom designs.
Generated: DETERMINISTIC_16426943345dfe4e
Batch ID: 20250612_150323
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```css
/* Metamark Custom Design Stylesheet */
/* Primary Colors */
:root {
  --primary-color: #2a5c8d;
  --secondary-color: #e67e22;
  --accent-color: #16a085;
  --light-color: #f5f5f5;
  --dark-color: #333333;
}

/* Base Styles */
body {
  font-family: 'Helvetica Neue', Arial, sans-serif;
  line-height: 1.6;
  color: var(--dark-color);
  background-color: var(--light-color);
  margin: 0;
  padding: 0;
}

/* Typography */
h1, h2, h3, h4, h5, h6 {
  font-family: 'Montserrat', sans-serif;
  font-weight: 700;
  color: var(--primary-color);
  margin-top: 0;
}

h1 {
  font-size: 2.5rem;
  line-height: 1.2;
}

h2 {
  font-size: 2rem;
}

p {
  margin-bottom: 1.5rem;
}

a {
  color: var(--accent-color);
  text-decoration: none;
  transition: color 0.3s ease;
}

a:hover {
  color: var(--secondary-color);
}

/* Buttons */
.btn {
  display: inline-block;
  padding: 0.75rem 1.5rem;
  border-radius: 4px;
  font-weight: 600;
  text-align: center;
  cursor: pointer;
  transition: all 0.3s ease;
}

.btn-primary {
  background-color: var(--primary-color);
  color: white;
  border: 2px solid var(--primary-color);
}

.btn-primary:hover {
  background-color: transparent;
  color: var(--primary-color);
}

.btn-secondary {
  background-color: var(--secondary-color);
  color: white;
  border: 2px solid var(--secondary-color);
}

.btn-secondary:hover {
  background-color: transparent;
  color: var(--secondary-color);
}

/* Navigation */
.navbar {
  background-color: white;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
  padding: 1rem 2rem;
}

.nav-logo {
  height: 40px;
}

.nav-menu {
  display: flex;
  list-style: none;
  margin: 0;
  padding: 0;
}

.nav-item {
  margin-left: 2rem;
}

.nav-link {
  color: var(--dark-color);
  font-weight: 600;
}

.nav-link:hover {
  color: var(--primary-color);
}

/* Layout */
.container {
  width: 100%;
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 1.5rem;
}

.section {
  padding: 4rem 0;
}

.section-title {
  text-align: center;
  margin-bottom: 3rem;
}

/* Cards */
.card {
  background: white;
  border-radius: 8px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  overflow: hidden;
  transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.card:hover {
  transform: translateY(-5px);
  box-shadow: 0 10px 20px rgba(0, 0, 0, 0.1);
}

.card-img {
  width: 100%;
  height: auto;
}

.card-body {
  padding: 1.5rem;
}

/* Forms */
.form-group {
  margin-bottom: 1.5rem;
}

.form-label {
  display: block;
  margin-bottom: 0.5rem;
  font-weight: 600;
}

.form-control {
  width: 100%;
  padding: 0.75rem;
  border: 1px solid #ddd;
  border-radius: 4px;
  font-size: 1rem;
}

.form-control:focus {
  outline: none;
  border-color: var(--accent-color);
  box-shadow: 0 0 0 2px rgba(22, 160, 133, 0.2);
}

/* Footer */
.footer {
  background-color: var(--dark-color);
  color: white;
  padding: 3rem 0;
}

.footer-links {
  display: flex;
  justify-content: center;
  list-style: none;
  padding: 0;
  margin: 2rem 0 0;
}

.footer-link {
  margin: 0 1rem;
}

.footer-link a {
  color: white;
}

.footer-link a:hover {
  color: var(--secondary-color);
}

/* Responsive Design */
@media (max-width: 768px) {
  .nav-menu {
    flex-direction: column;
    align-items: center;
  }

  .nav-item {
    margin: 0.5rem 0;
  }

  .section {
    padding: 2rem 0;
  }

  .footer-links {
    flex-direction: column;
    align-items: center;
  }

  .footer-link {
    margin: 0.5rem 0;
  }
}
```
