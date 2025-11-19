"""
Generated Code Metadata:
========================
Original URL: https://chile-horseriding.com
Prompt: Generate a code snippet in JavaScript to display the different horse riding tours offered by Chile Horse Riding, including the Cowboy Experience and Skiing & Riding Experience.
Generated: DETERMINISTIC_e8de8261d94f4803
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Define a class to represent a Horse Riding Tour
class HorseRidingTour {
    constructor(name, description, duration, price) {
        this.name = name; // Name of the tour
        this.description = description; // Description of the tour
        this.duration = duration; // Duration of the tour in hours
        this.price = price; // Price of the tour in USD
    }
}

// Create an array to hold the different tours offered
const tours = [
    new HorseRidingTour(
        "Cowboy Experience",
        "Experience the life of a Chilean cowboy, riding through beautiful landscapes and learning traditional skills.",
        4,
        150
    ),
    new HorseRidingTour(
        "Skiing & Riding Experience",
        "Combine skiing and horseback riding in the stunning Andes mountains for an unforgettable adventure.",
        6,
        250
    )
];

// Function to display the tours
function displayTours(tours) {
    // Check if the tours array is empty
    if (!Array.isArray(tours) || tours.length === 0) {
        console.error("No tours available to display.");
        return;
    }

    // Create a container for the tours
    const tourContainer = document.createElement('div');
    tourContainer.className = 'tour-container';

    // Iterate over each tour and create HTML elements to display them
    tours.forEach(tour => {
        const tourElement = document.createElement('div');
        tourElement.className = 'tour';

        // Create and append tour details
        tourElement.innerHTML = `
            <h2>${tour.name}</h2>
            <p>${tour.description}</p>
            <p><strong>Duration:</strong> ${tour.duration} hours</p>
            <p><strong>Price:</strong> $${tour.price}</p>
        `;

        // Append the tour element to the container
        tourContainer.appendChild(tourElement);
    });

    // Append the tour container to the body of the document
    document.body.appendChild(tourContainer);
}

// Call the function to display the tours
displayTours(tours);
```
