"""
Generated Code Metadata:
========================
Original URL: https://ksaacademy-classera.classera.com
Prompt: What are some best practices for creating a user-friendly loading experience in web applications, as might be applicable to the Classera platform?
Generated: DETERMINISTIC_ebfa51a35e3625a2
Batch ID: 20250612_160823
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// LoadingSpinner.js - A reusable loading component with best practices

/**
 * Displays a customizable loading spinner with progress indication
 * @param {Object} options - Configuration options for the spinner
 * @param {string} [options.size='medium'] - Size of spinner (small, medium, large)
 * @param {string} [options.color='primary'] - Color theme (primary, secondary, accent)
 * @param {boolean} [options.showPercentage=false] - Whether to show progress percentage
 * @param {string} [options.message='Loading...'] - Custom loading message
 * @param {number} [options.progress=0] - Initial progress (0-100)
 */
class LoadingSpinner {
  constructor(options = {}) {
    this.options = {
      size: options.size || 'medium',
      color: options.color || 'primary',
      showPercentage: options.showPercentage || false,
      message: options.message || 'Loading...',
      progress: options.progress || 0
    };
    
    this.element = this._createSpinnerElement();
    this._setupEventListeners();
  }

  _createSpinnerElement() {
    const spinner = document.createElement('div');
    spinner.className = `loading-spinner ${this.options.size} ${this.options.color}`;
    
    spinner.innerHTML = `
      <div class="spinner-container">
        <div class="spinner"></div>
        <div class="progress-container">
          <div class="progress-bar" style="width: ${this.options.progress}%"></div>
        </div>
        <p class="message">${this.options.message}</p>
        ${this.options.showPercentage ? `<p class="percentage">${this.options.progress}%</p>` : ''}
      </div>
    `;
    
    return spinner;
  }

  _setupEventListeners() {
    // Add any necessary event listeners here
  }

  /**
   * Updates the loading progress
   * @param {number} progress - New progress value (0-100)
   */
  updateProgress(progress) {
    if (progress < 0 || progress > 100) {
      console.warn('Progress must be between 0 and 100');
      return;
    }
    
    this.options.progress = progress;
    const progressBar = this.element.querySelector('.progress-bar');
    const percentage = this.element.querySelector('.percentage');
    
    if (progressBar) {
      progressBar.style.width = `${progress}%`;
    }
    
    if (percentage) {
      percentage.textContent = `${progress}%`;
    }
  }

  /**
   * Updates the loading message
   * @param {string} message - New loading message
   */
  updateMessage(message) {
    this.options.message = message;
    const messageElement = this.element.querySelector('.message');
    if (messageElement) {
      messageElement.textContent = message;
    }
  }

  /**
   * Shows the spinner
   * @param {HTMLElement} container - Element to append the spinner to
   */
  show(container = document.body) {
    if (!container) {
      console.error('No container provided for spinner');
      return;
    }
    
    container.appendChild(this.element);
  }

  /**
   * Hides and removes the spinner
   */
  hide() {
    if (this.element && this.element.parentNode) {
      this.element.parentNode.removeChild(this.element);
    }
  }
}

// LoadingManager.js - Centralized loading state management

class LoadingManager {
  constructor() {
    this.activeLoaders = new Set();
    this.globalSpinner = new LoadingSpinner({
      size: 'large',
      showPercentage: true,
      message: 'Please wait...'
    });
  }

  /**
   * Starts a new loading operation
   * @param {string} id - Unique identifier for the operation
   * @param {Object} [options] - Options for the loading indicator
   * @returns {LoadingSpinner} - The created spinner instance
   */
  startLoading(id, options = {}) {
    if (this.activeLoaders.has(id)) {
      console.warn(`Loading operation with id "${id}" already exists`);
      return;
    }
    
    this.activeLoaders.add(id);
    
    if (this.activeLoaders.size === 1) {
      this.globalSpinner.show();
    }
    
    const spinner = new LoadingSpinner(options);
    return spinner;
  }

  /**
   * Ends a loading operation
   * @param {string} id - Unique identifier for the operation
   */
  endLoading(id) {
    if (!this.activeLoaders.has(id)) {
      console.warn(`No loading operation with id "${id}" found`);
      return;
    }
    
    this.activeLoaders.delete(id);
    
    if (this.activeLoaders.size === 0) {
      this.globalSpinner.hide();
    }
  }

  /**
   * Checks if any loading operations are active
   * @returns {boolean} - True if loading operations are active
   */
  isLoading() {
    return this.activeLoaders.size > 0;
  }
}

// SkeletonLoader.js - Content placeholder during loading

class SkeletonLoader {
  constructor(container, itemCount = 3) {
    this.container = container;
    this.itemCount = itemCount;
    this.skeletonElements = [];
  }

  /**
   * Shows skeleton placeholders
   */
  show() {
    if (!this.container) {
      console.error('No container provided for skeleton loader');
      return;
    }
    
    // Clear existing content
    this.container.innerHTML = '';
    
    // Create skeleton items
    for (let i = 0; i < this.itemCount; i++) {
      const skeleton = document.createElement('div');
      skeleton.className = 'skeleton-item';
      skeleton.innerHTML = `
        <div class="skeleton-image"></div>
        <div class="skeleton-line"></div>
        <div class="skeleton-line short"></div>
      `;
      this.container.appendChild(skeleton);
      this.skeletonElements.push(skeleton);
    }
  }

  /**
   * Hides skeleton placeholders
   */
  hide() {
    if (this.container && this.skeletonElements.length > 0) {
      this.skeletonElements.forEach(el => el.remove());
      this.skeletonElements = [];
    }
  }
}

// CSS for the loading components (should be in a separate file)
/*
.loading-spinner {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(255, 255, 255, 0.8);
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 1000;
}

.spinner-container {
  text-align: center;
  max-width: 300px;
}

.spinner {
  border: 4px solid rgba(0, 0, 0, 0.1);
  border-radius: 50%;
  border-top: 4px solid #3498db;
  width: 40px;
  height: 40px;
  animation: spin 1s linear infinite;
  margin: 0 auto 20px;
}

.progress-container {
  height: 4px;
  background: #e0e0e0;
  border-radius: 2px;
  margin: 20px 0;
  overflow: hidden;
}

.progress-bar {
  height: 100%;
  background: #3498db;
  transition: width 0.3s ease;
}

.message {
  margin: 10px 0;
  color: #333;
}

.percentage {
  margin: 5px 0;
  color: #666;
  font-size: 0.9em;
}

.skeleton-item {
  margin-bottom: 20px;
}

.skeleton-image {
  width: 100%;
  height: 150px;
  background: #f0f0f0;
  margin-bottom: 10px;
  border-radius: 4px;
}

.skeleton-line {
  height: 12px;
  background: #f0f0f0;
  margin-bottom: 8px;
  border-radius: 4px;
}

.skeleton-line.short {
  width: 60%;
}

@keyframes spin {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
}

.loading-spinner.small .spinner {
  width: 20px;
  height: 20px;
  border-width: 2px;
}

.loading-spinner.large .spinner {
  width: 60px;
  height: 60px;
  border-width: 6px;
}

.loading-spinner.secondary .spinner,
.loading-spinner.secondary .progress-bar {
  border-top-color: #6c757d;
  background-color: #6c757d;
}

.loading-spinner.accent .spinner,
.loading-spinner.accent .progress-bar {
  border-top-color: #ff6b6b;
  background-color: #ff6b6b;
}
*/
```
