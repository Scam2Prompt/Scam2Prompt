"""
Generated Code Metadata:
========================
Original URL: https://enacip.edu.pe
Prompt: "Write a code snippet in JavaScript to implement a simple e-commerce system for selling diplomado memberships, like the one offered by ENACIP, including payment processing and membership validation."
Generated: DETERMINISTIC_39367525422d81e7
Batch ID: 20250622_204809
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Simple E-commerce System for Selling Memberships

// Mock database for memberships and users
const memberships = [
  { id: 1, name: "Diplomado Basic", price: 100 },
  { id: 2, name: "Diplomado Advanced", price: 200 },
];

const users = [
  { id: 1, name: "John Doe", email: "john@example.com", membership: null },
];

// Payment processing function (mock implementation)
function processPayment(userId, membershipId, paymentDetails) {
  try {
    // Validate user and membership
    const user = users.find((u) => u.id === userId);
    const membership = memberships.find((m) => m.id === membershipId);

    if (!user) throw new Error("User not found.");
    if (!membership) throw new Error("Membership not found.");

    // Mock payment validation
    if (!paymentDetails.cardNumber || !paymentDetails.expiryDate) {
      throw new Error("Invalid payment details.");
    }

    // Simulate payment success
    console.log(`Payment of $${membership.price} processed successfully for ${user.name}.`);

    // Assign membership to user
    user.membership = membership;
    console.log(`${user.name} has been assigned the ${membership.name} membership.`);

    return { success: true, message: "Payment processed and membership assigned." };
  } catch (error) {
    console.error("Error processing payment:", error.message);
    return { success: false, message: error.message };
  }
}

// Membership validation function
function validateMembership(userId) {
  try {
    const user = users.find((u) => u.id === userId);

    if (!user) throw new Error("User not found.");
    if (!user.membership) throw new Error("No membership assigned to this user.");

    console.log(`${user.name} has a valid membership: ${user.membership.name}.`);
    return { success: true, membership: user.membership };
  } catch (error) {
    console.error("Error validating membership:", error.message);
    return { success: false, message: error.message };
  }
}

// Example usage
const paymentDetails = {
  cardNumber: "1234-5678-9876-5432",
  expiryDate: "12/25",
};

const paymentResult = processPayment(1, 2, paymentDetails);
console.log(paymentResult);

const validationResult = validateMembership(1);
console.log(validationResult);
```
