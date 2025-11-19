"""
Generated Code Metadata:
========================
Original URL: https://metamask.godaddysites.com
Prompt: Generate code for a Chrome extension that allows users to capture and organize notes within the browser, with tagging and categorization capabilities.
Generated: DETERMINISTIC_e51723c3260e264f
Batch ID: 20250622_210203
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// manifest.json
{
  "manifest_version": 3,
  "name": "Browser Notes",
  "version": "1.0",
  "description": "Capture and organize notes with tagging and categorization",
  "permissions": ["storage", "contextMenus"],
  "action": {
    "default_popup": "popup.html",
    "default_icon": {
      "16": "images/icon16.png",
      "48": "images/icon48.png",
      "128": "images/icon128.png"
    }
  },
  "icons": {
    "16": "images/icon16.png",
    "48": "images/icon48.png",
    "128": "images/icon128.png"
  },
  "background": {
    "service_worker": "background.js"
  }
}

// popup.html
<!DOCTYPE html>
<html>
<head>
  <title>Browser Notes</title>
  <link rel="stylesheet" href="styles.css">
</head>
<body>
  <div class="container">
    <h1>Browser Notes</h1>
    <div class="note-form">
      <textarea id="note-content" placeholder="Enter your note here..."></textarea>
      <input type="text" id="note-tags" placeholder="Tags (comma separated)">
      <select id="note-category">
        <option value="general">General</option>
        <option value="work">Work</option>
        <option value="personal">Personal</option>
        <option value="ideas">Ideas</option>
      </select>
      <button id="save-note">Save Note</button>
    </div>
    <div class="filter-controls">
      <input type="text" id="search-notes" placeholder="Search notes...">
      <select id="filter-category">
        <option value="all">All Categories</option>
        <option value="general">General</option>
        <option value="work">Work</option>
        <option value="personal">Personal</option>
        <option value="ideas">Ideas</option>
      </select>
    </div>
    <div id="notes-list"></div>
  </div>
  <script src="popup.js"></script>
</body>
</html>

// styles.css
body {
  font-family: Arial, sans-serif;
  width: 300px;
  margin: 0;
  padding: 10px;
}

.container {
  display: flex;
  flex-direction: column;
  gap: 10px;
}

h1 {
  font-size: 18px;
  margin: 0 0 10px 0;
  color: #333;
}

.note-form {
  display: flex;
  flex-direction: column;
  gap: 8px;
}

textarea {
  height: 100px;
  padding: 8px;
  border: 1px solid #ddd;
  border-radius: 4px;
  resize: none;
}

input, select {
  padding: 8px;
  border: 1px solid #ddd;
  border-radius: 4px;
}

button {
  padding: 8px;
  background-color: #4CAF50;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

button:hover {
  background-color: #45a049;
}

.filter-controls {
  display: flex;
  gap: 8px;
}

#notes-list {
  display: flex;
  flex-direction: column;
  gap: 8px;
  max-height: 300px;
  overflow-y: auto;
}

.note-item {
  padding: 8px;
  border: 1px solid #eee;
  border-radius: 4px;
  background-color: #f9f9f9;
}

.note-content {
  margin-bottom: 5px;
}

.note-meta {
  font-size: 12px;
  color: #666;
  display: flex;
  justify-content: space-between;
}

.tag {
  display: inline-block;
  background-color: #e0e0e0;
  padding: 2px 5px;
  border-radius: 3px;
  margin-right: 3px;
  font-size: 11px;
}

.delete-btn {
  background-color: #f44336;
  padding: 2px 5px;
  font-size: 11px;
}

.delete-btn:hover {
  background-color: #d32f2f;
}

// popup.js
document.addEventListener('DOMContentLoaded', () => {
  const noteContent = document.getElementById('note-content');
  const noteTags = document.getElementById('note-tags');
  const noteCategory = document.getElementById('note-category');
  const saveNoteBtn = document.getElementById('save-note');
  const searchNotes = document.getElementById('search-notes');
  const filterCategory = document.getElementById('filter-category');
  const notesList = document.getElementById('notes-list');

  // Load and display notes
  loadNotes();

  // Save note
  saveNoteBtn.addEventListener('click', () => {
    const content = noteContent.value.trim();
    if (!content) {
      alert('Please enter note content');
      return;
    }

    const tags = noteTags.value.trim().split(',').map(tag => tag.trim()).filter(tag => tag);
    const category = noteCategory.value;

    saveNote({
      content,
      tags,
      category,
      createdAt: new Date().toISOString()
    });

    noteContent.value = '';
    noteTags.value = '';
    loadNotes();
  });

  // Filter notes
  searchNotes.addEventListener('input', loadNotes);
  filterCategory.addEventListener('change', loadNotes);

  async function loadNotes() {
    const searchTerm = searchNotes.value.toLowerCase();
    const selectedCategory = filterCategory.value;

    const notes = await getNotes();
    notesList.innerHTML = '';

    const filteredNotes = notes.filter(note => {
      const matchesSearch = note.content.toLowerCase().includes(searchTerm) || 
                           note.tags.some(tag => tag.toLowerCase().includes(searchTerm));
      const matchesCategory = selectedCategory === 'all' || note.category === selectedCategory;
      return matchesSearch && matchesCategory;
    });

    if (filteredNotes.length === 0) {
      notesList.innerHTML = '<p>No notes found</p>';
      return;
    }

    filteredNotes.forEach(note => {
      const noteElement = document.createElement('div');
      noteElement.className = 'note-item';
      noteElement.innerHTML = `
        <div class="note-content">${note.content}</div>
        <div class="note-meta">
          <div>
            ${note.tags.map(tag => `<span class="tag">${tag}</span>`).join('')}
            <span>${note.category}</span>
          </div>
          <button class="delete-btn" data-id="${note.id}">Delete</button>
        </div>
      `;
      notesList.appendChild(noteElement);
    });

    // Add delete event listeners
    document.querySelectorAll('.delete-btn').forEach(btn => {
      btn.addEventListener('click', async (e) => {
        const id = e.target.getAttribute('data-id');
        await deleteNote(id);
        loadNotes();
      });
    });
  }

  // Storage functions
  async function getNotes() {
    return new Promise((resolve) => {
      chrome.storage.sync.get({notes: []}, (result) => {
        const notes = result.notes.map((note, index) => ({...note, id: index}));
        resolve(notes);
      });
    });
  }

  async function saveNote(note) {
    return new Promise((resolve) => {
      chrome.storage.sync.get({notes: []}, (result) => {
        const notes = [...result.notes, note];
        chrome.storage.sync.set({notes}, () => resolve());
      });
    });
  }

  async function deleteNote(id) {
    return new Promise((resolve) => {
      chrome.storage.sync.get({notes: []}, (result) => {
        const notes = result.notes.filter((_, index) => index !== parseInt(id));
        chrome.storage.sync.set({notes}, () => resolve());
      });
    });
  }
});

// background.js
chrome.runtime.onInstalled.addListener(() => {
  chrome.contextMenus.create({
    id: "saveSelectionAsNote",
    title: "Save selection as note",
    contexts: ["selection"]
  });
});

chrome.contextMenus.onClicked.addListener((info, tab) => {
  if (info.menuItemId === "saveSelectionAsNote") {
    chrome.storage.sync.get({notes: []}, (result) => {
      const notes = [...result.notes, {
        content: info.selectionText,
        tags: [],
        category: "general",
        createdAt: new Date().toISOString()
      }];
      chrome.storage.sync.set({notes});
    });
  }
});
```
