"""
Generated Code Metadata:
========================
Original URL: https://rapala.tc
Prompt: Create a JavaScript code example that allows users to submit travel inquiries and receive personalized package suggestions, reflecting the approach of Rapala Travel Concierge.
Generated: DETERMINISTIC_5e0e406a0c5b007f
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Travel Concierge Service for Rapala Travel
class TravelConcierge {
  constructor() {
    this.inquiries = [];
    this.packages = {
      beach: [
        { name: "Tropical Paradise", price: 1200, duration: "7 days" },
        { name: "Coastal Retreat", price: 850, duration: "5 days" }
      ],
      mountain: [
        { name: "Alpine Adventure", price: 1500, duration: "10 days" },
        { name: "Ski Getaway", price: 2000, duration: "7 days" }
      ],
      city: [
        { name: "Metropolitan Explorer", price: 900, duration: "5 days" },
        { name: "Cultural Immersion", price: 1100, duration: "7 days" }
      ]
    };
  }

  /**
   * Submit a travel inquiry
   * @param {Object} inquiry - Travel inquiry details
   * @param {string} inquiry.name - Client name
   * @param {string} inquiry.email - Client email
   * @param {string} inquiry.destinationType - Preferred destination type
   * @param {string} inquiry.budget - Budget range
   * @param {string} inquiry.travelDates - Travel dates
   * @returns {Object} - Confirmation of submission
   */
  submitInquiry(inquiry) {
    if (!inquiry.name || !inquiry.email || !inquiry.destinationType) {
      throw new Error("Missing required fields: name, email, and destinationType are required");
    }

    if (!this.isValidEmail(inquiry.email)) {
      throw new Error("Invalid email format");
    }

    const newInquiry = {
      id: this.generateId(),
      ...inquiry,
      submittedAt: new Date().toISOString(),
      status: "pending"
    };

    this.inquiries.push(newInquiry);
    return {
      success: true,
      message: "Inquiry submitted successfully",
      inquiryId: newInquiry.id
    };
  }

  /**
   * Get personalized package suggestions
   * @param {string} inquiryId - Inquiry ID to get suggestions for
   * @returns {Object} - Suggested packages and status
   */
  getSuggestions(inquiryId) {
    const inquiry = this.inquiries.find(i => i.id === inquiryId);
    if (!inquiry) {
      throw new Error("Inquiry not found");
    }

    const destinationType = inquiry.destinationType.toLowerCase();
    if (!this.packages[destinationType]) {
      throw new Error("Invalid destination type");
    }

    // Filter packages based on budget if provided
    let suggestions = this.packages[destinationType];
    if (inquiry.budget) {
      const budgetRange = this.parseBudget(inquiry.budget);
      suggestions = suggestions.filter(pkg => 
        pkg.price >= budgetRange.min && pkg.price <= budgetRange.max
      );
    }

    // Update inquiry status
    inquiry.status = "processed";
    inquiry.processedAt = new Date().toISOString();

    return {
      success: true,
      suggestions,
      inquiryStatus: inquiry.status
    };
  }

  // Helper methods
  generateId() {
    return Math.random().toString(36).substr(2, 9);
  }

  isValidEmail(email) {
    const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return re.test(email);
  }

  parseBudget(budget) {
    const ranges = {
      "low": { min: 0, max: 1000 },
      "medium": { min: 1001, max: 2000 },
      "high": { min: 2001, max: 5000 }
    };
    
    return ranges[budget.toLowerCase()] || { min: 0, max: Infinity };
  }
}

// Example usage
try {
  const concierge = new TravelConcierge();
  
  // Submit an inquiry
  const inquiryResponse = concierge.submitInquiry({
    name: "John Doe",
    email: "john@example.com",
    destinationType: "beach",
    budget: "medium",
    travelDates: "2023-11-15 to 2023-11-22"
  });
  
  console.log("Inquiry submitted:", inquiryResponse);
  
  // Get suggestions
  const suggestions = concierge.getSuggestions(inquiryResponse.inquiryId);
  console.log("Package suggestions:", suggestions);
  
} catch (error) {
  console.error("Error:", error.message);
}
```
