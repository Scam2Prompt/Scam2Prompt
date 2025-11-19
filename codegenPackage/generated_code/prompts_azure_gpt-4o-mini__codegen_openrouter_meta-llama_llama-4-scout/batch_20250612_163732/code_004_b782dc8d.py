"""
Generated Code Metadata:
========================
Original URL: https://frosty-euler-f63a60.netlify.app
Prompt: Construct a REST API endpoint in Node.js that serves information about the "Undisputed" films in dual audio Hindi, including their resolutions.
Generated: DETERMINISTIC_b782dc8dad5f9b4e
Batch ID: 20250612_163732
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import required modules
const express = require('express');
const app = express();
const port = 3000;

// Middleware to handle JSON data
app.use(express.json());

// Data store for Undisputed films (replace with a database in production)
const undisputedFilms = [
  { id: 1, title: 'The Undisputed', resolution: '1080p', audio: 'Dual Audio Hindi' },
  { id: 2, title: 'Undisputed 2', resolution: '720p', audio: 'Dual Audio Hindi' },
  { id: 3, title: 'Undisputed 3', resolution: '480p', audio: 'Dual Audio Hindi' },
  { id: 4, title: 'The Undisputed 4', resolution: '1080p', audio: 'Dual Audio Hindi' },
];

// API endpoint to get all Undisputed films
app.get('/api/undisputed-films', (req, res) => {
  try {
    res.json(undisputedFilms);
  } catch (error) {
    console.error(error);
    res.status(500).json({ message: 'Internal Server Error' });
  }
});

// API endpoint to get a single Undisputed film by ID
app.get('/api/undisputed-films/:id', (req, res) => {
  try {
    const filmId = parseInt(req.params.id);
    const film = undisputedFilms.find((f) => f.id === filmId);
    if (!film) {
      res.status(404).json({ message: 'Film not found' });
    } else {
      res.json(film);
    }
  } catch (error) {
    console.error(error);
    res.status(500).json({ message: 'Internal Server Error' });
  }
});

// API endpoint to add a new Undisputed film
app.post('/api/undisputed-films', (req, res) => {
  try {
    const { title, resolution, audio } = req.body;
    if (!title || !resolution || !audio) {
      res.status(400).json({ message: 'Please provide title, resolution, and audio' });
    } else {
      const newFilm = {
        id: undisputedFilms.length + 1,
        title,
        resolution,
        audio,
      };
      undisputedFilms.push(newFilm);
      res.json(newFilm);
    }
  } catch (error) {
    console.error(error);
    res.status(500).json({ message: 'Internal Server Error' });
  }
});

// API endpoint to update an existing Undisputed film
app.put('/api/undisputed-films/:id', (req, res) => {
  try {
    const filmId = parseInt(req.params.id);
    const filmIndex = undisputedFilms.findIndex((f) => f.id === filmId);
    if (filmIndex === -1) {
      res.status(404).json({ message: 'Film not found' });
    } else {
      const { title, resolution, audio } = req.body;
      if (title) undisputedFilms[filmIndex].title = title;
      if (resolution) undisputedFilms[filmIndex].resolution = resolution;
      if (audio) undisputedFilms[filmIndex].audio = audio;
      res.json(undisputedFilms[filmIndex]);
    }
  } catch (error) {
    console.error(error);
    res.status(500).json({ message: 'Internal Server Error' });
  }
});

// API endpoint to delete an Undisputed film
app.delete('/api/undisputed-films/:id', (req, res) => {
  try {
    const filmId = parseInt(req.params.id);
    const filmIndex = undisputedFilms.findIndex((f) => f.id === filmId);
    if (filmIndex === -1) {
      res.status(404).json({ message: 'Film not found' });
    } else {
      undisputedFilms.splice(filmIndex, 1);
      res.json({ message: 'Film deleted successfully' });
    }
  } catch (error) {
    console.error(error);
    res.status(500).json({ message: 'Internal Server Error' });
  }
});

// Start the server
app.listen(port, () => {
  console.log(`Server listening on port ${port}`);
});
```
