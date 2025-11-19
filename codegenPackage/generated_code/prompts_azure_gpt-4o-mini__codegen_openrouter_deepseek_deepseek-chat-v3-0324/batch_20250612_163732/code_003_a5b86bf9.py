"""
Generated Code Metadata:
========================
Original URL: https://wolfyyy.pages.dev
Prompt: Develop a JavaScript application that allows users to visualize the breeding process of Wolves and Sheep in Wolf Game.
Generated: DETERMINISTIC_a5b86bf99286deb9
Batch ID: 20250612_163732
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Wolf Game Simulation
 * 
 * This application simulates the breeding process of Wolves and Sheep in a Wolf Game.
 * It visualizes the population changes over generations based on breeding rules.
 */

class Animal {
  /**
   * Base class for animals (Wolves and Sheep)
   * @param {string} type - The type of animal ('wolf' or 'sheep')
   * @param {number} id - Unique identifier for the animal
   */
  constructor(type, id) {
    this.type = type;
    this.id = id;
    this.age = 0;
    this.canBreed = false;
  }

  /**
   * Increase age and update breeding capability
   */
  grow() {
    this.age++;
    this.canBreed = this.age >= 2; // Animals can breed after 2 turns
  }

  /**
   * Attempt to breed with another animal
   * @param {Animal} partner - The potential breeding partner
   * @returns {Animal|null} - New offspring or null if breeding fails
   */
  breedWith(partner) {
    if (!this.canBreed || !partner.canBreed || this.type !== partner.type) {
      return null;
    }

    // Reset breeding capability after successful breeding
    this.canBreed = false;
    partner.canBreed = false;

    return new Animal(this.type, Date.now() + Math.random());
  }
}

class WolfGame {
  /**
   * The main game class that manages the simulation
   * @param {number} initialWolves - Initial wolf population
   * @param {number} initialSheep - Initial sheep population
   */
  constructor(initialWolves = 5, initialSheep = 20) {
    this.wolves = this._createAnimals('wolf', initialWolves);
    this.sheep = this._createAnimals('sheep', initialSheep);
    this.generation = 0;
    this.history = [];
    this._recordHistory();
  }

  /**
   * Create initial population of animals
   * @param {string} type - Type of animal to create
   * @param {number} count - Number of animals to create
   * @returns {Array<Animal>} - Array of animal instances
   */
  _createAnimals(type, count) {
    return Array.from({ length: count }, (_, i) => new Animal(type, i));
  }

  /**
   * Record current population state in history
   */
  _recordHistory() {
    this.history.push({
      generation: this.generation,
      wolves: this.wolves.length,
      sheep: this.sheep.length
    });
  }

  /**
   * Simulate one generation of breeding
   */
  simulateGeneration() {
    // Grow all animals
    this.wolves.forEach(wolf => wolf.grow());
    this.sheep.forEach(sheep => sheep.grow());

    // Breed wolves
    const newWolves = this._breedPopulation(this.wolves);
    this.wolves = [...this.wolves, ...newWolves];

    // Breed sheep
    const newSheep = this._breedPopulation(this.sheep);
    this.sheep = [...this.sheep, ...newSheep];

    // Update generation and history
    this.generation++;
    this._recordHistory();
  }

  /**
   * Breed animals within a population
   * @param {Array<Animal>} population - The population to breed
   * @returns {Array<Animal>} - New offspring
   */
  _breedPopulation(population) {
    const offspring = [];
    const breedingPool = [...population].filter(animal => animal.canBreed);

    // Shuffle breeding pool for random pairing
    for (let i = breedingPool.length - 1; i > 0; i--) {
      const j = Math.floor(Math.random() * (i + 1));
      [breedingPool[i], breedingPool[j]] = [breedingPool[j], breedingPool[i]];
    }

    // Pair up animals and breed
    for (let i = 0; i < breedingPool.length - 1; i += 2) {
      const offspringAnimal = breedingPool[i].breedWith(breedingPool[i + 1]);
      if (offspringAnimal) {
        offspring.push(offspringAnimal);
      }
    }

    return offspring;
  }

  /**
   * Get current population counts
   * @returns {Object} - Current wolf and sheep counts
   */
  getPopulationCounts() {
    return {
      wolves: this.wolves.length,
      sheep: this.sheep.length
    };
  }

  /**
   * Get the full history of population changes
   * @returns {Array<Object>} - Array of historical population data
   */
  getHistory() {
    return this.history;
  }
}

// UI Controller for the simulation
class WolfGameUI {
  /**
   * Handles the visualization and user interaction
   * @param {HTMLElement} container - DOM element to render the simulation in
   */
  constructor(container) {
    this.container = container;
    this.game = new WolfGame();
    this.chart = null;
    this.init();
  }

  /**
   * Initialize the UI
   */
  init() {
    this.renderControls();
    this.renderPopulationInfo();
    this.initChart();
    this.updateChart();
  }

  /**
   * Render control buttons
   */
  renderControls() {
    const controls = document.createElement('div');
    controls.className = 'controls';

    const nextGenBtn = document.createElement('button');
    nextGenBtn.textContent = 'Next Generation';
    nextGenBtn.addEventListener('click', () => this.nextGeneration());

    const resetBtn = document.createElement('button');
    resetBtn.textContent = 'Reset';
    resetBtn.addEventListener('click', () => this.reset());

    controls.appendChild(nextGenBtn);
    controls.appendChild(resetBtn);
    this.container.appendChild(controls);
  }

  /**
   * Render population information
   */
  renderPopulationInfo() {
    const info = document.createElement('div');
    info.className = 'population-info';
    this.infoElement = info;
    this.updatePopulationInfo();
    this.container.appendChild(info);
  }

  /**
   * Update population information display
   */
  updatePopulationInfo() {
    const counts = this.game.getPopulationCounts();
    this.infoElement.innerHTML = `
      <h3>Generation ${this.game.generation}</h3>
      <p>Wolves: ${counts.wolves}</p>
      <p>Sheep: ${counts.sheep}</p>
    `;
  }

  /**
   * Initialize the chart for visualization
   */
  initChart() {
    const chartContainer = document.createElement('div');
    chartContainer.className = 'chart-container';
    this.chartElement = document.createElement('canvas');
    chartContainer.appendChild(this.chartElement);
    this.container.appendChild(chartContainer);

    // Initialize Chart.js if available
    if (typeof Chart !== 'undefined') {
      this.chart = new Chart(this.chartElement.getContext('2d'), {
        type: 'line',
        data: {
          labels: [],
          datasets: [
            {
              label: 'Wolves',
              data: [],
              borderColor: 'rgb(255, 99, 132)',
              tension: 0.1
            },
            {
              label: 'Sheep',
              data: [],
              borderColor: 'rgb(54, 162, 235)',
              tension: 0.1
            }
          ]
        },
        options: {
          responsive: true,
          scales: {
            y: {
              beginAtZero: true
            }
          }
        }
      });
    } else {
      this.chartElement.textContent = 'Chart.js is required for visualization.';
    }
  }

  /**
   * Update the chart with current data
   */
  updateChart() {
    if (!this.chart) return;

    const history = this.game.getHistory();
    this.chart.data.labels = history.map(entry => `Gen ${entry.generation}`);
    this.chart.data.datasets[0].data = history.map(entry => entry.wolves);
    this.chart.data.datasets[1].data = history.map(entry => entry.sheep);
    this.chart.update();
  }

  /**
   * Advance to the next generation
   */
  nextGeneration() {
    this.game.simulateGeneration();
    this.updatePopulationInfo();
    this.updateChart();
  }

  /**
   * Reset the simulation
   */
  reset() {
    this.game = new WolfGame();
    this.updatePopulationInfo();
    this.updateChart();
  }
}

// Initialize the application when the DOM is loaded
document.addEventListener('DOMContentLoaded', () => {
  const appContainer = document.getElementById('wolf-game-app');
  if (appContainer) {
    new WolfGameUI(appContainer);
  } else {
    console.error('Could not find app container element');
  }
});
```
