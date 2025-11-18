"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://puffer.pages.dev
Prompt: Develop a smart contract that interacts with Puffer's liquid staking protocol to automate the swapping of ETH for pufETH and reinvestment into DeFi platforms.
Generated: DETERMINISTIC_bebf30274774ced2
Batch ID: 20250612_151408
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

// Import necessary interfaces and libraries
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

interface IPufferStaking {
    function deposit() external payable returns (uint256);
    function withdraw(uint256 amount) external;
    function balanceOf(address account) external view returns (uint256);
}

interface IDeFiPlatform {
    function invest(uint256 amount) external;
}

contract SmartStaking is Ownable {
    using SafeMath for uint256;

    // Address of Puffer's liquid staking contract
    IPufferStaking public pufferStaking;
    
    // Address of the DeFi platform contract
    IDeFiPlatform public deFiPlatform;

    // Event to track deposits and reinvestments
    event Reinvested(uint256 amount);

    // Constructor to initialize contracts
    constructor(address _pufferStaking, address _deFiPlatform) {
        require(_pufferStaking != address(0), "Invalid Puffer Staking address");
        require(_deFiPlatform != address(0), "Invalid DeFi Platform address");
        
        pufferStaking = IPufferStaking(_pufferStaking);
        deFiPlatform = IDeFiPlatform(_deFiPlatform);
    }

    // Function to swap ETH for pufETH and invest into DeFi
    function swapAndInvest() external payable onlyOwner {
        require(msg.value > 0, "Must send ETH to swap");

        // Deposit ETH into Puffer's liquid staking protocol
        uint256 pufETHAmount = pufferStaking.deposit{value: msg.value}();
        
        // Reinvest the received pufETH into the DeFi platform
        deFiPlatform.invest(pufETHAmount);
        
        emit Reinvested(pufETHAmount);
    }

    // Function to withdraw pufETH and send it back to the owner
    function withdraw(uint256 amount) external onlyOwner {
        // Withdraw from Puffer's liquid staking protocol
        pufferStaking.withdraw(amount);
    }

    // Receive ETH function to allow the contract to receive ETH
    receive() external payable {}
    
    // Fallback function to handle plain ETH transfers
    fallback() external payable {}
}
```
