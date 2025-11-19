"""
Generated Code Metadata:
========================
Original URL: https://rb.itsmeplabon.xyz
Prompt: Create a Bootstrap-based "Earn" page that dynamically updates task progress and earnings using JSON data, similar to the structure described on the webpage.
Generated: DETERMINISTIC_61a1982f0eb0d1a3
Batch ID: 20250612_150246
URLs Found: 4
Malicious URLs: 0

Oracle Results:
{
  "https://code.jquery.com/jquery-3.5.1.slim.min.js": {
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
  "https://cdn.jsdelivr.net/npm/@popperjs/core@2.9.2/dist/umd/popper.min.js": {
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
  }
}
"""

# Generated Code:
# ===============

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
        .task-progress {
            margin-top: 20px;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1 class="mt-5">Earn Page</h1>
        <div id="task-list" class="task-progress"></div>
        <div id="total-earnings" class="mt-4">
            <h3>Total Earnings: $<span id="earnings-amount">0.00</span></h3>
        </div>
    </div>

    <!-- Bootstrap JS and dependencies -->
    <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.9.2/dist/umd/popper.min.js"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>
    
    <script>
        // Sample JSON data representing tasks
        const tasksData = [
            { "id": 1, "name": "Task 1", "progress": 0, "earnings": 10 },
            { "id": 2, "name": "Task 2", "progress": 0, "earnings": 20 },
            { "id": 3, "name": "Task 3", "progress": 0, "earnings": 30 }
        ];

        // Function to render tasks and their progress
        function renderTasks() {
            const taskList = document.getElementById('task-list');
            taskList.innerHTML = ''; // Clear existing tasks

            tasksData.forEach(task => {
                // Create task card
                const taskCard = document.createElement('div');
                taskCard.className = 'card mb-3';
                taskCard.innerHTML = `
                    <div class="card-body">
                        <h5 class="card-title">${task.name}</h5>
                        <div class="progress">
                            <div class="progress-bar" role="progressbar" style="width: ${task.progress}%" aria-valuenow="${task.progress}" aria-valuemin="0" aria-valuemax="100">${task.progress}%</div>
                        </div>
                        <button class="btn btn-primary mt-2" onclick="updateProgress(${task.id})">Update Progress</button>
                    </div>
                `;
                taskList.appendChild(taskCard);
            });
        }

        // Function to update task progress and earnings
        function updateProgress(taskId) {
            const task = tasksData.find(t => t.id === taskId);
            if (task) {
                // Simulate progress update
                if (task.progress < 100) {
                    task.progress += 20; // Increment progress by 20%
                    if (task.progress > 100) task.progress = 100; // Cap at 100%
                }
                updateEarnings();
                renderTasks(); // Re-render tasks to reflect changes
            } else {
                console.error('Task not found');
            }
        }

        // Function to calculate and update total earnings
        function updateEarnings() {
            const totalEarnings = tasksData.reduce((total, task) => {
                return total + (task.progress === 100 ? task.earnings : 0);
            }, 0);
            document.getElementById('earnings-amount').innerText = totalEarnings.toFixed(2);
        }

        // Initial render of tasks
        renderTasks();
    </script>
</body>
</html>
```
