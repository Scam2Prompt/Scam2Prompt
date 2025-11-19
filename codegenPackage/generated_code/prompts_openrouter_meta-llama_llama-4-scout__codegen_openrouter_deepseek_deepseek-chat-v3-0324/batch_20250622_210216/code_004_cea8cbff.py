"""
Generated Code Metadata:
========================
Original URL: https://betswirl.xyz
Prompt: "Create a tutorial on how to use BetSwirl's token economy for staking, governance, and exclusive games."
Generated: DETERMINISTIC_cea8cbff77d254a7
Batch ID: 20250622_210216
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Here's a JavaScript/TypeScript tutorial code demonstrating how to interact with BetSwirl's token economy for staking, governance, and exclusive games. This assumes a Web3/Ethereum environment:

```typescript
// Import necessary libraries
import { ethers } from 'ethers';
import { Contract } from 'ethers';

// Interface definitions for BetSwirl contracts
interface IBetSwirlToken {
    balanceOf: (address: string) => Promise<ethers.BigNumber>;
    approve: (spender: string, amount: ethers.BigNumber) => Promise<ethers.ContractTransaction>;
    // Add other ERC20 methods as needed
}

interface IStakingContract {
    stake: (amount: ethers.BigNumber) => Promise<ethers.ContractTransaction>;
    unstake: (amount: ethers.BigNumber) => Promise<ethers.ContractTransaction>;
    claimRewards: () => Promise<ethers.ContractTransaction>;
    // Add other staking methods as needed
}

interface IGovernanceContract {
    propose: (description: string, targets: string[], values: ethers.BigNumber[], calldatas: string[]) => Promise<ethers.ContractTransaction>;
    vote: (proposalId: ethers.BigNumber, support: number) => Promise<ethers.ContractTransaction>;
    // Add other governance methods as needed
}

interface IGameContract {
    enterGame: (betAmount: ethers.BigNumber, gameId: ethers.BigNumber) => Promise<ethers.ContractTransaction>;
    claimWinnings: (gameId: ethers.BigNumber) => Promise<ethers.ContractTransaction>;
    // Add other game methods as needed
}

// Configuration
const CONTRACT_ADDRESSES = {
    token: '0x...', // BetSwirl token address
    staking: '0x...', // Staking contract address
    governance: '0x...', // Governance contract address
    games: '0x...' // Games contract address
};

const ABI = {
    token: [...], // BetSwirl token ABI
    staking: [...], // Staking contract ABI
    governance: [...], // Governance contract ABI
    games: [...] // Games contract ABI
};

class BetSwirlEconomy {
    private provider: ethers.providers.Web3Provider;
    private signer: ethers.Signer;
    private tokenContract: IBetSwirlToken;
    private stakingContract: IStakingContract;
    private governanceContract: IGovernanceContract;
    private gameContract: IGameContract;

    constructor(provider: ethers.providers.Web3Provider) {
        this.provider = provider;
        this.signer = provider.getSigner();
        
        // Initialize contracts
        this.tokenContract = new Contract(
            CONTRACT_ADDRESSES.token,
            ABI.token,
            this.signer
        ) as IBetSwirlToken;
        
        this.stakingContract = new Contract(
            CONTRACT_ADDRESSES.staking,
            ABI.staking,
            this.signer
        ) as IStakingContract;
        
        this.governanceContract = new Contract(
            CONTRACT_ADDRESSES.governance,
            ABI.governance,
            this.signer
        ) as IGovernanceContract;
        
        this.gameContract = new Contract(
            CONTRACT_ADDRESSES.games,
            ABI.games,
            this.signer
        ) as IGameContract;
    }

    // Token functions
    async getTokenBalance(address: string): Promise<string> {
        try {
            const balance = await this.tokenContract.balanceOf(address);
            return ethers.utils.formatUnits(balance, 18); // Assuming 18 decimals
        } catch (error) {
            console.error('Error fetching token balance:', error);
            throw error;
        }
    }

    async approveTokenSpender(spender: string, amount: string): Promise<void> {
        try {
            const amountWei = ethers.utils.parseUnits(amount, 18);
            const tx = await this.tokenContract.approve(spender, amountWei);
            await tx.wait();
        } catch (error) {
            console.error('Error approving token spender:', error);
            throw error;
        }
    }

    // Staking functions
    async stakeTokens(amount: string): Promise<void> {
        try {
            const amountWei = ethers.utils.parseUnits(amount, 18);
            const tx = await this.stakingContract.stake(amountWei);
            await tx.wait();
        } catch (error) {
            console.error('Error staking tokens:', error);
            throw error;
        }
    }

    async unstakeTokens(amount: string): Promise<void> {
        try {
            const amountWei = ethers.utils.parseUnits(amount, 18);
            const tx = await this.stakingContract.unstake(amountWei);
            await tx.wait();
        } catch (error) {
            console.error('Error unstaking tokens:', error);
            throw error;
        }
    }

    async claimStakingRewards(): Promise<void> {
        try {
            const tx = await this.stakingContract.claimRewards();
            await tx.wait();
        } catch (error) {
            console.error('Error claiming staking rewards:', error);
            throw error;
        }
    }

    // Governance functions
    async createProposal(
        description: string,
        targets: string[],
        values: string[],
        calldatas: string[]
    ): Promise<void> {
        try {
            const valuesWei = values.map(v => ethers.utils.parseUnits(v, 18));
            const tx = await this.governanceContract.propose(
                description,
                targets,
                valuesWei,
                calldatas
            );
            await tx.wait();
        } catch (error) {
            console.error('Error creating proposal:', error);
            throw error;
        }
    }

    async voteOnProposal(proposalId: string, support: number): Promise<void> {
        try {
            const tx = await this.governanceContract.vote(
                ethers.BigNumber.from(proposalId),
                support
            );
            await tx.wait();
        } catch (error) {
            console.error('Error voting on proposal:', error);
            throw error;
        }
    }

    // Game functions
    async enterGame(betAmount: string, gameId: string): Promise<void> {
        try {
            const amountWei = ethers.utils.parseUnits(betAmount, 18);
            const tx = await this.gameContract.enterGame(
                amountWei,
                ethers.BigNumber.from(gameId)
            );
            await tx.wait();
        } catch (error) {
            console.error('Error entering game:', error);
            throw error;
        }
    }

    async claimGameWinnings(gameId: string): Promise<void> {
        try {
            const tx = await this.gameContract.claimWinnings(
                ethers.BigNumber.from(gameId)
            );
            await tx.wait();
        } catch (error) {
            console.error('Error claiming game winnings:', error);
            throw error;
        }
    }
}

// Example usage
async function main() {
    // Initialize provider (e.g., from MetaMask)
    if (typeof window.ethereum !== 'undefined') {
        const provider = new ethers.providers.Web3Provider(window.ethereum);
        
        // Request account access
        await provider.send("eth_requestAccounts", []);
        
        const betSwirl = new BetSwirlEconomy(provider);
        
        // Example token operations
        const balance = await betSwirl.getTokenBalance(await provider.getSigner().getAddress());
        console.log(`Token balance: ${balance}`);
        
        // Example staking
        await betSwirl.approveTokenSpender(CONTRACT_ADDRESSES.staking, "100");
        await betSwirl.stakeTokens("100");
        
        // Example governance
        await betSwirl.createProposal(
            "Increase staking rewards by 2%",
            [CONTRACT_ADDRESSES.staking],
            ["0"],
            ["0x12345678"] // Example calldata
        );
        
        // Example game
        await betSwirl.enterGame("10", "1");
    } else {
        console.error("Web3 provider not found");
    }
}

main().catch(console.error);
```

Note: You'll need to:
1. Replace placeholder contract addresses with actual BetSwirl contract addresses
2. Fill in the ABI definitions for each contract
3. Adjust decimals if BetSwirl token uses something other than 18
4. Add more specific error handling as needed
5. Implement proper type definitions for all contract methods
