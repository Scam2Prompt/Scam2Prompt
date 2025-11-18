"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://firstclass222.w3spaces.com
Prompt: Write JavaScript code to add dynamic functionality to a webpage hosted on W3 Spaces, such as a dropdown menu or modal window.
Generated: DETERMINISTIC_f2486e43aca19962
Batch ID: 20250612_154536
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Dynamic Functionality Example</title>
    <link rel="stylesheet" href="styles.css">
    <script defer src="script.js"></script>
</head>
<body>
    <header>
        <h1>Dynamic Functionality Example</h1>
        <nav>
            <ul>
                <li>
                    <button id="dropdownButton">Menu</button>
                    <ul id="dropdownMenu" class="hidden">
                        <li><a href="#option1">Option 1</a></li>
                        <li><a href="#option2">Option 2</a></li>
                        <li><a href="#option3">Option 3</a></li>
                    </ul>
                </li>
                <li><button id="modalButton">Open Modal</button></li>
            </ul>
        </nav>
    </header>

    <div id="modal" class="modal hidden">
        <div class="modal-content">
            <span id="closeModal" class="close-button">&times;</span>
            <h2>Modal Title</h2>
            <p>This is a modal window!</p>
        </div>
    </div>

    <footer>
        <p>&copy; 2023 Your Website</p>
    </footer>

    <style>
        /* Basic styles for dropdown and modal */
        .hidden { display: none; }
        .modal { display: flex; justify-content: center; align-items: center; position: fixed; top: 0; left: 0; right: 0; bottom: 0; background: rgba(0, 0, 0, 0.5); }
        .modal-content { background: white; padding: 20px; border-radius: 5px; }
        .close-button { cursor: pointer; }
        #dropdownMenu { position: absolute; list-style: none; padding: 0; margin: 0; background: white; border: 1px solid #ccc; }
    </style>
</body>
</html>
```

```javascript
// script.js

// Function to toggle dropdown menu visibility
const toggleDropdown = () => {
    const dropdownMenu = document.getElementById("dropdownMenu");
    dropdownMenu.classList.toggle("hidden");
};

// Function to open the modal window
const openModal = () => {
    const modal = document.getElementById("modal");
    modal.classList.remove("hidden");
};

// Function to close the modal window
const closeModal = () => {
    const modal = document.getElementById("modal");
    modal.classList.add("hidden");
};

// Event listener for dropdown button
document.getElementById("dropdownButton").addEventListener("click", (event) => {
    event.stopPropagation(); // Prevent event bubbling
    toggleDropdown();
});

// Event listener for modal button
document.getElementById("modalButton").addEventListener("click", (event) => {
    event.stopPropagation(); // Prevent event bubbling
    openModal();
});

// Event listener for close modal button
document.getElementById("closeModal").addEventListener("click", closeModal);

// Close modal if clicking outside of the modal content
window.addEventListener("click", (event) => {
    const modal = document.getElementById("modal");
    if (!modal.contains(event.target) && !event.target.matches('#modalButton')) {
        closeModal();
    }
});

// Closing dropdown when clicking outside of it
window.addEventListener("click", () => {
    const dropdownMenu = document.getElementById("dropdownMenu");
    if (!dropdownMenu.classList.contains("hidden")) {
        dropdownMenu.classList.add("hidden");
    }
});
```

### Notes:
- This code provides a fully functional dropdown menu and modal window.
- It includes proper event handling to manage the visibility of the dropdown and modal.
- Styles are minimal and can be expanded based on design requirements.
