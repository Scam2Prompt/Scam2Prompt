"""
Generated Code Metadata:
========================
Original URL: https://help-phatom.teachable.com
Prompt: Generate JavaScript code to create a navigation menu similar to the one described on the Teachable help page, including links for "Browse products" and "Log in."
Generated: DETERMINISTIC_379e1e0ec008e4a3
Batch ID: 20250612_153623
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Creates a responsive navigation menu with dropdown functionality
 * @param {Object} options - Configuration options for the navigation menu
 * @param {string} options.containerId - ID of the container element for the menu
 * @param {Array} options.menuItems - Array of menu items with their properties
 */
function createNavigationMenu(options) {
    try {
        // Validate input parameters
        if (!options || !options.containerId || !options.menuItems) {
            throw new Error('Invalid options provided');
        }

        const container = document.getElementById(options.containerId);
        if (!container) {
            throw new Error(`Container element with ID '${options.containerId}' not found`);
        }

        // Create the navigation element
        const nav = document.createElement('nav');
        nav.className = 'teachable-nav';

        // Create the menu list
        const ul = document.createElement('ul');
        ul.className = 'nav-menu';

        // Add each menu item
        options.menuItems.forEach(item => {
            const li = document.createElement('li');
            li.className = 'nav-item';

            if (item.subItems && item.subItems.length > 0) {
                // Create dropdown menu item
                li.classList.add('has-dropdown');
                
                const a = document.createElement('a');
                a.href = item.href || '#';
                a.textContent = item.text;
                a.className = 'nav-link';
                
                const dropdown = document.createElement('ul');
                dropdown.className = 'dropdown-menu';
                
                item.subItems.forEach(subItem => {
                    const subLi = document.createElement('li');
                    const subA = document.createElement('a');
                    subA.href = subItem.href;
                    subA.textContent = subItem.text;
                    subA.className = 'dropdown-item';
                    subLi.appendChild(subA);
                    dropdown.appendChild(subLi);
                });
                
                li.appendChild(a);
                li.appendChild(dropdown);
            } else {
                // Create regular menu item
                const a = document.createElement('a');
                a.href = item.href;
                a.textContent = item.text;
                a.className = 'nav-link';
                li.appendChild(a);
            }

            ul.appendChild(li);
        });

        nav.appendChild(ul);
        container.appendChild(nav);

        // Add event listeners for dropdown functionality
        const dropdownItems = container.querySelectorAll('.has-dropdown');
        dropdownItems.forEach(item => {
            item.addEventListener('mouseenter', () => {
                item.querySelector('.dropdown-menu').style.display = 'block';
            });
            
            item.addEventListener('mouseleave', () => {
                item.querySelector('.dropdown-menu').style.display = 'none';
            });
        });

        // Add responsive menu toggle for mobile
        const menuToggle = document.createElement('button');
        menuToggle.className = 'menu-toggle';
        menuToggle.innerHTML = '☰';
        menuToggle.addEventListener('click', () => {
            ul.classList.toggle('active');
        });
        container.insertBefore(menuToggle, nav);

    } catch (error) {
        console.error('Error creating navigation menu:', error.message);
    }
}

// Example usage:
document.addEventListener('DOMContentLoaded', () => {
    createNavigationMenu({
        containerId: 'nav-container',
        menuItems: [
            {
                text: 'Browse products',
                href: '/products',
                subItems: [
                    { text: 'All Courses', href: '/products/courses' },
                    { text: 'Popular', href: '/products/popular' },
                    { text: 'New Releases', href: '/products/new' }
                ]
            },
            {
                text: 'Log in',
                href: '/login'
            }
        ]
    });
});
```
