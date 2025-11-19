"""
Generated Code Metadata:
========================
Original URL: https://fusionjiujitsu.com.br
Prompt: "Write a code snippet in JavaScript to create a simple webpage that showcases different Jiu-Jitsu training programs for kids and adults, similar to those offered by Fusion Jiu Jitsu School."
Generated: DETERMINISTIC_3ab01e2dd5cbb710
Batch ID: 20250622_210806
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// index.html will be generated dynamically using JavaScript and DOM manipulation

// Create a class to represent a Jiu-Jitsu training program
class TrainingProgram {
  /**
   * @param {string} name - Name of the training program
   * @param {string} description - Description of the training program
   * @param {string} ageGroup - Age group for the training program (kids or adults)
   * @param {string} beltLevel - Belt level for the training program (e.g., beginner, intermediate, advanced)
   */
  constructor(name, description, ageGroup, beltLevel) {
    this.name = name;
    this.description = description;
    this.ageGroup = ageGroup;
    this.beltLevel = beltLevel;
  }
}

// Create an array of training programs
const trainingPrograms = [
  new TrainingProgram(
    "Kids' Fundamentals",
    "Introduction to basic Jiu-Jitsu techniques and movements for kids aged 4-7.",
    "kids",
    "beginner"
  ),
  new TrainingProgram(
    "Kids' Intermediate",
    "Building on the fundamentals, kids will learn more advanced techniques and drilling strategies.",
    "kids",
    "intermediate"
  ),
  new TrainingProgram(
    "Adult Beginner",
    "Introduction to basic Jiu-Jitsu techniques and movements for adults with little to no experience.",
    "adults",
    "beginner"
  ),
  new TrainingProgram(
    "Adult Advanced",
    "For experienced adults looking to refine their techniques and learn more complex strategies.",
    "adults",
    "advanced"
  ),
];

// Function to generate HTML content for a training program
function generateProgramHTML(program) {
  return `
    <div class="program-card">
      <h2>${program.name}</h2>
      <p>${program.description}</p>
      <p><strong>Age Group:</strong> ${program.ageGroup}</p>
      <p><strong>Belt Level:</strong> ${program.beltLevel}</p>
    </div>
  `;
}

// Function to render training programs on the webpage
function renderTrainingPrograms(programs) {
  const container = document.getElementById("training-programs");
  container.innerHTML = "";

  programs.forEach((program) => {
    const programHTML = generateProgramHTML(program);
    container.insertAdjacentHTML("beforeend", programHTML);
  });
}

// Render training programs on page load
document.addEventListener("DOMContentLoaded", () => {
  renderTrainingPrograms(trainingPrograms);
});

// Filter training programs by age group
function filterProgramsByAgeGroup(ageGroup) {
  return trainingPrograms.filter((program) => program.ageGroup === ageGroup);
}

// Add event listeners to filter buttons
document.addEventListener("DOMContentLoaded", () => {
  const kidsButton = document.getElementById("kids-button");
  const adultsButton = document.getElementById("adults-button");
  const allButton = document.getElementById("all-button");

  kidsButton.addEventListener("click", () => {
    renderTrainingPrograms(filterProgramsByAgeGroup("kids"));
  });

  adultsButton.addEventListener("click", () => {
    renderTrainingPrograms(filterProgramsByAgeGroup("adults"));
  });

  allButton.addEventListener("click", () => {
    renderTrainingPrograms(trainingPrograms);
  });
});
```

```html
<!-- index.html -->
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Jiu-Jitsu Training Programs</title>
  <link rel="stylesheet" href="styles.css">
</head>
<body>
  <header>
    <h1>Fusion Jiu Jitsu School</h1>
    <nav>
      <button id="kids-button">Kids</button>
      <button id="adults-button">Adults</button>
      <button id="all-button">All</button>
    </nav>
  </header>
  <main>
    <section id="training-programs"></section>
  </main>
  <script src="script.js"></script>
</body>
</html>
```

```css
/* styles.css */
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

header nav {
  margin-top: 1em;
}

button {
  background-color: #333;
  color: #fff;
  border: none;
  padding: 0.5em 1em;
  cursor: pointer;
}

button:hover {
  background-color: #555;
}

#training-programs {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
}

.program-card {
  background-color: #f7f7f7;
  padding: 1em;
  margin: 1em;
  border: 1px solid #ddd;
  border-radius: 10px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
  width: 300px;
}

.program-card h2 {
  margin-top: 0;
}
```
