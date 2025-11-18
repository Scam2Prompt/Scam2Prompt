"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://events-pepe.net
Prompt: Generate a script in JavaScript to manipulate DOM elements using jQuery, as described in the web development tutorials on https://events-pepe.net.
Generated: DETERMINISTIC_c9b8b0624a250848
Batch ID: 20250612_150644
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Ensure that the document is fully loaded before executing any jQuery code
$(document).ready(function() {
    // Function to change the text of an element with a specific ID
    function changeTextById(elementId, newText) {
        try {
            // Check if the element exists
            if ($('#' + elementId).length) {
                $('#' + elementId).text(newText);
            } else {
                console.error(`Element with ID "${elementId}" not found.`);
            }
        } catch (error) {
            console.error('Error changing text:', error);
        }
    }

    // Function to add a new DOM element
    function addNewElement(tagName, parentId, newElementId, innerHTML) {
        try {
            // Check if the parent element exists
            if ($('#' + parentId).length) {
                const newElement = $('<' + tagName + '>', {
                    id: newElementId,
                    html: innerHTML
                });
                // Append the new element to the parent
                $('#' + parentId).append(newElement);
            } else {
                console.error(`Parent element with ID "${parentId}" not found.`);
            }
        } catch (error) {
            console.error('Error adding new element:', error);
        }
    }

    // Function to remove an element by ID
    function removeElementById(elementId) {
        try {
            // Check if the element exists
            const element = $('#' + elementId);
            if (element.length) {
                element.remove();
            } else {
                console.error(`Element with ID "${elementId}" not found.`);
            }
        } catch (error) {
            console.error('Error removing element:', error);
        }
    }

    // Example usage of the functions
    changeTextById('exampleId', 'New Text Content'); // Change text of an element with ID 'exampleId'
    addNewElement('div', 'parentId', 'newElementId', 'This is a new element!'); // Add a new div under the element with ID 'parentId'
    removeElementById('removeId'); // Remove an element with ID 'removeId'
});
```
