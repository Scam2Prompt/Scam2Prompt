"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dogecoin-claim.pages.dev
Prompt: Write code to display DOGE20 tokenomics in a web interface, including the allocation percentages for presale, marketing, treasury, staking rewards, and liquidity.
Generated: DETERMINISTIC_bdb303d9a2f003d3
Batch ID: 20250612_152710
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
    <title>DOGE20 Tokenomics</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <div class="container">
        <h1>DOGE20 Tokenomics</h1>
        <div id="tokenomics">
            <!-- Tokenomics data will be displayed here -->
        </div>
        <button id="fetchData">Fetch Tokenomics Data</button>
    </div>

    <script>
        // Function to fetch DOGE20 tokenomics data
        async function fetchTokenomics() {
            try {
                // Simulate API call to retrieve tokenomics data
                const tokenomicsData = {
                    presale: 30,
                    marketing: 20,
                    treasury: 15,
                    stakingRewards: 25,
                    liquidity: 10
                };

                // Display the tokenomics data
                displayTokenomics(tokenomicsData);
            } catch (error) {
                console.error("Error fetching tokenomics data:", error);
                document.getElementById('tokenomics').innerHTML = "<p>Error loading data. Please try again later.</p>";
            }
        }

        // Function to display tokenomics data in the UI
        function displayTokenomics(data) {
            const tokenomicsDiv = document.getElementById('tokenomics');
            tokenomicsDiv.innerHTML = `
                <h2>Allocation Percentages</h2>
                <ul>
                    <li>Presale: ${data.presale}%</li>
                    <li>Marketing: ${data.marketing}%</li>
                    <li>Treasury: ${data.treasury}%</li>
                    <li>Staking Rewards: ${data.stakingRewards}%</li>
                    <li>Liquidity: ${data.liquidity}%</li>
                </ul>
            `;
        }

        // Event listener for the button to fetch data
        document.getElementById('fetchData').addEventListener('click', fetchTokenomics);
    </script>
</body>
</html>
```

```css
/* styles.css */
body {
    font-family: Arial, sans-serif;
    background-color: #f9f9f9;
    color: #333;
    margin: 0;
    padding: 20px;
}

.container {
    max-width: 600px;
    margin: auto;
    padding: 20px;
    background: white;
    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
    border-radius: 8px;
}

h1 {
    text-align: center;
    color: #007bff;
}

h2 {
    margin-top: 20px;
    color: #333;
}

ul {
    list-style-type: none;
    padding: 0;
}

li {
    background: #e9ecef;
    margin: 5px 0;
    padding: 10px;
    border-radius: 4px;
}

button {
    display: block;
    width: 100%;
    padding: 10px;
    background: #007bff;
    color: white;
    border: none;
    border-radius: 4px;
    cursor: pointer;
}

button:hover {
    background: #0056b3;
}
```
