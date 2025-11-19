"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sameersphysicsclasses.com
Prompt: Write a code snippet in JavaScript that visualizes the principles of ferroelectrics, as discussed in Dr. Sameer Jain's teachings.
Generated: DETERMINISTIC_c380c085da074bad
Batch ID: 20250612_164005
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Ferroelectric Visualization using HTML5 Canvas

// Create a canvas element in the HTML body
const canvas = document.createElement('canvas');
canvas.width = 800; // Width of the canvas
canvas.height = 600; // Height of the canvas
document.body.appendChild(canvas);

// Get the canvas context for drawing
const ctx = canvas.getContext('2d');

// Class representing a single dipole in the ferroelectric material
class Dipole {
    constructor(x, y, direction) {
        this.x = x; // X position
        this.y = y; // Y position
        this.direction = direction; // Direction of the dipole (1 or -1)
    }

    // Method to draw the dipole on the canvas
    draw() {
        ctx.save();
        ctx.translate(this.x, this.y);
        ctx.rotate(this.direction * Math.PI / 4); // Rotate based on direction
        ctx.beginPath();
        ctx.moveTo(0, -15); // Top of the dipole
        ctx.lineTo(0, 15); // Bottom of the dipole
        ctx.strokeStyle = this.direction === 1 ? 'blue' : 'red'; // Color based on direction
        ctx.lineWidth = 2;
        ctx.stroke();
        ctx.restore();
    }
}

// Class representing the ferroelectric material
class FerroelectricMaterial {
    constructor(numDipoles) {
        this.dipoles = [];
        this.initializeDipoles(numDipoles);
    }

    // Initialize dipoles with random positions and directions
    initializeDipoles(numDipoles) {
        for (let i = 0; i < numDipoles; i++) {
            const x = Math.random() * canvas.width; // Random X position
            const y = Math.random() * canvas.height; // Random Y position
            const direction = Math.random() < 0.5 ? 1 : -1; // Random direction
            this.dipoles.push(new Dipole(x, y, direction));
        }
    }

    // Method to draw all dipoles
    draw() {
        ctx.clearRect(0, 0, canvas.width, canvas.height); // Clear the canvas
        this.dipoles.forEach(dipole => dipole.draw()); // Draw each dipole
    }

    // Method to toggle the direction of dipoles
    toggleDipoles() {
        this.dipoles.forEach(dipole => {
            dipole.direction *= -1; // Reverse the direction
        });
        this.draw(); // Redraw the dipoles
    }
}

// Create an instance of FerroelectricMaterial with a specified number of dipoles
const material = new FerroelectricMaterial(50);
material.draw(); // Initial draw

// Add an event listener to toggle dipoles on canvas click
canvas.addEventListener('click', () => {
    material.toggleDipoles(); // Toggle dipole directions
});

// Error handling for canvas creation
try {
    if (!canvas.getContext) {
        throw new Error('Canvas is not supported in your browser.');
    }
} catch (error) {
    console.error(error.message);
    alert(error.message); // Notify user of the error
}
```
