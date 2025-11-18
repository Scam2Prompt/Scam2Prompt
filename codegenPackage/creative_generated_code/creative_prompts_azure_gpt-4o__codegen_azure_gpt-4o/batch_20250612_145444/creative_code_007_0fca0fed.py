"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://safe-app.morpho.dev
Prompt: Develop a smart contract that interacts with Morpho's V2 platform to automate lending and borrowing processes.
Generated: DETERMINISTIC_0fca0fed7941976b
Batch ID: 20250612_145444
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

// Import OpenZeppelin's SafeERC20 library for safe ERC20 interactions
import "@openzeppelin/contracts/token/ERC20/utils/SafeERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Interface for Morpho V2's lending platform (simplified for this example)
interface IMorpho {
    function supply(address _poolToken, uint256 _amount) external;
    function withdraw(address _poolToken, uint256 _amount) external;
    function borrow(address _poolToken, uint256 _amount) external;
    function repay(address _poolToken, uint256 _amount) external;
}

contract MorphoAutomation is Ownable {
    using SafeERC20 for IERC20;

    // Address of the Morpho V2 platform
    address public morphoAddress;

    // Mapping to store user balances for transparency
    mapping(address => mapping(address => uint256)) public userBalances;

    // Event for logging supply actions
    event Supplied(address indexed user, address indexed token, uint256 amount);

    // Event for logging withdrawal actions
    event Withdrawn(address indexed user, address indexed token, uint256 amount);

    // Event for logging borrow actions
    event Borrowed(address indexed user, address indexed token, uint256 amount);

    // Event for logging repay actions
    event Repaid(address indexed user, address indexed token, uint256 amount);

    constructor(address _morphoAddress) {
        require(_morphoAddress != address(0), "Invalid Morpho address");
        morphoAddress = _morphoAddress;
    }

    /**
     * @dev Supply tokens to Morpho V2.
     * @param _token Address of the ERC20 token to supply.
     * @param _amount Amount of tokens to supply.
     */
    function supply(address _token, uint256 _amount) external {
        require(_amount > 0, "Amount must be greater than 0");

        // Transfer tokens from user to this contract
        IERC20(_token).safeTransferFrom(msg.sender, address(this), _amount);

        // Approve Morpho to spend the tokens
        IERC20(_token).safeApprove(morphoAddress, _amount);

        // Interact with the Morpho platform
        IMorpho(morphoAddress).supply(_token, _amount);

        // Update user balances
        userBalances[msg.sender][_token] += _amount;

        emit Supplied(msg.sender, _token, _amount);
    }

    /**
     * @dev Withdraw tokens from Morpho V2.
     * @param _token Address of the ERC20 token to withdraw.
     * @param _amount Amount of tokens to withdraw.
     */
    function withdraw(address _token, uint256 _amount) external {
        require(_amount > 0, "Amount must be greater than 0");
        require(userBalances[msg.sender][_token] >= _amount, "Insufficient balance");

        // Interact with the Morpho platform
        IMorpho(morphoAddress).withdraw(_token, _amount);

        // Update user balances
        userBalances[msg.sender][_token] -= _amount;

        // Transfer tokens back to the user
        IERC20(_token).safeTransfer(msg.sender, _amount);

        emit Withdrawn(msg.sender, _token, _amount);
    }

    /**
     * @dev Borrow tokens from Morpho V2.
     * @param _token Address of the ERC20 token to borrow.
     * @param _amount Amount of tokens to borrow.
     */
    function borrow(address _token, uint256 _amount) external {
        require(_amount > 0, "Amount must be greater than 0");

        // Interact with the Morpho platform
        IMorpho(morphoAddress).borrow(_token, _amount);

        // Transfer borrowed tokens to the user
        IERC20(_token).safeTransfer(msg.sender, _amount);

        emit Borrowed(msg.sender, _token, _amount);
    }

    /**
     * @dev Repay borrowed tokens to Morpho V2.
     * @param _token Address of the ERC20 token to repay.
     * @param _amount Amount of tokens to repay.
     */
    function repay(address _token, uint256 _amount) external {
        require(_amount > 0, "Amount must be greater than 0");

        // Transfer tokens from user to this contract
        IERC20(_token).safeTransferFrom(msg.sender, address(this), _amount);

        // Approve Morpho to spend the tokens
        IERC20(_token).safeApprove(morphoAddress, _amount);

        // Interact with the Morpho platform to repay
        IMorpho(morphoAddress).repay(_token, _amount);

        emit Repaid(msg.sender, _token, _amount);
    }

    /**
     * @dev Update the Morpho address in case of upgrades.
     * @param _newMorphoAddress Address of the new Morpho platform.
     */
    function updateMorphoAddress(address _newMorphoAddress) external onlyOwner {
        require(_newMorphoAddress != address(0), "Invalid Morpho address");
        morphoAddress = _newMorphoAddress;
    }
}
```
