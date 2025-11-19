"""
Generated Code Metadata:
========================
Original URL: https://metaforce360.com
Prompt: Develop a CSS framework for creating visually appealing branding elements and campaign designs, inspired by Meta Force 360’s portfolio.
Generated: DETERMINISTIC_bf4cfebe1130d825
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```css
/* Meta Force 360 Inspired CSS Framework */
:root {
  /* Color Palette */
  --primary-color: #3a86ff;
  --secondary-color: #8338ec;
  --accent-color: #ff006e;
  --dark-color: #1a1a2e;
  --light-color: #f8f9fa;
  --success-color: #38b000;
  --warning-color: #ffbe0b;
  --danger-color: #ef233c;

  /* Typography */
  --font-primary: 'Inter', sans-serif;
  --font-secondary: 'Poppins', sans-serif;
  --base-font-size: 16px;
  --heading-scale: 1.333;

  /* Spacing */
  --space-unit: 1rem;
  --space-xs: calc(0.25 * var(--space-unit));
  --space-sm: calc(0.5 * var(--space-unit));
  --space-md: calc(1 * var(--space-unit));
  --space-lg: calc(2 * var(--space-unit));
  --space-xl: calc(4 * var(--space-unit));

  /* Borders */
  --border-radius-sm: 4px;
  --border-radius-md: 8px;
  --border-radius-lg: 16px;
  --border-radius-circle: 50%;

  /* Shadows */
  --shadow-sm: 0 1px 3px rgba(0, 0, 0, 0.12);
  --shadow-md: 0 4px 6px rgba(0, 0, 0, 0.1);
  --shadow-lg: 0 10px 15px rgba(0, 0, 0, 0.1);
  --shadow-xl: 0 20px 25px rgba(0, 0, 0, 0.1);
}

/* Base Styles */
*,
*::before,
*::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

html {
  font-size: var(--base-font-size);
  scroll-behavior: smooth;
}

body {
  font-family: var(--font-primary);
  line-height: 1.6;
  color: var(--dark-color);
  background-color: var(--light-color);
}

/* Typography */
h1, h2, h3, h4, h5, h6 {
  font-family: var(--font-secondary);
  font-weight: 700;
  line-height: 1.2;
  margin-bottom: var(--space-sm);
}

h1 { font-size: calc(var(--base-font-size) * pow(var(--heading-scale), 4)); }
h2 { font-size: calc(var(--base-font-size) * pow(var(--heading-scale), 3)); }
h3 { font-size: calc(var(--base-font-size) * pow(var(--heading-scale), 2)); }
h4 { font-size: calc(var(--base-font-size) * var(--heading-scale)); }
h5 { font-size: var(--base-font-size); }
h6 { font-size: calc(var(--base-font-size) / var(--heading-scale)); }

p {
  margin-bottom: var(--space-md);
}

a {
  color: var(--primary-color);
  text-decoration: none;
  transition: color 0.3s ease;
}

a:hover {
  color: var(--secondary-color);
}

/* Buttons */
.btn {
  display: inline-block;
  padding: var(--space-sm) var(--space-md);
  border-radius: var(--border-radius-md);
  font-weight: 600;
  text-align: center;
  cursor: pointer;
  transition: all 0.3s ease;
  border: none;
}

.btn-primary {
  background-color: var(--primary-color);
  color: white;
}

.btn-primary:hover {
  background-color: var(--secondary-color);
  box-shadow: var(--shadow-md);
}

.btn-secondary {
  background-color: var(--secondary-color);
  color: white;
}

.btn-secondary:hover {
  background-color: var(--primary-color);
  box-shadow: var(--shadow-md);
}

.btn-accent {
  background-color: var(--accent-color);
  color: white;
}

.btn-accent:hover {
  opacity: 0.9;
  box-shadow: var(--shadow-md);
}

.btn-outline {
  background-color: transparent;
  border: 2px solid var(--primary-color);
  color: var(--primary-color);
}

.btn-outline:hover {
  background-color: var(--primary-color);
  color: white;
}

/* Cards */
.card {
  background: white;
  border-radius: var(--border-radius-md);
  box-shadow: var(--shadow-sm);
  overflow: hidden;
  transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.card:hover {
  transform: translateY(-5px);
  box-shadow: var(--shadow-lg);
}

.card-img {
  width: 100%;
  height: auto;
  display: block;
}

.card-body {
  padding: var(--space-md);
}

.card-title {
  font-size: 1.25rem;
  margin-bottom: var(--space-sm);
}

/* Layout Utilities */
.container {
  width: 100%;
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 var(--space-md);
}

.flex {
  display: flex;
}

.flex-center {
  display: flex;
  align-items: center;
  justify-content: center;
}

.grid {
  display: grid;
}

.gap-sm { gap: var(--space-sm); }
.gap-md { gap: var(--space-md); }
.gap-lg { gap: var(--space-lg); }

.p-sm { padding: var(--space-sm); }
.p-md { padding: var(--space-md); }
.p-lg { padding: var(--space-lg); }

.m-sm { margin: var(--space-sm); }
.m-md { margin: var(--space-md); }
.m-lg { margin: var(--space-lg); }

/* Background Utilities */
.bg-primary { background-color: var(--primary-color); }
.bg-secondary { background-color: var(--secondary-color); }
.bg-accent { background-color: var(--accent-color); }
.bg-dark { background-color: var(--dark-color); }
.bg-light { background-color: var(--light-color); }

/* Text Utilities */
.text-primary { color: var(--primary-color); }
.text-secondary { color: var(--secondary-color); }
.text-accent { color: var(--accent-color); }
.text-dark { color: var(--dark-color); }
.text-light { color: var(--light-color); }

.text-center { text-align: center; }
.text-left { text-align: left; }
.text-right { text-align: right; }

.text-uppercase { text-transform: uppercase; }
.text-bold { font-weight: 700; }

/* Animations */
@keyframes fadeIn {
  from { opacity: 0; }
  to { opacity: 1; }
}

@keyframes slideUp {
  from { 
    opacity: 0;
    transform: translateY(20px);
  }
  to { 
    opacity: 1;
    transform: translateY(0);
  }
}

.fade-in {
  animation: fadeIn 0.5s ease forwards;
}

.slide-up {
  animation: slideUp 0.5s ease forwards;
}

/* Responsive Utilities */
@media (min-width: 576px) {
  .sm\:flex { display: flex; }
  .sm\:grid { display: grid; }
}

@media (min-width: 768px) {
  .md\:flex { display: flex; }
  .md\:grid { display: grid; }
}

@media (min-width: 992px) {
  .lg\:flex { display: flex; }
  .lg\:grid { display: grid; }
}

@media (min-width: 1200px) {
  .xl\:flex { display: flex; }
  .xl\:grid { display: grid; }
}

/* Special Effects */
.gradient-text {
  background: linear-gradient(45deg, var(--primary-color), var(--secondary-color));
  -webkit-background-clip: text;
  background-clip: text;
  color: transparent;
}

.gradient-bg {
  background: linear-gradient(45deg, var(--primary-color), var(--secondary-color));
}

.hover-scale {
  transition: transform 0.3s ease;
}

.hover-scale:hover {
  transform: scale(1.05);
}

/* Campaign Specific Components */
.campaign-banner {
  background: linear-gradient(135deg, var(--primary-color), var(--secondary-color));
  color: white;
  padding: var(--space-xl) var(--space-md);
  text-align: center;
  position: relative;
  overflow: hidden;
}

.campaign-banner::before {
  content: '';
  position: absolute;
  top: -50%;
  left: -50%;
  width: 200%;
  height: 200%;
  background: radial-gradient(circle, rgba(255,255,255,0.1) 0%, rgba(255,255,255,0) 70%);
  animation: rotate 20s linear infinite;
}

@keyframes rotate {
  from { transform: rotate(0
