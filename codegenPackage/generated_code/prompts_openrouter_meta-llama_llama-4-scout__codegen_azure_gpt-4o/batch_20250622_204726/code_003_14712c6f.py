"""
Generated Code Metadata:
========================
Original URL: https://azimutfloor.com
Prompt: Develop a JavaScript library for creating interactive floor plans, incorporating Azimut Flooring's innovative concepts and technology, such as those featured in their Antico filo and Magellano series.
Generated: DETERMINISTIC_14712c6f8460ee43
Batch ID: 20250622_204726
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * AzimutFloorPlan.js
 * A JavaScript library for creating interactive floor plans, inspired by Azimut Flooring's innovative concepts.
 * Supports features like Antico Filo and Magellano series designs.
 * 
 * Author: [Your Name]
 * Version: 1.0.0
 * License: MIT
 */

class AzimutFloorPlan {
  /**
   * Constructor to initialize the floor plan.
   * @param {HTMLElement} container - The DOM element where the floor plan will be rendered.
   * @param {Object} options - Configuration options for the floor plan.
   */
  constructor(container, options = {}) {
    if (!container || !(container instanceof HTMLElement)) {
      throw new Error("A valid container element must be provided.");
    }

    // Default options
    this.options = {
      width: options.width || 800,
      height: options.height || 600,
      gridSize: options.gridSize || 20,
      theme: options.theme || "light", // Themes: light, dark
    };

    this.container = container;
    this.container.style.position = "relative";
    this.container.style.width = `${this.options.width}px`;
    this.container.style.height = `${this.options.height}px`;
    this.container.style.border = "1px solid #ccc";
    this.container.style.overflow = "hidden";
    this.container.style.backgroundColor =
      this.options.theme === "dark" ? "#333" : "#fff";

    this.elements = []; // Store floor plan elements
    this.init();
  }

  /**
   * Initialize the floor plan with a grid.
   */
  init() {
    this.drawGrid();
  }

  /**
   * Draws the grid on the floor plan.
   */
  drawGrid() {
    const { width, height, gridSize } = this.options;

    const gridCanvas = document.createElement("canvas");
    gridCanvas.width = width;
    gridCanvas.height = height;
    gridCanvas.style.position = "absolute";
    gridCanvas.style.top = "0";
    gridCanvas.style.left = "0";

    const ctx = gridCanvas.getContext("2d");
    ctx.strokeStyle = "#ddd";
    ctx.lineWidth = 0.5;

    // Draw vertical lines
    for (let x = 0; x <= width; x += gridSize) {
      ctx.beginPath();
      ctx.moveTo(x, 0);
      ctx.lineTo(x, height);
      ctx.stroke();
    }

    // Draw horizontal lines
    for (let y = 0; y <= height; y += gridSize) {
      ctx.beginPath();
      ctx.moveTo(0, y);
      ctx.lineTo(width, y);
      ctx.stroke();
    }

    this.container.appendChild(gridCanvas);
  }

  /**
   * Adds a flooring element to the floor plan.
   * @param {Object} element - The flooring element to add.
   * @param {string} element.type - The type of flooring (e.g., "AnticoFilo", "Magellano").
   * @param {number} element.x - The x-coordinate of the element.
   * @param {number} element.y - The y-coordinate of the element.
   * @param {number} element.width - The width of the element.
   * @param {number} element.height - The height of the element.
   * @param {string} element.color - The color of the element.
   */
  addElement(element) {
    const { type, x, y, width, height, color } = element;

    if (!type || !x || !y || !width || !height || !color) {
      throw new Error("All element properties must be provided.");
    }

    const flooringElement = document.createElement("div");
    flooringElement.style.position = "absolute";
    flooringElement.style.left = `${x}px`;
    flooringElement.style.top = `${y}px`;
    flooringElement.style.width = `${width}px`;
    flooringElement.style.height = `${height}px`;
    flooringElement.style.backgroundColor = color;
    flooringElement.style.border = "1px solid #000";
    flooringElement.setAttribute("data-type", type);

    // Add hover effect for interactivity
    flooringElement.addEventListener("mouseenter", () => {
      flooringElement.style.opacity = "0.8";
    });
    flooringElement.addEventListener("mouseleave", () => {
      flooringElement.style.opacity = "1";
    });

    this.container.appendChild(flooringElement);
    this.elements.push(flooringElement);
  }

  /**
   * Clears all elements from the floor plan.
   */
  clearElements() {
    this.elements.forEach((element) => {
      this.container.removeChild(element);
    });
    this.elements = [];
  }

  /**
   * Exports the current floor plan configuration as JSON.
   * @returns {string} - The JSON string representing the floor plan.
   */
  exportToJSON() {
    const exportedElements = this.elements.map((element) => {
      return {
        type: element.getAttribute("data-type"),
        x: parseInt(element.style.left, 10),
        y: parseInt(element.style.top, 10),
        width: parseInt(element.style.width, 10),
        height: parseInt(element.style.height, 10),
        color: element.style.backgroundColor,
      };
    });

    return JSON.stringify(exportedElements, null, 2);
  }

  /**
   * Imports a floor plan configuration from JSON.
   * @param {string} json - The JSON string representing the floor plan.
   */
  importFromJSON(json) {
    try {
      const elements = JSON.parse(json);
      this.clearElements();
      elements.forEach((element) => this.addElement(element));
    } catch (error) {
      console.error("Failed to import floor plan from JSON:", error);
    }
  }
}

// Example usage:
// const container = document.getElementById("floor-plan-container");
// const floorPlan = new AzimutFloorPlan(container, { width: 1000, height: 800, theme: "dark" });
// floorPlan.addElement({ type: "AnticoFilo", x: 50, y: 50, width: 100, height: 100, color: "#ffcc00" });
// console.log(floorPlan.exportToJSON());
```

This code defines a JavaScript library for creating interactive floor plans, inspired by Azimut Flooring's concepts. It includes features like grid rendering, adding/removing flooring elements, and importing/exporting configurations as JSON.
