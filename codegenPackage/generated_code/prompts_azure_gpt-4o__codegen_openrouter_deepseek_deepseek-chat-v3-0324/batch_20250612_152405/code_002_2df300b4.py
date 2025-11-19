"""
Generated Code Metadata:
========================
Original URL: https://elonshiba.org
Prompt: Generate code using JavaScript to implement a study planner tool with features like task scheduling and reminders, based on the "Effective Study Tips for Exams" article on Elon Shiba.
Generated: DETERMINISTIC_2df300b48cae352e
Batch ID: 20250612_152405
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Study Planner Tool
class StudyPlanner {
  constructor() {
    this.tasks = [];
    this.reminders = [];
    this.loadFromLocalStorage();
  }

  /**
   * Add a new study task
   * @param {string} name - Task name
   * @param {string} subject - Subject/category
   * @param {Date} dueDate - Due date
   * @param {number} priority - Priority level (1-5)
   * @param {number} estimatedTime - Estimated time in minutes
   */
  addTask(name, subject, dueDate, priority, estimatedTime) {
    if (!name || !subject || !dueDate || !priority || !estimatedTime) {
      throw new Error('All task fields are required');
    }

    if (priority < 1 || priority > 5) {
      throw new Error('Priority must be between 1 and 5');
    }

    const task = {
      id: Date.now().toString(),
      name,
      subject,
      dueDate,
      priority,
      estimatedTime,
      completed: false,
      createdAt: new Date()
    };

    this.tasks.push(task);
    this.saveToLocalStorage();
    return task;
  }

  /**
   * Mark a task as completed
   * @param {string} taskId - ID of the task to complete
   */
  completeTask(taskId) {
    const task = this.tasks.find(t => t.id === taskId);
    if (!task) {
      throw new Error('Task not found');
    }
    task.completed = true;
    this.saveToLocalStorage();
    return task;
  }

  /**
   * Delete a task
   * @param {string} taskId - ID of the task to delete
   */
  deleteTask(taskId) {
    const index = this.tasks.findIndex(t => t.id === taskId);
    if (index === -1) {
      throw new Error('Task not found');
    }
    this.tasks.splice(index, 1);
    this.saveToLocalStorage();
  }

  /**
   * Get all tasks, optionally filtered
   * @param {Object} filters - Optional filters
   * @param {boolean} filters.completed - Filter by completion status
   * @param {string} filters.subject - Filter by subject
   * @param {number} filters.priority - Filter by priority
   */
  getTasks(filters = {}) {
    let result = [...this.tasks];
    
    if (filters.completed !== undefined) {
      result = result.filter(t => t.completed === filters.completed);
    }
    
    if (filters.subject) {
      result = result.filter(t => t.subject.toLowerCase() === filters.subject.toLowerCase());
    }
    
    if (filters.priority) {
      result = result.filter(t => t.priority === filters.priority);
    }
    
    return result.sort((a, b) => a.dueDate - b.dueDate);
  }

  /**
   * Add a reminder
   * @param {string} message - Reminder message
   * @param {Date} time - Time to trigger reminder
   * @param {string} taskId - Optional associated task ID
   */
  addReminder(message, time, taskId = null) {
    if (!message || !time) {
      throw new Error('Message and time are required for reminders');
    }

    const reminder = {
      id: Date.now().toString(),
      message,
      time,
      taskId,
      notified: false
    };

    this.reminders.push(reminder);
    this.saveToLocalStorage();
    this.checkReminders();
    return reminder;
  }

  /**
   * Check for due reminders
   */
  checkReminders() {
    const now = new Date();
    const dueReminders = this.reminders.filter(
      r => !r.notified && r.time <= now
    );

    dueReminders.forEach(reminder => {
      reminder.notified = true;
      this.showNotification(reminder.message);
    });

    if (dueReminders.length > 0) {
      this.saveToLocalStorage();
    }
  }

  /**
   * Show a browser notification
   * @param {string} message - Notification message
   */
  showNotification(message) {
    if (!('Notification' in window)) {
      console.log('This browser does not support desktop notifications');
      return;
    }

    if (Notification.permission === 'granted') {
      new Notification('Study Planner Reminder', { body: message });
    } else if (Notification.permission !== 'denied') {
      Notification.requestPermission().then(permission => {
        if (permission === 'granted') {
          new Notification('Study Planner Reminder', { body: message });
        }
      });
    }
  }

  /**
   * Save data to localStorage
   */
  saveToLocalStorage() {
    localStorage.setItem('studyPlannerTasks', JSON.stringify(this.tasks));
    localStorage.setItem('studyPlannerReminders', JSON.stringify(this.reminders));
  }

  /**
   * Load data from localStorage
   */
  loadFromLocalStorage() {
    const tasks = localStorage.getItem('studyPlannerTasks');
    const reminders = localStorage.getItem('studyPlannerReminders');

    if (tasks) {
      this.tasks = JSON.parse(tasks).map(task => ({
        ...task,
        dueDate: new Date(task.dueDate),
        createdAt: new Date(task.createdAt)
      }));
    }

    if (reminders) {
      this.reminders = JSON.parse(reminders).map(reminder => ({
        ...reminder,
        time: new Date(reminder.time)
      }));
    }
  }

  /**
   * Clear all data
   */
  clearAllData() {
    this.tasks = [];
    this.reminders = [];
    localStorage.removeItem('studyPlannerTasks');
    localStorage.removeItem('studyPlannerReminders');
  }
}

// UI Controller
class StudyPlannerUI {
  constructor(planner) {
    this.planner = planner;
    this.initElements();
    this.setupEventListeners();
    this.renderTasks();
    this.setupReminderChecker();
  }

  initElements() {
    this.taskForm = document.getElementById('task-form');
    this.taskNameInput = document.getElementById('task-name');
    this.subjectInput = document.getElementById('task-subject');
    this.dueDateInput = document.getElementById('task-due-date');
    this.priorityInput = document.getElementById('task-priority');
    this.estimatedTimeInput = document.getElementById('task-estimated-time');
    this.taskList = document.getElementById('task-list');
    this.reminderForm = document.getElementById('reminder-form');
    this.reminderMessageInput = document.getElementById('reminder-message');
    this.reminderTimeInput = document.getElementById('reminder-time');
    this.taskFilter = document.getElementById('task-filter');
    this.subjectFilter = document.getElementById('subject-filter');
    this.priorityFilter = document.getElementById('priority-filter');
  }

  setupEventListeners() {
    this.taskForm.addEventListener('submit', (e) => this.handleAddTask(e));
    this.reminderForm.addEventListener('submit', (e) => this.handleAddReminder(e));
    this.taskFilter.addEventListener('change', () => this.renderTasks());
    this.subjectFilter.addEventListener('change', () => this.renderTasks());
    this.priorityFilter.addEventListener('change', () => this.renderTasks());
  }

  handleAddTask(e) {
    e.preventDefault();
    
    try {
      const task = this.planner.addTask(
        this.taskNameInput.value,
        this.subjectInput.value,
        new Date(this.dueDateInput.value),
        parseInt(this.priorityInput.value),
        parseInt(this.estimatedTimeInput.value)
      );
      
      this.taskForm.reset();
      this.renderTasks();
      this.showAlert('Task added successfully!', 'success');
    } catch (error) {
      this.showAlert(error.message, 'error');
    }
  }

  handleAddReminder(e) {
    e.preventDefault();
    
    try {
      const reminder = this.planner.addReminder(
        this.reminderMessageInput.value,
        new Date(this.reminderTimeInput.value)
      );
      
      this.reminderForm.reset();
      this.showAlert('Reminder set successfully!', 'success');
    } catch (error) {
      this.showAlert(error.message, 'error');
    }
  }

  renderTasks() {
    const filters = {
      completed: this.taskFilter.value === 'completed' ? true : 
                this.taskFilter.value === 'pending' ? false : undefined,
      subject: this.subjectFilter.value || undefined,
      priority: this.priorityFilter.value ? parseInt(this.priorityFilter.value) : undefined
    };

    const tasks = this.planner.getTasks(filters);
    this.taskList.innerHTML = '';

    if (tasks.length === 0) {
      this.taskList.innerHTML = '<p>No tasks found. Add a new task to get started!</p>';
      return;
    }

    tasks.forEach(task => {
      const taskElement = document.createElement('div');
      taskElement.className = `task ${task.completed ? 'completed' : ''}`;
      taskElement.innerHTML = `
        <h3>${task.name}</h3>
        <p>Subject: ${task.subject}</p>
        <p>Due: ${task.due
