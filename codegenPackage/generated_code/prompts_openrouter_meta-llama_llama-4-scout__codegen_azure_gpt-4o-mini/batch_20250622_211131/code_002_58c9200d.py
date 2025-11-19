"""
Generated Code Metadata:
========================
Original URL: https://to-ousd.pages.dev
Prompt: Generate a code example in Solidity to create a simple smart contract that utilizes OUSD's automated, on-chain, blue-chip stablecoin strategies, such as deploying funds to Morpho's Compound or Aave markets.
Generated: DETERMINISTIC_58c9200d4ba31c9d
Batch ID: 20250622_211131
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

// Importing the necessary interfaces for interacting with Aave and Morpho
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@aave/protocol-v2/contracts/interfaces/ILendingPool.sol";
import "@morpho.xyz/morpho-core/contracts/interfaces/IMorpho.sol";

contract OUSDStrategy {
    // State variables
    address public owner;
    ILendingPool public aaveLendingPool;
    IMorpho public morpho;
    IERC20 public stablecoin;

    // Events for logging
    event Deposited(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount);
    event StrategyExecuted(string strategy);

    // Modifier to restrict access to the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Not the contract owner");
        _;
    }

    // Constructor to initialize the contract with necessary parameters
    constructor(address _aaveLendingPool, address _morpho, address _stablecoin) {
        owner = msg.sender;
        aaveLendingPool = ILendingPool(_aaveLendingPool);
        morpho = IMorpho(_morpho);
        stablecoin = IERC20(_stablecoin);
    }

    // Function to deposit stablecoins into Aave
    function depositToAave(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        
        // Transfer stablecoins from the owner to this contract
        stablecoin.transferFrom(msg.sender, address(this), amount);
        
        // Approve the Aave lending pool to spend the stablecoins
        stablecoin.approve(address(aaveLendingPool), amount);
        
        // Deposit stablecoins into Aave
        aaveLendingPool.deposit(address(stablecoin), amount, address(this), 0);
        
        emit Deposited(msg.sender, amount);
        emit StrategyExecuted("Deposited to Aave");
    }

    // Function to withdraw stablecoins from Aave
    function withdrawFromAave(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        
        // Withdraw stablecoins from Aave
        aaveLendingPool.withdraw(address(stablecoin), amount, address(this));
        
        // Transfer the withdrawn stablecoins back to the owner
        stablecoin.transfer(msg.sender, amount);
        
        emit Withdrawn(msg.sender, amount);
        emit StrategyExecuted("Withdrawn from Aave");
    }

    // Function to deposit stablecoins into Morpho
    function depositToMorpho(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        
        // Transfer stablecoins from the owner to this contract
        stablecoin.transferFrom(msg.sender, address(this), amount);
        
        // Approve Morpho to spend the stablecoins
        stablecoin.approve(address(morpho), amount);
        
        // Deposit stablecoins into Morpho
        morpho.supply(address(stablecoin), amount);
        
        emit Deposited(msg.sender, amount);
        emit StrategyExecuted("Deposited to Morpho");
    }

    // Function to withdraw stablecoins from Morpho
    function withdrawFromMorpho(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        
        // Withdraw stablecoins from Morpho
        morpho.withdraw(address(stablecoin), amount);
        
        // Transfer the withdrawn stablecoins back to the owner
        stablecoin.transfer(msg.sender, amount);
        
        emit Withdrawn(msg.sender, amount);
        emit StrategyExecuted("Withdrawn from Morpho");
    }

    // Function to change the owner of the contract
    function transferOwnership(address newOwner) external onlyOwner {
        require(newOwner != address(0), "New owner is the zero address");
        owner = newOwner;
    }
}
```
