"""
Generated Code Metadata:
========================
Original URL: https://fuelvm.flowtrack.me
Prompt: Generate HTML and JavaScript code for a drag-and-drop website editor that allows users to insert and edit text dynamically.
Generated: DETERMINISTIC_e898a4aac5f3265e
Batch ID: 20250612_150327
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
    <title>Drag-and-Drop Website Editor</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            background-color: #f5f5f5;
        }
        .editor-container {
            display: flex;
            height: 100vh;
        }
        .sidebar {
            width: 200px;
            background-color: #333;
            color: white;
            padding: 10px;
        }
        .sidebar-item {
            background-color: #444;
            padding: 10px;
            margin-bottom: 10px;
            cursor: move;
            border-radius: 4px;
        }
        .workspace {
            flex: 1;
            padding: 20px;
            background-color: white;
            overflow-y: auto;
        }
        .droppable-area {
            min-height: 100%;
            border: 2px dashed #ccc;
            padding: 20px;
        }
        .text-element {
            padding: 10px;
            margin-bottom: 10px;
            border: 1px solid #ddd;
            background-color: #f9f9f9;
            cursor: move;
            position: relative;
        }
        .text-element:hover {
            background-color: #f0f0f0;
        }
        .edit-btn {
            position: absolute;
            top: 5px;
            right: 5px;
            background: #4CAF50;
            color: white;
            border: none;
            padding: 2px 5px;
            cursor: pointer;
            border-radius: 3px;
        }
        .delete-btn {
            position: absolute;
            top: 5px;
            right: 50px;
            background: #f44336;
            color: white;
            border: none;
            padding: 2px 5px;
            cursor: pointer;
            border-radius: 3px;
        }
        .modal {
            display: none;
            position: fixed;
            z-index: 1;
            left: 0;
            top: 0;
            width: 100%;
            height: 100%;
            background-color: rgba(0,0,0,0.4);
        }
        .modal-content {
            background-color: #fefefe;
            margin: 15% auto;
            padding: 20px;
            border: 1px solid #888;
            width: 50%;
        }
        .close {
            color: #aaa;
            float: right;
            font-size: 28px;
            font-weight: bold;
            cursor: pointer;
        }
        .close:hover {
            color: black;
        }
    </style>
</head>
<body>
    <div class="editor-container">
        <div class="sidebar">
            <h3>Elements</h3>
            <div class="sidebar-item" draggable="true" data-type="text">Text</div>
            <div class="sidebar-item" draggable="true" data-type="heading">Heading</div>
        </div>
        <div class="workspace">
            <div class="droppable-area" id="droppable-area">
                <!-- Dropped elements will appear here -->
            </div>
        </div>
    </div>

    <!-- Edit Modal -->
    <div id="editModal" class="modal">
        <div class="modal-content">
            <span class="close">&times;</span>
            <h2>Edit Text</h2>
            <textarea id="editTextarea" rows="10" style="width: 100%;"></textarea>
            <button id="saveChanges" style="margin-top: 10px;">Save Changes</button>
        </div>
    </div>

    <script>
        document.addEventListener('DOMContentLoaded', function() {
            // DOM elements
            const droppableArea = document.getElementById('droppable-area');
            const sidebarItems = document.querySelectorAll('.sidebar-item');
            const editModal = document.getElementById('editModal');
            const editTextarea = document.getElementById('editTextarea');
            const saveChangesBtn = document.getElementById('saveChanges');
            const closeModal = document.querySelector('.close');
            
            // Variables to track drag and drop
            let draggedItem = null;
            let currentlyEditingElement = null;
            let elementCounter = 0;

            // Add drag event listeners to sidebar items
            sidebarItems.forEach(item => {
                item.addEventListener('dragstart', function(e) {
                    draggedItem = this;
                    e.dataTransfer.setData('text/plain', this.dataset.type);
                    setTimeout(() => {
                        this.style.display = 'none';
                    }, 0);
                });

                item.addEventListener('dragend', function() {
                    this.style.display = 'block';
                    draggedItem = null;
                });
            });

            // Droppable area event listeners
            droppableArea.addEventListener('dragover', function(e) {
                e.preventDefault();
                this.style.borderColor = '#4CAF50';
            });

            droppableArea.addEventListener('dragleave', function() {
                this.style.borderColor = '#ccc';
            });

            droppableArea.addEventListener('drop', function(e) {
                e.preventDefault();
                this.style.borderColor = '#ccc';
                
                if (draggedItem) {
                    const elementType = draggedItem.dataset.type;
                    createNewElement(elementType);
                }
            });

            // Create a new draggable element
            function createNewElement(type) {
                elementCounter++;
                const newElement = document.createElement('div');
                newElement.className = 'text-element';
                newElement.draggable = true;
                newElement.dataset.id = 'element-' + elementCounter;
                
                // Set default content based on type
                let content = '';
                if (type === 'text') {
                    content = 'Double-click to edit this text.';
                } else if (type === 'heading') {
                    content = 'Heading';
                }
                
                newElement.innerHTML = `
                    ${content}
                    <button class="edit-btn">Edit</button>
                    <button class="delete-btn">Delete</button>
                `;
                
                // Add event listeners to the new element
                newElement.addEventListener('dragstart', handleElementDragStart);
                newElement.addEventListener('dragend', handleElementDragEnd);
                newElement.querySelector('.edit-btn').addEventListener('click', handleEditClick);
                newElement.querySelector('.delete-btn').addEventListener('click', handleDeleteClick);
                
                droppableArea.appendChild(newElement);
            }

            // Element drag handlers
            function handleElementDragStart(e) {
                this.classList.add('dragging');
                e.dataTransfer.setData('text/plain', this.dataset.id);
            }

            function handleElementDragEnd() {
                this.classList.remove('dragging');
            }

            // Edit and delete handlers
            function handleEditClick(e) {
                e.stopPropagation();
                currentlyEditingElement = this.parentElement;
                editTextarea.value = currentlyEditingElement.firstChild.textContent.trim();
                editModal.style.display = 'block';
            }

            function handleDeleteClick(e) {
                e.stopPropagation();
                if (confirm('Are you sure you want to delete this element?')) {
                    this.parentElement.remove();
                }
            }

            // Modal handlers
            saveChangesBtn.addEventListener('click', function() {
                if (currentlyEditingElement) {
                    currentlyEditingElement.firstChild.textContent = editTextarea.value;
                    editModal.style.display = 'none';
                }
            });

            closeModal.addEventListener('click', function() {
                editModal.style.display = 'none';
            });

            window.addEventListener('click', function(e) {
                if (e.target === editModal) {
                    editModal.style.display = 'none';
                }
            });

            // Allow reordering of elements
            droppableArea.addEventListener('dragover', function(e) {
                e.preventDefault();
                const afterElement = getDragAfterElement(this, e.clientY);
                const draggable = document.querySelector('.dragging');
                
                if (afterElement == null) {
                    this.appendChild(draggable);
                } else {
                    this.insertBefore(draggable, afterElement);
                }
            });

            function getDragAfterElement(container, y) {
                const draggableElements = [...container.querySelectorAll('.text-element:not(.dragging)')];
                
                return draggableElements.reduce((closest, child) => {
                    const box = child.getBoundingClientRect();
                    const offset = y - box.top - box.height / 2;
                    
                    if (offset < 0 && offset > closest.offset) {
                        return { offset: offset, element: child };
                    } else {
                        return closest;
                    }
                }, { offset: Number.NEGATIVE_INFINITY }).element;
            }
        });
    </script>
</body>
</html>
```
