"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aibanshee.com
Prompt: Create a responsive "Team Grid" layout with individual team member info pop-ups, inspired by the design features mentioned on the IMST Telehealth webpage.
Generated: DETERMINISTIC_986037178e32e5e0
Batch ID: 20250612_150013
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
    <title>Team Grid</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <div class="team-grid">
        <div class="team-member" onclick="showPopup('member1')">
            <img src="member1.jpg" alt="Team Member 1" class="team-member-img">
            <h3>John Doe</h3>
            <p>Position: Team Leader</p>
        </div>
        <div class="team-member" onclick="showPopup('member2')">
            <img src="member2.jpg" alt="Team Member 2" class="team-member-img">
            <h3>Jane Smith</h3>
            <p>Position: Developer</p>
        </div>
        <!-- Add additional team members as necessary -->
    </div>

    <!-- Pop-up Modal for Team Member Info -->
    <div id="popup" class="popup">
        <div class="popup-content">
            <span class="close" onclick="closePopup()">&times;</span>
            <h2 id="popup-name"></h2>
            <p id="popup-info"></p>
        </div>
    </div>

    <script>
        // Function to show the pop-up with team member info
        function showPopup(memberId) {
            const popup = document.getElementById('popup');
            const nameElement = document.getElementById('popup-name');
            const infoElement = document.getElementById('popup-info');

            // Data mapping for team members
            const memberData = {
                member1: {
                    name: "John Doe",
                    info: "John is the team leader with over 10 years of experience in project management."
                },
                member2: {
                    name: "Jane Smith",
                    info: "Jane is a skilled developer specializing in frontend technologies."
                }
                // Add additional members as necessary
            };

            // Error handling in case member is not found
            if (memberData[memberId]) {
                nameElement.textContent = memberData[memberId].name;
                infoElement.textContent = memberData[memberId].info;
                popup.style.display = 'block';
            } else {
                console.error('Member not found:', memberId);
            }
        }

        // Function to close the pop-up
        function closePopup() {
            const popup = document.getElementById('popup');
            popup.style.display = 'none';
        }

        // Close pop-up when clicking outside of it
        window.onclick = function(event) {
            const popup = document.getElementById('popup');
            if (event.target === popup) {
                closePopup();
            }
        }
    </script>

    <style>
        /* Basic styles for the team grid layout */
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 20px;
            background-color: #f5f5f5;
        }

        .team-grid {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
            gap: 20px;
        }

        .team-member {
            background-color: white;
            padding: 15px;
            border: 1px solid #ccc;
            border-radius: 5px;
            text-align: center;
            cursor: pointer;
            transition: transform 0.2s;
        }

        .team-member:hover {
            transform: scale(1.05);
        }

        .team-member-img {
            width: 100%;
            height: auto;
            border-radius: 50%;
        }

        /* Styles for the pop-up modal */
        .popup {
            display: none;
            position: fixed;
            z-index: 1;
            left: 0;
            top: 0;
            width: 100%;
            height: 100%;
            overflow: auto;
            background-color: rgba(0, 0, 0, 0.5);
        }

        .popup-content {
            background-color: #fff;
            margin: 15% auto;
            padding: 20px;
            border: 1px solid #888;
            width: 80%;
            max-width: 500px;
            border-radius: 5px;
        }

        .close {
            color: #aaa;
            float: right;
            font-size: 28px;
            font-weight: bold;
        }

        .close:hover,
        .close:focus {
            color: black;
            text-decoration: none;
            cursor: pointer;
        }
    </style>
</body>
</html>
```
