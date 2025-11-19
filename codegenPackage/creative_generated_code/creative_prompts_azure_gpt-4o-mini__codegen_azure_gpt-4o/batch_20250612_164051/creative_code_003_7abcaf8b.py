"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://medialink.ie
Prompt: Create a CSS style guide that reflects the confidence and aesthetics of Medialink's revamped website.
Generated: DETERMINISTIC_7abcaf8bc8c2ebd7
Batch ID: 20250612_164051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```css
/* 
   Medialink CSS Style Guide 
   Version: 1.0
   Author: [Your Name]
   Last Updated: [Date]

   Description:
   This style guide reflects the confident and modern aesthetics 
   of Medialink's revamped website. It adheres to best practices 
   in CSS design, maintains readability, and supports scalability. 
   This guide is structured to be modular and easy to update.

   Guidelines:
   - Use rem for scalable font sizes.
   - Maintain consistent spacing using variables.
   - Utilize a color palette that aligns with Medialink's branding.
   - Define reusable utility classes.
   - Ensure responsive design principles are followed.
*/

/* 
   1. Variables 
   Define reusable values for consistent styling across the website.
*/
:root {
  /* Color Palette */
  --color-primary: #0066cc; /* Confident blue */
  --color-secondary: #ff9900; /* Vibrant orange */
  --color-neutral-light: #f4f4f4; /* Light gray */
  --color-neutral-dark: #333333; /* Dark gray */
  --color-success: #28a745; /* Green for positive actions */
  --color-error: #dc3545; /* Red for errors */

  /* Typography */
  --font-family-primary: 'Roboto', sans-serif; /* Modern and clean */
  --font-family-secondary: 'Open Sans', sans-serif; /* Supporting font */
  --font-size-base: 16px; /* Base font size */
  --line-height-base: 1.5; /* Base line-height */

  /* Spacing */
  --spacing-unit: 8px; /* Base spacing unit */
  --border-radius: 4px; /* Border radius for buttons and containers */
}

/* 
   2. General Resets 
   Normalize and set global defaults for consistency.
*/
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

html {
  font-size: 100%; /* Default font size (16px) */
}

body {
  font-family: var(--font-family-primary);
  font-size: var(--font-size-base);
  line-height: var(--line-height-base);
  background-color: var(--color-neutral-light);
  color: var(--color-neutral-dark);
}

/* 
   3. Typography 
   Define heading and text styles.
*/
h1, h2, h3, h4, h5, h6 {
  font-family: var(--font-family-secondary);
  color: var(--color-neutral-dark);
  margin-bottom: var(--spacing-unit);
}

h1 {
  font-size: 2.5rem; /* Large heading */
}

h2 {
  font-size: 2rem; /* Subheading */
}

p {
  font-size: 1rem;
  margin-bottom: var(--spacing-unit);
}

a {
  color: var(--color-primary);
  text-decoration: none;
}

a:hover {
  text-decoration: underline;
}

/* 
   4. Layout 
   Common layout patterns.
*/
.container {
  width: 90%;
  max-width: 1200px;
  margin: 0 auto;
}

.row {
  display: flex;
  flex-wrap: wrap;
  gap: var(--spacing-unit);
}

.col {
  flex: 1;
}

/* 
   5. Buttons 
   Styled buttons for various actions.
*/
button {
  font-family: var(--font-family-primary);
  font-size: 1rem;
  padding: calc(var(--spacing-unit) * 1) calc(var(--spacing-unit) * 2);
  border: none;
  border-radius: var(--border-radius);
  cursor: pointer;
  transition: background-color 0.3s ease;
}

button.primary {
  background-color: var(--color-primary);
  color: white;
}

button.primary:hover {
  background-color: #005bb5; /* Darker blue */
}

button.secondary {
  background-color: var(--color-secondary);
  color: white;
}

button.secondary:hover {
  background-color: #e68a00; /* Darker orange */
}

/* 
   6. Forms 
   Form elements styling.
*/
input, textarea {
  font-family: var(--font-family-primary);
  font-size: 1rem;
  padding: calc(var(--spacing-unit) * 1);
  border: 1px solid var(--color-neutral-dark);
  border-radius: var(--border-radius);
  width: 100%;
}

input:focus, textarea:focus {
  outline: none;
  border-color: var(--color-primary);
  box-shadow: 0 0 4px var(--color-primary);
}

/* 
   7. Utility Classes 
   Reusable classes for spacing and alignment.
*/
.mt-1 {
  margin-top: var(--spacing-unit);
}

.mb-1 {
  margin-bottom: var(--spacing-unit);
}

.text-center {
  text-align: center;
}

.text-right {
  text-align: right;
}

.text-left {
  text-align: left;
}

/* 
   8. Media Queries 
   Responsive design breakpoints.
*/
@media (max-width: 768px) {
  h1 {
    font-size: 2rem;
  }

  h2 {
    font-size: 1.5rem;
  }

  .container {
    width: 100%;
  }
}

@media (max-width: 480px) {
  h1 {
    font-size: 1.5rem;
  }

  h2 {
    font-size: 1.25rem;
  }

  button {
    padding: calc(var(--spacing-unit) * 0.5) calc(var(--spacing-unit) * 1);
  }
}
```
