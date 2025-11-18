"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://thoreumcapital-migrate.pages.dev
Prompt: Create a smart contract function to facilitate the migration of THOREUM-BNB Biswap LP to THOREUM-SOL Pancake LP, ensuring the swap rate of 1:1 is adhered to.
Generated: DETERMINISTIC_4cb91261b890ee61
Batch ID: 20250612_151246
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

/**
 * @title LP Migration Smart Contract
 * @dev Facilitates the migration of THOREUM-BNB Biswap LP tokens to THOREUM-SOL Pancake LP tokens at a 1:1 swap rate.
 */
contract LPMigration {
    // Address of the THOREUM-BNB Biswap LP token contract
    IERC20 public biswapLP;

    // Address of the THOREUM-SOL Pancake LP token contract
    IERC20 public pancakeLP;

    // Address of the owner of the contract
    address public owner;

    // Event emitted when migration has successfully occurred
    event Migration(address indexed user, uint256 amount);

    /**
     * @dev Modifier to restrict access to only the owner of the contract.
     */
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    /**
     * @dev Constructor to initialize the LP token contracts and the owner.
     * @param _biswapLP Address of the THOREUM-BNB Biswap LP token contract.
     * @param _pancakeLP Address of the THOREUM-SOL Pancake LP token contract.
     */
    constructor(IERC20 _biswapLP, IERC20 _pancakeLP) {
        biswapLP = _biswapLP;
        pancakeLP = _pancakeLP;
        owner = msg.sender;
    }

    /**
     * @dev Migrates THOREUM-BNB Biswap LP tokens to THOREUM-SOL Pancake LP tokens at a 1:1 rate.
     * @param _amount Number of LP tokens to migrate.
     */
    function migrate(uint256 _amount) external {
        require(_amount > 0, "Amount must be greater than zero");

        // Transfer Biswap LP tokens from user to contract
        require(
            biswapLP.transferFrom(msg.sender, address(this), _amount),
            "Failed to transfer Biswap LP tokens"
        );

        // Transfer Pancake LP tokens from contract to user
        require(
            pancakeLP.transfer(msg.sender, _amount),
            "Failed to transfer Pancake LP tokens"
        );

        emit Migration(msg.sender, _amount);
    }

    /**
     * @dev Allows the owner to withdraw any tokens mistakenly sent to the contract.
     * @param _token Address of the token to withdraw.
     * @param _amount Amount of tokens to withdraw.
     */
    function emergencyWithdraw(address _token, uint256 _amount) external onlyOwner {
        IERC20(_token).transfer(owner, _amount);
    }
}

/**
 * @dev Minimal interface for ERC20 token functionality.
 */
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);

    function transferFrom(
        address sender,
        address recipient,
        uint256 amount
    ) external returns (bool);
}
```
