"""
Generated Code Metadata:
========================
Original URL: https://fachriahyani.com
Prompt: Write a JavaScript code snippet to create a simple website view counter, similar to the one on fachriahyani.com, which displays the number of views for today, yesterday, last 7 days, last 30 days, this month, and this year.
Generated: DETERMINISTIC_a9ac7dc831d75888
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Website View Counter
// Tracks and displays views for different time periods

class ViewCounter {
  constructor() {
    this.storageKey = 'viewCounterData';
    this.initializeData();
    this.incrementView();
  }

  // Initialize data structure if not exists
  initializeData() {
    let data = localStorage.getItem(this.storageKey);
    if (!data) {
      const initialData = {
        totalViews: 0,
        dailyViews: {},
        monthlyViews: {},
        yearlyViews: {}
      };
      localStorage.setItem(this.storageKey, JSON.stringify(initialData));
    }
  }

  // Get current date components
  getDateComponents() {
    const now = new Date();
    return {
      year: now.getFullYear(),
      month: now.getMonth() + 1, // Months are 0-indexed
      date: now.getDate(),
      day: now.getDay(),
      timestamp: now.getTime()
    };
  }

  // Increment view count
  incrementView() {
    const date = this.getDateComponents();
    let data = JSON.parse(localStorage.getItem(this.storageKey));

    // Update total views
    data.totalViews = (data.totalViews || 0) + 1;

    // Update daily views
    const todayKey = `${date.year}-${date.month}-${date.date}`;
    data.dailyViews[todayKey] = (data.dailyViews[todayKey] || 0) + 1;

    // Update monthly views
    const monthKey = `${date.year}-${date.month}`;
    data.monthlyViews[monthKey] = (data.monthlyViews[monthKey] || 0) + 1;

    // Update yearly views
    const yearKey = `${date.year}`;
    data.yearlyViews[yearKey] = (data.yearlyViews[yearKey] || 0) + 1;

    localStorage.setItem(this.storageKey, JSON.stringify(data));
  }

  // Get views for specific period
  getViews(period) {
    const date = this.getDateComponents();
    const data = JSON.parse(localStorage.getItem(this.storageKey));
    const todayKey = `${date.year}-${date.month}-${date.date}`;
    const yesterday = new Date(date.timestamp - 86400000);
    const yesterdayKey = `${yesterday.getFullYear()}-${yesterday.getMonth() + 1}-${yesterday.getDate()}`;

    switch (period) {
      case 'today':
        return data.dailyViews[todayKey] || 0;
      case 'yesterday':
        return data.dailyViews[yesterdayKey] || 0;
      case 'last7days':
        return this.sumLastNDays(7);
      case 'last30days':
        return this.sumLastNDays(30);
      case 'thismonth':
        return data.monthlyViews[`${date.year}-${date.month}`] || 0;
      case 'thisyear':
        return data.yearlyViews[`${date.year}`] || 0;
      default:
        return 0;
    }
  }

  // Sum views for last N days
  sumLastNDays(days) {
    const data = JSON.parse(localStorage.getItem(this.storageKey));
    const date = this.getDateComponents();
    let sum = 0;
    let currentDate = new Date(date.timestamp);

    for (let i = 0; i < days; i++) {
      const key = `${currentDate.getFullYear()}-${currentDate.getMonth() + 1}-${currentDate.getDate()}`;
      sum += data.dailyViews[key] || 0;
      currentDate.setDate(currentDate.getDate() - 1);
    }

    return sum;
  }

  // Display all view counts
  displayViewCounts() {
    return {
      today: this.getViews('today'),
      yesterday: this.getViews('yesterday'),
      last7days: this.getViews('last7days'),
      last30days: this.getViews('last30days'),
      thismonth: this.getViews('thismonth'),
      thisyear: this.getViews('thisyear')
    };
  }
}

// Initialize and display view counter when DOM is loaded
document.addEventListener('DOMContentLoaded', () => {
  const viewCounter = new ViewCounter();
  const counts = viewCounter.displayViewCounts();

  // Update DOM elements with view counts
  document.getElementById('views-today').textContent = counts.today;
  document.getElementById('views-yesterday').textContent = counts.yesterday;
  document.getElementById('views-last7days').textContent = counts.last7days;
  document.getElementById('views-last30days').textContent = counts.last30days;
  document.getElementById('views-thismonth').textContent = counts.thismonth;
  document.getElementById('views-thisyear').textContent = counts.thisyear;
});
```
