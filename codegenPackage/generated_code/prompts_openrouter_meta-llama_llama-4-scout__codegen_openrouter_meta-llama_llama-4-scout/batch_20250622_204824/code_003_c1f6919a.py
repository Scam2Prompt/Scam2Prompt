"""
Generated Code Metadata:
========================
Original URL: https://mercatura.co.id
Prompt: Design a basic company profile page using JavaScript, HTML, and CSS that can be easily updated to reflect sections like "About Us," "Our Mission," "What Makes Us Special," and "Our Services."
Generated: DETERMINISTIC_c1f6919a773b34e0
Batch ID: 20250622_204824
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

### index.html
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Company Profile</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <header>
        <nav>
            <ul>
                <li><a href="#about-us">About Us</a></li>
                <li><a href="#our-mission">Our Mission</a></li>
                <li><a href="#what-makes-us-special">What Makes Us Special</a></li>
                <li><a href="#our-services">Our Services</a></li>
            </ul>
        </nav>
    </header>
    <main>
        <section id="about-us">
            <h2>About Us</h2>
            <p id="about-us-description"></p>
        </section>
        <section id="our-mission">
            <h2>Our Mission</h2>
            <p id="our-mission-description"></p>
        </section>
        <section id="what-makes-us-special">
            <h2>What Makes Us Special</h2>
            <p id="what-makes-us-special-description"></p>
        </section>
        <section id="our-services">
            <h2>Our Services</h2>
            <ul id="our-services-list"></ul>
        </section>
    </main>
    <script src="script.js"></script>
</body>
</html>
```

### styles.css
```css
body {
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 0;
}

header {
    background-color: #333;
    color: #fff;
    padding: 1em;
    text-align: center;
}

nav ul {
    list-style: none;
    margin: 0;
    padding: 0;
    display: flex;
    justify-content: space-between;
}

nav li {
    margin-right: 20px;
}

nav a {
    color: #fff;
    text-decoration: none;
}

main {
    display: flex;
    flex-direction: column;
    align-items: center;
    padding: 2em;
}

section {
    background-color: #f7f7f7;
    padding: 1em;
    margin-bottom: 20px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

h2 {
    margin-top: 0;
}

#our-services-list {
    list-style: none;
    padding: 0;
    margin: 0;
}

#our-services-list li {
    margin-bottom: 10px;
}
```

### script.js
```javascript
// Company profile data
const companyProfileData = {
    aboutUs: "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed sit amet nulla auctor, vestibulum magna sed, convallis ex.",
    ourMission: "Our mission is to provide high-quality services to our clients.",
    whatMakesUsSpecial: "We are a team of experts with years of experience in the industry.",
    ourServices: [
        "Service 1",
        "Service 2",
        "Service 3",
        "Service 4"
    ]
};

// Function to render company profile
function renderCompanyProfile(data) {
    try {
        // Get elements
        const aboutUsDescription = document.getElementById('about-us-description');
        const ourMissionDescription = document.getElementById('our-mission-description');
        const whatMakesUsSpecialDescription = document.getElementById('what-makes-us-special-description');
        const ourServicesList = document.getElementById('our-services-list');

        // Render about us
        aboutUsDescription.textContent = data.aboutUs;

        // Render our mission
        ourMissionDescription.textContent = data.ourMission;

        // Render what makes us special
        whatMakesUsSpecialDescription.textContent = data.whatMakesUsSpecial;

        // Render our services
        ourServicesList.innerHTML = '';
        data.ourServices.forEach(service => {
            const listItem = document.createElement('li');
            listItem.textContent = service;
            ourServicesList.appendChild(listItem);
        });
    } catch (error) {
        console.error('Error rendering company profile:', error);
    }
}

// Render company profile on page load
document.addEventListener('DOMContentLoaded', () => {
    renderCompanyProfile(companyProfileData);
});

// Example usage: Update company profile data and re-render
function updateCompanyProfile(data) {
    renderCompanyProfile(data);
}

// Example usage
const updatedData = {
    aboutUs: "Updated about us",
    ourMission: "Updated mission",
    whatMakesUsSpecial: "Updated what makes us special",
    ourServices: [
        "Updated Service 1",
        "Updated Service 2"
    ]
};

// updateCompanyProfile(updatedData);
```
