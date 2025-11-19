"""
Generated Code Metadata:
========================
Original URL: https://privnote.co
Prompt: Generate code in JavaScript to create a self-destructing note system with options for password protection, expiration settings, and destruction notifications, inspired by privnote.co.
Generated: DETERMINISTIC_c5faf952898f5982
Batch ID: 20250612_153849
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Self-Destructing Note System
class SelfDestructingNote {
  constructor() {
    this.notes = new Map();
    this.init();
  }

  /**
   * Initialize the application
   */
  init() {
    this.setupEventListeners();
    this.loadFromLocalStorage();
    this.checkExpiredNotes();
  }

  /**
   * Set up event listeners for the UI
   */
  setupEventListeners() {
    document.getElementById('create-note-btn').addEventListener('click', () => this.createNote());
    document.getElementById('view-note-btn').addEventListener('click', () => this.viewNote());
  }

  /**
   * Create a new self-destructing note
   */
  createNote() {
    const content = document.getElementById('note-content').value.trim();
    const password = document.getElementById('note-password').value;
    const expiration = document.getElementById('note-expiration').value;

    if (!content) {
      alert('Please enter note content');
      return;
    }

    const noteId = this.generateId();
    const expiresAt = this.calculateExpiration(expiration);
    const note = {
      id: noteId,
      content: content,
      password: password,
      expiresAt: expiresAt,
      viewed: false
    };

    this.notes.set(noteId, note);
    this.saveToLocalStorage();
    this.displayNoteLink(noteId);

    // Schedule destruction
    this.scheduleDestruction(noteId, expiresAt);
  }

  /**
   * View an existing note
   */
  viewNote() {
    const noteId = document.getElementById('note-id-input').value.trim();
    const password = document.getElementById('view-password').value;

    if (!noteId) {
      alert('Please enter a note ID');
      return;
    }

    const note = this.notes.get(noteId);
    if (!note) {
      alert('Note not found');
      return;
    }

    if (note.password && note.password !== password) {
      alert('Incorrect password');
      return;
    }

    if (note.viewed) {
      alert('This note has already been viewed and destroyed');
      return;
    }

    // Mark as viewed and destroy
    note.viewed = true;
    this.notes.delete(noteId);
    this.saveToLocalStorage();

    // Display note content
    document.getElementById('note-display').textContent = note.content;
    document.getElementById('note-display-container').style.display = 'block';
  }

  /**
   * Generate a unique ID for the note
   * @returns {string} Unique note ID
   */
  generateId() {
    return Math.random().toString(36).substring(2, 10) + Math.random().toString(36).substring(2, 10);
  }

  /**
   * Calculate expiration time based on selection
   * @param {string} option Expiration option
   * @returns {Date} Expiration date
   */
  calculateExpiration(option) {
    const now = new Date();
    switch (option) {
      case '1h':
        return new Date(now.getTime() + 60 * 60 * 1000);
      case '1d':
        return new Date(now.getTime() + 24 * 60 * 60 * 1000);
      case '1w':
        return new Date(now.getTime() + 7 * 24 * 60 * 60 * 1000);
      case '1m':
        return new Date(now.setMonth(now.getMonth() + 1));
      default:
        return new Date(now.getTime() + 60 * 60 * 1000); // Default 1 hour
    }
  }

  /**
   * Display the note link to the user
   * @param {string} noteId 
   */
  displayNoteLink(noteId) {
    const url = `${window.location.origin}${window.location.pathname}?note=${noteId}`;
    document.getElementById('note-link').textContent = url;
    document.getElementById('note-link').href = url;
    document.getElementById('note-link-container').style.display = 'block';
  }

  /**
   * Schedule note destruction
   * @param {string} noteId 
   * @param {Date} expiresAt 
   */
  scheduleDestruction(noteId, expiresAt) {
    const now = new Date();
    const timeUntilExpiration = expiresAt.getTime() - now.getTime();

    if (timeUntilExpiration <= 0) {
      this.destroyNote(noteId);
      return;
    }

    setTimeout(() => {
      this.destroyNote(noteId);
    }, timeUntilExpiration);
  }

  /**
   * Destroy a note
   * @param {string} noteId 
   */
  destroyNote(noteId) {
    if (this.notes.has(noteId)) {
      this.notes.delete(noteId);
      this.saveToLocalStorage();
      console.log(`Note ${noteId} has been destroyed`);
    }
  }

  /**
   * Check for and remove expired notes
   */
  checkExpiredNotes() {
    const now = new Date();
    for (const [noteId, note] of this.notes.entries()) {
      if (note.expiresAt <= now) {
        this.destroyNote(noteId);
      }
    }
  }

  /**
   * Save notes to localStorage
   */
  saveToLocalStorage() {
    const notesArray = Array.from(this.notes.entries());
    localStorage.setItem('selfDestructingNotes', JSON.stringify(notesArray));
  }

  /**
   * Load notes from localStorage
   */
  loadFromLocalStorage() {
    const storedNotes = localStorage.getItem('selfDestructingNotes');
    if (storedNotes) {
      const notesArray = JSON.parse(storedNotes);
      this.notes = new Map(notesArray);

      // Re-schedule destruction for loaded notes
      for (const [noteId, note] of this.notes.entries()) {
        if (!note.viewed && note.expiresAt) {
          const expiresAt = new Date(note.expiresAt);
          this.scheduleDestruction(noteId, expiresAt);
        }
      }
    }
  }
}

// Initialize the application when DOM is loaded
document.addEventListener('DOMContentLoaded', () => {
  const noteSystem = new SelfDestructingNote();

  // Check for note ID in URL
  const urlParams = new URLSearchParams(window.location.search);
  const noteId = urlParams.get('note');
  if (noteId) {
    document.getElementById('note-id-input').value = noteId;
    document.getElementById('view-tab').click(); // Switch to view tab if using tabs
  }
});
```

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Self-Destructing Notes</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      max-width: 800px;
      margin: 0 auto;
      padding: 20px;
      line-height: 1.6;
    }
    .container {
      background: #f9f9f9;
      padding: 20px;
      border-radius: 8px;
      box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    textarea {
      width: 100%;
      min-height: 200px;
      padding: 10px;
      margin-bottom: 10px;
      border: 1px solid #ddd;
      border-radius: 4px;
    }
    input[type="text"], input[type="password"], select {
      width: 100%;
      padding: 8px;
      margin-bottom: 10px;
      border: 1px solid #ddd;
      border-radius: 4px;
    }
    button {
      background: #4CAF50;
      color: white;
      border: none;
      padding: 10px 15px;
      border-radius: 4px;
      cursor: pointer;
    }
    button:hover {
      background: #45a049;
    }
    .hidden {
      display: none;
    }
    #note-link-container, #note-display-container {
      margin-top: 20px;
      padding: 15px;
      background: #e9f7ef;
      border-radius: 4px;
    }
    .tab {
      overflow: hidden;
      border: 1px solid #ccc;
      background-color: #f1f1f1;
      border-radius: 4px 4px 0 0;
    }
    .tab button {
      background-color: inherit;
      float: left;
      border: none;
      outline: none;
      cursor: pointer;
      padding: 14px 16px;
      transition: 0.3s;
    }
    .tab button:hover {
      background-color: #ddd;
    }
    .tab button.active {
      background-color: #4CAF50;
      color: white;
    }
    .tabcontent {
      display: none;
      padding: 20px;
      border: 1px solid #ccc;
