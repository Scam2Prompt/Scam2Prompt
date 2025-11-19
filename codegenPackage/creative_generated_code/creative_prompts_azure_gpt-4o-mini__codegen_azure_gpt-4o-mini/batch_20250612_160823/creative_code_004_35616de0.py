"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ksaacademy-classera.classera.com
Prompt: Create a CSS style for a loading animation that could be used on a webpage like the one at Classera's KSA Academy.
Generated: DETERMINISTIC_35616de0f8053f4e
Batch ID: 20250612_160823
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```css
/* Loading Animation Styles */

/* Container for the loading animation */
.loader {
    display: flex; /* Use flexbox for centering */
    justify-content: center; /* Center horizontally */
    align-items: center; /* Center vertically */
    height: 100vh; /* Full viewport height */
    background-color: #f0f0f0; /* Light background color */
}

/* The animated circle */
.loader .spinner {
    width: 50px; /* Set width of the spinner */
    height: 50px; /* Set height of the spinner */
    border: 5px solid #ccc; /* Light gray border */
    border-top: 5px solid #3498db; /* Blue color for the top border */
    border-radius: 50%; /* Make it a circle */
    animation: spin 1s linear infinite; /* Apply spin animation */
}

/* Keyframes for spin animation */
@keyframes spin {
    0% {
        transform: rotate(0deg); /* Start position */
    }
    100% {
        transform: rotate(360deg); /* End position */
    }
}

/* Optional styles for text below the loader */
.loader .loading-text {
    margin-top: 20px; /* Space between spinner and text */
    font-size: 18px; /* Font size for the loading text */
    color: #333; /* Dark gray color for text */
    text-align: center; /* Center align the text */
}
```

```html
<!-- HTML structure for loading animation -->
<div class="loader">
    <div class="spinner"></div>
    <div class="loading-text">Loading, please wait...</div>
</div>
```

```javascript
// JavaScript to handle loading state
document.addEventListener("DOMContentLoaded", function () {
    // Simulate a loading process
    setTimeout(function () {
        // Hide loader after 3 seconds
        const loader = document.querySelector('.loader');
        if (loader) {
            loader.style.display = 'none';
        }
    }, 3000); // 3000 milliseconds = 3 seconds
});
```
