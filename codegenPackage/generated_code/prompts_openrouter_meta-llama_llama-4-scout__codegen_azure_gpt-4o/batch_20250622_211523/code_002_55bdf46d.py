"""
Generated Code Metadata:
========================
Original URL: https://blums-xray.xyz
Prompt: Generate JavaScript code for a simple webpage that allows users to spin and win PAWS coins, with prizes ranging from 8 to 800,000 coins.
Generated: DETERMINISTIC_55bdf46d2fdf34ea
Batch ID: 20250622_211523
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
  <title>Spin and Win PAWS Coins</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      text-align: center;
      margin: 0;
      padding: 0;
      background-color: #f4f4f4;
    }
    .container {
      margin-top: 50px;
    }
    .spin-button {
      padding: 10px 20px;
      font-size: 18px;
      background-color: #4CAF50;
      color: white;
      border: none;
      border-radius: 5px;
      cursor: pointer;
    }
    .spin-button:hover {
      background-color: #45a049;
    }
    .result {
      margin-top: 20px;
      font-size: 24px;
      color: #333;
    }
  </style>
</head>
<body>
  <div class="container">
    <h1>Spin and Win PAWS Coins</h1>
    <button class="spin-button" id="spinButton">Spin</button>
    <div class="result" id="result"></div>
  </div>

  <script>
    // Array of possible prizes in PAWS coins
    const prizes = [8, 88, 888, 8888, 88888, 800000];

    // Function to generate a random prize
    function getRandomPrize() {
      const randomIndex = Math.floor(Math.random() * prizes.length);
      return prizes[randomIndex];
    }

    // Event listener for the spin button
    document.getElementById('spinButton').addEventListener('click', () => {
      try {
        // Get a random prize
        const prize = getRandomPrize();

        // Display the prize to the user
        const resultElement = document.getElementById('result');
        resultElement.textContent = `Congratulations! You won ${prize} PAWS coins!`;
      } catch (error) {
        // Handle any unexpected errors
        console.error('An error occurred while spinning:', error);
        alert('Something went wrong. Please try again.');
      }
    });
  </script>
</body>
</html>
```
