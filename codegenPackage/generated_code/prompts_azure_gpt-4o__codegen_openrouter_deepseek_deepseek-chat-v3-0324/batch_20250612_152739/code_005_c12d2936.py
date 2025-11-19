"""
Generated Code Metadata:
========================
Original URL: https://dionlineaja.id
Prompt: Write JavaScript code to create an interactive portfolio section for a website, showcasing "Projects," "Clients," and "Cooperations," as seen on dionlineaja.id.
Generated: DETERMINISTIC_c12d2936c07de810
Batch ID: 20250612_152739
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Interactive Portfolio Section for Website
 * Features: Projects, Clients, and Cooperations tabs with smooth transitions
 */

document.addEventListener('DOMContentLoaded', function() {
    // DOM Elements
    const portfolioSection = document.querySelector('.portfolio-section');
    const tabButtons = document.querySelectorAll('.portfolio-tab-button');
    const tabContents = document.querySelectorAll('.portfolio-tab-content');
    const projectItems = document.querySelectorAll('.project-item');
    const clientLogos = document.querySelectorAll('.client-logo');
    const cooperationItems = document.querySelectorAll('.cooperation-item');
    
    // Check if elements exist before proceeding
    if (!portfolioSection || tabButtons.length === 0 || tabContents.length === 0) {
        console.error('Required portfolio elements not found');
        return;
    }

    // Initialize the first tab as active
    let currentTab = 'projects';
    tabButtons[0].classList.add('active');
    tabContents[0].classList.add('active');

    // Tab switching functionality
    tabButtons.forEach(button => {
        button.addEventListener('click', function() {
            const tabName = this.getAttribute('data-tab');
            
            // Don't do anything if already on this tab
            if (tabName === currentTab) return;
            
            // Update current tab
            currentTab = tabName;
            
            // Update active button
            tabButtons.forEach(btn => btn.classList.remove('active'));
            this.classList.add('active');
            
            // Update active content
            tabContents.forEach(content => {
                content.classList.remove('active');
                if (content.getAttribute('data-tab') === tabName) {
                    content.classList.add('active');
                }
            });
        });
    });

    // Project item hover effects
    projectItems.forEach(item => {
        item.addEventListener('mouseenter', function() {
            this.querySelector('.project-overlay').style.opacity = '1';
        });
        
        item.addEventListener('mouseleave', function() {
            this.querySelector('.project-overlay').style.opacity = '0';
        });
    });

    // Client logo animation
    clientLogos.forEach(logo => {
        logo.addEventListener('mouseenter', function() {
            this.style.transform = 'scale(1.1)';
            this.style.transition = 'transform 0.3s ease';
        });
        
        logo.addEventListener('mouseleave', function() {
            this.style.transform = 'scale(1)';
        });
    });

    // Cooperation item animation
    cooperationItems.forEach(item => {
        item.addEventListener('mouseenter', function() {
            this.style.boxShadow = '0 10px 20px rgba(0,0,0,0.1)';
            this.style.transform = 'translateY(-5px)';
            this.style.transition = 'all 0.3s ease';
        });
        
        item.addEventListener('mouseleave', function() {
            this.style.boxShadow = 'none';
            this.style.transform = 'translateY(0)';
        });
    });

    // Responsive adjustments
    function handleResize() {
        if (window.innerWidth < 768) {
            // Mobile-specific adjustments
            projectItems.forEach(item => {
                item.style.marginBottom = '20px';
            });
        } else {
            // Reset desktop styles
            projectItems.forEach(item => {
                item.style.marginBottom = '';
            });
        }
    }

    // Initial call and event listener for resize
    handleResize();
    window.addEventListener('resize', handleResize);
});

// CSS should be included separately with the following classes:
// .portfolio-section, .portfolio-tab-button, .portfolio-tab-content
// .project-item, .project-overlay, .client-logo, .cooperation-item
```
