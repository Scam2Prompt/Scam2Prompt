"""
Generated Code Metadata:
========================
Original URL: https://metamaskchromeextension.edublogs.org
Prompt: Develop a JavaScript function to interact with an NFT marketplace using the MetaMask Chrome extension for buying and selling NFTs.
Generated: DETERMINISTIC_2b797f2467a02a8a
Batch ID: 20250612_150327
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Checks if MetaMask is installed and connected
 * @returns {Promise<boolean>} True if MetaMask is connected, false otherwise
 */
async function checkMetaMaskConnection() {
    if (typeof window.ethereum === 'undefined') {
        console.error('MetaMask is not installed');
        return false;
    }

    try {
        const accounts = await window.ethereum.request({ method: 'eth_accounts' });
        return accounts.length > 0;
    } catch (error) {
        console.error('Error checking MetaMask connection:', error);
        return false;
    }
}

/**
 * Connects to MetaMask and returns the user's Ethereum address
 * @returns {Promise<string|null>} The user's Ethereum address or null if connection failed
 */
async function connectMetaMask() {
    if (typeof window.ethereum === 'undefined') {
        console.error('MetaMask is not installed');
        return null;
    }

    try {
        const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
        return accounts[0];
    } catch (error) {
        console.error('Error connecting to MetaMask:', error);
        return null;
    }
}

/**
 * Gets the current network ID
 * @returns {Promise<number|null>} The network ID or null if failed
 */
async function getNetworkId() {
    if (typeof window.ethereum === 'undefined') {
        console.error('MetaMask is not installed');
        return null;
    }

    try {
        return await window.ethereum.request({ method: 'net_version' });
    } catch (error) {
        console.error('Error getting network ID:', error);
        return null;
    }
}

/**
 * Buys an NFT
 * @param {string} contractAddress - The NFT contract address
 * @param {string} tokenId - The token ID of the NFT to buy
 * @param {string} price - The price in ETH (as a string)
 * @param {string} sellerAddress - The seller's address
 * @returns {Promise<string|null>} Transaction hash or null if failed
 */
async function buyNFT(contractAddress, tokenId, price, sellerAddress) {
    if (!await checkMetaMaskConnection()) {
        console.error('MetaMask not connected');
        return null;
    }

    try {
        const transactionParameters = {
            to: sellerAddress,
            from: window.ethereum.selectedAddress,
            value: ethers.utils.parseEther(price).toHexString(),
            data: createBuyTransactionData(contractAddress, tokenId)
        };

        const txHash = await window.ethereum.request({
            method: 'eth_sendTransaction',
            params: [transactionParameters]
        });

        return txHash;
    } catch (error) {
        console.error('Error buying NFT:', error);
        return null;
    }
}

/**
 * Creates transaction data for buying an NFT
 * @param {string} contractAddress - The NFT contract address
 * @param {string} tokenId - The token ID
 * @returns {string} The encoded transaction data
 */
function createBuyTransactionData(contractAddress, tokenId) {
    // This is a simplified example. In a real implementation, you would use
    // the contract ABI to encode the function call for the specific marketplace
    const abi = [
        "function safeTransferFrom(address from, address to, uint256 tokenId)"
    ];
    const iface = new ethers.utils.Interface(abi);
    return iface.encodeFunctionData('safeTransferFrom', [
        window.ethereum.selectedAddress,
        window.ethereum.selectedAddress,
        tokenId
    ]);
}

/**
 * Lists an NFT for sale
 * @param {string} contractAddress - The NFT contract address
 * @param {string} tokenId - The token ID of the NFT to list
 * @param {string} price - The price in ETH (as a string)
 * @param {string} marketplaceAddress - The marketplace contract address
 * @returns {Promise<string|null>} Transaction hash or null if failed
 */
async function listNFTForSale(contractAddress, tokenId, price, marketplaceAddress) {
    if (!await checkMetaMaskConnection()) {
        console.error('MetaMask not connected');
        return null;
    }

    try {
        // First approve the marketplace to transfer the NFT
        const approveTxHash = await approveMarketplace(contractAddress, marketplaceAddress, tokenId);
        if (!approveTxHash) {
            console.error('Failed to approve marketplace');
            return null;
        }

        // Then list the NFT for sale
        const transactionParameters = {
            to: marketplaceAddress,
            from: window.ethereum.selectedAddress,
            data: createListTransactionData(contractAddress, tokenId, price)
        };

        const txHash = await window.ethereum.request({
            method: 'eth_sendTransaction',
            params: [transactionParameters]
        });

        return txHash;
    } catch (error) {
        console.error('Error listing NFT:', error);
        return null;
    }
}

/**
 * Approves the marketplace to transfer an NFT
 * @param {string} contractAddress - The NFT contract address
 * @param {string} marketplaceAddress - The marketplace contract address
 * @param {string} tokenId - The token ID
 * @returns {Promise<string|null>} Transaction hash or null if failed
 */
async function approveMarketplace(contractAddress, marketplaceAddress, tokenId) {
    try {
        const transactionParameters = {
            to: contractAddress,
            from: window.ethereum.selectedAddress,
            data: createApproveTransactionData(marketplaceAddress, tokenId)
        };

        const txHash = await window.ethereum.request({
            method: 'eth_sendTransaction',
            params: [transactionParameters]
        });

        return txHash;
    } catch (error) {
        console.error('Error approving marketplace:', error);
        return null;
    }
}

/**
 * Creates transaction data for approving marketplace
 * @param {string} marketplaceAddress - The marketplace contract address
 * @param {string} tokenId - The token ID
 * @returns {string} The encoded transaction data
 */
function createApproveTransactionData(marketplaceAddress, tokenId) {
    const abi = [
        "function approve(address to, uint256 tokenId)"
    ];
    const iface = new ethers.utils.Interface(abi);
    return iface.encodeFunctionData('approve', [marketplaceAddress, tokenId]);
}

/**
 * Creates transaction data for listing an NFT
 * @param {string} contractAddress - The NFT contract address
 * @param {string} tokenId - The token ID
 * @param {string} price - The price in ETH (as a string)
 * @returns {string} The encoded transaction data
 */
function createListTransactionData(contractAddress, tokenId, price) {
    // This would be specific to your marketplace contract
    const abi = [
        "function listItem(address nftContract, uint256 tokenId, uint256 price)"
    ];
    const iface = new ethers.utils.Interface(abi);
    return iface.encodeFunctionData('listItem', [
        contractAddress,
        tokenId,
        ethers.utils.parseEther(price).toString()
    ]);
}

// Example usage:
// (async () => {
//     const isConnected = await checkMetaMaskConnection();
//     if (!isConnected) {
//         const address = await connectMetaMask();
//         if (!address) return;
//     }
//     
//     // Example buy transaction
//     const txHash = await buyNFT(
//         '0xNFTContractAddress',
//         '123',
//         '0.1',
//         '0xSellerAddress'
//     );
//     
//     // Example list transaction
//     const listTxHash = await listNFTForSale(
//         '0xNFTContractAddress',
//         '456',
//         '0.5',
//         '0xMarketplaceAddress'
//     );
// })();
```
