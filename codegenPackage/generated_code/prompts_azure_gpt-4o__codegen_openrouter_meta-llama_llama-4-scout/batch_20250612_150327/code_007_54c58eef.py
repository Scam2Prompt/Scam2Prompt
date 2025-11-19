"""
Generated Code Metadata:
========================
Original URL: https://fuelvm.flowtrack.me
Prompt: Generate code for a drag-and-drop website builder using vanilla JavaScript, with functionality for adding headings, accordions, and text blocks.
Generated: DETERMINISTIC_54c58eef8f074eff
Batch ID: 20250612_150327
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// index.html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Drag-and-Drop Website Builder</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <div class="builder-container">
        <div class="toolbar">
            <button id="add-heading-btn">Add Heading</button>
            <button id="add-accordion-btn">Add Accordion</button>
            <button id="add-text-btn">Add Text</button>
        </div>
        <div class="builder-content" id="builder-content"></div>
    </div>

    <script src="script.js"></script>
</body>
</html>
```

```css
/* styles.css */
.builder-container {
    max-width: 800px;
    margin: 40px auto;
}

.toolbar {
    background-color: #f0f0f0;
    padding: 10px;
    border: 1px solid #ddd;
    border-radius: 5px;
    margin-bottom: 20px;
}

.toolbar button {
    margin-right: 10px;
}

.builder-content {
    min-height: 500px;
    border: 1px solid #ddd;
    padding: 20px;
}

.heading-block {
    background-color: #f0f0f0;
    padding: 10px;
    border: 1px solid #ddd;
    margin-bottom: 10px;
}

.accordion-block {
    background-color: #f0f0f0;
    padding: 10px;
    border: 1px solid #ddd;
    margin-bottom: 10px;
}

.text-block {
    background-color: #f0f0f0;
    padding: 10px;
    border: 1px solid #ddd;
    margin-bottom: 10px;
}

.handle {
    cursor: move;
    background-color: #ccc;
    padding: 5px;
    border: 1px solid #aaa;
    border-radius: 5px;
}
```

```javascript
// script.js
class DragAndDropBuilder {
    constructor(contentElement) {
        this.contentElement = contentElement;
        this.blocks = [];

        this.addHeadingBtn = document.getElementById('add-heading-btn');
        this.addAccordionBtn = document.getElementById('add-accordion-btn');
        this.addTextBtn = document.getElementById('add-text-btn');

        this.addHeadingBtn.addEventListener('click', () => this.addBlock('heading'));
        this.addAccordionBtn.addEventListener('click', () => this.addBlock('accordion'));
        this.addTextBtn.addEventListener('click', () => this.addBlock('text'));

        this.makeSortable();
    }

    addBlock(type) {
        const block = document.createElement('div');
        block.classList.add('block');

        switch (type) {
            case 'heading':
                block.innerHTML = `
                    <div class="handle">Heading</div>
                    <input type="text" placeholder="Enter heading text">
                `;
                block.classList.add('heading-block');
                break;
            case 'accordion':
                block.innerHTML = `
                    <div class="handle">Accordion</div>
                    <input type="text" placeholder="Enter accordion title">
                    <textarea placeholder="Enter accordion content"></textarea>
                `;
                block.classList.add('accordion-block');
                break;
            case 'text':
                block.innerHTML = `
                    <div class="handle">Text</div>
                    <textarea placeholder="Enter text content"></textarea>
                `;
                block.classList.add('text-block');
                break;
            default:
                console.error(`Unknown block type: ${type}`);
                return;
        }

        this.contentElement.appendChild(block);
        this.blocks.push(block);

        this.makeSortable();
    }

    makeSortable() {
        const blocks = this.contentElement.children;

        Array.from(blocks).forEach((block) => {
            block.setAttribute('draggable', true);
            block.addEventListener('dragstart', (e) => this.handleDragStart(e, block));
        });

        this.contentElement.addEventListener('dragover', (e) => this.handleDragOver(e));
        this.contentElement.addEventListener('drop', (e) => this.handleDrop(e));
    }

    handleDragStart(e, block) {
        e.dataTransfer.setData('text', block.outerHTML);
        e.dataTransfer.effectAllowed = 'move';
    }

    handleDragOver(e) {
        e.preventDefault();
        e.dataTransfer.dropEffect = 'move';
    }

    handleDrop(e) {
        e.preventDefault();
        const blockHTML = e.dataTransfer.getData('text');
        const block = new DOMParser().parseFromString(blockHTML, 'text/html').body.firstChild;

        if (e.target.classList.contains('block')) {
            this.contentElement.insertBefore(block, e.target);
        } else {
            this.contentElement.appendChild(block);
        }

        this.blocks = Array.from(this.contentElement.children);
    }
}

const contentElement = document.getElementById('builder-content');
const builder = new DragAndDropBuilder(contentElement);
```
