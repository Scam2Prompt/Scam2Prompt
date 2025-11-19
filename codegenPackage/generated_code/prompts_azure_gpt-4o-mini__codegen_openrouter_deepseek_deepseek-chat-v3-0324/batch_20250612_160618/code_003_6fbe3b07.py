"""
Generated Code Metadata:
========================
Original URL: https://vascavotivadinoceto.it
Prompt: Develop a simple HTML page that includes an interactive calendar for the Museo Vasca Votiva di Noceto, highlighting special events and activities for families and schools.
Generated: DETERMINISTIC_6fbe3b0748f393e8
Batch ID: 20250612_160618
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
    <title>Museo Vasca Votiva di Noceto - Event Calendar</title>
    <style>
        body {
            font-family: 'Arial', sans-serif;
            line-height: 1.6;
            margin: 0;
            padding: 0;
            color: #333;
            background-color: #f9f9f9;
        }
        
        header {
            background-color: #2c3e50;
            color: white;
            text-align: center;
            padding: 1rem 0;
        }
        
        .container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 20px;
        }
        
        h1, h2 {
            color: #2c3e50;
        }
        
        .calendar {
            background: white;
            border-radius: 8px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
            padding: 20px;
            margin-bottom: 30px;
        }
        
        .calendar-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 20px;
        }
        
        .calendar-title {
            font-size: 1.5rem;
            font-weight: bold;
        }
        
        .calendar-nav button {
            background: #3498db;
            color: white;
            border: none;
            padding: 8px 15px;
            border-radius: 4px;
            cursor: pointer;
            margin: 0 5px;
        }
        
        .calendar-nav button:hover {
            background: #2980b9;
        }
        
        .calendar-grid {
            display: grid;
            grid-template-columns: repeat(7, 1fr);
            gap: 10px;
        }
        
        .calendar-day-header {
            text-align: center;
            font-weight: bold;
            padding: 10px;
            background: #f0f0f0;
            border-radius: 4px;
        }
        
        .calendar-day {
            min-height: 100px;
            padding: 10px;
            border: 1px solid #eee;
            border-radius: 4px;
            background: white;
        }
        
        .calendar-day.empty {
            background: #f9f9f9;
            border: none;
        }
        
        .calendar-day.today {
            background: #e3f2fd;
            border-color: #bbdefb;
        }
        
        .calendar-day-number {
            font-weight: bold;
            margin-bottom: 5px;
        }
        
        .event {
            font-size: 0.8rem;
            background: #e8f5e9;
            padding: 3px 6px;
            margin: 2px 0;
            border-radius: 3px;
            border-left: 3px solid #4caf50;
            cursor: pointer;
        }
        
        .event.family {
            border-left-color: #ff9800;
            background: #fff3e0;
        }
        
        .event.school {
            border-left-color: #2196f3;
            background: #e3f2fd;
        }
        
        .event-details {
            display: none;
            position: fixed;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            background: white;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 4px 20px rgba(0,0,0,0.2);
            z-index: 1000;
            max-width: 500px;
            width: 90%;
        }
        
        .event-details h3 {
            margin-top: 0;
            color: #2c3e50;
        }
        
        .event-details .close {
            position: absolute;
            top: 10px;
            right: 10px;
            cursor: pointer;
            font-size: 1.5rem;
            color: #7f8c8d;
        }
        
        .overlay {
            display: none;
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: rgba(0,0,0,0.5);
            z-index: 999;
        }
        
        footer {
            text-align: center;
            padding: 20px;
            background: #2c3e50;
            color: white;
            margin-top: 30px;
        }
        
        @media (max-width: 768px) {
            .calendar-grid {
                grid-template-columns: repeat(1, 1fr);
            }
            
            .calendar-day {
                min-height: auto;
            }
        }
    </style>
</head>
<body>
    <header>
        <h1>Museo Vasca Votiva di Noceto</h1>
        <p>Event Calendar for Families and Schools</p>
    </header>
    
    <div class="container">
        <div class="calendar">
            <div class="calendar-header">
                <div class="calendar-title" id="calendar-title">Month Year</div>
                <div class="calendar-nav">
                    <button id="prev-month">Previous</button>
                    <button id="today">Today</button>
                    <button id="next-month">Next</button>
                </div>
            </div>
            
            <div class="calendar-grid" id="calendar-grid">
                <!-- Calendar days will be generated by JavaScript -->
            </div>
        </div>
        
        <div class="event-categories">
            <h2>Event Categories</h2>
            <p><span class="event family" style="display: inline-block; width: 15px; height: 15px;"></span> Family Events</p>
            <p><span class="event school" style="display: inline-block; width: 15px; height: 15px;"></span> School Activities</p>
            <p><span class="event" style="display: inline-block; width: 15px; height: 15px;"></span> General Events</p>
        </div>
    </div>
    
    <div class="overlay" id="overlay"></div>
    
    <div class="event-details" id="event-details">
        <span class="close" id="close-details">&times;</span>
        <h3 id="event-title">Event Title</h3>
        <p><strong>Date:</strong> <span id="event-date"></span></p>
        <p><strong>Time:</strong> <span id="event-time"></span></p>
        <p><strong>Type:</strong> <span id="event-type"></span></p>
        <div id="event-description"></div>
    </div>
    
    <footer>
        <p>&copy; 2023 Museo Vasca Votiva di Noceto. All rights reserved.</p>
    </footer>
    
    <script>
        document.addEventListener('DOMContentLoaded', function() {
            // Current date
            let currentDate = new Date();
            
            // Sample events data
            const events = [
                {
                    id: 1,
                    title: "Family Workshop: Ancient Pottery",
                    date: new Date(currentDate.getFullYear(), currentDate.getMonth(), 5),
                    time: "10:00 - 12:00",
                    type: "family",
                    description: "Join us for a hands-on workshop where families can learn about ancient pottery techniques and create their own clay artifacts."
                },
                {
                    id: 2,
                    title: "School Tour: Archaeological Discoveries",
                    date: new Date(currentDate.getFullYear(), currentDate.getMonth(), 12),
                    time: "09:30 - 11:30",
                    type: "school",
                    description: "Special guided tour for school groups focusing on the archaeological discoveries at the Noceto site."
                },
                {
                    id: 3,
                    title: "Lecture: The Sacred Vasca",
                    date: new Date(currentDate.getFullYear(), currentDate.getMonth(), 15),
                    time: "18:00 - 19:30",
                    type: "general",
                    description: "Expert lecture on the significance of the sacred vasca and its role in ancient rituals."
                },
                {
                    id: 4,
                    title: "Kids' Archaeology Day",
                    date: new Date(currentDate.getFullYear(), currentDate.getMonth(), 20),
                    time: "14:00 - 16:00",
                    type: "family",
                    description: "Interactive activities for children to learn about archaeology through fun games and excavations."
                },
                {
                    id: 5,
                    title: "Teacher Training Workshop",
                    date: new Date(currentDate.getFullYear(), currentDate.getMonth(), 22),
                    time: "15:00 - 17:00",
                    type: "school",
                    description: "Workshop
