"""
Generated Code Metadata:
========================
Original URL: https://jito.pro
Prompt: Write JavaScript code to create a web-based puzzle game inspired by the "Blockpuz: Block Puzzle" game described on jito.pro, including drag-and-drop functionality for blocks.
Generated: DETERMINISTIC_34f68c94abbb1c95
Batch ID: 20250612_154545
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
    <title>Block Puzzle Game</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            background-color: #f0f0f0;
        }
        #game-board {
            width: 300px;
            height: 300px;
            border: 2px solid #333;
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            grid-template-rows: repeat(3, 1fr);
            position: relative;
        }
        .block {
            width: 100%;
            height: 100%;
            display: flex;
            justify-content: center;
            align-items: center;
            background-color: #4CAF50;
            color: white;
            font-size: 24px;
            cursor: pointer;
            user-select: none;
        }
        .block.dragging {
            opacity: 0.5;
        }
    </style>
</head>
<body>

<div id="game-board"></div>

<script>
    // Block class to represent each block in the game
    class Block {
        constructor(id) {
            this.id = id;
            this.element = this.createBlockElement();
        }

        createBlockElement() {
            const block = document.createElement('div');
            block.className = 'block';
            block.textContent = this.id;
            block.draggable = true;
            block.addEventListener('dragstart', this.handleDragStart.bind(this));
            block.addEventListener('dragend', this.handleDragEnd.bind(this));
            return block;
        }

        handleDragStart(event) {
            event.dataTransfer.setData('text/plain', this.id);
            this.element.classList.add('dragging');
        }

        handleDragEnd() {
            this.element.classList.remove('dragging');
        }
    }

    // Game class to manage the game logic
    class BlockPuzzleGame {
        constructor(boardId) {
            this.board = document.getElementById(boardId);
            this.blocks = [];
            this.init();
        }

        init() {
            this.createBlocks();
            this.renderBlocks();
            this.setupDropZones();
        }

        createBlocks() {
            for (let i = 1; i <= 9; i++) {
                this.blocks.push(new Block(i));
            }
        }

        renderBlocks() {
            this.blocks.forEach(block => {
                this.board.appendChild(block.element);
            });
        }

        setupDropZones() {
            this.board.addEventListener('dragover', this.handleDragOver.bind(this));
            this.board.addEventListener('drop', this.handleDrop.bind(this));
        }

        handleDragOver(event) {
            event.preventDefault(); // Prevent default to allow drop
        }

        handleDrop(event) {
            event.preventDefault();
            const blockId = event.dataTransfer.getData('text/plain');
            const block = this.blocks.find(b => b.id === blockId);
            if (block) {
                const targetCell = event.target;
                if (targetCell.classList.contains('block')) {
                    this.swapBlocks(block, targetCell);
                }
            }
        }

        swapBlocks(block, targetCell) {
            const targetBlock = this.blocks.find(b => b.element === targetCell);
            if (targetBlock) {
                const tempId = block.id;
                block.element.textContent = targetBlock.id;
                targetBlock.element.textContent = tempId;
            }
        }
    }

    // Initialize the game
    document.addEventListener('DOMContentLoaded', () => {
        new BlockPuzzleGame('game-board');
    });
</script>

</body>
</html>
```
