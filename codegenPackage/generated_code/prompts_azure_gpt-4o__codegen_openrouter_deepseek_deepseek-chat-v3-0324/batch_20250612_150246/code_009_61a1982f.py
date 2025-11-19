"""
Generated Code Metadata:
========================
Original URL: https://rb.itsmeplabon.xyz
Prompt: Create a Bootstrap-based "Earn" page that dynamically updates task progress and earnings using JSON data, similar to the structure described on the webpage.
Generated: DETERMINISTIC_61a1982f0eb0d1a3
Batch ID: 20250612_150246
URLs Found: 3
Malicious URLs: 0

Oracle Results:
{
  "https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css": {
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
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <!-- Font Awesome for icons -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <style>
        .task-card {
            transition: all 0.3s ease;
            margin-bottom: 20px;
            border-radius: 10px;
            overflow: hidden;
        }
        .task-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 10px 20px rgba(0,0,0,0.1);
        }
        .progress {
            height: 10px;
            border-radius: 5px;
        }
        .progress-bar {
            background-color: #4CAF50;
        }
        .earnings-badge {
            font-size: 1rem;
            padding: 8px 12px;
            border-radius: 20px;
        }
        .task-icon {
            font-size: 2rem;
            margin-bottom: 10px;
            color: #4CAF50;
        }
        .section-header {
            border-bottom: 2px solid #eee;
            padding-bottom: 10px;
            margin-bottom: 20px;
        }
    </style>
</head>
<body>
    <div class="container py-5">
        <div class="row mb-4">
            <div class="col-12">
                <h1 class="text-center mb-4">Earn Rewards</h1>
                <div class="card shadow-sm">
                    <div class="card-body">
                        <div class="row align-items-center">
                            <div class="col-md-6">
                                <h3 class="mb-3">Your Earnings</h3>
                                <div class="d-flex align-items-center">
                                    <i class="fas fa-coins me-3" style="font-size: 2rem; color: gold;"></i>
                                    <div>
                                        <h2 id="total-earnings" class="mb-0">0</h2>
                                        <small class="text-muted">Total points earned</small>
                                    </div>
                                </div>
                            </div>
                            <div class="col-md-6">
                                <div class="progress mt-3">
                                    <div id="level-progress" class="progress-bar" role="progressbar" style="width: 0%"></div>
                                </div>
                                <div class="d-flex justify-content-between mt-2">
                                    <small>Level 1</small>
                                    <small id="next-level">0/100 to Level 2</small>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <div class="row">
            <div class="col-12">
                <h3 class="section-header">Available Tasks</h3>
            </div>
        </div>

        <div id="tasks-container" class="row">
            <!-- Tasks will be dynamically inserted here -->
        </div>

        <div class="row mt-5">
            <div class="col-12">
                <h3 class="section-header">Completed Tasks</h3>
            </div>
        </div>

        <div id="completed-tasks-container" class="row">
            <!-- Completed tasks will be dynamically inserted here -->
        </div>
    </div>

    <!-- Bootstrap JS Bundle with Popper -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
    
    <script>
        // Sample JSON data for tasks
        const tasksData = {
            "totalEarnings": 45,
            "levelProgress": 45,
            "nextLevelThreshold": 100,
            "currentLevel": 1,
            "availableTasks": [
                {
                    "id": 1,
                    "title": "Complete Profile",
                    "description": "Fill out all sections of your profile to earn points",
                    "points": 20,
                    "completed": false,
                    "progress": 30,
                    "totalRequired": 100,
                    "icon": "user-check"
                },
                {
                    "id": 2,
                    "title": "Daily Check-in",
                    "description": "Check in every day to earn bonus points",
                    "points": 5,
                    "completed": false,
                    "progress": 0,
                    "totalRequired": 1,
                    "icon": "calendar-check"
                },
                {
                    "id": 3,
                    "title": "Refer a Friend",
                    "description": "Invite friends to join and earn points when they sign up",
                    "points": 50,
                    "completed": false,
                    "progress": 0,
                    "totalRequired": 3,
                    "icon": "user-plus"
                }
            ],
            "completedTasks": [
                {
                    "id": 4,
                    "title": "First Login",
                    "description": "You earned points for logging in for the first time",
                    "points": 10,
                    "completed": true,
                    "completedDate": "2023-06-15",
                    "icon": "sign-in-alt"
                },
                {
                    "id": 5,
                    "title": "Watch Tutorial",
                    "description": "You earned points for watching the introductory tutorial",
                    "points": 15,
                    "completed": true,
                    "completedDate": "2023-06-16",
                    "icon": "video"
                }
            ]
        };

        // Function to render tasks
        function renderTasks() {
            const tasksContainer = document.getElementById('tasks-container');
            const completedTasksContainer = document.getElementById('completed-tasks-container');
            
            // Update earnings and progress
            document.getElementById('total-earnings').textContent = tasksData.totalEarnings;
            document.getElementById('level-progress').style.width = `${(tasksData.levelProgress / tasksData.nextLevelThreshold) * 100}%`;
            document.getElementById('next-level').textContent = `${tasksData.levelProgress}/${tasksData.nextLevelThreshold} to Level ${tasksData.currentLevel + 1}`;
            
            // Clear containers
            tasksContainer.innerHTML = '';
            completedTasksContainer.innerHTML = '';
            
            // Render available tasks
            tasksData.availableTasks.forEach(task => {
                const progressPercentage = (task.progress / task.totalRequired) * 100;
                const taskCard = `
                    <div class="col-md-4">
                        <div class="card task-card h-100">
                            <div class="card-body text-center">
                                <i class="fas fa-${task.icon} task-icon"></i>
                                <h5 class="card-title">${task.title}</h5>
                                <p class="card-text">${task.description}</p>
                                <div class="progress mb-3">
                                    <div class="progress-bar" role="progressbar" style="width: ${progressPercentage}%" 
                                        aria-valuenow="${task.progress}" aria-valuemin="0" aria-valuemax="${task.totalRequired}"></div>
                                </div>
                                <span class="badge bg-success earnings-badge">+${task.points} points</span>
                                <button class="btn btn-primary mt-3" onclick="updateTaskProgress(${task.id})">
                                    ${task.progress > 0 ? 'Continue' : 'Start'}
                                </button>
                            </div>
                        </div>
                    </div>
                `;
                tasksContainer.innerHTML += taskCard;
            });
            
            // Render completed tasks
            tasksData.completedTasks.forEach(task => {
                const taskCard = `
                    <div class="col-md-4">
                        <div class="card task-card h-100">
                            <div class="card-body text-center">
                                <i class="fas fa-${task.icon} task-icon"></i>
                                <h5 class="card-title">${task.title}</h5>
                                <p class="card-text">${task.description}</p>
                                <p class="text-muted"><small>Completed on ${task.completedDate}</small></p>
                                <span class="badge bg-success earnings-badge">+${task.points} points</span>
                                <button class="btn btn-secondary mt-3" disabled>
                                    <i class="fas fa-check"></i> Completed
                                </button>
                            </div>
                        </div>
                    </div>
                `;
                completedTasksContainer.innerHTML += taskCard;
            });
        }
        
        // Function to update task progress (simulated)
        function updateTaskProgress(taskId) {
            const task = tasksData.availableTasks.find(t => t.id === taskId);
            if (task) {
                // Simulate progress update
                task.progress += 25;
                if (task.progress >= task.totalRequired) {
                    task.completed = true;
                    tasksData.completedTasks.push({
                        ...
