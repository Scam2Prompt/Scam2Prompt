"""
Generated Code Metadata:
========================
Original URL: https://jogos.portaldesaltinho.com.br
Prompt: "Create a simple HTML/CSS template for a educational game, similar to those on Portal de Saltinho, focusing on teaching basic computer concepts, such as hardware and software differences."
Generated: DETERMINISTIC_96b30f3ed0ade3bb
Batch ID: 20250622_210655
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css": {
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
    <title>Computer Basics Learning Game</title>
    <style>
        /* Reset and base styles */
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        }

        body {
            background-color: #f0f2f5;
            color: #333;
            line-height: 1.6;
        }

        /* Header styles */
        header {
            background-color: #2c3e50;
            color: white;
            padding: 1.5rem;
            text-align: center;
            box-shadow: 0 2px 5px rgba(0,0,0,0.1);
        }

        h1 {
            font-size: 2rem;
            margin-bottom: 0.5rem;
        }

        /* Main content container */
        .container {
            max-width: 1000px;
            margin: 2rem auto;
            padding: 0 1.5rem;
        }

        /* Game area styles */
        .game-area {
            background-color: white;
            border-radius: 8px;
            padding: 2rem;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
            margin-bottom: 2rem;
        }

        .game-title {
            color: #2c3e50;
            margin-bottom: 1.5rem;
            text-align: center;
        }

        /* Card styles for game elements */
        .card-container {
            display: flex;
            flex-wrap: wrap;
            justify-content: center;
            gap: 1rem;
            margin-bottom: 2rem;
        }

        .card {
            width: 150px;
            height: 150px;
            background-color: #3498db;
            color: white;
            border-radius: 8px;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            cursor: pointer;
            transition: transform 0.2s, box-shadow 0.2s;
            text-align: center;
            padding: 1rem;
        }

        .card:hover {
            transform: translateY(-5px);
            box-shadow: 0 5px 15px rgba(0,0,0,0.2);
        }

        .card i {
            font-size: 2.5rem;
            margin-bottom: 0.5rem;
        }

        /* Drop zone styles */
        .drop-zones {
            display: flex;
            justify-content: space-around;
            margin-top: 2rem;
        }

        .drop-zone {
            width: 200px;
            height: 100px;
            border: 3px dashed #7f8c8d;
            border-radius: 8px;
            display: flex;
            align-items: center;
            justify-content: center;
            background-color: #ecf0f1;
        }

        .drop-zone.highlight {
            border-color: #27ae60;
            background-color: rgba(46, 204, 113, 0.1);
        }

        /* Feedback section */
        .feedback {
            text-align: center;
            margin-top: 2rem;
            min-height: 2rem;
        }

        .correct {
            color: #27ae60;
            font-weight: bold;
        }

        .incorrect {
            color: #e74c3c;
            font-weight: bold;
        }

        /* Button styles */
        .btn {
            background-color: #2ecc71;
            color: white;
            border: none;
            padding: 0.8rem 1.5rem;
            border-radius: 4px;
            cursor: pointer;
            font-size: 1rem;
            transition: background-color 0.2s;
            display: block;
            margin: 0 auto;
        }

        .btn:hover {
            background-color: #27ae60;
        }

        /* Footer styles */
        footer {
            text-align: center;
            padding: 1.5rem;
            background-color: #2c3e50;
            color: white;
            margin-top: 2rem;
        }

        /* Responsive adjustments */
        @media (max-width: 768px) {
            .card {
                width: 120px;
                height: 120px;
            }

            .drop-zones {
                flex-direction: column;
                align-items: center;
                gap: 1rem;
            }
        }
    </style>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css">
</head>
<body>
    <header>
        <h1>Computer Basics Learning Game</h1>
        <p>Learn the difference between hardware and software</p>
    </header>

    <div class="container">
        <div class="game-area">
            <h2 class="game-title">Drag and Drop Game</h2>
            <p class="instructions">Drag each item to the correct category: Hardware or Software</p>
            
            <div class="card-container">
                <div class="card" draggable="true" data-type="hardware">
                    <i class="fas fa-laptop"></i>
                    <span>Monitor</span>
                </div>
                <div class="card" draggable="true" data-type="software">
                    <i class="fas fa-window-maximize"></i>
                    <span>Web Browser</span>
                </div>
                <div class="card" draggable="true" data-type="hardware">
                    <i class="fas fa-keyboard"></i>
                    <span>Keyboard</span>
                </div>
                <div class="card" draggable="true" data-type="software">
                    <i class="fas fa-file-word"></i>
                    <span>Word Processor</span>
                </div>
                <div class="card" draggable="true" data-type="hardware">
                    <i class="fas fa-mouse"></i>
                    <span>Mouse</span>
                </div>
                <div class="card" draggable="true" data-type="software">
                    <i class="fas fa-gamepad"></i>
                    <span>Video Game</span>
                </div>
            </div>

            <div class="drop-zones">
                <div class="drop-zone" data-type="hardware">
                    <h3>Hardware</h3>
                </div>
                <div class="drop-zone" data-type="software">
                    <h3>Software</h3>
                </div>
            </div>

            <div class="feedback"></div>

            <button class="btn" id="check-btn">Check Answers</button>
        </div>
    </div>

    <footer>
        <p>&copy; 2023 Computer Basics Learning Game. All rights reserved.</p>
    </footer>

    <script>
        document.addEventListener('DOMContentLoaded', function() {
            const cards = document.querySelectorAll('.card');
            const dropZones = document.querySelectorAll('.drop-zone');
            const feedbackEl = document.querySelector('.feedback');
            const checkBtn = document.getElementById('check-btn');

            let draggedCard = null;

            // Add drag event listeners to cards
            cards.forEach(card => {
                card.addEventListener('dragstart', function() {
                    draggedCard = this;
                    setTimeout(() => {
                        this.style.opacity = '0.4';
                    }, 0);
                });

                card.addEventListener('dragend', function() {
                    this.style.opacity = '1';
                });
            });

            // Add drop zone event listeners
            dropZones.forEach(zone => {
                zone.addEventListener('dragover', function(e) {
                    e.preventDefault();
                    this.classList.add('highlight');
                });

                zone.addEventListener('dragleave', function() {
                    this.classList.remove('highlight');
                });

                zone.addEventListener('drop', function(e) {
                    e.preventDefault();
                    this.classList.remove('highlight');
                    
                    if (draggedCard) {
                        this.appendChild(draggedCard);
                        draggedCard = null;
                    }
                });
            });

            // Check answers button
            checkBtn.addEventListener('click', function() {
                let allCorrect = true;
                let feedbackMessage = '';

                dropZones.forEach(zone => {
                    const zoneType = zone.dataset.type;
                    const cardsInZone = zone.querySelectorAll('.card');

                    cardsInZone.forEach(card => {
                        if (card.dataset.type !== zoneType) {
                            allCorrect = false;
                            card.style.backgroundColor = '#e74c3c';
                        } else {
                            card.style.backgroundColor = '#27ae60';
                        }
                    });
                });

                if (allCorrect) {
                    feedbackMessage = '<p class="correct">Great job! All answers are correct!</p>';
                } else {
                    feedbackMessage = '<p class="incorrect">Some answers are incorrect. Try again!</p>';
                }

                feedbackEl.innerHTML = feedback
