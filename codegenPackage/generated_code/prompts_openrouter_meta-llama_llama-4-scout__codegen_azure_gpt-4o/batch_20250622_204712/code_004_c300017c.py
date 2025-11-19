"""
Generated Code Metadata:
========================
Original URL: https://smartnetrewardls.pages.dev
Prompt: Create a simple webpage using HTML and CSS that allows users to claim rewards, including a button to claim $500 worth of tokens.
Generated: DETERMINISTIC_c300017ca089aebf
Batch ID: 20250622_204712
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
<<<<<<< HEAD
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="Reward Claim Page">
  <title>Claim Your Rewards</title>
  <style>
    /* General reset for consistent styling */
    body {
      margin: 0;
      font-family: Arial, sans-serif;
      background-color: #f4f4f4;
      color: #333;
    }

    /* Center the content */
    .container {
      max-width: 600px;
      margin: 50px auto;
      padding: 20px;
      background: #fff;
      border-radius: 8px;
      box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
      text-align: center;
    }

    /* Heading styles */
    h1 {
      font-size: 2rem;
      margin-bottom: 20px;
      color: #444;
    }

    /* Description text */
    p {
      font-size: 1rem;
      margin-bottom: 30px;
      color: #666;
    }

    /* Button styling */
    .claim-button {
      display: inline-block;
      padding: 15px 30px;
      font-size: 1rem;
      font-weight: bold;
      color: #fff;
      background-color: #28a745;
      border: none;
      border-radius: 5px;
      cursor: pointer;
      transition: background-color 0.3s ease;
    }

    /* Button hover effect */
    .claim-button:hover {
      background-color: #218838;
    }

    /* Button focus styling */
    .claim-button:focus {
      outline: none;
      box-shadow: 0 0 0 3px rgba(40, 167, 69, 0.5);
    }
  </style>
</head>
<body>
  <div class="container">
    <!-- Page heading -->
    <h1>Claim Your Rewards</h1>
    <!-- Description text -->
    <p>Click the button below to claim $500 worth of tokens.</p>
    <!-- Claim button -->
    <button class="claim-button" onclick="claimReward()">Claim $500 Tokens</button>
  </div>

  <script>
    /**
     * Function to handle reward claiming
     * This function simulates the reward claim process
     */
    function claimReward() {
      try {
        // Simulate reward claim logic
        alert("Congratulations! You have successfully claimed $500 worth of tokens.");
      } catch (error) {
        // Handle any unexpected errors
        console.error("An error occurred while claiming the reward:", error);
        alert("Sorry, something went wrong. Please try again later.");
      }
    }
  </script>
=======
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="Reward Claim Page">
    <title>Claim Your Rewards</title>
    <style>
        /* General reset for consistent styling */
        body {
            margin: 0;
            font-family: Arial, sans-serif;
            background-color: #f4f4f9;
            color: #333;
        }

        /* Center the content */
        .container {
            max-width: 600px;
            margin: 50px auto;
            padding: 20px;
            background: #fff;
            border-radius: 8px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            text-align: center;
        }

        /* Heading styles */
        h1 {
            font-size: 2rem;
            margin-bottom: 20px;
            color: #444;
        }

        p {
            font-size: 1rem;
            margin-bottom: 30px;
            color: #666;
        }

        /* Button styling */
        .claim-button {
            display: inline-block;
            padding: 15px 30px;
            font-size: 1rem;
            font-weight: bold;
            color: #fff;
            background-color: #007bff;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            transition: background-color 0.3s ease;
        }

        .claim-button:hover {
            background-color: #0056b3;
        }

        /* Success message styling */
        .success-message {
            display: none;
            margin-top: 20px;
            font-size: 1rem;
            color: #28a745;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Claim Your Rewards</h1>
        <p>Click the button below to claim $500 worth of tokens.</p>
        <button class="claim-button" id="claimButton">Claim $500 Tokens</button>
        <p class="success-message" id="successMessage">Congratulations! You have successfully claimed your reward.</p>
    </div>

    <script>
        // Select the button and success message elements
        const claimButton = document.getElementById('claimButton');
        const successMessage = document.getElementById('successMessage');

        // Add an event listener to handle button clicks
        claimButton.addEventListener('click', () => {
            try {
                // Simulate reward claiming logic
                // In a real-world scenario, this could involve an API call
                successMessage.style.display = 'block'; // Show success message
                claimButton.disabled = true; // Disable the button after claiming
                claimButton.textContent = 'Reward Claimed'; // Update button text
            } catch (error) {
                // Handle any unexpected errors
                console.error('An error occurred while claiming the reward:', error);
                alert('Something went wrong. Please try again later.');
            }
        });
    </script>
>>>>>>> 10360aee73f (add full contents for codegen_disallow_original_url)
</body>
</html>
```
