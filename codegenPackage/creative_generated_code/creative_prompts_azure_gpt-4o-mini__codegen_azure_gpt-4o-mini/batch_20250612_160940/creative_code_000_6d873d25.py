"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bafybeib57x2i3wjq47prbs73dicwjrqmh4z6xefonlbo3qd3bojsesqjra.ipfs.dweb.link
Prompt: How can I implement restaking of ETH using EigenLayer to provide cryptoeconomic security for new protocols?
Generated: DETERMINISTIC_6d873d25c89bb175
Batch ID: 20250612_160940
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

interface IEigenLayer {
    function restake(address staker, uint256 amount) external;
    function withdraw(address staker, uint256 amount) external;
}

contract ETHRestaking is Ownable {
    // State variables
    IERC20 public immutable ethToken; // ERC20 token representing staked ETH
    IEigenLayer public immutable eigenLayer; // EigenLayer interface

    // Events for logging actions
    event Restaked(address indexed staker, uint256 amount);
    event Withdrawn(address indexed staker, uint256 amount);

    // Constructor to initialize the contract with the ETH token and EigenLayer instance
    constructor(IERC20 _ethToken, IEigenLayer _eigenLayer) {
        require(address(_ethToken) != address(0), "Invalid token address");
        require(address(_eigenLayer) != address(0), "Invalid EigenLayer address");

        ethToken = _ethToken;
        eigenLayer = _eigenLayer;
    }

    // Function to restake ETH
    function restake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        require(ethToken.balanceOf(msg.sender) >= amount, "Insufficient balance");

        // Transfer the tokens to this contract
        ethToken.transferFrom(msg.sender, address(this), amount);

        // Call EigenLayer's restake function
        eigenLayer.restake(msg.sender, amount);

        emit Restaked(msg.sender, amount);
    }

    // Function to withdraw staked ETH
    function withdraw(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");

        // Call EigenLayer's withdraw function
        eigenLayer.withdraw(msg.sender, amount);

        // Transfer the tokens back to the staker
        ethToken.transfer(msg.sender, amount);

        emit Withdrawn(msg.sender, amount);
    }
}
```
