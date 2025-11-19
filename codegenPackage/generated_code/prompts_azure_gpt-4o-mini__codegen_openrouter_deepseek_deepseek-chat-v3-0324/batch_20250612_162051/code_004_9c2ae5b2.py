"""
Generated Code Metadata:
========================
Original URL: https://metaforce360.com
Prompt: Create a CSS style guide that aligns with the user-friendly design principles highlighted by Meta Force 360 for modern websites.
Generated: DETERMINISTIC_9c2ae5b262e4daab
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```css
/* 
 * Meta Force 360 CSS Style Guide
 * Aligns with user-friendly design principles for modern websites
 */

/* Base Styles */
:root {
    /* Color Palette */
    --primary-color: #4a6bff;
    --secondary-color: #6c757d;
    --success-color: #28a745;
    --danger-color: #dc3545;
    --warning-color: #ffc107;
    --info-color: #17a2b8;
    --light-color: #f8f9fa;
    --dark-color: #343a40;
    --white: #ffffff;
    --black: #000000;

    /* Typography */
    --font-family-sans-serif: 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
    --font-family-monospace: SFMono-Regular, Menlo, Monaco, Consolas, 'Liberation Mono', 'Courier New', monospace;
    --base-font-size: 16px;
    --line-height: 1.5;

    /* Spacing */
    --spacing-unit: 1rem;
    --spacing-xs: calc(var(--spacing-unit) * 0.25);
    --spacing-sm: calc(var(--spacing-unit) * 0.5);
    --spacing-md: var(--spacing-unit);
    --spacing-lg: calc(var(--spacing-unit) * 1.5);
    --spacing-xl: calc(var(--spacing-unit) * 3);

    /* Borders */
    --border-radius-sm: 0.2rem;
    --border-radius-md: 0.3rem;
    --border-radius-lg: 0.5rem;
    --border-width: 1px;
    --border-color: #dee2e6;

    /* Shadows */
    --box-shadow-sm: 0 0.125rem 0.25rem rgba(0, 0, 0, 0.075);
    --box-shadow-md: 0 0.5rem 1rem rgba(0, 0, 0, 0.15);
    --box-shadow-lg: 0 1rem 3rem rgba(0, 0, 0, 0.175);

    /* Transitions */
    --transition-speed: 0.3s;
    --transition-timing: ease-in-out;
}

/* Reset and Base Styles */
*,
*::before,
*::after {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
}

html {
    font-size: var(--base-font-size);
    line-height: var(--line-height);
    -webkit-text-size-adjust: 100%;
    -webkit-tap-highlight-color: transparent;
}

body {
    font-family: var(--font-family-sans-serif);
    color: var(--dark-color);
    background-color: var(--white);
    margin: 0;
    padding: 0;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
}

/* Typography */
h1, h2, h3, h4, h5, h6 {
    margin-top: 0;
    margin-bottom: var(--spacing-sm);
    font-weight: 600;
    line-height: 1.2;
}

h1 { font-size: 2.5rem; }
h2 { font-size: 2rem; }
h3 { font-size: 1.75rem; }
h4 { font-size: 1.5rem; }
h5 { font-size: 1.25rem; }
h6 { font-size: 1rem; }

p {
    margin-top: 0;
    margin-bottom: var(--spacing-md);
}

a {
    color: var(--primary-color);
    text-decoration: none;
    transition: color var(--transition-speed) var(--transition-timing);
}
a:hover {
    color: darken(var(--primary-color), 10%);
    text-decoration: underline;
}

/* Buttons */
.btn {
    display: inline-block;
    font-weight: 400;
    text-align: center;
    white-space: nowrap;
    vertical-align: middle;
    user-select: none;
    border: var(--border-width) solid transparent;
    padding: var(--spacing-sm) var(--spacing-md);
    font-size: 1rem;
    line-height: var(--line-height);
    border-radius: var(--border-radius-md);
    transition: all var(--transition-speed) var(--transition-timing);
    cursor: pointer;
}

.btn-primary {
    color: var(--white);
    background-color: var(--primary-color);
    border-color: var(--primary-color);
}
.btn-primary:hover {
    background-color: darken(var(--primary-color), 10%);
    border-color: darken(var(--primary-color), 10%);
}

/* Forms */
.form-control {
    display: block;
    width: 100%;
    padding: var(--spacing-sm) var(--spacing-md);
    font-size: 1rem;
    line-height: var(--line-height);
    color: var(--dark-color);
    background-color: var(--white);
    background-clip: padding-box;
    border: var(--border-width) solid var(--border-color);
    border-radius: var(--border-radius-md);
    transition: border-color var(--transition-speed) var(--transition-timing);
}
.form-control:focus {
    color: var(--dark-color);
    background-color: var(--white);
    border-color: lighten(var(--primary-color), 25%);
    outline: 0;
    box-shadow: 0 0 0 0.2rem rgba(74, 107, 255, 0.25);
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
.text-center { text-align: center; }
.text-left { text-align: left; }
.text-right { text-align: right; }

.mt-0 { margin-top: 0; }
.mt-1 { margin-top: var(--spacing-xs); }
.mt-2 { margin-top: var(--spacing-sm); }
.mt-3 { margin-top: var(--spacing-md); }
.mt-4 { margin-top: var(--spacing-lg); }
.mt-5 { margin-top: var(--spacing-xl); }

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

/* Animations */
@keyframes fadeIn {
    from { opacity: 0; }
    to { opacity: 1; }
}

.fade-in {
    animation: fadeIn var(--transition-speed) var(--transition-timing);
}
```
