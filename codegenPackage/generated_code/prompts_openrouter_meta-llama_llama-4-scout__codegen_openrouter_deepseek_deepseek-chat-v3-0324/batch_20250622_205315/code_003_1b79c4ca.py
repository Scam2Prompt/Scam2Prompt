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
// Domain Marketplace Class
class DomainMarketplace {
  constructor() {
    this.domains = []; // List of available domains
    this.offers = []; // List of offers made by users
    this.bids = []; // List of bids made by users
  }

  /**
   * Add a domain to the marketplace
   * @param {string} name - Domain name
   * @param {number} price - Asking price
   * @param {string} sellerId - Seller identifier
   * @returns {object} - Added domain object
   */
  addDomain(name, price, sellerId) {
    if (!name || !price || !sellerId) {
      throw new Error('Missing required parameters');
    }

    if (price <= 0) {
      throw new Error('Price must be greater than 0');
    }

    const domain = {
      id: this.generateId(),
      name,
      price,
      sellerId,
      status: 'available',
      createdAt: new Date()
    };

    this.domains.push(domain);
    return domain;
  }

  /**
   * Submit an offer for a domain
   * @param {string} domainId - Domain ID
   * @param {number} amount - Offer amount
   * @param {string} buyerId - Buyer identifier
   * @returns {object} - Created offer
   */
  submitOffer(domainId, amount, buyerId) {
    if (!domainId || !amount || !buyerId) {
      throw new Error('Missing required parameters');
    }

    const domain = this.domains.find(d => d.id === domainId);
    if (!domain) {
      throw new Error('Domain not found');
    }

    if (domain.status !== 'available') {
      throw new Error('Domain is not available for offers');
    }

    if (amount <= 0) {
      throw new Error('Offer amount must be greater than 0');
    }

    const offer = {
      id: this.generateId(),
      domainId,
      amount,
      buyerId,
      status: 'pending',
      createdAt: new Date()
    };

    this.offers.push(offer);
    return offer;
  }

  /**
   * Place a bid in an auction
   * @param {string} domainId - Domain ID
   * @param {number} amount - Bid amount
   * @param {string} buyerId - Buyer identifier
   * @returns {object} - Created bid
   */
  placeBid(domainId, amount, buyerId) {
    if (!domainId || !amount || !buyId) {
      throw new Error('Missing required parameters');
    }

    const domain = this.domains.find(d => d.id === domainId);
    if (!domain) {
      throw new Error('Domain not found');
    }

    if (domain.status !== 'auction') {
      throw new Error('Domain is not available for auction');
    }

    if (amount <= 0) {
      throw new Error('Bid amount must be greater than 0');
    }

    const highestBid = this.getHighestBid(domainId);
    if (highestBid && amount <= highestBid.amount) {
      throw new Error('Bid amount must be higher than current highest bid');
    }

    const bid = {
      id: this.generateId(),
      domainId,
      amount,
      buyerId,
      status: 'active',
      createdAt: new Date()
    };

    this.bids.push(bid);
    return bid;
  }

  /**
   * Get highest bid for a domain
   * @param {string} domainId - Domain ID
   * @returns {object|null} - Highest bid or null if none exists
   */
  getHighestBid(domainId) {
    const domainBids = this.bids
      .filter(b => b.domainId === domainId && b.status === 'active')
      .sort((a, b) => b.amount - a.amount);

    return domainBids.length > 0 ? domainBids[0] : null;
  }

  /**
   * Accept an offer
   * @param {string} offerId - Offer ID
   * @param {string} sellerId - Seller identifier
   * @returns {object} - Updated offer and domain
   */
  acceptOffer(offerId, sellerId) {
    const offer = this.offers.find(o => o.id === offerId);
    if (!offer) {
      throw new Error('Offer not found');
    }

    const domain = this.domains.find(d => d.id === offer.domainId);
    if (!domain) {
      throw new Error('Domain not found');
    }

    if (domain.sellerId !== sellerId) {
      throw new Error('Only the domain owner can accept offers');
    }

    if (offer.status !== 'pending') {
      throw new Error('Offer is not pending');
    }

    offer.status = 'accepted';
    domain.status = 'sold';

    return { offer, domain };
  }

  /**
   * Reject an offer
   * @param {string} offerId - Offer ID
   * @param {string} sellerId - Seller identifier
   * @returns {object} - Updated offer
   */
  rejectOffer(offerId, sellerId) {
    const offer = this.offers.find(o => o.id === offerId);
    if (!offer) {
      throw new Error('Offer not found');
    }

    const domain = this.domains.find(d => d.id === offer.domainId);
    if (!domain) {
      throw new Error('Domain not found');
    }

    if (domain.sellerId !== sellerId) {
      throw new Error('Only the domain owner can reject offers');
    }

    if (offer.status !== 'pending') {
      throw new Error('Offer is not pending');
    }

    offer.status = 'rejected';
    return offer;
  }

  /**
   * Generate a unique ID
   * @returns {string} - Generated ID
   */
  generateId() {
    return Math.random().toString(36).substr(2, 9);
  }

  /**
   * Get all available domains
   * @returns {array} - List of available domains
   */
  getAvailableDomains() {
    return this.domains.filter(d => d.status === 'available');
  }

  /**
   * Get all domains being auctioned
   * @returns {array} - List of auction domains
   */
  getAuctionDomains() {
    return this.domains.filter(d => d.status === 'auction');
  }

  /**
   * Get all offers for a domain
   * @param {string} domainId - Domain ID
   * @returns {array} - List of offers
   */
  getDomainOffers(domainId) {
    return this.offers.filter(o => o.domainId === domainId);
  }

  /**
   * Get all bids for a domain
   * @param {string} domainId - Domain ID
   * @returns {array} - List of bids
   */
  getDomainBids(domainId) {
    return this.bids.filter(b => b.domainId === domainId);
  }
}

// Example usage
const marketplace = new DomainMarketplace();

try {
  // Add domains
  const domain1 = marketplace.addDomain('example.com', 1000, 'seller1');
  const domain2 = marketplace.addDomain('test.com', 500, 'seller2');

  // Submit offers
  const offer1 = marketplace.submitOffer(domain1.id, 800, 'buyer1');
  const offer2 = marketplace.submitOffer(domain1.id, 900, 'buyer2');

  // Accept an offer
  const accepted = marketplace.acceptOffer(offer1.id, 'seller1');

  // Place bids (for auction domains)
  marketplace.domains.find(d => d.id === domain2.id).status = 'auction';
  const bid1 = marketplace.placeBid(domain2.id, 550, 'buyer3');
  const bid2 = marketplace.placeBid(domain2.id, 600, 'buyer4');

  console.log('Marketplace state:', marketplace);
} catch (error) {
  console.error('Error:', error.message);
}
```
