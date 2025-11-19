"""
Generated Code Metadata:
========================
Original URL: https://letz.dev
Prompt: Generate a JavaScript code snippet to create a simple domain name marketplace similar to Sedo, including features like bidding and offer submission.
Generated: DETERMINISTIC_1b79c4caf3c4623a
Batch ID: 20250622_205315
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// domainMarketplace.js

/**
 * Represents a Domain Listing in the marketplace.
 */
class DomainListing {
  /**
   * Creates a new DomainListing.
   * @param {string} name - The domain name.
   * @param {number} price - The initial price of the domain.
   */
  constructor(name, price) {
    this.name = name;
    this.price = price;
    this.bids = [];
    this.offers = [];
  }

  /**
   * Places a bid on the domain.
   * @param {string} bidder - The bidder's name.
   * @param {number} amount - The bid amount.
   */
  placeBid(bidder, amount) {
    if (amount <= this.price) {
      throw new Error('Bid amount must be greater than the current price.');
    }
    this.bids.push({ bidder, amount });
    this.price = amount;
  }

  /**
   * Submits an offer on the domain.
   * @param {string} offeror - The offeror's name.
   * @param {number} amount - The offer amount.
   */
  submitOffer(offeror, amount) {
    this.offers.push({ offeror, amount });
  }

  /**
   * Lists all bids on the domain.
   * @returns {Array} - A list of bids.
   */
  listBids() {
    return this.bids;
  }

  /**
   * Lists all offers on the domain.
   * @returns {Array} - A list of offers.
   */
  listOffers() {
    return this.offers;
  }
}

/**
 * Represents the Domain Marketplace.
 */
class DomainMarketplace {
  /**
   * Creates a new DomainMarketplace.
   */
  constructor() {
    this.domains = {};
  }

  /**
   * Lists a domain in the marketplace.
   * @param {string} name - The domain name.
   * @param {number} price - The initial price of the domain.
   */
  listDomain(name, price) {
    if (this.domains[name]) {
      throw new Error('Domain already listed.');
    }
    this.domains[name] = new DomainListing(name, price);
  }

  /**
   * Places a bid on a domain.
   * @param {string} name - The domain name.
   * @param {string} bidder - The bidder's name.
   * @param {number} amount - The bid amount.
   */
  placeBid(name, bidder, amount) {
    if (!this.domains[name]) {
      throw new Error('Domain not found.');
    }
    this.domains[name].placeBid(bidder, amount);
  }

  /**
   * Submits an offer on a domain.
   * @param {string} name - The domain name.
   * @param {string} offeror - The offeror's name.
   * @param {number} amount - The offer amount.
   */
  submitOffer(name, offeror, amount) {
    if (!this.domains[name]) {
      throw new Error('Domain not found.');
    }
    this.domains[name].submitOffer(offeror, amount);
  }

  /**
   * Lists all bids on a domain.
   * @param {string} name - The domain name.
   * @returns {Array} - A list of bids.
   */
  listBids(name) {
    if (!this.domains[name]) {
      throw new Error('Domain not found.');
    }
    return this.domains[name].listBids();
  }

  /**
   * Lists all offers on a domain.
   * @param {string} name - The domain name.
   * @returns {Array} - A list of offers.
   */
  listOffers(name) {
    if (!this.domains[name]) {
      throw new Error('Domain not found.');
    }
    return this.domains[name].listOffers();
  }
}

// Example usage:
function main() {
  const marketplace = new DomainMarketplace();

  try {
    marketplace.listDomain('example.com', 1000);
    marketplace.placeBid('example.com', 'John Doe', 1200);
    marketplace.submitOffer('example.com', 'Jane Doe', 1500);
    console.log(marketplace.listBids('example.com'));
    console.log(marketplace.listOffers('example.com'));
  } catch (error) {
    console.error(error.message);
  }
}

main();
```
