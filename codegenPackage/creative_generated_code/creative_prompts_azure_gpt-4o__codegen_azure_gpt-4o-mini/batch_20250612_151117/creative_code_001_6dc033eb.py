"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://yearn-in.pages.dev
Prompt: Generate code to lock YFI tokens using Yearn's veYFI governance protocol and retrieve governance participation details.
Generated: DETERMINISTIC_6dc033eb2767fbe2
Batch ID: 20250612_151117
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

// Importing necessary interfaces and libraries
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Interface for the Yearn governance contract
interface IYearnGovernance {
    function lock(uint256 amount) external;
    function unlock(uint256 amount) external;
    function getVotingPower(address account) external view returns (uint256);
    function getDelegation(address account) external view returns (address);
}

// Contract to interact with Yearn's veYFI governance protocol
contract YfiTokenLocker is Ownable {
    // State variables
    IERC20 public yfiToken; // YFI token contract
    IYearnGovernance public veYFI; // veYFI governance contract

    // Events for logging actions
    event TokensLocked(address indexed account, uint256 amount);
    event TokensUnlocked(address indexed account, uint256 amount);

    // Constructor to initialize the YFI token and governance contract addresses
    constructor(address _yfiTokenAddress, address _veYFIAddress) {
        require(_yfiTokenAddress != address(0), "Invalid YFI token address");
        require(_veYFIAddress != address(0), "Invalid veYFI address");
        
        yfiToken = IERC20(_yfiTokenAddress);
        veYFI = IYearnGovernance(_veYFIAddress);
    }

    // Function to lock tokens in the veYFI contract
    function lockTokens(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        require(yfiToken.balanceOf(msg.sender) >= amount, "Insufficient YFI balance");
        
        // Transfer YFI tokens from user to this contract
        yfiToken.transferFrom(msg.sender, address(this), amount);
        
        // Approve and lock YFI tokens in the veYFI governance protocol
        yfiToken.approve(address(veYFI), amount);
        veYFI.lock(amount);
        
        emit TokensLocked(msg.sender, amount);
    }

    // Function to unlock tokens from the veYFI contract
    function unlockTokens(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        
        // Unlock YFI tokens from the veYFI governance protocol
        veYFI.unlock(amount);
        
        // Transfer YFI tokens back to the user
        yfiToken.transfer(msg.sender, amount);
        
        emit TokensUnlocked(msg.sender, amount);
    }

    // Function to get the user's voting power
    function getUserVotingPower(address account) external view returns (uint256) {
        return veYFI.getVotingPower(account);
    }

    // Function to get the delegation address of a user
    function getUserDelegation(address account) external view returns (address) {
        return veYFI.getDelegation(account);
    }

    // Fallback function to receive ETH (if needed)
    receive() external payable {
        // Accept ETH payments
    }

    // Function to withdraw any ERC20 tokens sent to this contract
    function withdrawTokens(address tokenAddress, uint256 amount) external onlyOwner {
        IERC20(tokenAddress).transfer(msg.sender, amount);
    }
}
```
