"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://eveningdesertsafaridxb.ae
Prompt: Develop a JavaScript function that dynamically updates the price of the Evening Desert Safari based on selected options like VIP service and additional activities.
Generated: DETERMINISTIC_4ab08b4542c1968c
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Function to dynamically update the price of the Evening Desert Safari
function updateSafariPrice() {
    // Base price for the Evening Desert Safari
    const basePrice = 100;
    
    // Initialize total price with the base price
    let totalPrice = basePrice;

    // Get selected options from the form
    const vipService = document.getElementById('vipService').checked;
    const additionalActivities = document.querySelectorAll('input[name="activities"]:checked');

    // Check if VIP service is selected and update the price
    if (vipService) {
        totalPrice += 50; // Add VIP service charge
    }

    // Calculate the price for additional activities
    additionalActivities.forEach(activity => {
        switch (activity.value) {
            case 'camelRide':
                totalPrice += 30; // Camel Ride charge
                break;
            case 'duneBashing':
                totalPrice += 40; // Dune Bashing charge
                break;
            case 'sandboarding':
                totalPrice += 25; // Sandboarding charge
                break;
            // Add more activities as needed
            default:
                console.warn('Unknown activity selected: ' + activity.value);
        }
    });

    // Update the displayed total price on the webpage
    document.getElementById('totalPrice').innerText = `Total Price: $${totalPrice.toFixed(2)}`;
}

// Event listeners for the options to trigger price update
document.getElementById('vipService').addEventListener('change', updateSafariPrice);
document.querySelectorAll('input[name="activities"]').forEach(activity => {
    activity.addEventListener('change', updateSafariPrice);
});

// Initialize the price display on page load
window.onload = updateSafariPrice;
```

```html
<!-- Example HTML structure to work with the JavaScript function -->
<div>
    <h1>Evening Desert Safari</h1>
    <div>
        <label>
            <input type="checkbox" id="vipService"> VIP Service ($50 extra)
        </label>
    </div>
    <div>
        <h3>Select Additional Activities:</h3>
        <label>
            <input type="checkbox" name="activities" value="camelRide"> Camel Ride ($30)
        </label>
        <label>
            <input type="checkbox" name="activities" value="duneBashing"> Dune Bashing ($40)
        </label>
        <label>
            <input type="checkbox" name="activities" value="sandboarding"> Sandboarding ($25)
        </label>
    </div>
    <div id="totalPrice">Total Price: $100.00</div>
</div>
```
