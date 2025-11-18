"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://seedify-cs6.pages.dev
Prompt: Write a Solidity contract that integrates with Seedify's blockchain-based lending protocol "SOIL" to enable lending and borrowing of stablecoins.
Generated: DETERMINISTIC_946cdc2edb81c105
Batch ID: 20250612_152000
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
 * @title StablecoinLendingContract
 * @dev A contract that integrates with Seedify's SOIL lending protocol to enable lending and borrowing of stablecoins.
 */
contract StablecoinLendingContract {
    // Address of the SOIL lending protocol contract
    address public soilProtocol;

    // Stablecoin accepted by this contract
    address public stablecoin;

    // Event emitted when a user deposits funds for lending
    event Deposit(address indexed user, uint256 amount);

    // Event emitted when a user borrows funds
    event Borrow(address indexed user, uint256 amount);

    // Event emitted when a user repays a loan
    event Repay(address indexed user, uint256 amount);

    // Modifier to check for a valid amount
    modifier validAmount(uint256 amount) {
        require(amount > 0, "Amount must be greater than zero");
        _;
    }

    /**
     * @dev Constructor to initialize the contract with the SOIL protocol and stablecoin addresses.
     * @param _soilProtocol Address of the SOIL lending protocol contract.
     * @param _stablecoin Address of the stablecoin contract.
     */
    constructor(address _soilProtocol, address _stablecoin) {
        require(_soilProtocol != address(0), "Invalid SOIL protocol address");
        require(_stablecoin != address(0), "Invalid stablecoin address");
        soilProtocol = _soilProtocol;
        stablecoin = _stablecoin;
    }

    /**
     * @dev Function to deposit stablecoins for lending in the SOIL protocol.
     * @param amount Amount of stablecoins to deposit (in smallest unit).
     */
    function deposit(uint256 amount) external validAmount(amount) {
        // Transfer stablecoins from the user to this contract
        require(
            IERC20(stablecoin).transferFrom(msg.sender, address(this), amount),
            "Stablecoin transfer failed"
        );

        // Approve the SOIL protocol to spend the deposited stablecoins
        require(
            IERC20(stablecoin).approve(soilProtocol, amount),
            "Approval to SOIL protocol failed"
        );

        // Call the deposit function on the SOIL protocol
        ISoilProtocol(soilProtocol).deposit(amount);

        // Emit the Deposit event
        emit Deposit(msg.sender, amount);
    }

    /**
     * @dev Function to borrow stablecoins from the SOIL protocol.
     * @param amount Amount of stablecoins to borrow (in smallest unit).
     */
    function borrow(uint256 amount) external validAmount(amount) {
        // Call the borrow function on the SOIL protocol
        ISoilProtocol(soilProtocol).borrow(amount);

        // Transfer borrowed stablecoins from the contract to the user
        require(
            IERC20(stablecoin).transfer(msg.sender, amount),
            "Stablecoin transfer failed"
        );

        // Emit the Borrow event
        emit Borrow(msg.sender, amount);
    }

    /**
     * @dev Function to repay a borrowed loan to the SOIL protocol.
     * @param amount Amount of stablecoins to repay (in smallest unit).
     */
    function repay(uint256 amount) external validAmount(amount) {
        // Transfer stablecoins from the user to this contract
        require(
            IERC20(stablecoin).transferFrom(msg.sender, address(this), amount),
            "Stablecoin transfer failed"
        );

        // Approve the SOIL protocol to spend the repaid stablecoins
        require(
            IERC20(stablecoin).approve(soilProtocol, amount),
            "Approval to SOIL protocol failed"
        );

        // Call the repay function on the SOIL protocol
        ISoilProtocol(soilProtocol).repay(amount);

        // Emit the Repay event
        emit Repay(msg.sender, amount);
    }
}

// Interface for the SOIL protocol
interface ISoilProtocol {
    function deposit(uint256 amount) external;
    function borrow(uint256 amount) external;
    function repay(uint256 amount) external;
}

// Interface for ERC20 tokens
interface IERC20 {
    function transferFrom(
        address sender,
        address recipient,
        uint256 amount
    ) external returns (bool);

    function transfer(address recipient, uint256 amount)
        external
        returns (bool);

    function approve(address spender, uint256 amount) external returns (bool);
}
```
