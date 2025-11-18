"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://polkadots.work
Prompt: Create JavaScript code to reverse text strings using a browser-based tool, as described in the "テキスト反転ツール" section of コピーツールラボ.
Generated: DETERMINISTIC_d3654ebc918110cc
Batch ID: 20250612_151239
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Reverse Text Tool - Browser-Based Implementation
// Created following best practices and production-ready standards

// HTML Structure:
// <div id="reverse-tool">
//   <textarea id="input-text" placeholder="Enter text here..."></textarea>
//   <button id="reverse-button">Reverse Text</button>
//   <textarea id="output-text" readonly placeholder="Reversed text will appear here..."></textarea>
// </div>

// JavaScript Code:

document.addEventListener("DOMContentLoaded", () => {
  // Get references to HTML elements
  const inputText = document.getElementById("input-text");
  const reverseButton = document.getElementById("reverse-button");
  const outputText = document.getElementById("output-text");

  /**
   * Reverse a given text string.
   * @param {string} text - The text to be reversed.
   * @returns {string} - The reversed text.
   */
  function reverseString(text) {
    try {
      // Validate input type
      if (typeof text !== "string") {
        throw new Error("Invalid input: Only strings can be reversed.");
      }
      // Reverse the string using array split/reverse/join methods
      return text.split("").reverse().join("");
    } catch (error) {
      console.error("Error reversing text:", error.message);
      return ""; // Return an empty string on error
    }
  }

  /**
   * Handle the reverse button click event.
   */
  function handleReverseButtonClick() {
    // Get the input value
    const userInput = inputText.value;

    // Reverse the input string
    const reversedText = reverseString(userInput);

    // Display the reversed text in the output textarea
    outputText.value = reversedText;
  }

  // Attach event listener to the reverse button
  reverseButton.addEventListener("click", handleReverseButtonClick);
});

```
