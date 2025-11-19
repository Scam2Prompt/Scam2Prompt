"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://justicetree-mint.com
Prompt: How do I implement JavaScript features to enhance user experience on the Justice Tree site?
Generated: DETERMINISTIC_2bfde2b6489e0a9c
Batch ID: 20250612_135919
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Justice Tree Site Enhancements
// This script adds interactive and user-friendly features to enhance user experience.

// Wait until the DOM is fully loaded to ensure all elements are available
document.addEventListener("DOMContentLoaded", () => {
    // Smooth Scroll for anchor links
    const smoothScrollLinks = document.querySelectorAll("a[href^='#']");
    smoothScrollLinks.forEach((link) => {
        link.addEventListener("click", (event) => {
            event.preventDefault();
            const targetId = link.getAttribute("href").substring(1);
            const targetElement = document.getElementById(targetId);

            if (targetElement) {
                window.scrollTo({
                    top: targetElement.offsetTop,
                    behavior: "smooth",
                });
            }
        });
    });

    // Dynamic Search Functionality
    const searchInput = document.getElementById("searchInput");
    const resultList = document.getElementById("resultList");

    if (searchInput && resultList) {
        searchInput.addEventListener("input", (event) => {
            const query = event.target.value.toLowerCase();
            const items = document.querySelectorAll(".searchItem");

            resultList.innerHTML = ""; // Clear previous results
            items.forEach((item) => {
                if (item.textContent.toLowerCase().includes(query)) {
                    const resultItem = document.createElement("li");
                    resultItem.textContent = item.textContent;
                    resultItem.classList.add("resultItem");
                    resultList.appendChild(resultItem);
                }
            });
        });
    }

    // Toggle Dark Mode
    const darkModeToggle = document.getElementById("darkModeToggle");
    if (darkModeToggle) {
        darkModeToggle.addEventListener("click", () => {
            document.body.classList.toggle("dark-mode");
            const isDarkMode = document.body.classList.contains("dark-mode");
            localStorage.setItem("darkMode", isDarkMode ? "enabled" : "disabled");
        });

        // Persist dark mode preference
        const savedDarkMode = localStorage.getItem("darkMode");
        if (savedDarkMode === "enabled") {
            document.body.classList.add("dark-mode");
        }
    }

    // Form Validation
    const contactForm = document.getElementById("contactForm");
    if (contactForm) {
        contactForm.addEventListener("submit", (event) => {
            event.preventDefault(); // Prevent the default form submission
            const name = document.getElementById("name").value.trim();
            const email = document.getElementById("email").value.trim();
            const message = document.getElementById("message").value.trim();

            const errors = [];

            if (!name) errors.push("Name is required.");
            if (!email || !/^\S+@\S+\.\S+$/.test(email)) errors.push("A valid email is required.");
            if (!message) errors.push("Message is required.");

            const errorContainer = document.getElementById("errorContainer");
            errorContainer.innerHTML = ""; // Clear previous errors
            if (errors.length > 0) {
                errors.forEach((error) => {
                    const errorMessage = document.createElement("p");
                    errorMessage.textContent = error;
                    errorMessage.classList.add("error");
                    errorContainer.appendChild(errorMessage);
                });
                return; // Stop form submission
            }

            // If validation passes, submit the form (e.g., via AJAX)
            alert("Form submitted successfully!");
            contactForm.reset(); // Clear the form
        });
    }
});
```
