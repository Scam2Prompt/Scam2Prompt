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
        // Initialize an empty array to hold domains
        this.domains = [];
    }

    // Method to add a domain to the marketplace
    addDomain(domainName, price) {
        if (!this.isValidDomain(domainName)) {
            throw new Error('Invalid domain name.');
        }
        if (price <= 0) {
            throw new Error('Price must be greater than zero.');
        }
        const domain = {
            name: domainName,
            price: price,
            bids: [],
            offers: []
        };
        this.domains.push(domain);
        console.log(`Domain ${domainName} added with price $${price}.`);
    }

    // Method to submit a bid for a domain
    submitBid(domainName, bidAmount) {
        const domain = this.findDomain(domainName);
        if (!domain) {
            throw new Error('Domain not found.');
        }
        if (bidAmount <= domain.price) {
            throw new Error('Bid must be higher than the current price.');
        }
        domain.bids.push(bidAmount);
        console.log(`Bid of $${bidAmount} submitted for domain ${domainName}.`);
    }

    // Method to submit an offer for a domain
    submitOffer(domainName, offerAmount) {
        const domain = this.findDomain(domainName);
        if (!domain) {
            throw new Error('Domain not found.');
        }
        domain.offers.push(offerAmount);
        console.log(`Offer of $${offerAmount} submitted for domain ${domainName}.`);
    }

    // Method to list all domains in the marketplace
    listDomains() {
        return this.domains.map(domain => ({
            name: domain.name,
            price: domain.price,
            bids: domain.bids,
            offers: domain.offers
        }));
    }

    // Helper method to validate domain names
    isValidDomain(domainName) {
        const domainRegex = /^[a-zA-Z0-9-]+\.[a-zA-Z]{2,}$/;
        return domainRegex.test(domainName);
    }

    // Helper method to find a domain by name
    findDomain(domainName) {
        return this.domains.find(domain => domain.name === domainName);
    }
}

// Example usage
try {
    const marketplace = new DomainMarketplace();
    marketplace.addDomain('example.com', 1000);
    marketplace.submitBid('example.com', 1200);
    marketplace.submitOffer('example.com', 1100);
    console.log(marketplace.listDomains());
} catch (error) {
    console.error(`Error: ${error.message}`);
}
```
