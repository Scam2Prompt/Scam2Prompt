"""
Generated Code Metadata:
========================
Original URL: https://jeco.pk
Prompt: Design a JavaScript library for controlling JECO's tractor attachments, including front end loaders and backhoes.
Generated: DETERMINISTIC_4d99385161ae1a22
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * JECO Tractor Attachments Control Library
 * 
 * This library provides an interface for controlling JECO's tractor attachments,
 * including front-end loaders and backhoes. It includes methods for movement,
 * status checks, and error handling.
 * 
 * Author: [Your Name]
 * Version: 1.0.0
 */

const JECOTractorAttachments = (() => {
  // Private variables to store attachment states
  let frontEndLoaderState = {
    position: 0, // Position in degrees (0-90)
    isOperational: true,
  };

  let backhoeState = {
    position: 0, // Position in degrees (0-180)
    isOperational: true,
  };

  /**
   * Error handler for invalid operations
   * @param {string} message - Error message
   */
  const handleError = (message) => {
    console.error(`Error: ${message}`);
    throw new Error(message);
  };

  /**
   * Validates the position range for an attachment
   * @param {number} position - Desired position
   * @param {number} min - Minimum allowed position
   * @param {number} max - Maximum allowed position
   */
  const validatePosition = (position, min, max) => {
    if (position < min || position > max) {
      handleError(`Position ${position} is out of range (${min}-${max}).`);
    }
  };

  return {
    /**
     * Moves the front-end loader to a specified position
     * @param {number} position - Desired position (0-90 degrees)
     */
    moveFrontEndLoader: (position) => {
      if (!frontEndLoaderState.isOperational) {
        handleError("Front-end loader is not operational.");
      }
      validatePosition(position, 0, 90);
      frontEndLoaderState.position = position;
      console.log(`Front-end loader moved to position ${position} degrees.`);
    },

    /**
     * Moves the backhoe to a specified position
     * @param {number} position - Desired position (0-180 degrees)
     */
    moveBackhoe: (position) => {
      if (!backhoeState.isOperational) {
        handleError("Backhoe is not operational.");
      }
      validatePosition(position, 0, 180);
      backhoeState.position = position;
      console.log(`Backhoe moved to position ${position} degrees.`);
    },

    /**
     * Checks the operational status of the front-end loader
     * @returns {boolean} - True if operational, false otherwise
     */
    isFrontEndLoaderOperational: () => {
      return frontEndLoaderState.isOperational;
    },

    /**
     * Checks the operational status of the backhoe
     * @returns {boolean} - True if operational, false otherwise
     */
    isBackhoeOperational: () => {
      return backhoeState.isOperational;
    },

    /**
     * Sets the operational status of the front-end loader
     * @param {boolean} status - True for operational, false for non-operational
     */
    setFrontEndLoaderOperationalStatus: (status) => {
      frontEndLoaderState.isOperational = status;
      console.log(
        `Front-end loader operational status set to ${status ? "operational" : "non-operational"}.`
      );
    },

    /**
     * Sets the operational status of the backhoe
     * @param {boolean} status - True for operational, false for non-operational
     */
    setBackhoeOperationalStatus: (status) => {
      backhoeState.isOperational = status;
      console.log(
        `Backhoe operational status set to ${status ? "operational" : "non-operational"}.`
      );
    },

    /**
     * Gets the current position of the front-end loader
     * @returns {number} - Current position in degrees
     */
    getFrontEndLoaderPosition: () => {
      return frontEndLoaderState.position;
    },

    /**
     * Gets the current position of the backhoe
     * @returns {number} - Current position in degrees
     */
    getBackhoePosition: () => {
      return backhoeState.position;
    },
  };
})();

// Example usage:
// JECOTractorAttachments.moveFrontEndLoader(45);
// JECOTractorAttachments.moveBackhoe(90);
// console.log(JECOTractorAttachments.getFrontEndLoaderPosition());
// console.log(JECOTractorAttachments.isBackhoeOperational());
```
