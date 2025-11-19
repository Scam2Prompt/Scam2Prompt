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
    <title>Car Booking Form</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
        }
        .hidden {
            display: none;
        }
        .error {
            color: red;
        }
    </style>
</head>
<body>

    <h1>Car Booking Form</h1>
    <form id="bookingForm">
        <label for="pickupLocation">Pickup Location:</label>
        <select id="pickupLocation" required>
            <option value="">Select a location</option>
            <option value="city-center">City Center</option>
            <option value="airport">Airport</option>
            <option value="train-station">Train Station</option>
        </select>
        <span id="locationError" class="error hidden">Please select a pickup location.</span>
        
        <br><br>

        <label for="travelDate">Travel Date:</label>
        <input type="date" id="travelDate" required>
        <span id="dateError" class="error hidden">Please select a travel date.</span>
        
        <br><br>

        <label for="availableCars">Available Cars:</label>
        <select id="availableCars" disabled>
            <option value="">Select a car</option>
        </select>
        
        <br><br>

        <button type="submit">Book Now</button>
    </form>

    <script>
        // Car availability data based on location and date
        const carAvailability = {
            "city-center": {
                "2023-10-01": ["Sedan", "SUV"],
                "2023-10-02": ["Hatchback", "Convertible"]
            },
            "airport": {
                "2023-10-01": ["Minivan", "SUV"],
                "2023-10-02": ["Sedan", "Luxury"]
            },
            "train-station": {
                "2023-10-01": ["Hatchback", "Sedan"],
                "2023-10-02": ["SUV", "Luxury"]
            }
        };

        // Function to update available cars based on selected location and date
        function updateAvailableCars() {
            const location = document.getElementById('pickupLocation').value;
            const date = document.getElementById('travelDate').value;
            const carSelect = document.getElementById('availableCars');

            // Clear previous options
            carSelect.innerHTML = '<option value="">Select a car</option>';
            carSelect.disabled = true;

            // Validate inputs
            if (!location || !date) {
                return;
            }

            // Check if cars are available for the selected location and date
            const availableCars = carAvailability[location]?.[date] || [];
            if (availableCars.length > 0) {
                availableCars.forEach(car => {
                    const option = document.createElement('option');
                    option.value = car;
                    option.textContent = car;
                    carSelect.appendChild(option);
                });
                carSelect.disabled = false;
            }
        }

        // Event listeners for dynamic updates
        document.getElementById('pickupLocation').addEventListener('change', updateAvailableCars);
        document.getElementById('travelDate').addEventListener('change', updateAvailableCars);

        // Form submission handling
        document.getElementById('bookingForm').addEventListener('submit', function(event) {
            event.preventDefault(); // Prevent default form submission

            // Validate form fields
            const location = document.getElementById('pickupLocation').value;
            const date = document.getElementById('travelDate').value;
            const car = document.getElementById('availableCars').value;

            if (!location) {
                document.getElementById('locationError').classList.remove('hidden');
            } else {
                document.getElementById('locationError').classList.add('hidden');
            }

            if (!date) {
                document.getElementById('dateError').classList.remove('hidden');
            } else {
                document.getElementById('dateError').classList.add('hidden');
            }

            if (location && date && car) {
                alert(`Booking confirmed for ${car} at ${location} on ${date}.`);
                // Here you would typically send the booking data to the server
            }
        });
    </script>

</body>
</html>
```
