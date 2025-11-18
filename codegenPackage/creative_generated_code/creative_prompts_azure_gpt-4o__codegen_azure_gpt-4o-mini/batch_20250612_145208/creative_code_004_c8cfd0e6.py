"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lite-nuxt-git-f-veda-vault-instadapp-eng.vercel.app
Prompt: Develop a smart contract that integrates with Instadapp Lite to execute cross-protocol refinancing strategies, leveraging protocols like AAVE and Compound.
Generated: DETERMINISTIC_c8cfd0e6c5f834d7
Batch ID: 20250612_145208
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

// Import required interfaces from AAVE, Compound, and Instadapp Lite
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@aave/protocol-v2/contracts/interfaces/IAaveLendingPool.sol";
import "@compound/contracts/CToken.sol";
import "@instadapp/interfaces/IAaveV2.sol";
import "@instadapp/interfaces/ICompound.sol";

contract CrossProtocolRefinance {
    // State variables for managing protocol addresses
    IAaveLendingPool public aaveLendingPool;
    ICompound public compound;
    
    // Address of the token being used (e.g., DAI, USDC)
    IERC20 public stableToken;

    // Event to be emitted after refinancing
    event RefinanceExecuted(address indexed user, uint256 amount);

    // Constructor to initialize contract with AAVE, Compound, and token addresses
    constructor(
        address _aaveLendingPool,
        address _compound,
        address _stableToken
    ) {
        aaveLendingPool = IAaveLendingPool(_aaveLendingPool);
        compound = ICompound(_compound);
        stableToken = IERC20(_stableToken);
    }

    // Function to execute refinancing from AAVE to Compound or vice versa
    function refinance(uint256 amount, bool fromAaveToCompound) external {
        require(amount > 0, "Amount must be greater than zero");
        
        // Transfer tokens from the user to the contract
        stableToken.transferFrom(msg.sender, address(this), amount);
        
        // Check if the move is from AAVE to Compound or the opposite
        if (fromAaveToCompound) {
            // Deposit tokens into AAVE
            stableToken.approve(address(aaveLendingPool), amount);
            aaveLendingPool.deposit(address(stableToken), amount, address(this), 0);

            // Borrow from Compound
            uint256 cTokenAmount = compound.borrow(amount);
            require(cTokenAmount > 0, "Borrowing failed");

            // Emit event after refinancing
            emit RefinanceExecuted(msg.sender, amount);
        } else {
            // Borrow from AAVE
            uint256 aTokenAmount = aaveLendingPool.borrow(amount, 2, 0, address(this)); // 2 indicates stable rate
            require(aTokenAmount > 0, "Borrowing failed");

            // Deposit the borrowed amount into Compound
            stableToken.approve(address(compound), aTokenAmount);
            compound.mint(aTokenAmount);
            
            // Emit event after refinancing
            emit RefinanceExecuted(msg.sender, amount);
        }
    }

    // Function to withdraw tokens back to the user
    function withdraw(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");

        // Withdraw logic from Compound or AAVE depending on the state
        // Placeholder for withdraw logic, needs to be implemented based on borrowed state
        stableToken.transfer(msg.sender, amount);
    }

    // Fallback function to prevent ether from being sent to the contract
    receive() external payable {
        revert("Contract does not accept ether");
    }
}
```
