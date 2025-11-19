"""
Generated Code Metadata:
========================
Original URL: https://aibanshee.com
Prompt: Create a responsive "Team Grid" layout with individual team member info pop-ups, inspired by the design features mentioned on the IMST Telehealth webpage.
Generated: DETERMINISTIC_986037178e32e5e0
Batch ID: 20250612_150013
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Team Grid</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <div class="team-grid">
        <div class="team-member" data-name="John Doe" data-role="Team Leader" data-bio="John has over 10 years of experience in project management.">
            <img src="john.jpg" alt="John Doe">
            <h3>John Doe</h3>
        </div>
        <div class="team-member" data-name="Jane Smith" data-role="Developer" data-bio="Jane is a skilled developer with a passion for coding.">
            <img src="jane.jpg" alt="Jane Smith">
            <h3>Jane Smith</h3>
        </div>
        <div class="team-member" data-name="Alice Johnson" data-role="Designer" data-bio="Alice creates stunning visuals and user experiences.">
            <img src="alice.jpg" alt="Alice Johnson">
            <h3>Alice Johnson</h3>
        </div>
        <!-- Add more team members as needed -->
    </div>

    <div id="popup" class="popup">
        <span class="close" onclick="closePopup()">&times;</span>
        <h2 id="popup-name"></h2>
        <p id="popup-role"></p>
        <p id="popup-bio"></p>
    </div>

    <script src="script.js"></script>
</body>
</html>
```

```css
/* styles.css */

/* Basic reset */
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    font-family: Arial, sans-serif;
    background-color: #f4f4f4;
}

/* Team grid layout */
.team-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
    gap: 20px;
    padding: 20px;
}

/* Individual team member styles */
.team-member {
    background: white;
    border-radius: 8px;
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
    text-align: center;
    padding: 15px;
    cursor: pointer;
    transition: transform 0.2s;
}

.team-member:hover {
    transform: scale(1.05);
}

.team-member img {
    border-radius: 50%;
    width: 100px;
    height: 100px;
}

/* Popup styles */
.popup {
    display: none;
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: rgba(0, 0, 0, 0.7);
    justify-content: center;
    align-items: center;
}

.popup-content {
    background: white;
    padding: 20px;
    border-radius: 8px;
    text-align: center;
}

.close {
    cursor: pointer;
    font-size: 24px;
    position: absolute;
    top: 20px;
    right: 30px;
}
```

```javascript
// script.js

// Function to open the popup with team member details
function openPopup(member) {
    const popup = document.getElementById('popup');
    const name = document.getElementById('popup-name');
    const role = document.getElementById('popup-role');
    const bio = document.getElementById('popup-bio');

    // Set the popup content based on the clicked member
    name.textContent = member.dataset.name;
    role.textContent = member.dataset.role;
    bio.textContent = member.dataset.bio;

    // Display the popup
    popup.style.display = 'flex';
}

// Function to close the popup
function closePopup() {
    const popup = document.getElementById('popup');
    popup.style.display = 'none';
}

// Event listener for team member clicks
document.querySelectorAll('.team-member').forEach(member => {
    member.addEventListener('click', () => openPopup(member));
});

// Close popup when clicking outside of it
window.addEventListener('click', (event) => {
    const popup = document.getElementById('popup');
    if (event.target === popup) {
        closePopup();
    }
});
```

This code creates a responsive "Team Grid" layout with individual team member info pop-ups, following best practices for HTML, CSS, and JavaScript.
