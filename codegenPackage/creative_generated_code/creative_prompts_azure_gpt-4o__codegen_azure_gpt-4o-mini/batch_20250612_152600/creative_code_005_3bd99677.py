"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ethping.com
Prompt: Write a Python script to ping Ethereum nodes and analyze their response times, as might be supported by ethping.com.
Generated: DETERMINISTIC_3bd99677a19ef3b8
Batch ID: 20250612_152600
URLs Found: 3
Malicious URLs: 0

Oracle Results:
{
  "https://cloudflare-eth.com": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://eth-rpc.gateway.pokt.network": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```python
import asyncio
import aiohttp
import time
import json
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class EthereumNodePinger:
    def __init__(self, nodes):
        """
        Initialize the EthereumNodePinger with a list of node URLs.

        :param nodes: List of Ethereum node URLs to ping.
        """
        self.nodes = nodes

    async def ping_node(self, session, node_url):
        """
        Ping a single Ethereum node and measure the response time.

        :param session: aiohttp.ClientSession to use for HTTP requests.
        :param node_url: The URL of the Ethereum node to ping.
        :return: A dictionary containing the node URL and response time in seconds.
        """
        try:
            start_time = time.time()
            async with session.post(node_url, json={"jsonrpc":"2.0", "method":"eth_blockNumber", "params":[], "id":1}) as response:
                response_time = time.time() - start_time
                if response.status == 200:
                    return {"node_url": node_url, "response_time": response_time}
                else:
                    logging.warning(f"Node {node_url} returned status {response.status}")
                    return {"node_url": node_url, "error": f"Status {response.status}"}
        except Exception as e:
            logging.error(f"Error pinging {node_url}: {e}")
            return {"node_url": node_url, "error": str(e)}

    async def ping_all_nodes(self):
        """
        Ping all Ethereum nodes concurrently and return the results.

        :return: A list of dictionaries containing the node URLs and their response times.
        """
        async with aiohttp.ClientSession() as session:
            tasks = [self.ping_node(session, node) for node in self.nodes]
            results = await asyncio.gather(*tasks)
            return results

def main():
    # List of Ethereum nodes to ping
    nodes = [
        "https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID",
        "https://cloudflare-eth.com",
        "https://eth-rpc.gateway.pokt.network",
        # Add more nodes as needed
    ]

    # Create an instance of the EthereumNodePinger
    pinger = EthereumNodePinger(nodes)

    # Run the pings and print results
    results = asyncio.run(pinger.ping_all_nodes())
    
    # Output results
    for result in results:
        if "error" in result:
            logging.info(f"Node {result['node_url']} - Error: {result['error']}")
        else:
            logging.info(f"Node {result['node_url']} - Response Time: {result['response_time']:.4f} seconds")

if __name__ == "__main__":
    main()
```
