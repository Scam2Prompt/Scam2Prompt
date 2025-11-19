"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-4--eager-lichterman-0ed312.netlify.app
Prompt: Describe how to implement mouse hover functionality to display additional information on a COVID-19 graph, similar to the interactive features highlighted in the webpage content.
Generated: DETERMINISTIC_3fb874be136946dc
Batch ID: 20250612_163408
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
    <title>COVID-19 Graph with Mouse Hover</title>
    <style>
        /* Basic styles for the canvas and tooltip */
        #chart {
            width: 600px;
            height: 400px;
            border: 1px solid #ccc;
            position: relative;
        }
        #tooltip {
            position: absolute;
            background-color: rgba(0, 0, 0, 0.7);
            color: white;
            padding: 5px;
            border-radius: 5px;
            display: none; /* Hidden by default */
            pointer-events: none; /* Prevents mouse events */
        }
    </style>
</head>
<body>

    <h1>COVID-19 Cases Over Time</h1>
    <canvas id="chart"></canvas>
    <div id="tooltip"></div>

    <script>
        // Data for the COVID-19 graph
        const covidData = [
            { date: "2023-01-01", cases: 100 },
            { date: "2023-01-02", cases: 150 },
            { date: "2023-01-03", cases: 200 },
            { date: "2023-01-04", cases: 250 },
            { date: "2023-01-05", cases: 300 }
        ];

        const canvas = document.getElementById('chart');
        const ctx = canvas.getContext('2d');
        const tooltip = document.getElementById('tooltip');

        // Function to draw the COVID-19 graph
        function drawGraph(data) {
            ctx.clearRect(0, 0, canvas.width, canvas.height);
            ctx.beginPath();
            ctx.moveTo(0, canvas.height - data[0].cases);

            // Draw the line graph
            data.forEach((point, index) => {
                const x = (index / (data.length - 1)) * canvas.width;
                const y = canvas.height - point.cases;
                ctx.lineTo(x, y);
                ctx.arc(x, y, 5, 0, Math.PI * 2); // Draw points
            });

            ctx.strokeStyle = '#007BFF';
            ctx.stroke();
            ctx.fillStyle = '#007BFF';
            ctx.fill();
        }

        // Function to handle mouse movement over the canvas
        function handleMouseMove(event) {
            const rect = canvas.getBoundingClientRect();
            const mouseX = event.clientX - rect.left;
            const mouseY = event.clientY - rect.top;
            const dataPointIndex = Math.round((mouseX / canvas.width) * (covidData.length - 1));

            // Check if the mouse is near a data point
            if (dataPointIndex >= 0 && dataPointIndex < covidData.length) {
                const point = covidData[dataPointIndex];
                const y = canvas.height - point.cases;

                // Display tooltip near the mouse pointer
                tooltip.style.left = `${event.clientX}px`;
                tooltip.style.top = `${event.clientY}px`;
                tooltip.innerHTML = `Date: ${point.date}<br>Cases: ${point.cases}`;
                tooltip.style.display = 'block';
            } else {
                tooltip.style.display = 'none'; // Hide tooltip if no data point
            }
        }

        // Function to hide tooltip on mouse leave
        function handleMouseLeave() {
            tooltip.style.display = 'none';
        }

        // Initialize the graph and event listeners
        try {
            drawGraph(covidData);
            canvas.addEventListener('mousemove', handleMouseMove);
            canvas.addEventListener('mouseleave', handleMouseLeave);
        } catch (error) {
            console.error("An error occurred while initializing the graph:", error);
        }
    </script>

</body>
</html>
```
