"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://to-ousd.pages.dev
Prompt: Explain how OUSD utilizes Morpho and Aave for yield generation, and provide an example of how to implement this in a smart contract.
Generated: DETERMINISTIC_7aefcc88aad086e8
Batch ID: 20250612_162746
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

// Importing required interfaces from Aave and Morpho
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@aave/protocol-v2/contracts/interfaces/IAaveLendingPool.sol";
import "@morpho-org/morpho-ape/contracts/interfaces/IMorpho.sol";

contract OUSDMorphoAaveYieldStrategy {
    // Storage variables
    IERC20 public immutable ousd; // OUSD token
    IAaveLendingPool public immutable aaveLendingPool; // Aave Lending Pool
    IMorpho public immutable morpho; // Morpho protocol
    
    // Events for monitoring deposits and withdrawals
    event Deposited(uint256 amount);
    event Withdrawn(uint256 amount);
    
    // Constructor to initialize token and protocol addresses
    constructor(
        address _ousd,
        address _aaveLendingPool,
        address _morpho
    ) {
        require(_ousd != address(0), "OUSD address cannot be zero");
        require(_aaveLendingPool != address(0), "Aave LendingPool address cannot be zero");
        require(_morpho != address(0), "Morpho address cannot be zero");

        ousd = IERC20(_ousd);
        aaveLendingPool = IAaveLendingPool(_aaveLendingPool);
        morpho = IMorpho(_morpho);
    }

    // Function to deposit OUSD into Aave and then utilize Morpho for yield generation
    function deposit(uint256 amount) external {
        require(amount > 0, "Deposit amount must be greater than zero");
        
        // Transfer OUSD from msg.sender to this contract
        require(ousd.transferFrom(msg.sender, address(this), amount), "Transfer failed");

        // Approve Aave to spend OUSD
        ousd.approve(address(aaveLendingPool), amount);
        
        // Deposit OUSD into Aave
        aaveLendingPool.deposit(address(ousd), amount, address(this), 0);
        
        // Utilize Morpho for yield generation
        morpho.supply(address(ousd), amount, address(this));
        
        emit Deposited(amount);
    }

    // Function to withdraw funds from Morpho and Aave
    function withdraw(uint256 amount) external {
        require(amount > 0, "Withdraw amount must be greater than zero");
        
        // Withdraw from Morpho
        morpho.withdraw(address(ousd), amount, address(this));
        
        // Withdraw from Aave
        aaveLendingPool.withdraw(address(ousd), amount, address(this));
        
        // Transfer OUSD back to msg.sender
        require(ousd.transfer(msg.sender, amount), "Transfer failed");
        
        emit Withdrawn(amount);
    }

    // Function to check the balance of OUSD held by this contract
    function balance() external view returns (uint256) {
        return ousd.balanceOf(address(this));
    }
}
```
