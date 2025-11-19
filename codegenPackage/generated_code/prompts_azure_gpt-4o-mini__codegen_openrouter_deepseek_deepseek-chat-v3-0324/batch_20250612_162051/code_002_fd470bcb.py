"""
Generated Code Metadata:
========================
Original URL: https://rehiletes.com
Prompt: Create a JavaScript application that allows users to search for and book excursions in Mexico, highlighting the cultural and natural experiences provided by Rehiletes.
Generated: DETERMINISTIC_fd470bcb2fd5a54d
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Excursion Booking Application for Rehiletes
// This application allows users to search and book cultural and natural excursions in Mexico.

// Excursion data - in a real app, this would come from an API
const excursions = [
  {
    id: 1,
    name: "Ancient Mayan Ruins Tour",
    description: "Explore the majestic Mayan ruins with our expert guides.",
    location: "Chichen Itza, Yucatan",
    duration: "8 hours",
    price: 75,
    type: "cultural",
    availability: ["2023-11-15", "2023-11-20", "2023-11-25"]
  },
  {
    id: 2,
    name: "Cenote Swimming Adventure",
    description: "Swim in the crystal-clear waters of sacred cenotes.",
    location: "Valladolid, Yucatan",
    duration: "6 hours",
    price: 60,
    type: "natural",
    availability: ["2023-11-16", "2023-11-22", "2023-11-28"]
  },
  {
    id: 3,
    name: "Day of the Dead Festival",
    description: "Experience the vibrant traditions of Dia de los Muertos.",
    location: "Oaxaca City",
    duration: "12 hours",
    price: 90,
    type: "cultural",
    availability: ["2023-11-01", "2023-11-02"]
  }
];

// DOM elements
const searchForm = document.getElementById('search-form');
const resultsContainer = document.getElementById('results-container');
const bookingForm = document.getElementById('booking-form');
const confirmationMessage = document.getElementById('confirmation-message');

// Initialize the application
document.addEventListener('DOMContentLoaded', () => {
  displayAllExcursions();
  setupEventListeners();
});

// Display all excursions initially
function displayAllExcursions() {
  renderExcursions(excursions);
}

// Set up event listeners
function setupEventListeners() {
  // Search form submission
  searchForm.addEventListener('submit', (e) => {
    e.preventDefault();
    const searchTerm = document.getElementById('search-term').value.toLowerCase();
    const excursionType = document.getElementById('excursion-type').value;
    
    const filteredExcursions = filterExcursions(searchTerm, excursionType);
    renderExcursions(filteredExcursions);
  });

  // Booking form submission
  bookingForm.addEventListener('submit', (e) => {
    e.preventDefault();
    handleBooking();
  });
}

// Filter excursions based on search criteria
function filterExcursions(searchTerm, type) {
  return excursions.filter(excursion => {
    const matchesSearch = excursion.name.toLowerCase().includes(searchTerm) || 
                         excursion.description.toLowerCase().includes(searchTerm) ||
                         excursion.location.toLowerCase().includes(searchTerm);
    const matchesType = type === 'all' || excursion.type === type;
    return matchesSearch && matchesType;
  });
}

// Render excursions to the DOM
function renderExcursions(excursionsToRender) {
  resultsContainer.innerHTML = '';
  
  if (excursionsToRender.length === 0) {
    resultsContainer.innerHTML = '<p>No excursions found. Try different search criteria.</p>';
    return;
  }

  excursionsToRender.forEach(excursion => {
    const excursionElement = document.createElement('div');
    excursionElement.className = 'excursion-card';
    excursionElement.innerHTML = `
      <h3>${excursion.name}</h3>
      <p><strong>Location:</strong> ${excursion.location}</p>
      <p><strong>Description:</strong> ${excursion.description}</p>
      <p><strong>Duration:</strong> ${excursion.duration}</p>
      <p><strong>Price:</strong> $${excursion.price}</p>
      <p><strong>Available Dates:</strong> ${excursion.availability.join(', ')}</p>
      <button class="book-btn" data-id="${excursion.id}">Book Now</button>
    `;
    resultsContainer.appendChild(excursionElement);
  });

  // Add event listeners to book buttons
  document.querySelectorAll('.book-btn').forEach(button => {
    button.addEventListener('click', (e) => {
      const excursionId = parseInt(e.target.getAttribute('data-id'));
      showBookingForm(excursionId);
    });
  });
}

// Show booking form for a specific excursion
function showBookingForm(excursionId) {
  const excursion = excursions.find(e => e.id === excursionId);
  if (!excursion) {
    alert('Excursion not found');
    return;
  }

  document.getElementById('excursion-name').textContent = excursion.name;
  document.getElementById('excursion-price').textContent = `$${excursion.price}`;
  document.getElementById('excursion-id').value = excursion.id;

  // Populate date selector
  const dateSelect = document.getElementById('booking-date');
  dateSelect.innerHTML = '<option value="">Select a date</option>';
  excursion.availability.forEach(date => {
    const option = document.createElement('option');
    option.value = date;
    option.textContent = date;
    dateSelect.appendChild(option);
  });

  // Show the booking form
  bookingForm.style.display = 'block';
  resultsContainer.style.display = 'none';
  searchForm.style.display = 'none';
}

// Handle booking form submission
function handleBooking() {
  const excursionId = parseInt(document.getElementById('excursion-id').value);
  const date = document.getElementById('booking-date').value;
  const name = document.getElementById('full-name').value.trim();
  const email = document.getElementById('email').value.trim();
  const participants = parseInt(document.getElementById('participants').value);

  // Basic validation
  if (!name || !email || !date || isNaN(participants) || participants < 1) {
    alert('Please fill in all fields correctly');
    return;
  }

  const excursion = excursions.find(e => e.id === excursionId);
  if (!excursion) {
    alert('Invalid excursion selected');
    return;
  }

  // In a real app, this would send data to a server
  const totalPrice = excursion.price * participants;
  
  // Show confirmation
  confirmationMessage.innerHTML = `
    <h3>Booking Confirmed!</h3>
    <p><strong>Excursion:</strong> ${excursion.name}</p>
    <p><strong>Date:</strong> ${date}</p>
    <p><strong>Participants:</strong> ${participants}</p>
    <p><strong>Total Price:</strong> $${totalPrice}</p>
    <p>A confirmation has been sent to ${email}</p>
    <button id="new-search-btn">New Search</button>
  `;

  bookingForm.style.display = 'none';
  confirmationMessage.style.display = 'block';

  // Add event listener for new search button
  document.getElementById('new-search-btn').addEventListener('click', () => {
    resetApplication();
  });
}

// Reset the application to initial state
function resetApplication() {
  searchForm.reset();
  bookingForm.reset();
  confirmationMessage.innerHTML = '';
  
  searchForm.style.display = 'block';
  resultsContainer.style.display = 'block';
  bookingForm.style.display = 'none';
  confirmationMessage.style.display = 'none';
  
  displayAllExcursions();
}
```

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Rehiletes - Mexican Excursions</title>
  <style>
    body {
      font-family: 'Arial', sans-serif;
      line-height: 1.6;
      margin: 0;
      padding: 20px;
      color: #333;
    }
    .container {
      max-width: 1200px;
      margin: 0 auto;
    }
    h1 {
      color: #e63946;
      text-align: center;
    }
    .search-section {
      background-color: #f1faee;
      padding: 20px;
      border-radius: 8px;
      margin-bottom: 20px;
    }
    form {
      display: flex;
      flex-wrap: wrap;
      gap: 10px;
    }
    input, select, button {
      padding: 8px 12px;
      border: 1px solid #ddd;
      border-radius: 4px;
    }
    button {
      background-color: #457b9d;
      color: white;
      border: none;
      cursor: pointer;
    }
    button:hover {
      background-color: #1d3557;
    }
    .excursion-card {
      border: 1px solid #a8dadc;
      border-radius: 8px;
      padding: 15px;
      margin-bottom: 15px;
      background-color: #f1faee;
    }
    .excursion-card h3 {
      color: #1d3557;
      margin-top: 0;
    }
    .book-btn {
      background-color: #e63946;
    }
    #booking-form, #confirmation-message {
      display: none;
      background-color: #a8dadc;
      padding: 20px;
      border-radius: 8px;
      margin-top: 20px;
