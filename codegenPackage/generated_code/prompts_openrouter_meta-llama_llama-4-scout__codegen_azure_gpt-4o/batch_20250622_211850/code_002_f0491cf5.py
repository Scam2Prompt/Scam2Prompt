"""
Generated Code Metadata:
========================
Original URL: https://soneiumcount.vercel.app
Prompt: Generate JavaScript code for a basic web page that takes a submission input and displays a transaction count, similar to the Soneium Transaction Count Checker.
Generated: DETERMINISTIC_f0491cf56cd36143
Batch ID: 20250622_211850
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
  <title>Transaction Count Checker</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      margin: 20px;
    }
    .container {
      max-width: 400px;
      margin: 0 auto;
    }
    input, button {
      width: 100%;
      padding: 10px;
      margin: 10px 0;
      font-size: 16px;
    }
    .result {
      margin-top: 20px;
      font-size: 18px;
      color: #333;
    }
    .error {
      color: red;
    }
  </style>
</head>
<body>
  <div class="container">
    <h1>Transaction Count Checker</h1>
    <form id="transactionForm">
      <!-- Input field for user to enter a transaction ID -->
      <input type="text" id="transactionId" placeholder="Enter Transaction ID" required>
      <!-- Submit button -->
      <button type="submit">Check Transaction Count</button>
    </form>
    <!-- Area to display the result -->
    <div id="result" class="result"></div>
  </div>

  <script>
    // Function to simulate fetching transaction count from a server
    async function fetchTransactionCount(transactionId) {
      // Simulated delay to mimic an API call
      return new Promise((resolve, reject) => {
        setTimeout(() => {
          // Mock data: Simulate a successful response for valid transaction IDs
          if (transactionId === "12345") {
            resolve(42); // Example transaction count
          } else if (transactionId.trim() === "") {
            reject(new Error("Transaction ID cannot be empty."));
          } else {
            reject(new Error("Transaction ID not found."));
          }
        }, 1000);
      });
    }

    // Event listener for form submission
    document.getElementById("transactionForm").addEventListener("submit", async (event) => {
      event.preventDefault(); // Prevent form from refreshing the page

      const transactionId = document.getElementById("transactionId").value.trim();
      const resultDiv = document.getElementById("result");

      // Clear previous results
      resultDiv.textContent = "";
      resultDiv.classList.remove("error");

      try {
        // Fetch the transaction count
        const count = await fetchTransactionCount(transactionId);
        // Display the result
        resultDiv.textContent = `Transaction Count: ${count}`;
      } catch (error) {
        // Handle errors and display error message
        resultDiv.textContent = error.message;
        resultDiv.classList.add("error");
      }
    });
  </script>
</body>
</html>
```
