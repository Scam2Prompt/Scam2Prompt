"""
Generated Code Metadata:
========================
Original URL: https://stellarcropgame.fun
Prompt: Write a JavaScript function to implement the "Cloudra Horizon" mechanic in Stellar Crop, where players manage floating islands with dynamic wind patterns and resource distribution.
Generated: DETERMINISTIC_00d840d1b656ffec
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
 * Cloudra Horizon - Stellar Crop Floating Island Management System
 * 
 * Manages floating islands with dynamic wind patterns and resource distribution.
 */
class CloudraHorizon {
  /**
   * Initialize the Cloudra Horizon system
   * @param {Object} config - Configuration object
   * @param {number} config.islandCount - Number of floating islands
   * @param {number} config.windIntensity - Base wind intensity (0-100)
   * @param {Object} config.resources - Initial resource distribution
   */
  constructor(config) {
    this.validateConfig(config);
    
    this.islands = [];
    this.windPatterns = [];
    this.resourceDistribution = {};
    this.timeCycle = 0;
    
    this.initializeIslands(config.islandCount);
    this.initializeResources(config.resources);
    this.initializeWindPatterns(config.windIntensity);
  }

  /**
   * Validate configuration parameters
   * @param {Object} config - Configuration object
   * @throws {Error} If configuration is invalid
   */
  validateConfig(config) {
    if (!config || typeof config !== 'object') {
      throw new Error('Invalid configuration: must be an object');
    }
    
    const required = ['islandCount', 'windIntensity', 'resources'];
    for (const field of required) {
      if (!(field in config)) {
        throw new Error(`Missing required configuration field: ${field}`);
      }
    }
    
    if (config.islandCount <= 0 || !Number.isInteger(config.islandCount)) {
      throw new Error('islandCount must be a positive integer');
    }
    
    if (config.windIntensity < 0 || config.windIntensity > 100) {
      throw new Error('windIntensity must be between 0 and 100');
    }
  }

  /**
   * Initialize floating islands
   * @param {number} count - Number of islands to create
   */
  initializeIslands(count) {
    for (let i = 0; i < count; i++) {
      this.islands.push({
        id: i,
        position: {
          x: Math.random() * 1000,
          y: Math.random() * 1000,
          z: Math.random() * 500 + 100
        },
        stability: 100,
        resources: {},
        connections: []
      });
    }
  }

  /**
   * Initialize resource distribution
   * @param {Object} resources - Initial resource quantities
   */
  initializeResources(resources) {
    this.resourceDistribution = { ...resources };
    this.distributeResources();
  }

  /**
   * Distribute resources randomly across islands
   */
  distributeResources() {
    const resourceTypes = Object.keys(this.resourceDistribution);
    
    for (const island of this.islands) {
      island.resources = {};
      
      for (const resource of resourceTypes) {
        if (Math.random() > 0.7) { // 30% chance to have this resource
          const maxAmount = this.resourceDistribution[resource];
          island.resources[resource] = Math.floor(Math.random() * maxAmount * 0.3);
        }
      }
    }
  }

  /**
   * Initialize wind patterns
   * @param {number} baseIntensity - Base wind intensity
   */
  initializeWindPatterns(baseIntensity) {
    const directions = ['north', 'south', 'east', 'west', 'northeast', 'northwest', 'southeast', 'southwest'];
    
    for (let i = 0; i < 4; i++) {
      this.windPatterns.push({
        direction: directions[Math.floor(Math.random() * directions.length)],
        intensity: baseIntensity * (0.8 + Math.random() * 0.4), // ±20% variation
        duration: Math.floor(Math.random() * 10) + 5 // 5-15 time units
      });
    }
  }

  /**
   * Update the system state for the next time cycle
   */
  update() {
    this.timeCycle++;
    this.updateWindPatterns();
    this.updateIslandPositions();
    this.updateResourceAvailability();
    this.updateIslandConnections();
  }

  /**
   * Update wind patterns (rotate and modify)
   */
  updateWindPatterns() {
    // Every 5 cycles, add a new wind pattern
    if (this.timeCycle % 5 === 0) {
      const directions = ['north', 'south', 'east', 'west', 'northeast', 'northwest', 'southeast', 'southwest'];
      this.windPatterns.push({
        direction: directions[Math.floor(Math.random() * directions.length)],
        intensity: Math.random() * 100,
        duration: Math.floor(Math.random() * 10) + 5
      });
    }

    // Update existing patterns
    for (let i = this.windPatterns.length - 1; i >= 0; i--) {
      this.windPatterns[i].duration--;
      
      if (this.windPatterns[i].duration <= 0) {
        this.windPatterns.splice(i, 1);
      } else {
        // Randomly fluctuate intensity
        this.windPatterns[i].intensity *= (0.95 + Math.random() * 0.1);
      }
    }
  }

  /**
   * Update island positions based on wind patterns
   */
  updateIslandPositions() {
    const windVectors = this.calculateWindVectors();
    
    for (let i = 0; i < this.islands.length; i++) {
      const island = this.islands[i];
      const windEffect = windVectors[i % windVectors.length];
      
      // Apply wind effect with some randomness
      island.position.x += windEffect.x * (0.8 + Math.random() * 0.4);
      island.position.y += windEffect.y * (0.8 + Math.random() * 0.4);
      
      // Apply slight vertical movement
      island.position.z += (Math.random() - 0.5) * 2;
      
      // Decrease stability based on wind intensity
      const totalIntensity = windVectors.reduce((sum, vec) => sum + Math.sqrt(vec.x**2 + vec.y**2), 0);
      island.stability = Math.max(0, island.stability - totalIntensity * 0.01);
    }
  }

  /**
   * Calculate wind vectors for each island
   * @returns {Array} Array of wind vectors {x, y}
   */
  calculateWindVectors() {
    const vectors = [];
    
    for (const pattern of this.windPatterns) {
      let x = 0, y = 0;
      
      switch (pattern.direction) {
        case 'north': y = -pattern.intensity; break;
        case 'south': y = pattern.intensity; break;
        case 'east': x = pattern.intensity; break;
        case 'west': x = -pattern.intensity; break;
        case 'northeast': 
          x = pattern.intensity * 0.707; 
          y = -pattern.intensity * 0.707; 
          break;
        case 'northwest': 
          x = -pattern.intensity * 0.707; 
          y = -pattern.intensity * 0.707; 
          break;
        case 'southeast': 
          x = pattern.intensity * 0.707; 
          y = pattern.intensity * 0.707; 
          break;
        case 'southwest': 
          x = -pattern.intensity * 0.707; 
          y = pattern.intensity * 0.707; 
          break;
      }
      
      vectors.push({ x, y });
    }
    
    return vectors;
  }

  /**
   * Update resource availability based on wind patterns
   */
  updateResourceAvailability() {
    const resourceTypes = Object.keys(this.resourceDistribution);
    const windIntensity = this.windPatterns.reduce((sum, p) => sum + p.intensity, 0) / this.windPatterns.length;
    
    for (const island of this.islands) {
      for (const resource of resourceTypes) {
        // Resources grow slightly based on stability
        if (island.resources[resource] !== undefined) {
          const growthRate = 1 + (island.stability / 100) * 0.05;
          island.resources[resource] = Math.min(
            this.resourceDistribution[resource],
            island.resources[resource] * growthRate
          );
        }
        
        // Chance to spread resources to nearby islands
        if (windIntensity > 30 && Math.random() > 0.9) {
          this.spreadResources(island, resource);
        }
      }
    }
  }

  /**
   * Spread resources from one island to connected islands
   * @param {Object} sourceIsland - Source island
   * @param {string} resource - Resource type to spread
   */
  spreadResources(sourceIsland, resource) {
    if (!sourceIsland.resources[resource] || sourceIsland.resources[resource] < 10) {
