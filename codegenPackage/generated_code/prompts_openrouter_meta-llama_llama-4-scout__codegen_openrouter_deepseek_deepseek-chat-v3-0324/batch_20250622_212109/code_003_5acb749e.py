"""
Generated Code Metadata:
========================
Original URL: https://seawallet.app
Prompt: "What are the key features of a digital wallet app like Sea Wallet, and how can they be implemented using JavaScript?"
Generated: DETERMINISTIC_5acb749ee0115bf9
Batch ID: 20250622_212109
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Digital Wallet Class representing core features of a wallet like Sea Wallet
 */
class DigitalWallet {
  /**
   * Initialize wallet with user and balance
   * @param {string} userId - Unique user identifier
   * @param {number} initialBalance - Initial wallet balance
   */
  constructor(userId, initialBalance = 0) {
    if (!userId) throw new Error('User ID is required');
    if (initialBalance < 0) throw new Error('Initial balance cannot be negative');

    this.userId = userId;
    this.balance = initialBalance;
    this.transactionHistory = [];
    this.linkedCards = [];
    this.security = {
      pin: null,
      biometricEnabled: false
    };
  }

  /**
   * Add money to wallet
   * @param {number} amount - Amount to add
   * @returns {number} New balance
   */
  addMoney(amount) {
    if (amount <= 0) throw new Error('Amount must be positive');
    this.balance += amount;
    this._recordTransaction('deposit', amount);
    return this.balance;
  }

  /**
   * Send money to another user
   * @param {string} recipientId - Recipient user ID
   * @param {number} amount - Amount to send
   * @returns {string} Transaction ID
   */
  sendMoney(recipientId, amount) {
    if (!recipientId) throw new Error('Recipient ID is required');
    if (amount <= 0) throw new Error('Amount must be positive');
    if (amount > this.balance) throw new Error('Insufficient balance');

    this.balance -= amount;
    const transactionId = `txn_${Date.now()}`;
    this._recordTransaction('transfer', -amount, recipientId, transactionId);
    return transactionId;
  }

  /**
   * Link payment card to wallet
   * @param {string} cardNumber - Card number
   * @param {string} expiryDate - Expiry date (MM/YY)
   * @param {string} cvv - Card CVV
   * @returns {boolean} Success status
   */
  linkCard(cardNumber, expiryDate, cvv) {
    if (!cardNumber || !expiryDate || !cvv) {
      throw new Error('Card details are incomplete');
    }

    const card = {
      cardNumber: cardNumber.replace(/\s/g, ''),
      expiryDate,
      cvv,
      lastFour: cardNumber.slice(-4)
    };

    this.linkedCards.push(card);
    return true;
  }

  /**
   * Set security PIN
   * @param {string} pin - 4-6 digit PIN
   */
  setPin(pin) {
    if (!/^\d{4,6}$/.test(pin)) {
      throw new Error('PIN must be 4-6 digits');
    }
    this.security.pin = pin;
  }

  /**
   * Enable biometric authentication
   * @param {boolean} enable - Whether to enable biometric auth
   */
  setBiometricAuth(enable) {
    this.security.biometricEnabled = enable;
  }

  /**
   * Get transaction history
   * @param {number} limit - Number of transactions to return
   * @returns {Array} Transaction history
   */
  getTransactionHistory(limit = 10) {
    return this.transactionHistory.slice(0, limit);
  }

  /**
   * Record a transaction
   * @private
   * @param {string} type - Transaction type
   * @param {number} amount - Transaction amount
   * @param {string} [recipient] - Recipient ID
   * @param {string} [transactionId] - Transaction ID
   */
  _recordTransaction(type, amount, recipient = null, transactionId = null) {
    const transaction = {
      id: transactionId || `txn_${Date.now()}`,
      type,
      amount,
      date: new Date().toISOString(),
      balance: this.balance,
      recipient
    };
    this.transactionHistory.unshift(transaction);
  }
}

/**
 * Utility class for QR code generation
 */
class QRService {
  /**
   * Generate QR code data for payment
   * @param {string} userId - User ID
   * @param {number} amount - Payment amount
   * @returns {string} QR code data
   */
  static generatePaymentQR(userId, amount) {
    if (!userId) throw new Error('User ID is required');
    return `wallet:${userId}?amount=${amount}`;
  }
}

/**
 * API Service for wallet operations
 */
class WalletAPIService {
  /**
   * Simulate API request
   * @private
   * @param {string} endpoint - API endpoint
   * @param {Object} data - Request data
   * @returns {Promise<Object>} API response
   */
  static async _makeRequest(endpoint, data) {
    // In a real app, this would be an actual API call
    return new Promise((resolve) => {
      setTimeout(() => {
        resolve({
          success: true,
          data: {
            ...data,
            timestamp: new Date().toISOString()
          }
        });
      }, 500);
    });
  }

  /**
   * Process payment via linked card
   * @param {string} userId - User ID
   * @param {string} cardId - Card identifier
   * @param {number} amount - Payment amount
   * @returns {Promise<Object>} Payment result
   */
  static async processCardPayment(userId, cardId, amount) {
    if (!userId || !cardId) throw new Error('Missing required parameters');
    if (amount <= 0) throw new Error('Amount must be positive');

    return this._makeRequest('/payments/card', {
      userId,
      cardId,
      amount
    });
  }

  /**
   * Verify transaction
   * @param {string} transactionId - Transaction ID
   * @returns {Promise<Object>} Verification result
   */
  static async verifyTransaction(transactionId) {
    if (!transactionId) throw new Error('Transaction ID is required');
    return this._makeRequest('/transactions/verify', { transactionId });
  }
}

// Example usage
/*
const userWallet = new DigitalWallet('user123', 1000);
userWallet.setPin('1234');
userWallet.setBiometricAuth(true);
userWallet.linkCard('4111 1111 1111 1111', '12/25', '123');

userWallet.addMoney(500);
userWallet.sendMoney('user456', 200);

const qrData = QRService.generatePaymentQR('user123', 300);
console.log('Payment QR:', qrData);

WalletAPIService.processCardPayment('user123', 'card_1', 150)
  .then(console.log)
  .catch(console.error);
*/
```
