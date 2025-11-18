"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metamask-ai-agent.vercel.app
Prompt: Write code to track transactions and manage tokens using MetaMask's API, with AI-powered insights provided by OpenAI.
Generated: DETERMINISTIC_f04954049324b138
Batch ID: 20250612_153915
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries and dependencies
const ethers = require('ethers'); // For interacting with Ethereum blockchain
const OpenAI = require('openai'); // For AI-powered insights (requires OpenAI Node.js library)

// Initialize OpenAI API client
const openai = new OpenAI({
  apiKey: process.env.OPENAI_API_KEY, // Ensure OpenAI API key is securely stored in environment variables
});

// Function to connect to MetaMask and retrieve account information
async function connectMetaMask() {
  if (!window.ethereum) {
    throw new Error('MetaMask is not installed. Please install MetaMask.');
  }

  try {
    const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
    const provider = new ethers.providers.Web3Provider(window.ethereum);
    const signer = provider.getSigner();
    const account = accounts[0];
    console.log(`Connected account: ${account}`);
    return { provider, signer, account };
  } catch (error) {
    console.error('Failed to connect to MetaMask:', error.message);
    throw error;
  }
}

// Function to fetch token balance for a specific ERC-20 token
async function getTokenBalance(signer, tokenAddress) {
  try {
    // ERC-20 Token ABI (minimal for balanceOf function)
    const tokenAbi = ['function balanceOf(address owner) view returns (uint256)'];
    const tokenContract = new ethers.Contract(tokenAddress, tokenAbi, signer);

    // Fetch balance
    const balance = await tokenContract.balanceOf(await signer.getAddress());
    console.log(`Token balance: ${balance.toString()}`);
    return balance;
  } catch (error) {
    console.error('Error fetching token balance:', error.message);
    throw error;
  }
}

// Function to track transactions on an account
async function fetchTransactionHistory(provider, account) {
  try {
    const history = await provider.getHistory(account);
    console.log(`Transaction history for account ${account}:`, history);
    return history;
  } catch (error) {
    console.error('Error fetching transaction history:', error.message);
    throw error;
  }
}

// Function to get AI insights on transaction history using OpenAI
async function getAIInsights(transactions) {
  try {
    const transactionDescriptions = transactions.map(tx => {
      return `Transaction ${tx.hash}: Sent ${ethers.utils.formatEther(tx.value)} ETH`;
    });

    const prompt = `
      Analyze the following Ethereum transaction data and provide insights. 
      Focus on spending patterns, potential risks, and opportunities:
      ${transactionDescriptions.join('\n')}
    `;

    const response = await openai.chat.completions.create({
      model: 'gpt-4', // Select appropriate model
      messages: [{ role: 'user', content: prompt }],
    });

    const insights = response.choices[0].message.content;
    console.log('AI Insights:', insights);
    return insights;
  } catch (error) {
    console.error('Error fetching AI insights:', error.message);
    throw error;
  }
}

// Main execution function
(async function main() {
  try {
    console.log('Connecting to MetaMask...');
    const { provider, signer, account } = await connectMetaMask();

    console.log('Fetching token balance...');
    const tokenAddress = '0xTokenAddressHere'; // Replace with valid ERC-20 token address
    const balance = await getTokenBalance(signer, tokenAddress);

    console.log('Fetching transaction history...');
    const transactions = await fetchTransactionHistory(provider, account);

    console.log('Fetching AI insights...');
    const insights = await getAIInsights(transactions);

    console.log('Execution completed.');
  } catch (error) {
    console.error('An error occurred during execution:', error.message);
  }
})();
```

### Notes on Production Readiness:
1. **Environment Variables**: Ensure `OPENAI_API_KEY` is securely stored and not hardcoded.
2. **Error Handling**: Comprehensive error handling is included for each step.
3. **Best Practices**: Modular functions make the code reusable and maintainable.
4. **Dependencies**: Install necessary libraries (`ethers` and `openai`) via `npm install ethers openai`.
