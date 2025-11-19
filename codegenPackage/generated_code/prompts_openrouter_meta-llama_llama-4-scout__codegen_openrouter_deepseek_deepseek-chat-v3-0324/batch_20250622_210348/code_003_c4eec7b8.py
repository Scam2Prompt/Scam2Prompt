"""
Generated Code Metadata:
========================
Original URL: https://munakalati.org
Prompt: Develop a JavaScript function to create interactive animations for educational content, similar to those offered by Muna Kalati's platform.
Generated: DETERMINISTIC_c4eec7b8ef68b09f
Batch ID: 20250622_210348
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Creates interactive animations for educational content.
 * @class
 */
class EducationalAnimation {
  /**
   * @constructor
   * @param {string} containerId - The ID of the DOM element to contain the animation
   * @param {Object} options - Configuration options for the animation
   * @param {number} [options.width=800] - Width of the animation canvas
   * @param {number} [options.height=600] - Height of the animation canvas
   * @param {string} [options.backgroundColor='#ffffff'] - Background color of the canvas
   */
  constructor(containerId, options = {}) {
    this.container = document.getElementById(containerId);
    if (!this.container) {
      throw new Error(`Container element with ID '${containerId}' not found`);
    }

    this.options = {
      width: 800,
      height: 600,
      backgroundColor: '#ffffff',
      ...options
    };

    this.initCanvas();
    this.setupEventListeners();
    this.animationObjects = [];
    this.animationId = null;
    this.isPlaying = false;
  }

  /**
   * Initializes the canvas element
   * @private
   */
  initCanvas() {
    this.canvas = document.createElement('canvas');
    this.canvas.width = this.options.width;
    this.canvas.height = this.options.height;
    this.canvas.style.backgroundColor = this.options.backgroundColor;
    this.container.appendChild(this.canvas);
    this.ctx = this.canvas.getContext('2d');
  }

  /**
   * Sets up event listeners for interactivity
   * @private
   */
  setupEventListeners() {
    this.canvas.addEventListener('click', this.handleClick.bind(this));
    this.canvas.addEventListener('mousemove', this.handleMouseMove.bind(this));
  }

  /**
   * Handles click events on the canvas
   * @private
   * @param {MouseEvent} event - The mouse event
   */
  handleClick(event) {
    const rect = this.canvas.getBoundingClientRect();
    const x = event.clientX - rect.left;
    const y = event.clientY - rect.top;

    this.animationObjects.forEach(obj => {
      if (obj.isPointInPath && obj.isPointInPath(x, y)) {
        if (obj.onClick) obj.onClick();
      }
    });
  }

  /**
   * Handles mouse move events on the canvas
   * @private
   * @param {MouseEvent} event - The mouse event
   */
  handleMouseMove(event) {
    const rect = this.canvas.getBoundingClientRect();
    const x = event.clientX - rect.left;
    const y = event.clientY - rect.top;

    this.animationObjects.forEach(obj => {
      if (obj.isPointInPath && obj.isPointInPath(x, y)) {
        this.canvas.style.cursor = 'pointer';
        if (obj.onHover) obj.onHover();
      } else {
        this.canvas.style.cursor = 'default';
      }
    });
  }

  /**
   * Adds an object to the animation
   * @param {Object} obj - The animation object to add
   * @param {Function} obj.draw - Function to draw the object
   * @param {Function} [obj.update] - Function to update the object state
   * @param {Function} [obj.isPointInPath] - Function to check if point is in object
   * @param {Function} [obj.onClick] - Click handler for the object
   * @param {Function} [obj.onHover] - Hover handler for the object
   */
  addObject(obj) {
    if (!obj.draw) {
      throw new Error('Animation object must have a draw method');
    }
    this.animationObjects.push(obj);
  }

  /**
   * Starts the animation loop
   */
  play() {
    if (this.isPlaying) return;

    this.isPlaying = true;
    const animate = () => {
      this.ctx.clearRect(0, 0, this.canvas.width, this.canvas.height);
      
      this.animationObjects.forEach(obj => {
        if (obj.update) obj.update();
        obj.draw(this.ctx);
      });

      this.animationId = requestAnimationFrame(animate);
    };

    animate();
  }

  /**
   * Pauses the animation
   */
  pause() {
    if (!this.isPlaying) return;
    
    cancelAnimationFrame(this.animationId);
    this.isPlaying = false;
  }

  /**
   * Resets the animation to its initial state
   */
  reset() {
    this.pause();
    this.ctx.clearRect(0, 0, this.canvas.width, this.canvas.height);
    this.animationObjects.forEach(obj => {
      if (obj.reset) obj.reset();
    });
  }

  /**
   * Removes all animation objects and cleans up resources
   */
  destroy() {
    this.pause();
    this.container.removeChild(this.canvas);
    this.canvas.removeEventListener('click', this.handleClick);
    this.canvas.removeEventListener('mousemove', this.handleMouseMove);
    this.animationObjects = [];
  }
}

// Example usage:
/*
const animation = new EducationalAnimation('animation-container', {
  width: 800,
  height: 600,
  backgroundColor: '#f0f0f0'
});

// Add a simple bouncing ball
animation.addObject({
  x: 100,
  y: 100,
  radius: 30,
  dx: 2,
  dy: 2,
  color: '#3498db',
  
  draw: function(ctx) {
    ctx.beginPath();
    ctx.arc(this.x, this.y, this.radius, 0, Math.PI * 2);
    ctx.fillStyle = this.color;
    ctx.fill();
    ctx.closePath();
  },
  
  update: function() {
    if (this.x + this.radius > animation.options.width || this.x - this.radius < 0) {
      this.dx = -this.dx;
    }
    if (this.y + this.radius > animation.options.height || this.y - this.radius < 0) {
      this.dy = -this.dy;
    }
    this.x += this.dx;
    this.y += this.dy;
  },
  
  isPointInPath: function(x, y) {
    const distance = Math.sqrt((x - this.x) ** 2 + (y - this.y) ** 2);
    return distance <= this.radius;
  },
  
  onClick: function() {
    this.color = `#${Math.floor(Math.random()*16777215).toString(16)}`;
  },
  
  onHover: function() {
    this.radius = 35;
    setTimeout(() => { this.radius = 30; }, 200);
  }
});

animation.play();
*/
```
