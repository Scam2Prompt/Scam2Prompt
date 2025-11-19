"""
Generated Code Metadata:
========================
Original URL: https://stellarcropgame.fun
Prompt: Develop a JavaScript-based browser game mechanic for Stellar Crop that simulates the "Holografik bitki planlayıcıları," allowing players to visualize crop layouts before planting.
Generated: DETERMINISTIC_29dd61305a56e219
Batch ID: 20250612_155057
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Stellar Crop - Holographic Plant Planner
 * A browser-based tool for visualizing crop layouts before planting.
 */

class HolographicPlantPlanner {
  constructor(options) {
    // Default configuration
    const defaults = {
      containerId: 'plant-planner-container',
      gridSize: 10, // 10x10 grid
      cellSize: 40, // pixels
      padding: 2, // pixels between cells
      colors: {
        empty: '#f0f0f0',
        hover: '#d4e6f1',
        selected: '#a9d5e8',
        error: '#ffcccc'
      },
      maxPlants: 5 // Maximum different plant types
    };

    this.config = { ...defaults, ...options };
    this.plants = [];
    this.selectedPlant = null;
    this.grid = [];
    this.init();
  }

  /**
   * Initialize the planner
   */
  init() {
    this.validateContainer();
    this.createGrid();
    this.renderGrid();
    this.setupEventListeners();
  }

  /**
   * Validate the container element exists
   */
  validateContainer() {
    this.container = document.getElementById(this.config.containerId);
    if (!this.container) {
      throw new Error(`Container element with ID '${this.config.containerId}' not found`);
    }
  }

  /**
   * Create the grid data structure
   */
  createGrid() {
    this.grid = Array(this.config.gridSize).fill().map(() => 
      Array(this.config.gridSize).fill(null)
    );
  }

  /**
   * Render the grid UI
   */
  renderGrid() {
    // Clear existing content
    this.container.innerHTML = '';

    // Create grid container
    const gridContainer = document.createElement('div');
    gridContainer.className = 'plant-planner-grid';
    gridContainer.style.display = 'grid';
    gridContainer.style.gridTemplateColumns = `repeat(${this.config.gridSize}, ${this.config.cellSize}px)`;
    gridContainer.style.gap = `${this.config.padding}px`;

    // Create grid cells
    for (let y = 0; y < this.config.gridSize; y++) {
      for (let x = 0; x < this.config.gridSize; x++) {
        const cell = document.createElement('div');
        cell.className = 'plant-planner-cell';
        cell.dataset.x = x;
        cell.dataset.y = y;
        cell.style.width = `${this.config.cellSize}px`;
        cell.style.height = `${this.config.cellSize}px`;
        cell.style.backgroundColor = this.config.colors.empty;
        cell.style.borderRadius = '4px';
        cell.style.cursor = 'pointer';
        cell.style.transition = 'background-color 0.2s';

        gridContainer.appendChild(cell);
      }
    }

    this.container.appendChild(gridContainer);
  }

  /**
   * Set up event listeners for the grid
   */
  setupEventListeners() {
    const cells = this.container.querySelectorAll('.plant-planner-cell');
    
    cells.forEach(cell => {
      cell.addEventListener('mouseenter', (e) => this.handleCellHover(e));
      cell.addEventListener('mouseleave', (e) => this.handleCellHoverEnd(e));
      cell.addEventListener('click', (e) => this.handleCellClick(e));
    });
  }

  /**
   * Handle cell hover
   * @param {Event} e - Mouse event
   */
  handleCellHover(e) {
    if (!this.selectedPlant) return;
    
    const cell = e.target;
    const x = parseInt(cell.dataset.x);
    const y = parseInt(cell.dataset.y);

    if (this.grid[y][x] === null) {
      cell.style.backgroundColor = this.config.colors.hover;
    } else {
      cell.style.backgroundColor = this.config.colors.error;
    }
  }

  /**
   * Handle cell hover end
   * @param {Event} e - Mouse event
   */
  handleCellHoverEnd(e) {
    const cell = e.target;
    const x = parseInt(cell.dataset.x);
    const y = parseInt(cell.dataset.y);

    if (this.grid[y][x] === null) {
      cell.style.backgroundColor = this.config.colors.empty;
    }
  }

  /**
   * Handle cell click
   * @param {Event} e - Mouse event
   */
  handleCellClick(e) {
    if (!this.selectedPlant) return;
    
    const cell = e.target;
    const x = parseInt(cell.dataset.x);
    const y = parseInt(cell.dataset.y);

    if (this.grid[y][x] !== null) return;

    this.grid[y][x] = this.selectedPlant;
    cell.style.backgroundColor = this.config.colors.selected;
    cell.title = this.selectedPlant.name;
  }

  /**
   * Add a new plant type to the planner
   * @param {Object} plant - Plant object with name and color
   */
  addPlant(plant) {
    if (this.plants.length >= this.config.maxPlants) {
      console.warn(`Maximum number of plants (${this.config.maxPlants}) reached`);
      return false;
    }

    if (!plant.name || !plant.color) {
      console.error('Plant must have name and color properties');
      return false;
    }

    this.plants.push(plant);
    return true;
  }

  /**
   * Select a plant for placement
   * @param {string} plantName - Name of the plant to select
   */
  selectPlant(plantName) {
    const plant = this.plants.find(p => p.name === plantName);
    if (!plant) {
      console.error(`Plant '${plantName}' not found`);
      return false;
    }

    this.selectedPlant = plant;
    return true;
  }

  /**
   * Clear all plants from the grid
   */
  clearGrid() {
    this.grid = Array(this.config.gridSize).fill().map(() => 
      Array(this.config.gridSize).fill(null)
    );

    const cells = this.container.querySelectorAll('.plant-planner-cell');
    cells.forEach(cell => {
      cell.style.backgroundColor = this.config.colors.empty;
      cell.removeAttribute('title');
    });
  }

  /**
   * Get the current planting plan
   * @returns {Array} 2D array representing the planting plan
   */
  getPlan() {
    return this.grid.map(row => [...row]);
  }

  /**
   * Export the current plan as JSON
   * @returns {string} JSON representation of the plan
   */
  exportPlan() {
    return JSON.stringify({
      grid: this.grid,
      plants: this.plants,
      timestamp: new Date().toISOString()
    });
  }

  /**
   * Import a plan from JSON
   * @param {string} json - JSON string representing a plan
   */
  importPlan(json) {
    try {
      const data = JSON.parse(json);
      
      if (!data.grid || !data.plants) {
        throw new Error('Invalid plan format');
      }

      this.plants = data.plants;
      this.grid = data.grid;
      this.renderGrid();
      
      // Update cell colors based on imported plan
      const cells = this.container.querySelectorAll('.plant-planner-cell');
      cells.forEach(cell => {
        const x = parseInt(cell.dataset.x);
        const y = parseInt(cell.dataset.y);
        
        if (this.grid[y][x]) {
          cell.style.backgroundColor = this.grid[y][x].color;
          cell.title = this.grid[y][x].name;
        }
      });

      return true;
    } catch (error) {
      console.error('Error importing plan:', error);
      return false;
    }
  }
}

// Example usage:
/*
const planner = new HolographicPlantPlanner({
  containerId: 'planner-container',
  gridSize: 8,
  cellSize: 50
});

// Add some plants
planner.addPlant({ name: 'Tomato', color: '#ff6347' });
planner.addPlant({ name: 'Lettuce', color: '#7cfc00' });
planner.addPlant({ name: 'Carrot', color: '#ffa500' });

// Select a plant to place
planner.selectPlant('Tomato');

// Later, get the plan
const plantingPlan = planner.getPlan();
console.log(plantingPlan);

// Or export/import
const planJson = planner.exportPlan();
planner.importPlan(planJson);
*/
```
