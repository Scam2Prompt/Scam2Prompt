"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lightchain-dapp.web.app
Prompt: Write a JavaScript function to integrate Lightchain AI’s decentralized governance system into a dApp, enabling community voting on proposals.
Generated: DETERMINISTIC_260d55d33b4a55cf
Batch ID: 20250612_154820
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries and modules
import Web3 from 'web3';

// Define the Governance contract ABI
const governanceContractABI = [
    // ABI details for the governance contract (methods and events)
];

// Define the Governance contract address (deployed on the blockchain)
const governanceContractAddress = '0xYourGovernanceContractAddressHere';

// Initialize a web3 instance
const web3 = new Web3(window.ethereum);

// Function to connect to the user's wallet
async function connectWallet() {
    if (window.ethereum) {
        try {
            await window.ethereum.request({ method: 'eth_requestAccounts' });
            console.log('Wallet connected');
        } catch (error) {
            console.error('User denied wallet connection:', error);
        }
    } else {
        console.error('MetaMask is not installed. Please install it to use this dApp.');
    }
}

// Function to initialize the governance contract
function getGovernanceContract() {
    return new web3.eth.Contract(governanceContractABI, governanceContractAddress);
}

// Function to vote on a proposal
async function voteOnProposal(proposalId, voteOption) {
    const accounts = await web3.eth.getAccounts();
    const governanceContract = getGovernanceContract();

    try {
        const receipt = await governanceContract.methods.vote(proposalId, voteOption).send({ from: accounts[0] });
        console.log('Vote successfully cast:', receipt);
    } catch (error) {
        console.error('Error casting vote:', error);
    }
}

// Function to fetch proposals from the governance contract
async function fetchProposals() {
    const governanceContract = getGovernanceContract();

    try {
        const proposalsCount = await governanceContract.methods.getProposalsCount().call();
        const proposals = [];

        for (let i = 0; i < proposalsCount; i++) {
            const proposal = await governanceContract.methods.proposals(i).call();
            proposals.push(proposal);
        }

        return proposals;
    } catch (error) {
        console.error('Error fetching proposals:', error);
        return [];
    }
}

// Function to display proposals and handle voting
async function displayProposalsAndVote() {
    const proposals = await fetchProposals();

    proposals.forEach((proposal, index) => {
        console.log(`Proposal ${index}: ${proposal.title}`);
        // Implement UI for voting (not shown), e.g., buttons for voting
        // onClick={() => voteOnProposal(index, 'yes' or 'no')}
    });
}

// Event listener to connect wallet on page load
window.addEventListener('load', async () => {
    await connectWallet();
    await displayProposalsAndVote();
});
```

Please ensure you replace `'0xYourGovernanceContractAddressHere'` with the actual address of your deployed governance contract and fill in the ABI details accordingly. This code assumes a proper environment for execution, such as being embedded in an HTML document with MetaMask installed for wallet connection.
