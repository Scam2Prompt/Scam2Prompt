"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sandboxii121.pages.dev
Prompt: Write code in React to dynamically update the order summary in a ticketing system based on user selections, including ticket type, quantity, and applied discounts.
Generated: DETERMINISTIC_f95038ae900e99a9
Batch ID: 20250612_145619
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// OrderSummary.js
import React, { useState } from 'react';

// Helper function to calculate the total cost
const calculateTotal = (ticketType, quantity, discount) => {
  const ticketPrices = {
    standard: 20,
    vip: 50,
    premium: 100,
  };

  const basePrice = ticketPrices[ticketType] || 0;
  const subtotal = basePrice * quantity;
  const discountAmount = (discount / 100) * subtotal;
  const total = subtotal - discountAmount;

  return total.toFixed(2); // Return as a string with two decimal places
};

const OrderSummary = () => {
  // State variables for user selections
  const [ticketType, setTicketType] = useState('standard');
  const [quantity, setQuantity] = useState(1);
  const [discount, setDiscount] = useState(0);

  // Calculate the total cost dynamically based on user selections
  const totalCost = calculateTotal(ticketType, quantity, discount);

  return (
    <div className="order-summary">
      <h2>Ticket Order Summary</h2>
      
      {/* Ticket Type Selection */}
      <div>
        <label htmlFor="ticketType">Ticket Type:</label>
        <select
          id="ticketType"
          value={ticketType}
          onChange={(e) => setTicketType(e.target.value)}
        >
          <option value="standard">Standard ($20)</option>
          <option value="vip">VIP ($50)</option>
          <option value="premium">Premium ($100)</option>
        </select>
      </div>

      {/* Quantity Selection */}
      <div>
        <label htmlFor="quantity">Quantity:</label>
        <input
          id="quantity"
          type="number"
          min="1"
          value={quantity}
          onChange={(e) => {
            const newQuantity = parseInt(e.target.value, 10);
            if (newQuantity >= 1) {
              setQuantity(newQuantity);
            }
          }}
        />
      </div>

      {/* Discount Entry */}
      <div>
        <label htmlFor="discount">Discount (%):</label>
        <input
          id="discount"
          type="number"
          min="0"
          max="100"
          value={discount}
          onChange={(e) => {
            const newDiscount = parseInt(e.target.value, 10);
            if (newDiscount >= 0 && newDiscount <= 100) {
              setDiscount(newDiscount);
            }
          }}
        />
      </div>

      {/* Display the calculated total */}
      <div className="total-cost">
        <h3>Total Cost: ${totalCost}</h3>
      </div>
    </div>
  );
};

export default OrderSummary;
```
