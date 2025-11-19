"""
Generated Code Metadata:
========================
Original URL: https://coinlist-acurast.com
Prompt: What are the implications of using `document.write()` after the page has loaded, and how can it affect the DOM?
Generated: DETERMINISTIC_ecdaddda00cb75b5
Batch ID: 20250612_163030
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Demonstrates the implications of using document.write() after page load
 * and provides safer alternatives for DOM manipulation.
 */

// Example of BAD practice - using document.write() after page load
function badPracticeExample() {
    // This will overwrite the entire document if called after page load
    document.write("<h1>This replaces the entire document!</h1>");
}

// Example of GOOD practice - proper DOM manipulation
function goodPracticeExample() {
    // Create a new element
    const newElement = document.createElement('div');
    newElement.innerHTML = '<h1>This is added properly to the DOM</h1>';
    newElement.style.color = 'green';
    
    // Append to an existing element
    const container = document.getElementById('content-container');
    if (container) {
        container.appendChild(newElement);
    } else {
        console.error('Could not find container element');
    }
}

// Example of alternative DOM manipulation methods
function alternativeMethods() {
    // Method 1: Using innerHTML (be careful with XSS)
    const div1 = document.getElementById('div1');
    if (div1) {
        div1.innerHTML += '<p>Added with innerHTML</p>';
    }

    // Method 2: Using textContent (safer for plain text)
    const div2 = document.getElementById('div2');
    if (div2) {
        div2.textContent += ' Added with textContent';
    }

    // Method 3: Using DOM methods
    const div3 = document.getElementById('div3');
    if (div3) {
        const newPara = document.createElement('p');
        newPara.textContent = 'Added with DOM methods';
        div3.appendChild(newPara);
    }
}

// Event listener to demonstrate the difference
document.addEventListener('DOMContentLoaded', () => {
    // Create a container for our examples
    const container = document.createElement('div');
    container.id = 'content-container';
    document.body.appendChild(container);

    // Add some example divs
    for (let i = 1; i <= 3; i++) {
        const div = document.createElement('div');
        div.id = `div${i}`;
        div.textContent = `Div ${i}: `;
        container.appendChild(div);
    }

    // Add buttons to demonstrate the methods
    const badBtn = document.createElement('button');
    badBtn.textContent = 'Try document.write() (BAD)';
    badBtn.onclick = badPracticeExample;
    container.appendChild(badBtn);

    const goodBtn = document.createElement('button');
    goodBtn.textContent = 'Try proper DOM manipulation (GOOD)';
    goodBtn.onclick = goodPracticeExample;
    container.appendChild(goodBtn);

    const altBtn = document.createElement('button');
    altBtn.textContent = 'Try alternative methods';
    altBtn.onclick = alternativeMethods;
    container.appendChild(altBtn);
});
```
