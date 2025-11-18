"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://usdc-wl.web.app
Prompt: Generate code to display the remaining whitelist mint count dynamically on a webpage, using the data format described in the USDC Whitelist Mint system.
Generated: DETERMINISTIC_91e6c0bd6678d1b4
Batch ID: 20250612_150040
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Whitelist Mint Count</title>
    <style>
        body {
            font-family: Arial, sans-serif;
        }
        .mint-count {
            font-size: 24px;
            color: #333;
            margin-top: 20px;
        }
        .error {
            color: red;
            font-size: 18px;
        }
    </style>
</head>
<body>
    <h1>USDC Whitelist Mint System</h1>
    <div id="mint-count-container">
        <!-- Dynamic content will be inserted here -->
    </div>

    <script>
        // Example data format from the USDC Whitelist Mint system
        const whitelistMintData = {
            totalWhitelisted: 1000, // Total number of users in the whitelist
            totalMinted: 650       // Number of users who have already minted
        };

        /**
         * Function to calculate the remaining whitelist mint count.
         * @param {object} data - The whitelist mint data object.
         * @returns {number} - The remaining whitelist mint count.
         */
        function calculateRemainingMintCount(data) {
            try {
                // Validate the input data
                if (!data || typeof data !== 'object') {
                    throw new Error("Invalid data format.");
                }

                const { totalWhitelisted, totalMinted } = data;

                if (typeof totalWhitelisted !== 'number' || typeof totalMinted !== 'number') {
                    throw new Error("Data properties must be numbers.");
                }

                if (totalMinted > totalWhitelisted) {
                    throw new Error("Total minted cannot exceed total whitelisted.");
                }

                // Calculate remaining mint count
                return totalWhitelisted - totalMinted;
            } catch (error) {
                console.error(error.message);
                // Display error message to the user
                const container = document.getElementById('mint-count-container');
                container.innerHTML = `<p class="error">Error: ${error.message}</p>`;
                return null;
            }
        }

        /**
         * Function to dynamically display the remaining whitelist mint count.
         */
        function displayRemainingMintCount() {
            const remainingCount = calculateRemainingMintCount(whitelistMintData);

            if (remainingCount !== null) {
                // Display the remaining mint count on the page
                const container = document.getElementById('mint-count-container');
                container.innerHTML = `<p class="mint-count">Remaining Whitelist Mint Count: ${remainingCount}</p>`;
            }
        }

        // Call the function to display data when the page loads
        displayRemainingMintCount();
    </script>
</body>
</html>
```
