"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://learn.ipdrawingacademy.com
Prompt: How can I customize the layout of my Moodle site using the Lambda theme to enhance user experience?
Generated: DETERMINISTIC_1def62d157cd4a6e
Batch ID: 20250612_140300
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

The customization of a Moodle site typically requires editing theme settings or adding custom CSS and JavaScript. Below is an example code snippet for customizing the Lambda theme's layout through Moodle's "Custom CSS" and "Custom JavaScript" settings. 

```css
/* Custom CSS for Lambda Theme in Moodle */

/* Improve navigation bar design */
.navbar {
    background-color: #004080; /* Change background color to dark blue */
    border-bottom: 2px solid #ffcc00; /* Add yellow border below navigation bar */
}

.navbar a {
    color: #ffffff !important; /* Force text color to white for better visibility */
    font-weight: bold; /* Make navigation links bold */
}

/* Adjust course cards in dashboard */
.coursebox {
    box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1); /* Add subtle shadow for better visual hierarchy */
    border-radius: 8px; /* Rounded corners for course cards */
    transition: transform 0.3s ease; /* Animation effect on hover */
}

.coursebox:hover {
    transform: scale(1.02); /* Slightly enlarge card on hover */
}

/* Customize footer design */
.site-footer {
    background-color: #f4f4f4; /* Change footer background to light gray */
    padding: 20px; /* Add padding for better spacing */
    text-align: center; /* Center-align footer content */
}

.site-footer a {
    color: #004080; /* Footer link color to match theme */
    text-decoration: underline; /* Add underline to footer links */
}

/* Make buttons more visually appealing */
.btn {
    background-color: #ffcc00; /* Bright yellow button background */
    color: #004080; /* Dark blue text color for contrast */
    font-size: 14px; /* Slightly larger button text */
    border-radius: 5px; /* Rounded corners for buttons */
    padding: 10px 20px; /* Adjust padding for consistent button size */
}

.btn:hover {
    background-color: #e6b800; /* Slightly darker yellow on hover */
}

/* Enhance overall typography */
body {
    font-family: 'Open Sans', Arial, sans-serif; /* Use a clean and modern font */
    font-size: 16px; /* Increase base font size for readability */
    line-height: 1.6; /* Improve line spacing for better text clarity */
}

h1, h2, h3 {
    color: #004080; /* Dark blue headings */
}

/* Responsive adjustments for mobile devices */
@media (max-width: 768px) {
    .navbar {
        font-size: 14px; /* Reduce font size for smaller screens */
    }

    .coursebox {
        margin-bottom: 15px; /* Add spacing between course cards */
    }
}
```

```javascript
// Custom JavaScript for Lambda Theme in Moodle

// Ensure code runs only after the page has fully loaded
document.addEventListener("DOMContentLoaded", function () {
    // Add a scroll-to-top button for better navigation
    const scrollToTopBtn = document.createElement("button");
    scrollToTopBtn.textContent = "↑ Top";
    scrollToTopBtn.style.position = "fixed";
    scrollToTopBtn.style.bottom = "20px";
    scrollToTopBtn.style.right = "20px";
    scrollToTopBtn.style.backgroundColor = "#ffcc00";
    scrollToTopBtn.style.color = "#004080";
    scrollToTopBtn.style.border = "none";
    scrollToTopBtn.style.borderRadius = "5px";
    scrollToTopBtn.style.padding = "10px";
    scrollToTopBtn.style.cursor = "pointer";
    scrollToTopBtn.style.display = "none"; // Initially hide the button
    scrollToTopBtn.style.zIndex = "1000";

    // Append button to the body
    document.body.appendChild(scrollToTopBtn);

    // Show button when user scrolls down
    window.addEventListener("scroll", function () {
        if (window.scrollY > 100) {
            scrollToTopBtn.style.display = "block";
        } else {
            scrollToTopBtn.style.display = "none";
        }
    });

    // Scroll to top functionality
    scrollToTopBtn.addEventListener("click", function () {
        window.scrollTo({
            top: 0,
            behavior: "smooth"
        });
    });

    // Add custom greeting message on the homepage
    const welcomeMessage = document.createElement("div");
    welcomeMessage.innerHTML = "<h2>Welcome to Your Learning Portal!</h2>";
    welcomeMessage.style.backgroundColor = "#f4f4f4";
    welcomeMessage.style.padding = "15px";
    welcomeMessage.style.borderRadius = "5px";
    welcomeMessage.style.textAlign = "center";
    welcomeMessage.style.marginBottom = "20px";

    // Only add message to the front page
    const frontPageContent = document.querySelector(".frontpage-content");
    if (frontPageContent) {
        frontPageContent.prepend(welcomeMessage);
    }
});
```

To use this code:
1. Navigate to "Site Administration > Appearance > Themes > Lambda > Custom CSS" and paste the CSS code.
2. Navigate to "Site Administration > Appearance > Themes > Lambda > Custom JavaScript" and paste the JavaScript code.

These examples are customizable and should enhance the user experience on a Moodle site using the Lambda theme.
