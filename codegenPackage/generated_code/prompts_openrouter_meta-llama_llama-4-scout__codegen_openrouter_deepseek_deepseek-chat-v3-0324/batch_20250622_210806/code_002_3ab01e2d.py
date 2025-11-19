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

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Fusion Jiu Jitsu - Training Programs</title>
    <style>
        body {
            font-family: 'Arial', sans-serif;
            line-height: 1.6;
            margin: 0;
            padding: 0;
            color: #333;
            background-color: #f5f5f5;
        }
        
        header {
            background-color: #1a1a1a;
            color: white;
            padding: 1rem 0;
            text-align: center;
        }
        
        .container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 20px;
        }
        
        h1 {
            margin: 0;
            font-size: 2.5rem;
        }
        
        h2 {
            color: #d4af37;
            border-bottom: 2px solid #d4af37;
            padding-bottom: 10px;
            margin-top: 30px;
        }
        
        .programs-container {
            display: flex;
            flex-wrap: wrap;
            gap: 20px;
            justify-content: center;
            margin-top: 30px;
        }
        
        .program-card {
            background: white;
            border-radius: 8px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            padding: 20px;
            width: 300px;
            transition: transform 0.3s ease;
        }
        
        .program-card:hover {
            transform: translateY(-5px);
        }
        
        .program-card h3 {
            color: #1a1a1a;
            margin-top: 0;
        }
        
        .program-card p {
            color: #666;
        }
        
        .age-group {
            font-weight: bold;
            color: #d4af37;
        }
        
        .btn {
            display: inline-block;
            background-color: #d4af37;
            color: white;
            padding: 10px 20px;
            text-decoration: none;
            border-radius: 5px;
            font-weight: bold;
            margin-top: 15px;
            transition: background-color 0.3s ease;
        }
        
        .btn:hover {
            background-color: #b6952a;
        }
        
        footer {
            background-color: #1a1a1a;
            color: white;
            text-align: center;
            padding: 20px 0;
            margin-top: 40px;
        }
    </style>
</head>
<body>
    <header>
        <div class="container">
            <h1>Fusion Jiu Jitsu</h1>
            <p>Brazilian Jiu-Jitsu Training Programs</p>
        </div>
    </header>
    
    <div class="container">
        <h2>Kids Programs</h2>
        <div class="programs-container">
            <div class="program-card">
                <h3>Little Champions</h3>
                <p class="age-group">Ages 4-6</p>
                <p>Introduction to Jiu-Jitsu fundamentals through fun games and exercises. Focus on coordination, discipline, and basic techniques.</p>
                <a href="#contact" class="btn">Learn More</a>
            </div>
            
            <div class="program-card">
                <h3>Junior Warriors</h3>
                <p class="age-group">Ages 7-12</p>
                <p>Structured training program focusing on technique, self-defense, and character development. Perfect for building confidence.</p>
                <a href="#contact" class="btn">Learn More</a>
            </div>
            
            <div class="program-card">
                <h3>Teen Elite</h3>
                <p class="age-group">Ages 13-17</p>
                <p>Advanced training for teens preparing for competition or self-defense scenarios. Includes strength and conditioning.</p>
                <a href="#contact" class="btn">Learn More</a>
            </div>
        </div>
        
        <h2>Adult Programs</h2>
        <div class="programs-container">
            <div class="program-card">
                <h3>Fundamentals</h3>
                <p class="age-group">All Levels</p>
                <p>Learn the core techniques of Brazilian Jiu-Jitsu in a supportive environment. Perfect for beginners.</p>
                <a href="#contact" class="btn">Learn More</a>
            </div>
            
            <div class="program-card">
                <h3>Advanced</h3>
                <p class="age-group">Blue Belt & Up</p>
                <p>High-level techniques and strategies for experienced practitioners. Focus on competition preparation.</p>
                <a href="#contact" class="btn">Learn More</a>
            </div>
            
            <div class="program-card">
                <h3>No-Gi</h3>
                <p class="age-group">All Levels</p>
                <p>Training without the traditional gi/kimono. Focus on wrestling, submissions, and modern Jiu-Jitsu techniques.</p>
                <a href="#contact" class="btn">Learn More</a>
            </div>
        </div>
    </div>
    
    <footer>
        <div class="container">
            <p>&copy; 2023 Fusion Jiu Jitsu. All rights reserved.</p>
            <p id="contact">Contact us at: info@fusionjiujitsu.com | (555) 123-4567</p>
        </div>
    </footer>
</body>
</html>
```
