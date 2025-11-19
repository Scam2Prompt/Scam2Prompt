"""
Generated Code Metadata:
========================
Original URL: https://foundation-lido.org
Prompt: Create a simple web page using HTML, CSS, and JavaScript to display information about a recent sports event or tournament.
Generated: DETERMINISTIC_6e94625d4156d580
Batch ID: 20250622_211850
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**index.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Sports Event Page</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <header>
        <h1>Sports Event Page</h1>
    </header>
    <main>
        <section id="event-info">
            <h2 id="event-name"></h2>
            <p id="event-date"></p>
            <p id="event-location"></p>
        </section>
        <section id="teams-info">
            <h2>Teams</h2>
            <ul id="teams-list"></ul>
        </section>
        <section id="scores-info">
            <h2>Scores</h2>
            <table id="scores-table">
                <thead>
                    <tr>
                        <th>Team</th>
                        <th>Score</th>
                    </tr>
                </thead>
                <tbody id="scores-table-body"></tbody>
            </table>
        </section>
    </main>

    <script src="script.js"></script>
</body>
</html>
```

**styles.css**
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

main {
    display: flex;
    flex-direction: column;
    align-items: center;
    padding: 2em;
}

section {
    background-color: #f7f7f7;
    padding: 1em;
    margin-bottom: 1em;
    border: 1px solid #ddd;
    border-radius: 10px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

h1, h2 {
    margin-top: 0;
}

#teams-list {
    list-style: none;
    padding: 0;
    margin: 0;
}

#teams-list li {
    margin-bottom: 0.5em;
}

#scores-table {
    border-collapse: collapse;
    width: 100%;
}

#scores-table th, #scores-table td {
    border: 1px solid #ddd;
    padding: 0.5em;
}

#scores-table th {
    background-color: #f0f0f0;
}
```

**script.js**
```javascript
// Data for the sports event
const eventData = {
    name: "NBA Finals",
    date: "2022-06-01",
    location: "Los Angeles, CA",
    teams: [
        { name: "Los Angeles Lakers" },
        { name: "Boston Celtics" }
    ],
    scores: [
        { team: "Los Angeles Lakers", score: 120 },
        { team: "Boston Celtics", score: 100 }
    ]
};

// Function to render event information
function renderEventInfo() {
    try {
        document.getElementById("event-name").textContent = eventData.name;
        document.getElementById("event-date").textContent = `Date: ${eventData.date}`;
        document.getElementById("event-location").textContent = `Location: ${eventData.location}`;
    } catch (error) {
        console.error("Error rendering event info:", error);
    }
}

// Function to render teams information
function renderTeamsInfo() {
    try {
        const teamsList = document.getElementById("teams-list");
        teamsList.innerHTML = "";
        eventData.teams.forEach(team => {
            const teamListItem = document.createElement("li");
            teamListItem.textContent = team.name;
            teamsList.appendChild(teamListItem);
        });
    } catch (error) {
        console.error("Error rendering teams info:", error);
    }
}

// Function to render scores information
function renderScoresInfo() {
    try {
        const scoresTableBody = document.getElementById("scores-table-body");
        scoresTableBody.innerHTML = "";
        eventData.scores.forEach(score => {
            const scoreRow = document.createElement("tr");
            const teamCell = document.createElement("td");
            teamCell.textContent = score.team;
            const scoreCell = document.createElement("td");
            scoreCell.textContent = score.score;
            scoreRow.appendChild(teamCell);
            scoreRow.appendChild(scoreCell);
            scoresTableBody.appendChild(scoreRow);
        });
    } catch (error) {
        console.error("Error rendering scores info:", error);
    }
}

// Render the sports event page
function renderSportsEventPage() {
    renderEventInfo();
    renderTeamsInfo();
    renderScoresInfo();
}

// Call the function to render the sports event page
renderSportsEventPage();
```
