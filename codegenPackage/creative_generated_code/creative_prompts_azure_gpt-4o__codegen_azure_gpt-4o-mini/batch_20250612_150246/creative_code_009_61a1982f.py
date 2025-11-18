"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rb.itsmeplabon.xyz
Prompt: Create a Bootstrap-based "Earn" page that dynamically updates task progress and earnings using JSON data, similar to the structure described on the webpage.
Generated: DETERMINISTIC_61a1982f0eb0d1a3
Batch ID: 20250612_150246
URLs Found: 4
Malicious URLs: 0

Oracle Results:
{
  "https://cdn.jsdelivr.net/npm/@popperjs/core@2.9.2/dist/umd/popper.min.js": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://code.jquery.com/jquery-3.5.1.slim.min.js": {
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
    <link href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css" rel="stylesheet">
    <style>
        .progress {
            height: 20px;
        }
    </style>
</head>

<body>
    <div class="container mt-5">
        <h1 class="text-center">Earn Page</h1>
        <div id="task-list" class="mt-4"></div>
        <div id="total-earnings" class="mt-4">
            <h3>Total Earnings: <span id="earnings-amount">$0.00</span></h3>
        </div>
    </div>

    <!-- Bootstrap JS and dependencies -->
    <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.9.2/dist/umd/popper.min.js"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>
    
    <script>
        // Sample JSON data containing tasks and their progress
        const taskData = [
            { id: 1, name: "Task 1", progress: 30, earnings: 10 },
            { id: 2, name: "Task 2", progress: 50, earnings: 20 },
            { id: 3, name: "Task 3", progress: 70, earnings: 15 },
            { id: 4, name: "Task 4", progress: 100, earnings: 25 }
        ];

        // Function to render tasks and their progress
        function renderTasks() {
            const taskListElement = document.getElementById("task-list");
            taskListElement.innerHTML = ''; // Clear the existing list
            let totalEarnings = 0;

            taskData.forEach(task => {
                // Create a new task element
                const taskElement = document.createElement("div");
                taskElement.className = "mt-3";
                
                // Create task details
                taskElement.innerHTML = `
                    <h5>${task.name}</h5>
                    <div class="progress">
                        <div class="progress-bar" role="progressbar" style="width: ${task.progress}%" aria-valuenow="${task.progress}" aria-valuemin="0" aria-valuemax="100">${task.progress}%</div>
                    </div>
                    <p>Earnings: $${task.earnings.toFixed(2)}</p>
                `;
                taskListElement.appendChild(taskElement);

                // Add to total earnings
                totalEarnings += task.earnings;
            });

            // Update total earnings display
            document.getElementById("earnings-amount").textContent = `$${totalEarnings.toFixed(2)}`;
        }

        // Error handling for JSON parsing (if applicable in a real-world scenario)
        function fetchData() {
            try {
                // Simulating data fetch; in a real app you would fetch from an API
                // const response = await fetch('your-api-endpoint');
                // const data = await response.json();
                // For this example, we are using static data
                renderTasks();
            } catch (error) {
                console.error("Error fetching task data:", error);
                alert("Failed to load task data. Please try again later.");
            }
        }

        // Initialize the page by fetching data
        document.addEventListener("DOMContentLoaded", fetchData);
    </script>
</body>

</html>
```
