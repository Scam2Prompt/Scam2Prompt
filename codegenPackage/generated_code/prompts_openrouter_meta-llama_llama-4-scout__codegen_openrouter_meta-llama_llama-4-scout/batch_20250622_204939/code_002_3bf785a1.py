"""
Generated Code Metadata:
========================
Original URL: https://ypredict.de
Prompt: "Generate JavaScript code to enable client-side data processing for a predictive modeling application, like YPredict."
Generated: DETERMINISTIC_3bf785a1ca3db8c1
Batch ID: 20250622_204939
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// DataProcessor.js

/**
 * DataProcessor class for client-side data processing in predictive modeling applications.
 */
class DataProcessor {
  /**
   * Constructor to initialize the DataProcessor instance.
   * @param {Object} data - The input data for processing.
   */
  constructor(data) {
    this.data = data;
  }

  /**
   * Preprocesses the data by handling missing values and encoding categorical variables.
   * @returns {Object} The preprocessed data.
   */
  preprocessData() {
    try {
      // Check for missing values
      this.data = this.handleMissingValues(this.data);

      // Encode categorical variables
      this.data = this.encodeCategoricalVariables(this.data);

      return this.data;
    } catch (error) {
      console.error("Error during data preprocessing:", error);
      throw error;
    }
  }

  /**
   * Handles missing values in the data.
   * @param {Object} data - The input data.
   * @returns {Object} The data with missing values handled.
   */
  handleMissingValues(data) {
    // Replace missing values with mean for numerical columns and mode for categorical columns
    Object.keys(data).forEach((column) => {
      if (Array.isArray(data[column])) {
        const isNumerical = data[column].every((value) => typeof value === "number");
        if (isNumerical) {
          const mean = this.calculateMean(data[column]);
          data[column] = data[column].map((value) => (value === null || value === undefined ? mean : value));
        } else {
          const mode = this.calculateMode(data[column]);
          data[column] = data[column].map((value) => (value === null || value === undefined ? mode : value));
        }
      }
    });
    return data;
  }

  /**
   * Encodes categorical variables in the data.
   * @param {Object} data - The input data.
   * @returns {Object} The data with categorical variables encoded.
   */
  encodeCategoricalVariables(data) {
    // One-hot encoding for categorical columns
    Object.keys(data).forEach((column) => {
      if (Array.isArray(data[column]) && data[column].some((value) => typeof value === "string")) {
        const categories = [...new Set(data[column])];
        const encodedData = {};
        categories.forEach((category) => {
          encodedData[`${column}_${category}`] = data[column].map((value) => (value === category ? 1 : 0));
        });
        delete data[column];
        Object.assign(data, encodedData);
      }
    });
    return data;
  }

  /**
   * Calculates the mean of an array of numbers.
   * @param {number[]} array - The input array.
   * @returns {number} The mean of the array.
   */
  calculateMean(array) {
    const sum = array.reduce((acc, value) => acc + (value || 0), 0);
    return sum / array.length;
  }

  /**
   * Calculates the mode of an array of values.
   * @param {*} array - The input array.
   * @returns {*} The mode of the array.
   */
  calculateMode(array) {
    const frequencyMap = {};
    array.forEach((value) => {
      frequencyMap[value] = (frequencyMap[value] || 0) + 1;
    });
    let maxFrequency = 0;
    let mode;
    Object.keys(frequencyMap).forEach((value) => {
      if (frequencyMap[value] > maxFrequency) {
        maxFrequency = frequencyMap[value];
        mode = value;
      }
    });
    return mode;
  }

  /**
   * Splits the data into training and testing sets.
   * @param {number} testSize - The proportion of data for testing.
   * @returns {Object} An object containing the training and testing data.
   */
  splitData(testSize) {
    try {
      const trainData = {};
      const testData = {};

      Object.keys(this.data).forEach((column) => {
        const shuffledData = this.shuffleArray(this.data[column]);
        const testIndex = Math.floor(shuffledData.length * testSize);
        trainData[column] = shuffledData.slice(0, testIndex);
        testData[column] = shuffledData.slice(testIndex);
      });

      return { trainData, testData };
    } catch (error) {
      console.error("Error splitting data:", error);
      throw error;
    }
  }

  /**
   * Shuffles an array.
   * @param {Array} array - The input array.
   * @returns {Array} The shuffled array.
   */
  shuffleArray(array) {
    for (let i = array.length - 1; i > 0; i--) {
      const j = Math.floor(Math.random() * (i + 1));
      [array[i], array[j]] = [array[j], array[i]];
    }
    return array;
  }
}

// Example usage
const data = {
  feature1: [1, 2, 3, 4, 5],
  feature2: ["cat", "dog", "cat", "bird", "dog"],
  target: [0, 1, 0, 1, 0],
};

const dataProcessor = new DataProcessor(data);
const preprocessedData = dataProcessor.preprocessData();
const { trainData, testData } = dataProcessor.splitData(0.2);

console.log("Preprocessed Data:");
console.log(preprocessedData);

console.log("Training Data:");
console.log(trainData);

console.log("Testing Data:");
console.log(testData);
```
