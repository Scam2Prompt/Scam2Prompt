"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aibanshee.com
Prompt: Create a responsive "Team Grid" layout with individual team member info pop-ups, inspired by the design features mentioned on the IMST Telehealth webpage.
Generated: DETERMINISTIC_986037178e32e5e0
Batch ID: 20250612_150013
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://via.placeholder.com/250": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

Here's the code for the "Team Grid" layout with individual team member info pop-ups using HTML, CSS, and JavaScript:

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Responsive Team Grid</title>
  <style>
    /* General Reset */
    * {
      margin: 0;
      padding: 0;
      box-sizing: border-box;
    }

    body {
      font-family: Arial, sans-serif;
      line-height: 1.6;
      background-color: #f4f4f9;
      color: #333;
    }

    /* Container for the team grid */
    .team-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
      gap: 20px;
      padding: 20px;
      max-width: 1200px;
      margin: 0 auto;
    }

    /* Individual team card styling */
    .team-card {
      background: #fff;
      border-radius: 8px;
      box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
      overflow: hidden;
      text-align: center;
      position: relative;
      cursor: pointer;
    }

    .team-card:hover {
      transform: scale(1.05);
      transition: transform 0.3s ease-in-out;
    }

    .team-card img {
      width: 100%;
      height: auto;
    }

    .team-card-name {
      font-size: 1.2em;
      font-weight: bold;
      margin: 10px 0;
    }

    .team-card-position {
      font-size: 1em;
      color: #666;
      margin-bottom: 10px;
    }

    .team-card-bio {
      padding: 15px;
      font-size: 0.9em;
      color: #444;
      display: none; /* Hidden initially */
    }

    /* Pop-up styles */
    .popup-overlay {
      position: fixed;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      background: rgba(0, 0, 0, 0.7);
      display: none;
      justify-content: center;
      align-items: center;
      z-index: 1000;
    }

    .popup-content {
      background: #fff;
      padding: 30px;
      border-radius: 8px;
      max-width: 500px;
      text-align: center;
      box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
    }

    .popup-close {
      position: absolute;
      top: 10px;
      right: 10px;
      background: #e74c3c;
      color: #fff;
      border: none;
      border-radius: 50%;
      width: 30px;
      height: 30px;
      text-align: center;
      font-size: 1.2em;
      cursor: pointer;
    }

    .popup-close:hover {
      background: #c0392b;
    }
  </style>
</head>
<body>
  <!-- Team Grid -->
  <div class="team-grid">
    <!-- Example team member card -->
    <div class="team-card" data-name="John Doe" data-position="Telehealth Specialist" data-bio="John has over 10 years of experience in telehealth solutions and patient care.">
      <img src="https://via.placeholder.com/250" alt="John Doe">
      <div class="team-card-name">John Doe</div>
      <div class="team-card-position">Telehealth Specialist</div>
    </div>
    <div class="team-card" data-name="Jane Smith" data-position="Healthcare Advisor" data-bio="Jane focuses on providing expert advice on telehealth integration in clinics.">
      <img src="https://via.placeholder.com/250" alt="Jane Smith">
      <div class="team-card-name">Jane Smith</div>
      <div class="team-card-position">Healthcare Advisor</div>
    </div>
    <!-- Add more team cards as needed -->
  </div>

  <!-- Pop-up Modal -->
  <div class="popup-overlay" id="popup-overlay">
    <div class="popup-content">
      <button class="popup-close" id="popup-close">&times;</button>
      <h2 id="popup-name"></h2>
      <h4 id="popup-position"></h4>
      <p id="popup-bio"></p>
    </div>
  </div>

  <script>
    // Select elements for pop-up functionality
    const teamCards = document.querySelectorAll('.team-card');
    const popupOverlay = document.getElementById('popup-overlay');
    const popupClose = document.getElementById('popup-close');
    const popupName = document.getElementById('popup-name');
    const popupPosition = document.getElementById('popup-position');
    const popupBio = document.getElementById('popup-bio');

    // Function to open the pop-up
    function openPopup(event) {
      const card = event.currentTarget;
      popupName.textContent = card.dataset.name;
      popupPosition.textContent = card.dataset.position;
      popupBio.textContent = card.dataset.bio;

      popupOverlay.style.display = 'flex';
    }

    // Function to close the pop-up
    function closePopup() {
      popupOverlay.style.display = 'none';
    }

    // Add click event listeners to each team card
    teamCards.forEach((card) => {
      card.addEventListener('click', openPopup);
    });

    // Add click event listener to the close button
    popupClose.addEventListener('click', closePopup);

    // Close the pop-up when clicking outside the modal content
    popupOverlay.addEventListener('click', (event) => {
      if (event.target === popupOverlay) {
        closePopup();
      }
    });
  </script>
</body>
</html>
```
