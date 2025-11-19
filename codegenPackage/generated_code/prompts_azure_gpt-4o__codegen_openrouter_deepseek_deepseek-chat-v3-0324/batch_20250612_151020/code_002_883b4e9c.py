"""
Generated Code Metadata:
========================
Original URL: https://mommyanew.com
Prompt: Generate JavaScript code for a web-based parental control dashboard that allows single moms to monitor and adjust their children's screen time, referencing the strategies outlined in Mommy Anew's content.
Generated: DETERMINISTIC_883b4e9c5bdab911
Batch ID: 20250612_151020
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Parental Control Dashboard for Single Moms
// Implements screen time monitoring and adjustment features
// References strategies from Mommy Anew's content

class ParentalControlDashboard {
  constructor() {
    this.children = [];
    this.screenTimeRules = {};
    this.currentUser = null;
    this.initialize();
  }

  // Initialize the dashboard
  initialize() {
    this.loadUserData();
    this.setupEventListeners();
    this.renderDashboard();
  }

  // Load user data from localStorage or initialize defaults
  loadUserData() {
    const storedData = localStorage.getItem('parentalControlData');
    if (storedData) {
      const data = JSON.parse(storedData);
      this.children = data.children || [];
      this.screenTimeRules = data.screenTimeRules || {};
      this.currentUser = data.currentUser || null;
    } else {
      this.setDefaultValues();
    }
  }

  // Set default values for new users
  setDefaultValues() {
    this.children = [];
    this.screenTimeRules = {
      defaultDailyLimit: 120, // minutes
      bedtimeLock: { enabled: true, start: '20:00', end: '07:00' },
      educationalBonus: { enabled: true, bonusMinutes: 30 }
    };
    this.currentUser = {
      name: 'Parent',
      email: '',
      subscription: 'basic'
    };
    this.saveData();
  }

  // Save data to localStorage
  saveData() {
    const data = {
      children: this.children,
      screenTimeRules: this.screenTimeRules,
      currentUser: this.currentUser
    };
    localStorage.setItem('parentalControlData', JSON.stringify(data));
  }

  // Setup event listeners for UI interactions
  setupEventListeners() {
    document.addEventListener('DOMContentLoaded', () => {
      // Add child form
      document.getElementById('add-child-form').addEventListener('submit', (e) => {
        e.preventDefault();
        this.addChild();
      });

      // Update screen time rules
      document.getElementById('screen-time-form').addEventListener('submit', (e) => {
        e.preventDefault();
        this.updateScreenTimeRules();
      });

      // Toggle bedtime lock
      document.getElementById('bedtime-toggle').addEventListener('change', (e) => {
        this.toggleBedtimeLock(e.target.checked);
      });

      // Toggle educational bonus
      document.getElementById('bonus-toggle').addEventListener('change', (e) => {
        this.toggleEducationalBonus(e.target.checked);
      });
    });
  }

  // Add a new child profile
  addChild() {
    const name = document.getElementById('child-name').value.trim();
    const age = parseInt(document.getElementById('child-age').value);
    const device = document.getElementById('child-device').value.trim();

    if (!name || isNaN(age) || !device) {
      this.showAlert('Please fill all fields with valid data', 'error');
      return;
    }

    const newChild = {
      id: Date.now().toString(),
      name,
      age,
      device,
      screenTime: {
        dailyLimit: this.screenTimeRules.defaultDailyLimit,
        usedToday: 0,
        history: []
      }
    };

    this.children.push(newChild);
    this.saveData();
    this.renderDashboard();
    this.showAlert(`${name} has been added successfully!`, 'success');
    document.getElementById('add-child-form').reset();
  }

  // Update screen time rules
  updateScreenTimeRules() {
    const dailyLimit = parseInt(document.getElementById('daily-limit').value);
    const bedtimeStart = document.getElementById('bedtime-start').value;
    const bedtimeEnd = document.getElementById('bedtime-end').value;
    const bonusMinutes = parseInt(document.getElementById('bonus-minutes').value);

    if (isNaN(dailyLimit) || isNaN(bonusMinutes) || !bedtimeStart || !bedtimeEnd) {
      this.showAlert('Please fill all fields with valid data', 'error');
      return;
    }

    this.screenTimeRules.defaultDailyLimit = dailyLimit;
    this.screenTimeRules.bedtimeLock.start = bedtimeStart;
    this.screenTimeRules.bedtimeLock.end = bedtimeEnd;
    this.screenTimeRules.educationalBonus.bonusMinutes = bonusMinutes;

    // Update all children's daily limits
    this.children.forEach(child => {
      child.screenTime.dailyLimit = dailyLimit;
    });

    this.saveData();
    this.renderDashboard();
    this.showAlert('Screen time rules updated successfully!', 'success');
  }

  // Toggle bedtime lock feature
  toggleBedtimeLock(enabled) {
    this.screenTimeRules.bedtimeLock.enabled = enabled;
    this.saveData();
    this.showAlert(`Bedtime lock ${enabled ? 'enabled' : 'disabled'}`, 'info');
  }

  // Toggle educational bonus feature
  toggleEducationalBonus(enabled) {
    this.screenTimeRules.educationalBonus.enabled = enabled;
    this.saveData();
    this.showAlert(`Educational bonus ${enabled ? 'enabled' : 'disabled'}`, 'info');
  }

  // Adjust screen time for a child
  adjustScreenTime(childId, minutes) {
    const child = this.children.find(c => c.id === childId);
    if (!child) return;

    child.screenTime.usedToday += minutes;
    child.screenTime.history.push({
      date: new Date().toISOString(),
      adjustment: minutes,
      reason: 'Manual adjustment'
    });

    this.saveData();
    this.renderDashboard();
  }

  // Add educational bonus to a child
  addEducationalBonus(childId) {
    if (!this.screenTimeRules.educationalBonus.enabled) return;

    const child = this.children.find(c => c.id === childId);
    if (!child) return;

    const bonus = this.screenTimeRules.educationalBonus.bonusMinutes;
    child.screenTime.dailyLimit += bonus;
    child.screenTime.history.push({
      date: new Date().toISOString(),
      adjustment: bonus,
      reason: 'Educational bonus'
    });

    this.saveData();
    this.renderDashboard();
    this.showAlert(`Added ${bonus} bonus minutes for ${child.name}`, 'success');
  }

  // Reset daily screen time for all children
  resetDailyScreenTime() {
    this.children.forEach(child => {
      child.screenTime.usedToday = 0;
      child.screenTime.history.push({
        date: new Date().toISOString(),
        adjustment: 0,
        reason: 'Daily reset'
      });
    });

    this.saveData();
    this.renderDashboard();
    this.showAlert('Daily screen time reset for all children', 'info');
  }

  // Render the dashboard UI
  renderDashboard() {
    this.renderChildrenList();
    this.renderScreenTimeRules();
    this.renderUsageStats();
  }

  // Render the children list
  renderChildrenList() {
    const container = document.getElementById('children-list');
    container.innerHTML = '';

    if (this.children.length === 0) {
      container.innerHTML = '<p>No children added yet. Add your first child above.</p>';
      return;
    }

    this.children.forEach(child => {
      const progress = Math.min(100, (child.screenTime.usedToday / child.screenTime.dailyLimit) * 100);
      const progressClass = progress >= 90 ? 'danger' : progress >= 70 ? 'warning' : '';

      const childElement = document.createElement('div');
      childElement.className = 'child-card';
      childElement.innerHTML = `
        <h3>${child.name} (Age ${child.age})</h3>
        <p>Device: ${child.device}</p>
        <div class="progress-container">
          <div class="progress-bar ${progressClass}" style="width: ${progress}%"></div>
          <span>${child.screenTime.usedToday} / ${child.screenTime.dailyLimit} minutes</span>
        </div>
        <div class="child-actions">
          <button class="btn btn-sm btn-add" data-id="${child.id}" data-minutes="15">+15 min</button>
          <button class="btn btn-sm btn-add" data-id="${child.id}" data-minutes="30">+30 min</button>
          <button class="btn btn-sm btn-remove" data-id="${child.id}" data-minutes="15">-15 min</button>
          <button class="btn btn-sm btn-bonus" data-id="${child.id}">Add Bonus</button>
        </div>
      `;

      container.appendChild(childElement);
    });

    // Add event listeners to action buttons
    document.querySelectorAll('.btn-add').forEach(btn => {
      btn.addEventListener('click', (e) => {
        const childId = e.target.dataset.id;
        const minutes = parseInt(e.target.dataset.minutes);
        this.adjustScreenTime(childId, minutes);
      });
    });

    document.querySelectorAll('.btn-remove').forEach(btn => {
      btn.addEventListener('click', (e) => {
        const childId = e.target.dataset.id;
        const minutes = -parseInt(e.target.dataset.minutes);
        this.adjustScreenTime(childId, minutes);
