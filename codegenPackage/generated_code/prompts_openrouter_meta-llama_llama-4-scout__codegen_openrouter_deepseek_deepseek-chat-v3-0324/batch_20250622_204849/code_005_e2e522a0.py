"""
Generated Code Metadata:
========================
Original URL: https://pediatricdentistinpune.com
Prompt: Write a code snippet in JavaScript to create a simple web application that allows users to search for pediatric dentists in Pune by location.
Generated: DETERMINISTIC_e2e522a098ccb7ea
Batch ID: 20250622_204849
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Pediatric Dentist Search Application for Pune

// Main App Component
class DentistSearchApp {
  constructor() {
    this.dentists = [
      { name: "Dr. Smith's Pediatric Dental Care", location: "Kothrud", rating: 4.5 },
      { name: "Little Smiles Dental Clinic", location: "Baner", rating: 4.2 },
      { name: "Happy Teeth Pediatric Dentistry", location: "Wakad", rating: 4.7 },
      { name: "Kids Dental World", location: "Hinjewadi", rating: 4.0 },
      { name: "Tiny Tooth Care Center", location: "Aundh", rating: 4.3 }
    ];

    this.init();
  }

  init() {
    this.renderSearchForm();
    this.setupEventListeners();
  }

  renderSearchForm() {
    const appContainer = document.getElementById('app');
    if (!appContainer) {
      console.error('App container not found');
      return;
    }

    appContainer.innerHTML = `
      <div class="search-container">
        <h1>Pediatric Dentist Search - Pune</h1>
        <div class="search-form">
          <select id="locationSelect">
            <option value="">All Locations</option>
            <option value="Kothrud">Kothrud</option>
            <option value="Baner">Baner</option>
            <option value="Wakad">Wakad</option>
            <option value="Hinjewadi">Hinjewadi</option>
            <option value="Aundh">Aundh</option>
          </select>
          <button id="searchBtn">Search</button>
        </div>
        <div id="resultsContainer" class="results-container"></div>
      </div>
    `;
  }

  setupEventListeners() {
    document.getElementById('searchBtn')?.addEventListener('click', () => this.handleSearch());
    document.getElementById('locationSelect')?.addEventListener('keypress', (e) => {
      if (e.key === 'Enter') this.handleSearch();
    });
  }

  handleSearch() {
    const locationSelect = document.getElementById('locationSelect');
    if (!locationSelect) return;

    const selectedLocation = locationSelect.value;
    const filteredDentists = selectedLocation 
      ? this.dentists.filter(dentist => dentist.location === selectedLocation)
      : this.dentists;

    this.displayResults(filteredDentists);
  }

  displayResults(dentists) {
    const resultsContainer = document.getElementById('resultsContainer');
    if (!resultsContainer) return;

    if (dentists.length === 0) {
      resultsContainer.innerHTML = '<p>No pediatric dentists found in the selected location.</p>';
      return;
    }

    const resultsHTML = dentists.map(dentist => `
      <div class="dentist-card">
        <h3>${dentist.name}</h3>
        <p><strong>Location:</strong> ${dentist.location}</p>
        <p><strong>Rating:</strong> ${dentist.rating} ★</p>
      </div>
    `).join('');

    resultsContainer.innerHTML = resultsHTML;
  }
}

// Initialize the app when DOM is loaded
document.addEventListener('DOMContentLoaded', () => {
  try {
    new DentistSearchApp();
  } catch (error) {
    console.error('Failed to initialize application:', error);
    const appContainer = document.getElementById('app');
    if (appContainer) {
      appContainer.innerHTML = '<p class="error">An error occurred while loading the application. Please try again later.</p>';
    }
  }
});

// CSS would typically be in a separate file, but included here for completeness
const style = document.createElement('style');
style.textContent = `
  body {
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 20px;
    background-color: #f5f5f5;
  }
  .search-container {
    max-width: 800px;
    margin: 0 auto;
    background: white;
    padding: 20px;
    border-radius: 8px;
    box-shadow: 0 2px 4px rgba(0,0,0,0.1);
  }
  .search-form {
    display: flex;
    gap: 10px;
    margin-bottom: 20px;
  }
  select, button {
    padding: 10px;
    font-size: 16px;
  }
  button {
    background-color: #4CAF50;
    color: white;
    border: none;
    cursor: pointer;
    border-radius: 4px;
  }
  button:hover {
    background-color: #45a049;
  }
  .results-container {
    display: flex;
    flex-direction: column;
    gap: 15px;
  }
  .dentist-card {
    border: 1px solid #ddd;
    padding: 15px;
    border-radius: 4px;
    background-color: #f9f9f9;
  }
  .error {
    color: red;
    text-align: center;
  }
`;
document.head.appendChild(style);
```
