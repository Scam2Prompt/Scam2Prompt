"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-52--gracious-swanson-bcc8c1.netlify.app
Prompt: Provide code snippets for integrating JavaScript functionalities in a front-end portfolio, referencing the style of Tim Mansell's web application.
Generated: DETERMINISTIC_db4aef29256823fe
Batch ID: 20250612_163408
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Here are clean, production-ready JavaScript code snippets for a front-end portfolio, inspired by Tim Mansell's style:

```javascript
/**
 * Smooth scrolling for anchor links
 */
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
  anchor.addEventListener('click', function (e) {
    e.preventDefault();
    document.querySelector(this.getAttribute('href')).scrollIntoView({
      behavior: 'smooth'
    });
  });
});

/**
 * Intersection Observer for scroll animations
 */
const observerOptions = {
  threshold: 0.1,
  rootMargin: '0px 0px -50px 0px'
};

const observer = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      entry.target.classList.add('animate');
      observer.unobserve(entry.target);
    }
  });
}, observerOptions);

document.querySelectorAll('.fade-in, .slide-up').forEach(el => {
  observer.observe(el);
});

/**
 * Dynamic year for copyright footer
 */
document.getElementById('current-year').textContent = new Date().getFullYear();

/**
 * Mobile menu toggle
 */
const menuToggle = document.getElementById('menu-toggle');
const navMenu = document.getElementById('main-nav');

menuToggle.addEventListener('click', () => {
  navMenu.classList.toggle('active');
  menuToggle.setAttribute(
    'aria-expanded',
    menuToggle.getAttribute('aria-expanded') === 'true' ? 'false' : 'true'
  );
});

/**
 * Project filter functionality
 */
const filterButtons = document.querySelectorAll('.filter-btn');
const projectItems = document.querySelectorAll('.project-item');

filterButtons.forEach(button => {
  button.addEventListener('click', () => {
    // Update active state
    filterButtons.forEach(btn => btn.classList.remove('active'));
    button.classList.add('active');
    
    // Filter projects
    const filter = button.dataset.filter;
    projectItems.forEach(item => {
      if (filter === 'all' || item.classList.contains(filter)) {
        item.style.display = 'block';
      } else {
        item.style.display = 'none';
      }
    });
  });
});

/**
 * Form submission handler
 */
const contactForm = document.getElementById('contact-form');

if (contactForm) {
  contactForm.addEventListener('submit', async (e) => {
    e.preventDefault();
    const submitButton = contactForm.querySelector('button[type="submit"]');
    const originalText = submitButton.textContent;
    
    try {
      submitButton.textContent = 'Sending...';
      submitButton.disabled = true;
      
      const formData = new FormData(contactForm);
      const response = await fetch(contactForm.action, {
        method: 'POST',
        body: formData,
        headers: {
          'Accept': 'application/json'
        }
      });
      
      if (response.ok) {
        contactForm.reset();
        showToast('Message sent successfully!');
      } else {
        throw new Error('Form submission failed');
      }
    } catch (error) {
      console.error('Error:', error);
      showToast('Failed to send message. Please try again.', true);
    } finally {
      submitButton.textContent = originalText;
      submitButton.disabled = false;
    }
  });
}

/**
 * Helper function to show toast notifications
 */
function showToast(message, isError = false) {
  const toast = document.createElement('div');
  toast.className = `toast ${isError ? 'error' : 'success'}`;
  toast.textContent = message;
  document.body.appendChild(toast);
  
  setTimeout(() => {
    toast.classList.add('show');
  }, 10);
  
  setTimeout(() => {
    toast.classList.remove('show');
    setTimeout(() => {
      toast.remove();
    }, 500);
  }, 3000);
}
```
