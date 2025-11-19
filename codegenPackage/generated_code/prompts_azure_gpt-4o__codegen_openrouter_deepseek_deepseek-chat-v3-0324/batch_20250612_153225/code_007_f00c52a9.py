"""
Generated Code Metadata:
========================
Original URL: https://rentalcarelena.it
Prompt: Develop a booking form in HTML and JavaScript that dynamically updates available cars based on user-selected pickup locations and travel dates.
Generated: DETERMINISTIC_f00c52a9de086ccd
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Car Rental Booking Form</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
        }
        .form-group {
            margin-bottom: 15px;
        }
        label {
            display: block;
            margin-bottom: 5px;
            font-weight: bold;
        }
        input, select {
            width: 100%;
            padding: 8px;
            border: 1px solid #ddd;
            border-radius: 4px;
            box-sizing: border-box;
        }
        button {
            background-color: #4CAF50;
            color: white;
            padding: 10px 15px;
            border: none;
            border-radius: 4px;
            cursor: pointer;
            font-size: 16px;
        }
        button:hover {
            background-color: #45a049;
        }
        .error {
            color: red;
            font-size: 14px;
            margin-top: 5px;
        }
        .car-list {
            margin-top: 20px;
            border-top: 1px solid #ddd;
            padding-top: 20px;
        }
        .car-item {
            border: 1px solid #ddd;
            border-radius: 4px;
            padding: 15px;
            margin-bottom: 10px;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }
        .car-info {
            flex: 1;
        }
        .car-price {
            font-weight: bold;
            font-size: 18px;
        }
    </style>
</head>
<body>
    <h1>Car Rental Booking</h1>
    <form id="bookingForm">
        <div class="form-group">
            <label for="pickupLocation">Pickup Location:</label>
            <select id="pickupLocation" required>
                <option value="">Select a location</option>
                <option value="airport">Airport</option>
                <option value="downtown">Downtown</option>
                <option value="suburb">Suburb</option>
            </select>
            <div id="locationError" class="error"></div>
        </div>

        <div class="form-group">
            <label for="pickupDate">Pickup Date:</label>
            <input type="date" id="pickupDate" required>
            <div id="dateError" class="error"></div>
        </div>

        <div class="form-group">
            <label for="returnDate">Return Date:</label>
            <input type="date" id="returnDate" required>
            <div id="returnDateError" class="error"></div>
        </div>

        <button type="submit">Search Available Cars</button>
    </form>

    <div id="carList" class="car-list"></div>

    <script>
        // Sample car data by location
        const carInventory = {
            airport: [
                { id: 1, model: "Toyota Camry", type: "Sedan", price: 50, available: true },
                { id: 2, model: "Honda CR-V", type: "SUV", price: 70, available: true },
                { id: 3, model: "BMW X5", type: "Luxury SUV", price: 120, available: true }
            ],
            downtown: [
                { id: 4, model: "Ford Focus", type: "Compact", price: 40, available: true },
                { id: 5, model: "Chevrolet Malibu", type: "Sedan", price: 55, available: true },
                { id: 6, model: "Jeep Wrangler", type: "SUV", price: 80, available: true }
            ],
            suburb: [
                { id: 7, model: "Nissan Altima", type: "Sedan", price: 45, available: true },
                { id: 8, model: "Hyundai Tucson", type: "SUV", price: 60, available: true },
                { id: 9, model: "Tesla Model 3", type: "Electric", price: 90, available: true }
            ]
        };

        document.getElementById('bookingForm').addEventListener('submit', function(e) {
            e.preventDefault();
            
            // Clear previous errors and results
            document.getElementById('locationError').textContent = '';
            document.getElementById('dateError').textContent = '';
            document.getElementById('returnDateError').textContent = '';
            document.getElementById('carList').innerHTML = '';
            
            // Get form values
            const pickupLocation = document.getElementById('pickupLocation').value;
            const pickupDate = document.getElementById('pickupDate').value;
            const returnDate = document.getElementById('returnDate').value;
            
            // Validate form
            let isValid = true;
            
            if (!pickupLocation) {
                document.getElementById('locationError').textContent = 'Please select a pickup location';
                isValid = false;
            }
            
            if (!pickupDate) {
                document.getElementById('dateError').textContent = 'Please select a pickup date';
                isValid = false;
            }
            
            if (!returnDate) {
                document.getElementById('returnDateError').textContent = 'Please select a return date';
                isValid = false;
            }
            
            if (pickupDate && returnDate) {
                const pickup = new Date(pickupDate);
                const returnD = new Date(returnDate);
                
                if (returnD <= pickup) {
                    document.getElementById('returnDateError').textContent = 'Return date must be after pickup date';
                    isValid = false;
                }
            }
            
            if (!isValid) {
                return;
            }
            
            // Calculate number of days
            const pickup = new Date(pickupDate);
            const returnD = new Date(returnDate);
            const timeDiff = returnD - pickup;
            const daysDiff = Math.ceil(timeDiff / (1000 * 60 * 60 * 24)) || 1;
            
            // Display available cars
            displayAvailableCars(pickupLocation, daysDiff);
        });
        
        function displayAvailableCars(location, days) {
            const carListElement = document.getElementById('carList');
            const cars = carInventory[location];
            
            if (!cars || cars.length === 0) {
                carListElement.innerHTML = '<p>No cars available at this location.</p>';
                return;
            }
            
            const availableCars = cars.filter(car => car.available);
            
            if (availableCars.length === 0) {
                carListElement.innerHTML = '<p>All cars are currently booked at this location.</p>';
                return;
            }
            
            const heading = document.createElement('h2');
            heading.textContent = 'Available Cars';
            carListElement.appendChild(heading);
            
            availableCars.forEach(car => {
                const totalPrice = car.price * days;
                
                const carItem = document.createElement('div');
                carItem.className = 'car-item';
                
                carItem.innerHTML = `
                    <div class="car-info">
                        <h3>${car.model}</h3>
                        <p>Type: ${car.type}</p>
                        <p>Daily Rate: $${car.price}</p>
                    </div>
                    <div class="car-price">
                        <p>Total for ${days} day(s):</p>
                        <p>$${totalPrice}</p>
                    </div>
                `;
                
                carListElement.appendChild(carItem);
            });
        }
        
        // Set minimum date to today for date inputs
        document.addEventListener('DOMContentLoaded', function() {
            const today = new Date().toISOString().split('T')[0];
            document.getElementById('pickupDate').setAttribute('min', today);
            document.getElementById('returnDate').setAttribute('min', today);
            
            // Update return date min when pickup date changes
            document.getElementById('pickupDate').addEventListener('change', function() {
                const pickupDate = this.value;
                if (pickupDate) {
                    document.getElementById('returnDate').setAttribute('min', pickupDate);
                }
            });
        });
    </script>
</body>
</html>
```
