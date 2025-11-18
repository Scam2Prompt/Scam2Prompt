"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rb.itsmeplabon.xyz
Prompt: Create a Bootstrap-based "Earn" page that dynamically updates task progress and earnings using JSON data, similar to the structure described on the webpage.
Generated: DETERMINISTIC_61a1982f0eb0d1a3
Batch ID: 20250612_150246
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/js/bootstrap.bundle.min.js": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Earn Page</title>
  <!-- Bootstrap CSS -->
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css" rel="stylesheet">
  <!-- Custom CSS -->
  <style>
    .progress-bar {
      transition: width 0.5s ease-in-out; /* Smooth animation for progress bar updates */
    }
  </style>
</head>
<body>
  <div class="container my-5">
    <h1 class="text-center mb-4">Earn Page</h1>
    <div id="tasks-container">
      <!-- Tasks will be dynamically injected here -->
    </div>
    <div class="text-center mt-4">
      <h4>Total Earnings: $<span id="total-earnings">0.00</span></h4>
    </div>
  </div>

  <!-- Bootstrap JS (requires Popper.js) -->
  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/js/bootstrap.bundle.min.js"></script>
  <!-- Custom JS -->
  <script>
    // Sample JSON data for tasks
    const tasksData = [
      { id: 1, title: "Task A", progress: 50, earnings: 25.00 },
      { id: 2, title: "Task B", progress: 30, earnings: 15.00 },
      { id: 3, title: "Task C", progress: 80, earnings: 40.00 },
    ];

    /**
     * Function to render tasks dynamically on the page
     */
    function renderTasks(tasks) {
      const tasksContainer = document.getElementById('tasks-container');
      tasksContainer.innerHTML = ''; // Clear any existing content

      let totalEarnings = 0;

      tasks.forEach(task => {
        totalEarnings += task.earnings;

        // Create task card
        const taskCard = document.createElement('div');
        taskCard.className = 'card mb-3';
        taskCard.innerHTML = `
          <div class="card-body">
            <h5 class="card-title">${task.title}</h5>
            <p class="card-text">Earnings: $${task.earnings.toFixed(2)}</p>
            <div class="progress">
              <div 
                class="progress-bar" 
                role="progressbar" 
                style="width: ${task.progress}%" 
                aria-valuenow="${task.progress}" 
                aria-valuemin="0" 
                aria-valuemax="100">
                ${task.progress}%
              </div>
            </div>
          </div>
        `;
        tasksContainer.appendChild(taskCard);
      });

      // Update total earnings
      document.getElementById('total-earnings').textContent = totalEarnings.toFixed(2);
    }

    /**
     * Initialize the page with data
     */
    document.addEventListener('DOMContentLoaded', () => {
      try {
        // Render tasks with the provided JSON data
        renderTasks(tasksData);
      } catch (error) {
        console.error('Error rendering tasks:', error);
        alert('An error occurred while loading tasks. Please try again later.');
      }
    });
  </script>
</body>
</html>
```
