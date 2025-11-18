"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bafybeigfvszp46s3snhdvtr6cjaqasj42yritad4wljrbrflup5v5itywu.ipfs.dweb.link
Prompt: Develop a smart contract in Solidity for burning FLOKI tokens automatically based on the fee structure outlined in the FlokiFi Locker documentation.
Generated: DETERMINISTIC_9ec9d1de63003f9b
Batch ID: 20250612_152924
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
 * @title FlokiTokenBurner
 * @dev A smart contract for burning FLOKI tokens automatically based on a fee structure.
 *      Implements best practices for Solidity, including error handling and gas efficiency.
 */
interface IERC20 {
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);

    function balanceOf(address account) external view returns (uint256);

    function burn(uint256 amount) external;
}

contract FlokiTokenBurner {
    // State variables
    address public owner;             // Owner of the contract
    IERC20 public flokiToken;         // FLOKI token contract
    uint256 public burnPercentage;    // Fee percentage for burning tokens (e.g., 3 for 3%)

    event TokensBurned(address indexed user, uint256 amountBurned, uint256 feePercentage);
    event BurnPercentageUpdated(uint256 oldPercentage, uint256 newPercentage);

    // Modifier to restrict access to the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can call this function");
        _;
    }

    /**
     * @dev Constructor to initialize the contract.
     * @param _flokiToken Address of the FLOKI ERC20 token contract.
     * @param _burnPercentage Initial percentage of tokens to burn.
     */
    constructor(address _flokiToken, uint256 _burnPercentage) {
        require(_flokiToken != address(0), "Invalid FLOKI token address");
        require(_burnPercentage > 0 && _burnPercentage <= 100, "Burn percentage must be between 1 and 100");

        owner = msg.sender;
        flokiToken = IERC20(_flokiToken);
        burnPercentage = _burnPercentage;
    }

    /**
     * @dev Updates the burn percentage. Can only be called by the owner.
     * @param _newBurnPercentage New percentage of tokens to burn.
     */
    function updateBurnPercentage(uint256 _newBurnPercentage) external onlyOwner {
        require(_newBurnPercentage > 0 && _newBurnPercentage <= 100, "Burn percentage must be between 1 and 100");

        uint256 oldPercentage = burnPercentage;
        burnPercentage = _newBurnPercentage;

        emit BurnPercentageUpdated(oldPercentage, _newBurnPercentage);
    }

    /**
     * @dev Burns a percentage of the specified token amount.
     * @param amount The total amount of tokens being processed for burning.
     * @notice The caller must approve this contract to spend the tokens beforehand.
     */
    function burnTokens(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");

        uint256 burnAmount = (amount * burnPercentage) / 100; // Calculate the burn amount
        require(burnAmount > 0, "Burn amount must be greater than zero");

        // Transfer tokens from the user to this contract
        bool success = flokiToken.transferFrom(msg.sender, address(this), amount);
        require(success, "Token transfer failed");

        // Burn the calculated amount
        flokiToken.burn(burnAmount);

        emit TokensBurned(msg.sender, burnAmount, burnPercentage);
    }

    /**
     * @dev Withdraw any accidentally sent tokens to the contract address. Can only be called by the owner.
     * @param token Address of the token to withdraw.
     * @param amount Amount of tokens to withdraw.
     */
    function recoverTokens(address token, uint256 amount) external onlyOwner {
        require(token != address(0), "Invalid token address");
        require(amount > 0, "Amount must be greater than zero");

        IERC20(token).transferFrom(address(this), owner, amount);
    }
}
```
