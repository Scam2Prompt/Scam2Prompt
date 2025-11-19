"""
Generated Code Metadata:
========================
Original URL: https://codyalt.com
Prompt: Develop a JavaScript function to display motivational quotes or strategies for entrepreneurship, inspired by Cody Alt's "The Infinite Game" newsletter.
Generated: DETERMINISTIC_39e1d41464d52d0e
Batch ID: 20250612_145436
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * MotivationalQuoteGenerator - A utility to display motivational quotes and strategies for entrepreneurship.
 * Inspired by Cody Alt's "The Infinite Game" newsletter.
 */
class MotivationalQuoteGenerator {
  constructor() {
    this.quotes = [
      {
        text: "Entrepreneurship is not about playing finite games with clear winners and losers. It's about playing the infinite game where the goal is to keep playing.",
        author: "Cody Alt",
        category: "Mindset"
      },
      {
        text: "The most successful entrepreneurs focus on creating value, not just capturing it.",
        author: "Cody Alt",
        category: "Strategy"
      },
      {
        text: "Your competition isn't other businesses—it's the status quo. Focus on changing behavior, not beating competitors.",
        author: "Cody Alt",
        category: "Competition"
      },
      {
        text: "Sustainable growth comes from building systems, not just chasing tactics.",
        author: "Cody Alt",
        category: "Growth"
      },
      {
        text: "The infinite player understands that the game is never over, so they build for the long term.",
        author: "Cody Alt",
        category: "Long-term Thinking"
      }
    ];
  }

  /**
   * Get a random motivational quote
   * @returns {Object} A quote object with text, author, and category
   */
  getRandomQuote() {
    if (!this.quotes || this.quotes.length === 0) {
      throw new Error("No quotes available");
    }
    const randomIndex = Math.floor(Math.random() * this.quotes.length);
    return this.quotes[randomIndex];
  }

  /**
   * Get all quotes from a specific category
   * @param {string} category - The category to filter by
   * @returns {Array} Array of quote objects matching the category
   */
  getQuotesByCategory(category) {
    if (!category || typeof category !== 'string') {
      throw new Error("Invalid category provided");
    }
    
    const filteredQuotes = this.quotes.filter(quote => 
      quote.category.toLowerCase() === category.toLowerCase()
    );
    
    if (filteredQuotes.length === 0) {
      throw new Error(`No quotes found in category: ${category}`);
    }
    
    return filteredQuotes;
  }

  /**
   * Display a formatted random quote in the console
   */
  displayRandomQuote() {
    try {
      const quote = this.getRandomQuote();
      console.log(`"${quote.text}"\n- ${quote.author} (${quote.category})`);
    } catch (error) {
      console.error("Error displaying quote:", error.message);
    }
  }

  /**
   * Display all quotes from a category in the console
   * @param {string} category - The category to display
   */
  displayQuotesByCategory(category) {
    try {
      const quotes = this.getQuotesByCategory(category);
      console.log(`=== ${category.toUpperCase()} QUOTES ===`);
      quotes.forEach(quote => {
        console.log(`\n"${quote.text}"\n- ${quote.author}\n`);
      });
    } catch (error) {
      console.error("Error displaying quotes:", error.message);
    }
  }
}

// Example usage:
// const quoteGenerator = new MotivationalQuoteGenerator();
// quoteGenerator.displayRandomQuote();
// quoteGenerator.displayQuotesByCategory("Mindset");
```
