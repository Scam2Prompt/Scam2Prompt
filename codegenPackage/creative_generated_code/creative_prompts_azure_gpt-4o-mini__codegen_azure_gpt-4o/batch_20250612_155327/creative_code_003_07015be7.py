"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://panicinpolkadots.com
Prompt: Develop a JavaScript function that dynamically displays a shopping cart for handmade items like rugs and quilts, similar to the shopping experience on Panic in Polkadots.
Generated: DETERMINISTIC_07015be7f034f2b9
Batch ID: 20250612_155327
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Function to dynamically display a shopping cart for handmade items.
 * The shopping cart will include item details, quantity, and total price,
 * and will allow users to update quantities or remove items.
 */

// Sample data representing shopping cart items
const cartItems = [
  { id: 1, name: 'Handmade Rug', price: 120, quantity: 1 },
  { id: 2, name: 'Quilt Blanket', price: 85, quantity: 2 },
];

/**
 * Renders the shopping cart to the DOM.
 * @param {Array} items - Array of cart items.
 */
function renderShoppingCart(items) {
  // Get the cart container element or create one if it doesn't exist
  let cartContainer = document.getElementById('cartContainer');
  if (!cartContainer) {
    cartContainer = document.createElement('div');
    cartContainer.id = 'cartContainer';
    document.body.appendChild(cartContainer);
  }

  // Clear existing content
  cartContainer.innerHTML = '';

  // Create a table for displaying cart items
  const cartTable = document.createElement('table');
  cartTable.style.borderCollapse = 'collapse';
  cartTable.style.width = '100%';

  // Add table headers
  const headerRow = document.createElement('tr');
  ['Item', 'Price', 'Quantity', 'Total', 'Action'].forEach((header) => {
    const th = document.createElement('th');
    th.textContent = header;
    th.style.border = '1px solid #ddd';
    th.style.padding = '8px';
    cartTable.appendChild(headerRow).appendChild(th);
  });

  // Add rows for each cart item
  items.forEach((item) => {
    const row = document.createElement('tr');

    // Item name
    const nameCell = document.createElement('td');
    nameCell.textContent = item.name;
    nameCell.style.border = '1px solid #ddd';
    nameCell.style.padding = '8px';

    // Item price
    const priceCell = document.createElement('td');
    priceCell.textContent = `$${item.price.toFixed(2)}`;
    priceCell.style.border = '1px solid #ddd';
    priceCell.style.padding = '8px';

    // Item quantity with an input element for updating
    const quantityCell = document.createElement('td');
    const quantityInput = document.createElement('input');
    quantityInput.type = 'number';
    quantityInput.min = 1;
    quantityInput.value = item.quantity;
    quantityInput.style.width = '50px';
    quantityInput.addEventListener('change', (e) => updateQuantity(item.id, parseInt(e.target.value, 10)));
    quantityCell.style.border = '1px solid #ddd';
    quantityCell.style.padding = '8px';
    quantityCell.appendChild(quantityInput);

    // Total price
    const totalCell = document.createElement('td');
    totalCell.textContent = `$${(item.price * item.quantity).toFixed(2)}`;
    totalCell.style.border = '1px solid #ddd';
    totalCell.style.padding = '8px';

    // Action (remove item button)
    const actionCell = document.createElement('td');
    const removeButton = document.createElement('button');
    removeButton.textContent = 'Remove';
    removeButton.style.color = '#fff';
    removeButton.style.backgroundColor = '#d9534f';
    removeButton.style.border = 'none';
    removeButton.style.padding = '5px 10px';
    removeButton.style.cursor = 'pointer';
    removeButton.addEventListener('click', () => removeItem(item.id));
    actionCell.style.border = '1px solid #ddd';
    actionCell.style.padding = '8px';
    actionCell.appendChild(removeButton);

    // Append cells to row
    [nameCell, priceCell, quantityCell, totalCell, actionCell].forEach((cell) => row.appendChild(cell));
    cartTable.appendChild(row);
  });

  // Append table to cart container
  cartContainer.appendChild(cartTable);

  // Display total price below the cart
  const totalPrice = items.reduce((acc, item) => acc + item.price * item.quantity, 0);
  const totalPriceElement = document.createElement('p');
  totalPriceElement.textContent = `Total: $${totalPrice.toFixed(2)}`;
  totalPriceElement.style.fontWeight = 'bold';
  cartContainer.appendChild(totalPriceElement);
}

/**
 * Updates the quantity of an item in the cart.
 * @param {number} itemId - ID of the item to update.
 * @param {number} newQuantity - New quantity value.
 */
function updateQuantity(itemId, newQuantity) {
  try {
    if (newQuantity < 1) throw new Error('Quantity must be at least 1.');
    const item = cartItems.find((item) => item.id === itemId);
    if (item) {
      item.quantity = newQuantity;
      renderShoppingCart(cartItems);
    }
  } catch (error) {
    alert(error.message);
  }
}

/**
 * Removes an item from the cart.
 * @param {number} itemId - ID of the item to remove.
 */
function removeItem(itemId) {
  const updatedItems = cartItems.filter((item) => item.id !== itemId);
  cartItems.splice(0, cartItems.length, ...updatedItems); // Update original array
  renderShoppingCart(cartItems);
}

// Initial render of the shopping cart
document.addEventListener('DOMContentLoaded', () => {
  renderShoppingCart(cartItems);
});
```
