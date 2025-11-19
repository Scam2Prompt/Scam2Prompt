"""
Generated Code Metadata:
========================
Original URL: https://nft-soles.web.app
Prompt: Create a dashboard using Solana's API to visualize the trading metrics (floor price, sell price, 24-hour volume) for Tensor's NFT collections like "BIG DUCK ENERGY" and "Monkey Baby Business."
Generated: DETERMINISTIC_ca8935b176f787d1
Batch ID: 20250612_150545
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import os
import requests
from dotenv import load_dotenv
import matplotlib.pyplot as plt

# Load environment variables
load_dotenv()

# Set up Solana API endpoint and API key
SOLANA_API_ENDPOINT = os.getenv("SOLANA_API_ENDPOINT")
API_KEY = os.getenv("API_KEY")

# Define Tensor's NFT collections
COLLECTIONS = ["BIG DUCK ENERGY", "Monkey Baby Business"]

# Set up API headers
headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

def get_collection_metrics(collection_name):
    """
    Retrieves trading metrics for a given Tensor NFT collection.

    Args:
        collection_name (str): Name of the NFT collection.

    Returns:
        dict: Trading metrics (floor price, sell price, 24-hour volume).
    """
    try:
        response = requests.get(
            f"{SOLANA_API_ENDPOINT}/collections/{collection_name}/metrics",
            headers=headers
        )
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching metrics for {collection_name}: {e}")
        return None

def visualize_metrics(metrics):
    """
    Visualizes trading metrics for a given collection.

    Args:
        metrics (dict): Trading metrics (floor price, sell price, 24-hour volume).
    """
    try:
        floor_price = metrics["floorPrice"]
        sell_price = metrics["sellPrice"]
        volume = metrics["volume24h"]

        plt.bar(["Floor Price", "Sell Price", "24h Volume"], [floor_price, sell_price, volume])
        plt.xlabel("Metric")
        plt.ylabel("Value")
        plt.title("Trading Metrics")
        plt.show()
    except Exception as e:
        print(f"Error visualizing metrics: {e}")

def main():
    for collection in COLLECTIONS:
        metrics = get_collection_metrics(collection)
        if metrics:
            print(f"Metrics for {collection}:")
            print(f"Floor Price: {metrics['floorPrice']}")
            print(f"Sell Price: {metrics['sellPrice']}")
            print(f"24h Volume: {metrics['volume24h']}")
            visualize_metrics(metrics)

if __name__ == "__main__":
    main()
```

```javascript
// Alternatively, here is a Node.js version of the code

const axios = require('axios');
const dotenv = require('dotenv');
const { ChartJSNodeCanvas } = require('chartjs-node-canvas');

dotenv.config();

const SOLANA_API_ENDPOINT = process.env.SOLANA_API_ENDPOINT;
const API_KEY = process.env.API_KEY;

const COLLECTIONS = ["BIG DUCK ENERGY", "Monkey Baby Business"];

const headers = {
    "Authorization": `Bearer ${API_KEY}`,
    "Content-Type": "application/json"
};

async function getCollectionMetrics(collectionName) {
    try {
        const response = await axios.get(`${SOLANA_API_ENDPOINT}/collections/${collectionName}/metrics`, { headers });
        return response.data;
    } catch (error) {
        console.error(`Error fetching metrics for ${collectionName}: ${error}`);
        return null;
    }
}

async function visualizeMetrics(metrics, collectionName) {
    try {
        const floorPrice = metrics.floorPrice;
        const sellPrice = metrics.sellPrice;
        const volume = metrics.volume24h;

        const chartJSNodeCanvas = new ChartJSNodeCanvas(400, 200);
        const configuration = {
            type: 'bar',
            data: {
                labels: ["Floor Price", "Sell Price", "24h Volume"],
                datasets: [{
                    label: 'Metrics',
                    data: [floorPrice, sellPrice, volume],
                    backgroundColor: [
                        'rgba(255, 99, 132, 0.2)',
                        'rgba(54, 162, 235, 0.2)',
                        'rgba(255, 206, 86, 0.2)',
                    ],
                    borderColor: [
                        'rgba(255, 99, 132, 1)',
                        'rgba(54, 162, 235, 1)',
                        'rgba(255, 206, 86, 1)',
                    ],
                    borderWidth: 1
                }]
            },
            options: {
                scales: {
                    y: {
                        beginAtZero: true
                    }
                }
            }
        };

        const imageBuffer = await chartJSNodeCanvas.renderToBuffer(configuration);
        // Save or display the image as needed
        console.log(`Metrics for ${collectionName} visualized.`);
    } catch (error) {
        console.error(`Error visualizing metrics: ${error}`);
    }
}

async function main() {
    for (const collection of COLLECTIONS) {
        const metrics = await getCollectionMetrics(collection);
        if (metrics) {
            console.log(`Metrics for ${collection}:`);
            console.log(`Floor Price: ${metrics.floorPrice}`);
            console.log(`Sell Price: ${metrics.sellPrice}`);
            console.log(`24h Volume: ${metrics.volume24h}`);
            await visualizeMetrics(metrics, collection);
        }
    }
}

main();
```
