"""
Generated Code Metadata:
========================
Original URL: https://metalcoin.vercel.app
Prompt: Create a simple meme-making contest platform using HTML, CSS, and JavaScript, where users can submit and vote on memes, and winners receive METAL tokens as rewards.
Generated: DETERMINISTIC_90903d1c35edaec6
Batch ID: 20250622_211009
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Meme Contest Platform</title>
  <style>
    /* Basic styling for the platform */
    body {
      font-family: Arial, sans-serif;
      margin: 0;
      padding: 0;
      background-color: #f4f4f4;
    }

    header {
      background-color: #333;
      color: #fff;
      padding: 1rem;
      text-align: center;
    }

    main {
      padding: 2rem;
    }

    .meme-form {
      margin-bottom: 2rem;
      background: #fff;
      padding: 1rem;
      border-radius: 5px;
      box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
    }

    .meme-form input, .meme-form button {
      display: block;
      width: 100%;
      margin-bottom: 1rem;
      padding: 0.5rem;
      border: 1px solid #ccc;
      border-radius: 5px;
    }

    .meme-list {
      display: flex;
      flex-wrap: wrap;
      gap: 1rem;
    }

    .meme-item {
      background: #fff;
      padding: 1rem;
      border-radius: 5px;
      box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
      width: calc(33.333% - 1rem);
      text-align: center;
    }

    .meme-item img {
      max-width: 100%;
      border-radius: 5px;
    }

    .meme-item button {
      margin-top: 0.5rem;
      padding: 0.5rem;
      border: none;
      background-color: #007bff;
      color: #fff;
      border-radius: 5px;
      cursor: pointer;
    }

    .meme-item button:hover {
      background-color: #0056b3;
    }
  </style>
</head>
<body>
  <header>
    <h1>Meme Contest Platform</h1>
  </header>
  <main>
    <!-- Meme submission form -->
    <div class="meme-form">
      <h2>Submit Your Meme</h2>
      <input type="text" id="memeTitle" placeholder="Meme Title" required>
      <input type="url" id="memeUrl" placeholder="Meme Image URL" required>
      <button id="submitMeme">Submit Meme</button>
    </div>

    <!-- List of memes -->
    <div class="meme-list" id="memeList">
      <!-- Memes will be dynamically added here -->
    </div>
  </main>

  <script>
    // JavaScript for handling meme submissions and voting
    const memeList = document.getElementById('memeList');
    const submitMemeButton = document.getElementById('submitMeme');

    // Array to store memes
    const memes = [];

    // Function to render memes
    function renderMemes() {
      memeList.innerHTML = ''; // Clear the list
      memes.forEach((meme, index) => {
        const memeItem = document.createElement('div');
        memeItem.className = 'meme-item';
        memeItem.innerHTML = `
          <h3>${meme.title}</h3>
          <img src="${meme.url}" alt="${meme.title}">
          <p>Votes: ${meme.votes}</p>
          <button onclick="voteMeme(${index})">Vote</button>
        `;
        memeList.appendChild(memeItem);
      });
    }

    // Function to handle meme submission
    submitMemeButton.addEventListener('click', () => {
      const memeTitle = document.getElementById('memeTitle').value.trim();
      const memeUrl = document.getElementById('memeUrl').value.trim();

      // Validate inputs
      if (!memeTitle || !memeUrl) {
        alert('Please provide both a title and a valid image URL.');
        return;
      }

      // Add meme to the list
      memes.push({ title: memeTitle, url: memeUrl, votes: 0 });
      renderMemes();

      // Clear input fields
      document.getElementById('memeTitle').value = '';
      document.getElementById('memeUrl').value = '';
    });

    // Function to handle voting
    function voteMeme(index) {
      memes[index].votes += 1;
      renderMemes();
    }
  </script>
</body>
</html>
```
