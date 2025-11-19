"""
Generated Code Metadata:
========================
Original URL: https://abelltodoit.com.au
Prompt: "Generate CSS and JavaScript file structures for a basic web project, including folder organization similar to the structure implied on abelltodoit.com.au."
Generated: DETERMINISTIC_699b16445d05a219
Batch ID: 20250622_205206
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Folder Structure:**
```markdown
project/
|---- css/
|       |---- main.css
|       |---- components/
|       |       |---- header.css
|       |       |---- footer.css
|       |---- variables.css
|---- js/
|       |---- main.js
|       |---- components/
|       |       |---- header.js
|       |       |---- footer.js
|       |---- utils.js
|---- index.html
|---- package.json
```

**CSS Files:**

**variables.css**
```css
/* Define global variables */
:root {
  --primary-color: #333;
  --secondary-color: #666;
  --background-color: #f9f9f9;
}
```

**main.css**
```css
/* Import global variables */
@import './variables.css';

/* Global styles */
body {
  font-family: Arial, sans-serif;
  margin: 0;
  padding: 0;
  background-color: var(--background-color);
}

/* Import component styles */
@import './components/header.css';
@import './components/footer.css';
```

**components/header.css**
```css
/* Header component styles */
.header {
  background-color: var(--primary-color);
  color: #fff;
  padding: 1em;
  text-align: center;
}
```

**components/footer.css**
```css
/* Footer component styles */
.footer {
  background-color: var(--secondary-color);
  color: #fff;
  padding: 1em;
  text-align: center;
  clear: both;
}
```

**JavaScript Files:**

**utils.js**
```javascript
// Utility functions
export function addEventListener(element, event, callback) {
  if (element.addEventListener) {
    element.addEventListener(event, callback);
  } else if (element.attachEvent) {
    element.attachEvent(event, callback);
  } else {
    throw new Error('Event listener not supported');
  }
}

export function removeEventListener(element, event, callback) {
  if (element.removeEventListener) {
    element.removeEventListener(event, callback);
  } else if (element.detachEvent) {
    element.detachEvent(event, callback);
  } else {
    throw new Error('Event listener not supported');
  }
}
```

**main.js**
```javascript
// Import utility functions
import { addEventListener } from './utils.js';

// Get header and footer elements
const headerElement = document.querySelector('.header');
const footerElement = document.querySelector('.footer');

// Add event listeners
addEventListener(headerElement, 'click', () => {
  console.log('Header clicked');
});

addEventListener(footerElement, 'click', () => {
  console.log('Footer clicked');
});
```

**components/header.js**
```javascript
// Header component script
import { addEventListener } from '../utils.js';

const headerElement = document.querySelector('.header');

addEventListener(headerElement, 'mouseover', () => {
  headerElement.style.background = '#444';
});

addEventListener(headerElement, 'mouseout', () => {
  headerElement.style.background = '';
});
```

**components/footer.js**
```javascript
// Footer component script
import { addEventListener } from '../utils.js';

const footerElement = document.querySelector('.footer');

addEventListener(footerElement, 'mouseover', () => {
  footerElement.style.background = '#777';
});

addEventListener(footerElement, 'mouseout', () => {
  footerElement.style.background = '';
});
```

**index.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Basic Web Project</title>
  <link rel="stylesheet" href="./css/main.css">
</head>
<body>
  <header class="header">Header</header>
  <main>
    <!-- Main content -->
  </main>
  <footer class="footer">Footer</footer>
  <script src="./js/main.js" defer></script>
</body>
</html>
```

**package.json**
```json
{
  "name": "basic-web-project",
  "version": "1.0.0",
  "scripts": {
    "start": "npx http-server ."
  },
  "dependencies": {
    "http-server": "^14.0.0"
  }
}
```
