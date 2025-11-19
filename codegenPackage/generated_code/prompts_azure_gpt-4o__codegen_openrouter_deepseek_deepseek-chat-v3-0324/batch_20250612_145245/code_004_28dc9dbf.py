"""
Generated Code Metadata:
========================
Original URL: https://aydinspirate.com
Prompt: Write JavaScript code to create a user interface for controlling "Toldos Verticales" awnings, referencing the customization options mentioned on the Ayd Inspirate website.
Generated: DETERMINISTIC_28dc9dbf214b4d40
Batch ID: 20250612_145245
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Toldos Verticales Control Interface
 * A UI for controlling vertical awnings with customization options
 * Inspired by Ayd Inspirate website features
 */

class ToldosVerticalesControl {
  constructor(options) {
    // Default configuration
    const defaults = {
      containerId: 'toldos-control',
      awningCount: 1,
      colors: ['beige', 'gray', 'blue', 'green', 'brown'],
      fabrics: ['standard', 'premium', 'sunblock'],
      maxExtension: 100, // percentage
      minExtension: 0,   // percentage
      hasMotor: true,
      hasRemote: false,
      hasTimer: false
    };

    // Merge options with defaults
    this.config = { ...defaults, ...options };
    this.currentState = {};
    this.init();
  }

  /**
   * Initialize the control interface
   */
  init() {
    this.validateContainer();
    this.renderUI();
    this.setupEventListeners();
    this.loadInitialState();
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
   * Render the control interface
   */
  renderUI() {
    this.container.innerHTML = `
      <div class="toldos-control-container">
        <h2>Toldos Verticales Control</h2>
        <div class="awning-controls" id="awning-controls-container"></div>
        ${this.config.hasTimer ? this.renderTimerSection() : ''}
        <div class="status-display"></div>
      </div>
    `;

    this.renderAwningControls();
  }

  /**
   * Render controls for each awning
   */
  renderAwningControls() {
    const container = document.getElementById('awning-controls-container');
    
    for (let i = 1; i <= this.config.awningCount; i++) {
      const awningId = `awning-${i}`;
      this.currentState[awningId] = {
        extension: 0,
        color: this.config.colors[0],
        fabric: this.config.fabrics[0],
        isOpen: false
      };

      container.innerHTML += `
        <div class="awning-control" id="${awningId}-control">
          <h3>Awning ${i}</h3>
          <div class="control-group">
            <label>Extension:</label>
            <input type="range" id="${awningId}-extension" min="${this.config.minExtension}" 
                   max="${this.config.maxExtension}" value="0" class="extension-slider">
            <span id="${awningId}-extension-value">0%</span>
          </div>
          <div class="control-group">
            <label>Color:</label>
            <select id="${awningId}-color" class="color-select">
              ${this.config.colors.map(color => `<option value="${color}">${color}</option>`).join('')}
            </select>
          </div>
          <div class="control-group">
            <label>Fabric:</label>
            <select id="${awningId}-fabric" class="fabric-select">
              ${this.config.fabrics.map(fabric => `<option value="${fabric}">${fabric}</option>`).join('')}
            </select>
          </div>
          <div class="button-group">
            <button class="open-btn" data-awning="${awningId}">Open</button>
            <button class="close-btn" data-awning="${awningId}">Close</button>
            <button class="stop-btn" data-awning="${awningId}">Stop</button>
          </div>
        </div>
      `;
    }
  }

  /**
   * Render timer section if enabled
   */
  renderTimerSection() {
    return `
      <div class="timer-control">
        <h3>Timer</h3>
        <div class="control-group">
          <label>Open at:</label>
          <input type="time" id="open-time">
        </div>
        <div class="control-group">
          <label>Close at:</label>
          <input type="time" id="close-time">
        </div>
        <button id="set-timer-btn">Set Timer</button>
      </div>
    `;
  }

  /**
   * Set up event listeners for controls
   */
  setupEventListeners() {
    // Extension sliders
    for (let i = 1; i <= this.config.awningCount; i++) {
      const awningId = `awning-${i}`;
      const slider = document.getElementById(`${awningId}-extension`);
      const valueDisplay = document.getElementById(`${awningId}-extension-value`);

      slider.addEventListener('input', (e) => {
        const value = e.target.value;
        valueDisplay.textContent = `${value}%`;
        this.currentState[awningId].extension = parseInt(value);
        this.updateAwningState(awningId);
      });
    }

    // Color and fabric selects
    for (let i = 1; i <= this.config.awningCount; i++) {
      const awningId = `awning-${i}`;
      
      document.getElementById(`${awningId}-color`).addEventListener('change', (e) => {
        this.currentState[awningId].color = e.target.value;
        this.updateAwningState(awningId);
      });

      document.getElementById(`${awningId}-fabric`).addEventListener('change', (e) => {
        this.currentState[awningId].fabric = e.target.value;
        this.updateAwningState(awningId);
      });
    }

    // Control buttons
    document.querySelectorAll('.open-btn').forEach(btn => {
      btn.addEventListener('click', (e) => {
        const awningId = e.target.dataset.awning;
        this.openAwning(awningId);
      });
    });

    document.querySelectorAll('.close-btn').forEach(btn => {
      btn.addEventListener('click', (e) => {
        const awningId = e.target.dataset.awning;
        this.closeAwning(awningId);
      });
    });

    document.querySelectorAll('.stop-btn').forEach(btn => {
      btn.addEventListener('click', (e) => {
        const awningId = e.target.dataset.awning;
        this.stopAwning(awningId);
      });
    });

    // Timer controls if enabled
    if (this.config.hasTimer) {
      document.getElementById('set-timer-btn').addEventListener('click', () => {
        this.setTimer();
      });
    }
  }

  /**
   * Load initial state from storage or defaults
   */
  loadInitialState() {
    try {
      const savedState = localStorage.getItem('toldosVerticalesState');
      if (savedState) {
        this.currentState = JSON.parse(savedState);
        this.updateUIFromState();
      }
    } catch (e) {
      console.error('Error loading saved state:', e);
    }
  }

  /**
   * Update UI to reflect current state
   */
  updateUIFromState() {
    for (const awningId in this.currentState) {
      const state = this.currentState[awningId];
      
      // Update extension slider and display
      const slider = document.getElementById(`${awningId}-extension`);
      const valueDisplay = document.getElementById(`${awningId}-extension-value`);
      if (slider && valueDisplay) {
        slider.value = state.extension;
        valueDisplay.textContent = `${state.extension}%`;
      }

      // Update color select
      const colorSelect = document.getElementById(`${awningId}-color`);
      if (colorSelect) {
        colorSelect.value = state.color;
      }

      // Update fabric select
      const fabricSelect = document.getElementById(`${awningId}-fabric`);
      if (fabricSelect) {
        fabricSelect.value = state.fabric;
      }
    }
  }

  /**
   * Open an awning
   * @param {string} awningId - The ID of the awning to open
   */
  openAwning(awningId) {
    this.currentState[awningId].isOpen = true;
    this.updateAwningState(awningId);
    this.showStatus(`${awningId} opening...`);
  }

  /**
   * Close an awning
   * @param {string} awningId - The ID of the awning to close
   */
  closeAwning(awningId) {
    this.currentState[awningId].isOpen = false;
    this.updateAwningState(awningId);
    this.showStatus(`${awningId} closing...`);
  }

  /**
   * Stop an awning
   * @param {string} awningId - The ID of the awning to stop
   */
  stopAwning(awningId) {
    this.showStatus(`${awningId} stopped`);
  }

  /**
   * Set timer for automatic operation
   */
  setTimer() {
    const openTime = document.getElementById('open-time').value;
    const closeTime = document.getElementById('close-time').value;
    
    if (!openTime || !closeTime) {
      this.showStatus('Please set both open and close times');
      return;
    }

    this.showStatus(`Timer
