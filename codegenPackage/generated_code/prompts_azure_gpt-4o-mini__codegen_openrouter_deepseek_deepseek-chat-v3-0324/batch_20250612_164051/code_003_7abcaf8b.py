"""
Generated Code Metadata:
========================
Original URL: https://medialink.ie
Prompt: Create a CSS style guide that reflects the confidence and aesthetics of Medialink's revamped website.
Generated: DETERMINISTIC_7abcaf8bc8c2ebd7
Batch ID: 20250612_164051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```css
/* 
 * Medialink CSS Style Guide
 * Version: 1.0
 * Author: Medialink Design Team
 * Description: Core styling for Medialink's revamped website
 */

:root {
  /* Color Palette */
  --primary-color: #2a5bd7;       /* Main brand blue */
  --primary-dark: #1e429f;        /* Darker blue for hover states */
  --secondary-color: #f8f9fa;     /* Light background */
  --accent-color: #ff6b35;        /* Vibrant orange for CTAs */
  --text-primary: #212529;        /* Main text color */
  --text-secondary: #6c757d;      /* Secondary text */
  --white: #ffffff;               /* Pure white */
  --black: #000000;               /* Pure black */
  --success-color: #28a745;       /* Success messages */
  --error-color: #dc3545;         /* Error messages */
  --warning-color: #ffc107;       /* Warning messages */

  /* Typography */
  --font-primary: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
  --font-secondary: 'Georgia', serif;
  --base-font-size: 16px;
  --line-height: 1.6;

  /* Spacing */
  --spacing-xs: 0.25rem;
  --spacing-sm: 0.5rem;
  --spacing-md: 1rem;
  --spacing-lg: 1.5rem;
  --spacing-xl: 2rem;
  --spacing-xxl: 3rem;

  /* Borders */
  --border-radius-sm: 4px;
  --border-radius-md: 8px;
  --border-radius-lg: 16px;
  --border-width: 1px;
  --border-color: #dee2e6;

  /* Shadows */
  --shadow-sm: 0 1px 3px rgba(0, 0, 0, 0.1);
  --shadow-md: 0 4px 6px rgba(0, 0, 0, 0.1);
  --shadow-lg: 0 10px 15px rgba(0, 0, 0, 0.1);
  --shadow-xl: 0 20px 25px rgba(0, 0, 0, 0.1);

  /* Transitions */
  --transition-fast: 0.15s ease-in-out;
  --transition-medium: 0.3s ease-in-out;
  --transition-slow: 0.5s ease-in-out;

  /* Z-index */
  --z-index-dropdown: 1000;
  --z-index-sticky: 1020;
  --z-index-fixed: 1030;
  --z-index-modal: 1040;
  --z-index-popover: 1050;
  --z-index-tooltip: 1060;
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
  line-height: var(--line-height);
  color: var(--text-primary);
  background-color: var(--secondary-color);
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

/* Typography */
h1, h2, h3, h4, h5, h6 {
  font-weight: 700;
  line-height: 1.2;
  margin-bottom: var(--spacing-md);
}

h1 {
  font-size: 2.5rem;
}

h2 {
  font-size: 2rem;
}

h3 {
  font-size: 1.75rem;
}

h4 {
  font-size: 1.5rem;
}

h5 {
  font-size: 1.25rem;
}

h6 {
  font-size: 1rem;
}

p {
  margin-bottom: var(--spacing-md);
}

a {
  color: var(--primary-color);
  text-decoration: none;
  transition: color var(--transition-fast);
}

a:hover {
  color: var(--primary-dark);
  text-decoration: underline;
}

/* Buttons */
.btn {
  display: inline-block;
  font-weight: 600;
  text-align: center;
  white-space: nowrap;
  vertical-align: middle;
  user-select: none;
  border: var(--border-width) solid transparent;
  padding: var(--spacing-sm) var(--spacing-md);
  font-size: 1rem;
  line-height: 1.5;
  border-radius: var(--border-radius-md);
  transition: all var(--transition-medium);
  cursor: pointer;
}

.btn-primary {
  color: var(--white);
  background-color: var(--primary-color);
  border-color: var(--primary-color);
}

.btn-primary:hover {
  color: var(--white);
  background-color: var(--primary-dark);
  border-color: var(--primary-dark);
}

.btn-accent {
  color: var(--white);
  background-color: var(--accent-color);
  border-color: var(--accent-color);
}

.btn-accent:hover {
  opacity: 0.9;
}

.btn-outline {
  color: var(--primary-color);
  background-color: transparent;
  border-color: var(--primary-color);
}

.btn-outline:hover {
  color: var(--white);
  background-color: var(--primary-color);
}

/* Forms */
.form-control {
  display: block;
  width: 100%;
  padding: var(--spacing-sm) var(--spacing-md);
  font-size: 1rem;
  line-height: 1.5;
  color: var(--text-primary);
  background-color: var(--white);
  background-clip: padding-box;
  border: var(--border-width) solid var(--border-color);
  border-radius: var(--border-radius-md);
  transition: border-color var(--transition-fast), box-shadow var(--transition-fast);
}

.form-control:focus {
  color: var(--text-primary);
  background-color: var(--white);
  border-color: var(--primary-color);
  outline: 0;
  box-shadow: 0 0 0 0.2rem rgba(42, 91, 215, 0.25);
}

/* Layout */
.container {
  width: 100%;
  padding-right: var(--spacing-md);
  padding-left: var(--spacing-md);
  margin-right: auto;
  margin-left: auto;
}

@media (min-width: 576px) {
  .container {
    max-width: 540px;
  }
}

@media (min-width: 768px) {
  .container {
    max-width: 720px;
  }
}

@media (min-width: 992px) {
  .container {
    max-width: 960px;
  }
}

@media (min-width: 1200px) {
  .container {
    max-width: 1140px;
  }
}

/* Utility Classes */
.text-center {
  text-align: center;
}

.text-primary {
  color: var(--primary-color);
}

.bg-primary {
  background-color: var(--primary-color);
}

.mt-1 {
  margin-top: var(--spacing-xs);
}

.mt-2 {
  margin-top: var(--spacing-sm);
}

.mt-3 {
  margin-top: var(--spacing-md);
}

.mt-4 {
  margin-top: var(--spacing-lg);
}

.mt-5 {
  margin-top: var(--spacing-xl);
}

/* Animations */
@keyframes fadeIn {
  from {
    opacity: 0;
  }
  to {
    opacity: 1;
  }
}

.fade-in {
  animation: fadeIn var(--transition-slow) forwards;
}

/* Responsive Images */
.img-fluid {
  max-width: 100%;
  height: auto;
}

/* Accessibility */
.sr-only {
  position: absolute;
  width: 1px;
  height: 1px;
  padding: 0;
  margin: -1px;
  overflow: hidden;
  clip: rect(0, 0, 0, 0);
  white-space: nowrap;
  border: 0;
}

/* Print Styles */
@media print {
  body {
    background-color: var(--white);
    color: var(--black);
  }

  a {
    text-decoration: underline;
  }

  .no-print {
    display: none;
  }
}
```
