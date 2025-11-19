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
 * Azimut Flooring Interactive Floor Plan Library
 * Version: 1.0.0
 * 
 * Features:
 * - Interactive floor plan creation
 * - Support for Azimut's Antico filo and Magellano series
 * - Customizable flooring patterns and materials
 * - Responsive design for various devices
 */

class AzimutFloorPlan {
  /**
   * Initialize the floor plan
   * @param {Object} options - Configuration options
   * @param {HTMLElement} options.container - DOM element to render the floor plan
   * @param {string} [options.series='magellano'] - Flooring series ('magellano' or 'antico-filo')
   * @param {string} [options.defaultMaterial='wood'] - Default material type
   * @param {number} [options.width=800] - Floor plan width in pixels
   * @param {number} [options.height=600] - Floor plan height in pixels
   */
  constructor(options) {
    if (!options || !options.container) {
      throw new Error('Container element is required');
    }

    this.container = options.container;
    this.series = options.series || 'magellano';
    this.defaultMaterial = options.defaultMaterial || 'wood';
    this.width = options.width || 800;
    this.height = options.height || 600;
    this.materials = this._getMaterialsBySeries(this.series);
    this.rooms = [];
    this.selectedRoom = null;
    this.renderer = null;

    this._initializeRenderer();
    this._setupEventListeners();
  }

  /**
   * Initialize the renderer
   * @private
   */
  _initializeRenderer() {
    this.container.innerHTML = '';
    this.container.style.width = `${this.width}px`;
    this.container.style.height = `${this.height}px`;
    this.container.style.position = 'relative';
    this.container.style.border = '1px solid #ccc';
    this.container.style.overflow = 'hidden';

    this.renderer = document.createElement('div');
    this.renderer.className = 'azimut-floorplan-renderer';
    this.renderer.style.width = '100%';
    this.renderer.style.height = '100%';
    this.renderer.style.position = 'relative';

    this.container.appendChild(this.renderer);
  }

  /**
   * Get available materials by series
   * @param {string} series - Flooring series
   * @returns {Object} Available materials
   * @private
   */
  _getMaterialsBySeries(series) {
    const materials = {
      'magellano': {
        'wood': { name: 'Magellano Wood', texture: 'url(textures/magellano-wood.jpg)' },
        'stone': { name: 'Magellano Stone', texture: 'url(textures/magellano-stone.jpg)' },
        'concrete': { name: 'Magellano Concrete', texture: 'url(textures/magellano-concrete.jpg)' }
      },
      'antico-filo': {
        'wood': { name: 'Antico Filo Wood', texture: 'url(textures/antico-wood.jpg)' },
        'marble': { name: 'Antico Filo Marble', texture: 'url(textures/antico-marble.jpg)' },
        'terrazzo': { name: 'Antico Filo Terrazzo', texture: 'url(textures/antico-terrazzo.jpg)' }
      }
    };

    return materials[series] || materials['magellano'];
  }

  /**
   * Setup event listeners
   * @private
   */
  _setupEventListeners() {
    this.renderer.addEventListener('click', (e) => this._handleCanvasClick(e));
    this.renderer.addEventListener('mousemove', (e) => this._handleMouseMove(e));
  }

  /**
   * Handle canvas click event
   * @param {MouseEvent} e - Mouse event
   * @private
   */
  _handleCanvasClick(e) {
    const rect = this.renderer.getBoundingClientRect();
    const x = e.clientX - rect.left;
    const y = e.clientY - rect.top;

    if (!this.selectedRoom) {
      this._createRoom(x, y);
    } else {
      this._completeRoom(x, y);
    }
  }

  /**
   * Handle mouse move event
   * @param {MouseEvent} e - Mouse event
   * @private
   */
  _handleMouseMove(e) {
    if (!this.selectedRoom) return;

    const rect = this.renderer.getBoundingClientRect();
    const x = e.clientX - rect.left;
    const y = e.clientY - rect.top;

    this._updateRoomPreview(x, y);
  }

  /**
   * Create a new room
   * @param {number} x - X coordinate
   * @param {number} y - Y coordinate
   * @private
   */
  _createRoom(x, y) {
    this.selectedRoom = {
      startX: x,
      startY: y,
      endX: x,
      endY: y,
      element: document.createElement('div'),
      material: this.defaultMaterial
    };

    this.selectedRoom.element.className = 'azimut-room-preview';
    this.selectedRoom.element.style.position = 'absolute';
    this.selectedRoom.element.style.backgroundColor = 'rgba(0, 150, 255, 0.2)';
    this.selectedRoom.element.style.border = '2px dashed #0096ff';
    this.selectedRoom.element.style.pointerEvents = 'none';

    this.renderer.appendChild(this.selectedRoom.element);
  }

  /**
   * Update room preview during creation
   * @param {number} x - X coordinate
   * @param {number} y - Y coordinate
   * @private
   */
  _updateRoomPreview(x, y) {
    if (!this.selectedRoom) return;

    this.selectedRoom.endX = x;
    this.selectedRoom.endY = y;

    const left = Math.min(this.selectedRoom.startX, this.selectedRoom.endX);
    const top = Math.min(this.selectedRoom.startY, this.selectedRoom.endY);
    const width = Math.abs(this.selectedRoom.endX - this.selectedRoom.startX);
    const height = Math.abs(this.selectedRoom.endY - this.selectedRoom.startY);

    this.selectedRoom.element.style.left = `${left}px`;
    this.selectedRoom.element.style.top = `${top}px`;
    this.selectedRoom.element.style.width = `${width}px`;
    this.selectedRoom.element.style.height = `${height}px`;
  }

  /**
   * Complete room creation
   * @param {number} x - X coordinate
   * @param {number} y - Y coordinate
   * @private
   */
  _completeRoom(x, y) {
    this.selectedRoom.endX = x;
    this.selectedRoom.endY = y;

    const left = Math.min(this.selectedRoom.startX, this.selectedRoom.endX);
    const top = Math.min(this.selectedRoom.startY, this.selectedRoom.endY);
    const width = Math.abs(this.selectedRoom.endX - this.selectedRoom.startX);
    const height = Math.abs(this.selectedRoom.endY - this.selectedRoom.startY);

    if (width < 20 || height < 20) {
      this.renderer.removeChild(this.selectedRoom.element);
      this.selectedRoom = null;
      return;
    }

    const room = {
      id: `room-${Date.now()}`,
      x: left,
      y: top,
      width: width,
      height: height,
      material: this.selectedRoom.material,
      element: document.createElement('div')
    };

    room.element.className = 'azimut-room';
    room.element.style.position = 'absolute';
    room.element.style.left = `${room.x}px`;
    room.element.style.top = `${room.y}px`;
    room.element.style.width = `${room.width}px`;
    room.element.style.height = `${room.height}px`;
    room.element.style.backgroundImage = this.materials[room.material].texture;
    room.element.style.backgroundSize = 'cover';
    room.element.style.border = '1px solid #333';
    room.element.style.cursor = 'pointer';

    room.element.addEventListener('click', (e) => {
      e.stopPropagation();
      this._selectRoom(room);
    });

    this.renderer.removeChild(this.selectedRoom.element);
    this.renderer.appendChild(room.element);
    this.rooms.push(room);
    this.selectedRoom = null;
  }

  /**
   * Select a room
   * @param {Object} room - Room object
   * @private
   */
  _selectRoom(room) {
    // Deselect all rooms
    this.rooms.forEach(r => {
      r.element.style.boxShadow = 'none';
    });

    // Select the clicked room
    room.element.style.boxShadow = '0 0 0 3px rgba(0, 150, 255, 0.5)';
    this.selectedRoom = room;
  }

  /**
   * Change material for selected room
   * @param {string} material - Material type
   */
  changeMaterial(material) {
    if (!this.selectedRoom || !this.materials
