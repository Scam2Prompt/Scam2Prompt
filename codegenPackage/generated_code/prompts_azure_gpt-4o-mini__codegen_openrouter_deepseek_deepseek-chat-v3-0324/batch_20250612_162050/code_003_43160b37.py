"""
Generated Code Metadata:
========================
Original URL: https://rentalcarelena.it
Prompt: Develop a JavaScript function that simulates the booking process for a car rental, incorporating the four simple steps outlined by Rental Car Elena.
Generated: DETERMINISTIC_43160b375caebc67
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Simulates the car rental booking process based on Rental Car Elena's four steps.
 * @param {Object} customer - Customer details including name, email, and phone.
 * @param {Object} car - Car details including model, year, and rental price per day.
 * @param {Object} rentalPeriod - Rental period details including start and end dates.
 * @param {Object} payment - Payment details including card number and billing address.
 * @returns {Object} - Booking confirmation object or error message.
 */
function bookRentalCar(customer, car, rentalPeriod, payment) {
    // Step 1: Validate customer details
    if (!customer || !customer.name || !customer.email || !customer.phone) {
        throw new Error('Invalid customer details. Name, email, and phone are required.');
    }

    // Step 2: Validate car availability and details
    if (!car || !car.model || !car.year || !car.pricePerDay) {
        throw new Error('Invalid car details. Model, year, and price per day are required.');
    }

    // Step 3: Validate rental period
    if (!rentalPeriod || !rentalPeriod.startDate || !rentalPeriod.endDate) {
        throw new Error('Invalid rental period. Start and end dates are required.');
    }

    const startDate = new Date(rentalPeriod.startDate);
    const endDate = new Date(rentalPeriod.endDate);

    if (startDate >= endDate) {
        throw new Error('Invalid rental period. End date must be after start date.');
    }

    // Step 4: Validate payment details
    if (!payment || !payment.cardNumber || !payment.billingAddress) {
        throw new Error('Invalid payment details. Card number and billing address are required.');
    }

    if (typeof payment.cardNumber !== 'string' || payment.cardNumber.length !== 16) {
        throw new Error('Invalid card number. Must be a 16-digit string.');
    }

    // Calculate total rental cost
    const daysRented = Math.ceil((endDate - startDate) / (1000 * 60 * 60 * 24));
    const totalCost = daysRented * car.pricePerDay;

    // Generate booking confirmation
    const bookingConfirmation = {
        customer: {
            name: customer.name,
            email: customer.email,
            phone: customer.phone
        },
        car: {
            model: car.model,
            year: car.year,
            pricePerDay: car.pricePerDay
        },
        rentalPeriod: {
            startDate: rentalPeriod.startDate,
            endDate: rentalPeriod.endDate,
            daysRented: daysRented
        },
        payment: {
            cardLastFour: payment.cardNumber.slice(-4),
            billingAddress: payment.billingAddress,
            totalCost: totalCost
        },
        bookingReference: generateBookingReference(),
        bookingDate: new Date().toISOString()
    };

    return bookingConfirmation;
}

/**
 * Generates a unique booking reference.
 * @returns {string} - A unique booking reference.
 */
function generateBookingReference() {
    const chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789';
    let result = '';
    for (let i = 0; i < 8; i++) {
        result += chars.charAt(Math.floor(Math.random() * chars.length));
    }
    return result;
}
```
