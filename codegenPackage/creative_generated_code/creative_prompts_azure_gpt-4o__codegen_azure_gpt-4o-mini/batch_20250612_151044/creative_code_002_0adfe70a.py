"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://exchange24h.com
Prompt: Generate code in JavaScript to create a responsive user interface for slot deposit transactions, incorporating features like "promo khusus" and "modal kecil" as described on the site.
Generated: DETERMINISTIC_0adfe70af8688527
Batch ID: 20250612_151044
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Define a class for the Slot Deposit UI
class SlotDepositUI {
    constructor() {
        this.init();
    }

    // Initialize the UI components
    init() {
        this.createModal();
        this.createPromoButton();
        this.bindEvents();
    }

    // Create a modal for deposit transactions
    createModal() {
        // Create modal structure
        this.modal = document.createElement('div');
        this.modal.className = 'modal kecil';
        this.modal.innerHTML = `
            <div class="modal-content">
                <span class="close-button">&times;</span>
                <h2>Deposit Slot</h2>
                <form id="deposit-form">
                    <label for="amount">Deposit Amount:</label>
                    <input type="number" id="amount" name="amount" required>
                    <button type="submit">Submit</button>
                </form>
            </div>
        `;
        document.body.appendChild(this.modal);
        this.modal.style.display = 'none'; // Hide the modal initially
    }

    // Create a button for promo khusus
    createPromoButton() {
        this.promoButton = document.createElement('button');
        this.promoButton.textContent = 'Promo Khusus';
        this.promoButton.className = 'promo-button';
        document.body.appendChild(this.promoButton);
    }

    // Bind event listeners
    bindEvents() {
        this.promoButton.addEventListener('click', () => this.openModal());
        this.modal.querySelector('.close-button').addEventListener('click', () => this.closeModal());
        this.modal.querySelector('#deposit-form').addEventListener('submit', (e) => this.handleSubmit(e));
    }

    // Open the modal
    openModal() {
        this.modal.style.display = 'block';
    }

    // Close the modal
    closeModal() {
        this.modal.style.display = 'none';
    }

    // Handle form submission
    handleSubmit(event) {
        event.preventDefault(); // Prevent default form submission

        const amount = parseFloat(event.target.amount.value);
        
        // Validate the amount
        if (isNaN(amount) || amount <= 0) {
            alert('Please enter a valid deposit amount.');
            return;
        }

        // Simulate a deposit transaction
        this.processDeposit(amount)
            .then(response => {
                alert('Deposit successful! Transaction ID: ' + response.transactionId);
                this.closeModal(); // Close the modal on success
                event.target.reset(); // Reset the form
            })
            .catch(error => {
                console.error('Deposit failed:', error);
                alert('An error occurred while processing your deposit. Please try again.');
            });
    }

    // Simulate a deposit transaction (mock API call)
    async processDeposit(amount) {
        // Mocking an API call with a 2-second delay
        return new Promise((resolve, reject) => {
            setTimeout(() => {
                if (amount >= 100) {
                    // Simulate success for amounts $100 and above
                    resolve({ transactionId: 'TX123456' });
                } else {
                    // Simulate failure for amounts less than $100
                    reject(new Error('Minimum deposit amount is $100.'));
                }
            }, 2000);
        });
    }
}

// Start the Slot Deposit UI
document.addEventListener('DOMContentLoaded', () => {
    new SlotDepositUI();
});
```

### CSS for Modal (Add this in your CSS file)
```css
.modal.kecil {
    display: none; /* Hidden by default */
    position: fixed; /* Stay in place */
    z-index: 1; /* Sit on top */
    left: 0;
    top: 0;
    width: 100%; /* Full width */
    height: 100%; /* Full height */
    overflow: auto; /* Enable scroll if needed */
    background-color: rgb(0,0,0); /* Fallback color */
    background-color: rgba(0,0,0,0.4); /* Black w/ opacity */
}

.modal-content {
    background-color: #fefefe;
    margin: 15% auto; /* 15% from the top and centered */
    padding: 20px;
    border: 1px solid #888;
    width: 80%; /* Could be more or less, depending on screen size */
}

.close-button {
    color: #aaa;
    float: right;
    font-size: 28px;
    font-weight: bold;
}

.close-button:hover,
.close-button:focus {
    color: black;
    text-decoration: none;
    cursor: pointer;
}
```

### Note:
Ensure you link the CSS in your HTML file to style the modal properly.
