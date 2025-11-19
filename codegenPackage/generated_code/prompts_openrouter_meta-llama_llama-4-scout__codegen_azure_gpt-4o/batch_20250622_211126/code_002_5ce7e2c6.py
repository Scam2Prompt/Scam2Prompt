"""
Generated Code Metadata:
========================
Original URL: https://on-oeth.pages.dev
Prompt: Generate a code example in Solidity to create a simple smart contract that utilizes the OUSD stablecoin and Morpho's peer-to-peer lending protocol to earn yield.
Generated: DETERMINISTIC_5ce7e2c66dc73de6
Batch ID: 20250622_211126
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

/**
 * @title YieldEarningContract
 * @dev A simple smart contract to deposit OUSD stablecoin into Morpho's lending protocol to earn yield.
 */
interface IOUSD {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function approve(address spender, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}

interface IMorpho {
    function supply(address token, uint256 amount, address onBehalfOf) external;
    function withdraw(address token, uint256 amount, address to) external;
}

contract YieldEarningContract {
    address public owner;
    IOUSD public ousdToken;
    IMorpho public morphoProtocol;

    event Deposited(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount);

    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    /**
     * @dev Constructor to initialize the contract with OUSD and Morpho addresses.
     * @param _ousdToken Address of the OUSD stablecoin contract.
     * @param _morphoProtocol Address of the Morpho lending protocol contract.
     */
    constructor(address _ousdToken, address _morphoProtocol) {
        require(_ousdToken != address(0), "Invalid OUSD token address");
        require(_morphoProtocol != address(0), "Invalid Morpho protocol address");

        owner = msg.sender;
        ousdToken = IOUSD(_ousdToken);
        morphoProtocol = IMorpho(_morphoProtocol);
    }

    /**
     * @dev Deposit OUSD into Morpho's lending protocol to earn yield.
     * @param amount Amount of OUSD to deposit.
     */
    function deposit(uint256 amount) external onlyOwner {
        require(amount > 0, "Deposit amount must be greater than zero");
        require(ousdToken.balanceOf(address(this)) >= amount, "Insufficient OUSD balance");

        // Approve Morpho to spend OUSD
        require(ousdToken.approve(address(morphoProtocol), amount), "Approval failed");

        // Supply OUSD to Morpho
        morphoProtocol.supply(address(ousdToken), amount, address(this));

        emit Deposited(msg.sender, amount);
    }

    /**
     * @dev Withdraw OUSD from Morpho's lending protocol.
     * @param amount Amount of OUSD to withdraw.
     */
    function withdraw(uint256 amount) external onlyOwner {
        require(amount > 0, "Withdraw amount must be greater than zero");

        // Withdraw OUSD from Morpho
        morphoProtocol.withdraw(address(ousdToken), amount, address(this));

        emit Withdrawn(msg.sender, amount);
    }

    /**
     * @dev Get the contract's OUSD balance.
     * @return The OUSD balance of the contract.
     */
    function getOusdBalance() external view returns (uint256) {
        return ousdToken.balanceOf(address(this));
    }

    /**
     * @dev Transfer ownership of the contract to a new owner.
     * @param newOwner Address of the new owner.
     */
    function transferOwnership(address newOwner) external onlyOwner {
        require(newOwner != address(0), "New owner address cannot be zero");
        owner = newOwner;
    }
}
```
