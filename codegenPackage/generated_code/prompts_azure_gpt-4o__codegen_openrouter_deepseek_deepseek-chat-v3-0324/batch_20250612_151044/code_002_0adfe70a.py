"""
Generated Code Metadata:
========================
Original URL: https://exchange24h.com
Prompt: Generate code in JavaScript to create a responsive user interface for slot deposit transactions, incorporating features like "promo khusus" and "modal kecil" as described on the site.
Generated: DETERMINISTIC_0adfe70af8688527
Batch ID: 20250612_151044
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Slot Deposit Transaction UI Component
class SlotDepositUI {
  constructor() {
    this.initUI();
    this.bindEvents();
  }

  initUI() {
    // Create main container
    this.container = document.createElement('div');
    this.container.className = 'slot-deposit-container';
    this.container.innerHTML = `
      <div class="header">
        <h2>Slot Deposit</h2>
        <div class="balance-display">
          <span>Balance: </span>
          <span class="balance-amount">Rp0</span>
        </div>
      </div>
      
      <div class="deposit-section">
        <div class="input-group">
          <label for="deposit-amount">Deposit Amount</label>
          <input type="number" id="deposit-amount" min="10000" step="10000" placeholder="Minimum Rp10,000">
        </div>
        
        <div class="promo-section">
          <div class="promo-toggle">
            <input type="checkbox" id="use-promo">
            <label for="use-promo">Gunakan Promo Khusus</label>
          </div>
          <div class="promo-options hidden">
            <select id="promo-select">
              <option value="">Pilih Promo</option>
              <option value="bonus50">Bonus 50%</option>
              <option value="modal-kecil">Modal Kecil</option>
              <option value="cashback10">Cashback 10%</option>
            </select>
            <div class="promo-details hidden" id="promo-details"></div>
          </div>
        </div>
        
        <div class="payment-methods">
          <h3>Payment Methods</h3>
          <div class="method-grid">
            <div class="method-option" data-method="bank-transfer">
              <img src="icons/bank-transfer.png" alt="Bank Transfer">
              <span>Bank Transfer</span>
            </div>
            <div class="method-option" data-method="e-wallet">
              <img src="icons/e-wallet.png" alt="E-Wallet">
              <span>E-Wallet</span>
            </div>
            <div class="method-option" data-method="pulsa">
              <img src="icons/pulsa.png" alt="Pulsa">
              <span>Pulsa</span>
            </div>
          </div>
        </div>
        
        <button class="deposit-button" id="deposit-button">Deposit Now</button>
      </div>
      
      <div class="transaction-history hidden">
        <h3>Recent Transactions</h3>
        <div class="history-list"></div>
      </div>
    `;

    document.body.appendChild(this.container);
    this.loadBalance();
    this.loadTransactionHistory();
  }

  bindEvents() {
    // Promo toggle
    document.getElementById('use-promo').addEventListener('change', (e) => {
      const promoOptions = document.querySelector('.promo-options');
      if (e.target.checked) {
        promoOptions.classList.remove('hidden');
      } else {
        promoOptions.classList.add('hidden');
        document.getElementById('promo-details').classList.add('hidden');
      }
    });

    // Promo selection
    document.getElementById('promo-select').addEventListener('change', (e) => {
      const promoDetails = document.getElementById('promo-details');
      if (e.target.value) {
        promoDetails.classList.remove('hidden');
        this.showPromoDetails(e.target.value);
      } else {
        promoDetails.classList.add('hidden');
      }
    });

    // Payment method selection
    document.querySelectorAll('.method-option').forEach(option => {
      option.addEventListener('click', () => {
        document.querySelectorAll('.method-option').forEach(opt => {
          opt.classList.remove('selected');
        });
        option.classList.add('selected');
      });
    });

    // Deposit button
    document.getElementById('deposit-button').addEventListener('click', () => {
      this.processDeposit();
    });

    // Responsive adjustments
    window.addEventListener('resize', this.handleResponsiveLayout.bind(this));
  }

  showPromoDetails(promoCode) {
    const promoDetails = document.getElementById('promo-details');
    let details = '';
    
    switch(promoCode) {
      case 'bonus50':
        details = '<p>Dapatkan bonus 50% dari deposit Anda (maksimal Rp500,000)</p>';
        break;
      case 'modal-kecil':
        details = `
          <p>Promo Modal Kecil:</p>
          <ul>
            <li>Deposit minimal Rp10,000</li>
            <li>Bonus 20% untuk deposit pertama</li>
            <li>Bebas biaya admin</li>
          </ul>
        `;
        break;
      case 'cashback10':
        details = '<p>Dapatkan cashback 10% dari kekalahan Anda (maksimal Rp200,000 per hari)</p>';
        break;
      default:
        details = '<p>Promo tidak tersedia</p>';
    }
    
    promoDetails.innerHTML = details;
  }

  async loadBalance() {
    try {
      // Simulate API call
      const response = await this.fetchBalance();
      document.querySelector('.balance-amount').textContent = `Rp${response.balance.toLocaleString()}`;
    } catch (error) {
      console.error('Failed to load balance:', error);
      this.showError('Gagal memuat saldo. Silakan coba lagi.');
    }
  }

  async loadTransactionHistory() {
    try {
      // Simulate API call
      const response = await this.fetchTransactions();
      const historyList = document.querySelector('.history-list');
      
      if (response.transactions.length > 0) {
        document.querySelector('.transaction-history').classList.remove('hidden');
        historyList.innerHTML = response.transactions.map(tx => `
          <div class="transaction-item">
            <div class="tx-date">${tx.date}</div>
            <div class="tx-amount ${tx.type}">${tx.type === 'deposit' ? '+' : '-'}Rp${tx.amount.toLocaleString()}</div>
            <div class="tx-status ${tx.status}">${tx.status}</div>
          </div>
        `).join('');
      }
    } catch (error) {
      console.error('Failed to load transaction history:', error);
    }
  }

  async processDeposit() {
    const amountInput = document.getElementById('deposit-amount');
    const amount = parseFloat(amountInput.value);
    const promoSelect = document.getElementById('promo-select');
    const promoCode = promoSelect.value;
    const selectedMethod = document.querySelector('.method-option.selected');
    
    // Validation
    if (!amount || amount < 10000) {
      this.showError('Minimum deposit adalah Rp10,000');
      return;
    }
    
    if (!selectedMethod) {
      this.showError('Silakan pilih metode pembayaran');
      return;
    }
    
    const paymentMethod = selectedMethod.dataset.method;
    
    try {
      // Show loading state
      const depositButton = document.getElementById('deposit-button');
      depositButton.disabled = true;
      depositButton.textContent = 'Processing...';
      
      // Simulate API call
      const response = await this.submitDeposit({
        amount,
        promoCode,
        paymentMethod
      });
      
      // Update UI
      this.showSuccess('Deposit berhasil diproses!');
      this.loadBalance();
      this.loadTransactionHistory();
      
      // Reset form
      amountInput.value = '';
      if (document.getElementById('use-promo').checked) {
        document.getElementById('use-promo').click();
      }
      selectedMethod.classList.remove('selected');
      
    } catch (error) {
      console.error('Deposit failed:', error);
      this.showError('Deposit gagal. Silakan coba lagi.');
    } finally {
      const depositButton = document.getElementById('deposit-button');
      depositButton.disabled = false;
      depositButton.textContent = 'Deposit Now';
    }
  }

  showError(message) {
    const errorElement = document.createElement('div');
    errorElement.className = 'error-message';
    errorElement.textContent = message;
    
    const depositSection = document.querySelector('.deposit-section');
    const existingError = depositSection.querySelector('.error-message');
    if (existingError) {
      depositSection.removeChild(existingError);
    }
    
    depositSection.insertBefore(errorElement, depositSection.firstChild);
    
    setTimeout(() => {
      errorElement.classList.add('fade-out');
      setTimeout(() => {
        if (errorElement.parentNode) {
          depositSection.removeChild(errorElement);
        }
      }, 500);
    }, 5000);
  }

  showSuccess(message) {
    const successElement = document.createElement('div');
    successElement.className = 'success-message';
    successElement.textContent = message;
    
    const depositSection = document.querySelector('.deposit-section');
    const existingSuccess = depositSection.querySelector('.success-message');
    if (existingSuccess) {
      depositSection.removeChild(existingSuccess);
    }
    
    depositSection.insertBefore(successElement, deposit
