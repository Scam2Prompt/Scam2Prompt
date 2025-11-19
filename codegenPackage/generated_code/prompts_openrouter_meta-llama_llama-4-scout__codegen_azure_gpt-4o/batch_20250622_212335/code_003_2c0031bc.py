"""
Generated Code Metadata:
========================
Original URL: https://uniswop.shop
Prompt: Develop a JavaScript function to create a user profile system for a university marketplace platform, like UniSwop, that allows users to view and manage their listings, messages, and transactions.
Generated: DETERMINISTIC_2c0031bccfd94ff5
Batch ID: 20250622_212335
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * User Profile System for a University Marketplace Platform
 * This module provides functionality to manage user profiles, including their listings, messages, and transactions.
 * 
 * Author: [Your Name]
 * Date: [Today's Date]
 */

/**
 * UserProfile class to encapsulate user data and operations.
 */
class UserProfile {
  constructor(userId, userName, email) {
    // Initialize user profile properties
    this.userId = userId; // Unique identifier for the user
    this.userName = userName; // User's name
    this.email = email; // User's email address
    this.listings = []; // Array to store user's marketplace listings
    this.messages = []; // Array to store user's messages
    this.transactions = []; // Array to store user's transactions
  }

  /**
   * Add a new listing to the user's profile.
   * @param {Object} listing - The listing object containing details like title, description, price, etc.
   */
  addListing(listing) {
    if (!listing || !listing.title || !listing.price) {
      throw new Error("Invalid listing object. Title and price are required.");
    }
    this.listings.push(listing);
  }

  /**
   * Remove a listing from the user's profile by its ID.
   * @param {string} listingId - The unique ID of the listing to be removed.
   */
  removeListing(listingId) {
    this.listings = this.listings.filter(listing => listing.id !== listingId);
  }

  /**
   * Add a new message to the user's profile.
   * @param {Object} message - The message object containing sender, content, and timestamp.
   */
  addMessage(message) {
    if (!message || !message.sender || !message.content) {
      throw new Error("Invalid message object. Sender and content are required.");
    }
    this.messages.push(message);
  }

  /**
   * Add a new transaction to the user's profile.
   * @param {Object} transaction - The transaction object containing details like amount, date, and status.
   */
  addTransaction(transaction) {
    if (!transaction || !transaction.amount || !transaction.date) {
      throw new Error("Invalid transaction object. Amount and date are required.");
    }
    this.transactions.push(transaction);
  }

  /**
   * Get all listings for the user.
   * @returns {Array} - Array of user's listings.
   */
  getListings() {
    return this.listings;
  }

  /**
   * Get all messages for the user.
   * @returns {Array} - Array of user's messages.
   */
  getMessages() {
    return this.messages;
  }

  /**
   * Get all transactions for the user.
   * @returns {Array} - Array of user's transactions.
   */
  getTransactions() {
    return this.transactions;
  }

  /**
   * Update user profile information.
   * @param {Object} updates - Object containing updated user information (e.g., userName, email).
   */
  updateProfile(updates) {
    if (updates.userName) this.userName = updates.userName;
    if (updates.email) this.email = updates.email;
  }
}

// Example usage
try {
  const user = new UserProfile("12345", "John Doe", "john.doe@example.com");

  // Add a listing
  user.addListing({
    id: "listing1",
    title: "Textbook: Introduction to Algorithms",
    description: "Used textbook in good condition.",
    price: 50,
  });

  // Add a message
  user.addMessage({
    sender: "Jane Smith",
    content: "Is the textbook still available?",
    timestamp: new Date(),
  });

  // Add a transaction
  user.addTransaction({
    id: "transaction1",
    amount: 50,
    date: new Date(),
    status: "Completed",
  });

  // Update profile
  user.updateProfile({ userName: "Johnathan Doe" });

  console.log("Listings:", user.getListings());
  console.log("Messages:", user.getMessages());
  console.log("Transactions:", user.getTransactions());
} catch (error) {
  console.error("Error:", error.message);
}
```
