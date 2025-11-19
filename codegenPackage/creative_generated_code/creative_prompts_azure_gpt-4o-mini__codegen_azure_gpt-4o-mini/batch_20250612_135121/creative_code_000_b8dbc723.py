"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fuelvm.flowtrack.me
Prompt: How can I implement a drag-and-drop feature similar to the one described on fuelvm.flowtrack.me for a web application?
Generated: DETERMINISTIC_b8dbc723d1e106ae
Batch ID: 20250612_135121
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
    <title>Drag and Drop Example</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
        }
        #container {
            display: flex;
            justify-content: space-between;
        }
        .dropzone {
            width: 45%;
            height: 400px;
            border: 2px dashed #ccc;
            border-radius: 8px;
            padding: 10px;
            overflow-y: auto;
            position: relative;
        }
        .draggable {
            padding: 10px;
            margin: 5px;
            background-color: #007bff;
            color: white;
            border-radius: 4px;
            cursor: grab;
        }
    </style>
</head>
<body>

    <h1>Drag and Drop Feature</h1>
    <div id="container">
        <div class="dropzone" id="source">
            <div class="draggable" draggable="true" id="item1">Item 1</div>
            <div class="draggable" draggable="true" id="item2">Item 2</div>
            <div class="draggable" draggable="true" id="item3">Item 3</div>
        </div>
        <div class="dropzone" id="target">
            <h3>Drop Here</h3>
        </div>
    </div>

    <script>
        // Get references to the drop zones
        const sourceZone = document.getElementById('source');
        const targetZone = document.getElementById('target');

        // Add drag event listeners to each draggable item
        sourceZone.addEventListener('dragstart', (event) => {
            // Store the id of the dragged element
            event.dataTransfer.setData('text/plain', event.target.id);
            event.target.style.opacity = '0.5'; // Optional: make the item semi-transparent during drag
        });

        sourceZone.addEventListener('dragend', (event) => {
            event.target.style.opacity = ''; // Reset the opacity after drag
        });

        // Prevent default behavior for dragover
        targetZone.addEventListener('dragover', (event) => {
            event.preventDefault(); // Allow dropping by preventing default behavior
        });

        // Handle drop event
        targetZone.addEventListener('drop', (event) => {
            event.preventDefault(); // Prevent default action of the drop
            
            const id = event.dataTransfer.getData('text/plain'); // Get the id of the dragged element
            const draggableElement = document.getElementById(id); // Find the dragged element
            const clonedElement = draggableElement.cloneNode(true); // Clone the element for dropping
            
            clonedElement.removeAttribute('id'); // Remove id to prevent duplicates
            targetZone.appendChild(clonedElement); // Append cloned element to the target zone

            // Make the new element draggable again
            clonedElement.setAttribute('draggable', 'true'); 
            clonedElement.addEventListener('dragstart', (event) => {
                event.dataTransfer.setData('text/plain', clonedElement.id);
                clonedElement.style.opacity = '0.5'; 
            });

            clonedElement.addEventListener('dragend', (event) => {
                clonedElement.style.opacity = ''; 
            });
        });
    </script>

</body>
</html>
```
