"""
Generated Code Metadata:
========================
Original URL: https://ungleder.no
Prompt: Generate a code snippet in JavaScript to implement a simple navigation menu, like the one on ungLeder.no, that allows users to access different sections, such as "Hva er ungLeder Norge?" and "Opplæringsdager".
Generated: DETERMINISTIC_898862039eeb0268
Batch ID: 20250622_205523
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Simple Navigation Menu Component
 * 
 * This script creates a responsive navigation menu with smooth scrolling to sections.
 * It handles click events for menu items and highlights the active section.
 */

class NavigationMenu {
  /**
   * Initialize the navigation menu
   * @param {Object} options - Configuration options
   * @param {string} options.menuSelector - CSS selector for the menu container
   * @param {string} options.menuItemSelector - CSS selector for menu items
   * @param {string} options.sectionSelector - CSS selector for page sections
   * @param {string} options.activeClass - Class name for active menu item
   */
  constructor(options) {
    this.options = {
      menuSelector: '.nav-menu',
      menuItemSelector: '.nav-item',
      sectionSelector: 'section',
      activeClass: 'active',
      ...options
    };

    this.menu = document.querySelector(this.options.menuSelector);
    this.menuItems = document.querySelectorAll(this.options.menuItemSelector);
    this.sections = document.querySelectorAll(this.options.sectionSelector);

    this.init();
  }

  /**
   * Initialize event listeners and set up the menu
   */
  init() {
    if (!this.menu || this.menuItems.length === 0 || this.sections.length === 0) {
      console.error('Navigation menu elements not found');
      return;
    }

    // Add click event listeners to menu items
    this.menuItems.forEach(item => {
      item.addEventListener('click', (e) => this.handleMenuItemClick(e));
    });

    // Add scroll event listener to highlight active section
    window.addEventListener('scroll', () => this.handleScroll());

    // Initialize active menu item
    this.handleScroll();
  }

  /**
   * Handle menu item click events
   * @param {Event} event - Click event
   */
  handleMenuItemClick(event) {
    event.preventDefault();
    const targetId = event.target.getAttribute('href');
    
    if (!targetId || targetId === '#') return;

    try {
      const targetSection = document.querySelector(targetId);
      if (targetSection) {
        targetSection.scrollIntoView({
          behavior: 'smooth',
          block: 'start'
        });
      }
    } catch (error) {
      console.error('Error scrolling to section:', error);
    }
  }

  /**
   * Handle scroll events to update active menu item
   */
  handleScroll() {
    let currentSection = '';
    
    this.sections.forEach(section => {
      const sectionTop = section.offsetTop;
      const sectionHeight = section.clientHeight;
      
      if (window.scrollY >= sectionTop - 100 && window.scrollY < sectionTop + sectionHeight - 100) {
        currentSection = `#${section.id}`;
      }
    });

    this.updateActiveMenuItem(currentSection);
  }

  /**
   * Update the active menu item based on current section
   * @param {string} currentSectionId - ID of the current section
   */
  updateActiveMenuItem(currentSectionId) {
    this.menuItems.forEach(item => {
      item.classList.remove(this.options.activeClass);
      if (item.getAttribute('href') === currentSectionId) {
        item.classList.add(this.options.activeClass);
      }
    });
  }
}

// Example usage when DOM is loaded
document.addEventListener('DOMContentLoaded', () => {
  new NavigationMenu({
    menuSelector: '.nav-menu',
    menuItemSelector: '.nav-item',
    sectionSelector: 'section',
    activeClass: 'active'
  });
});
```

HTML structure example (for reference):
```html
<nav class="nav-menu">
  <ul>
    <li><a href="#about" class="nav-item">Hva er ungLeder Norge?</a></li>
    <li><a href="#training" class="nav-item">Opplæringsdager</a></li>
    <li><a href="#contact" class="nav-item">Kontakt oss</a></li>
  </ul>
</nav>

<section id="about">
  <!-- Content for "Hva er ungLeder Norge?" section -->
</section>

<section id="training">
  <!-- Content for "Opplæringsdager" section -->
</section>

<section id="contact">
  <!-- Contact section content -->
</section>
```

CSS example (for reference):
```css
.nav-menu {
  background: #f8f8f8;
  padding: 1rem;
  position: sticky;
  top: 0;
  z-index: 100;
}

.nav-menu ul {
  display: flex;
  list-style: none;
  margin: 0;
  padding: 0;
  gap: 1rem;
}

.nav-item {
  text-decoration: none;
  color: #333;
  padding: 0.5rem 1rem;
  border-radius: 4px;
  transition: background-color 0.3s ease;
}

.nav-item:hover {
  background-color: #e0e0e0;
}

.nav-item.active {
  background-color: #007bff;
  color: white;
}

section {
  min-height: 100vh;
  padding: 2rem;
}
```
