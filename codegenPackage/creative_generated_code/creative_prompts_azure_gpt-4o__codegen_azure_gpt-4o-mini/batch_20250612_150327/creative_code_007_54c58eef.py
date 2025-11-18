"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fuelvm.flowtrack.me
Prompt: Generate code for a drag-and-drop website builder using vanilla JavaScript, with functionality for adding headings, accordions, and text blocks.
Generated: DETERMINISTIC_54c58eef8f074eff
Batch ID: 20250612_150327
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
    <title>Drag-and-Drop Website Builder</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 20px;
            background-color: #f0f0f0;
        }
        #builder {
            width: 100%;
            min-height: 400px;
            border: 1px dashed #ccc;
            background-color: white;
            position: relative;
            overflow: auto;
        }
        .draggable {
            padding: 10px;
            margin: 10px;
            background-color: #007bff;
            color: white;
            cursor: move;
            border-radius: 5px;
        }
        .dropzone {
            border: 2px dashed #007bff;
            padding: 10px;
            margin: 10px;
            background-color: #e9ecef;
            border-radius: 5px;
        }
    </style>
</head>
<body>

    <h1>Drag-and-Drop Website Builder</h1>
    
    <div id="toolbox">
        <div class="draggable" draggable="true" data-type="heading">Add Heading</div>
        <div class="draggable" draggable="true" data-type="accordion">Add Accordion</div>
        <div class="draggable" draggable="true" data-type="text">Add Text Block</div>
    </div>

    <div id="builder" class="dropzone">
        <p>Drop your elements here!</p>
    </div>

    <script>
        document.addEventListener('DOMContentLoaded', () => {
            const builder = document.getElementById('builder');
            const draggables = document.querySelectorAll('.draggable');

            // Add drag events to draggables
            draggables.forEach(draggable => {
                draggable.addEventListener('dragstart', dragStart);
                draggable.addEventListener('dragend', dragEnd);
            });

            // Add drop events to the builder
            builder.addEventListener('dragover', dragOver);
            builder.addEventListener('drop', drop);

            function dragStart(e) {
                // Store the type of element being dragged
                e.dataTransfer.setData('text/plain', e.target.dataset.type);
            }

            function dragEnd() {
                // Reset the style after dragging ends
                this.style.opacity = '1';
            }

            function dragOver(e) {
                // Prevent default to allow dropping
                e.preventDefault();
            }

            function drop(e) {
                e.preventDefault();
                const type = e.dataTransfer.getData('text/plain');
                
                // Create the appropriate element based on the type
                let element;
                switch (type) {
                    case 'heading':
                        element = document.createElement('h2');
                        element.textContent = 'New Heading';
                        break;
                    case 'accordion':
                        element = createAccordion();
                        break;
                    case 'text':
                        element = document.createElement('p');
                        element.textContent = 'New text block';
                        break;
                    default:
                        console.error('Unknown type:', type);
                        return;
                }
                
                // Append the new element to the builder
                builder.appendChild(element);
            }

            function createAccordion() {
                const accordion = document.createElement('div');
                accordion.className = 'accordion';
                accordion.innerHTML = `
                    <button class="accordion-button">Accordion Title</button>
                    <div class="accordion-content" style="display:none;">
                        <p>Accordion content goes here.</p>
                    </div>
                `;
                
                // Toggle accordion content on button click
                accordion.querySelector('.accordion-button').addEventListener('click', function() {
                    const content = this.nextElementSibling;
                    if (content.style.display === 'block') {
                        content.style.display = 'none';
                    } else {
                        content.style.display = 'block';
                    }
                });

                return accordion;
            }
        });
    </script>

</body>
</html>
```
