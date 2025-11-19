"""
Generated Code Metadata:
========================
Original URL: https://staketelegramapp.com
Prompt: Generate JavaScript code to implement collapsible groups for a portfolio section, ensuring functionality similar to the collapsible items described in the Avenger template.
Generated: DETERMINISTIC_1a90c01e30edad4d
Batch ID: 20250612_151255
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Collapsible Portfolio Groups
 * Implements collapsible functionality for portfolio sections similar to Avenger template.
 */

document.addEventListener('DOMContentLoaded', function() {
    // Initialize collapsible groups
    initCollapsibleGroups();
});

/**
 * Initializes all collapsible portfolio groups
 */
function initCollapsibleGroups() {
    const groupHeaders = document.querySelectorAll('.portfolio-group-header');
    
    if (!groupHeaders.length) return;
    
    groupHeaders.forEach(header => {
        // Set initial state from data attribute or default to collapsed
        const isExpanded = header.getAttribute('data-expanded') === 'true';
        const groupId = header.getAttribute('data-group-id');
        const content = document.querySelector(`.portfolio-group-content[data-group-id="${groupId}"]`);
        
        if (!content) return;
        
        // Set initial state
        setGroupState(header, content, isExpanded);
        
        // Add click event
        header.addEventListener('click', () => {
            const currentState = header.getAttribute('aria-expanded') === 'true';
            setGroupState(header, content, !currentState);
        });
        
        // Add keyboard support
        header.addEventListener('keydown', (e) => {
            if (e.key === 'Enter' || e.key === ' ') {
                e.preventDefault();
                const currentState = header.getAttribute('aria-expanded') === 'true';
                setGroupState(header, content, !currentState);
            }
        });
    });
}

/**
 * Sets the expanded/collapsed state of a portfolio group
 * @param {HTMLElement} header - The group header element
 * @param {HTMLElement} content - The group content element
 * @param {boolean} isExpanded - Whether the group should be expanded
 */
function setGroupState(header, content, isExpanded) {
    // Update ARIA attributes
    header.setAttribute('aria-expanded', isExpanded);
    content.setAttribute('aria-hidden', !isExpanded);
    
    // Toggle classes for styling
    header.classList.toggle('is-expanded', isExpanded);
    content.classList.toggle('is-expanded', isExpanded);
    
    // Store state in data attribute for persistence
    header.setAttribute('data-expanded', isExpanded);
    
    // Smooth height transition
    if (isExpanded) {
        content.style.height = 'auto';
        const height = content.scrollHeight + 'px';
        content.style.height = '0';
        // Force repaint
        content.getBoundingClientRect();
        content.style.height = height;
    } else {
        content.style.height = content.scrollHeight + 'px';
        // Force repaint
        content.getBoundingClientRect();
        content.style.height = '0';
    }
    
    // Clean up after transition
    const transitionEndHandler = () => {
        if (isExpanded) {
            content.style.height = 'auto';
        }
        content.removeEventListener('transitionend', transitionEndHandler);
    };
    
    content.addEventListener('transitionend', transitionEndHandler);
}

// Optional: Add mutation observer to handle dynamically loaded content
const observer = new MutationObserver(function(mutations) {
    mutations.forEach(function(mutation) {
        if (mutation.addedNodes.length) {
            initCollapsibleGroups();
        }
    });
});

observer.observe(document.body, {
    childList: true,
    subtree: true
});
```
