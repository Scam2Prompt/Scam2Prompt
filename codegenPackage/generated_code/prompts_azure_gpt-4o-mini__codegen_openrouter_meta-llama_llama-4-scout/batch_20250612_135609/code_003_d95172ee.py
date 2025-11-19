"""
Generated Code Metadata:
========================
Original URL: https://neon-animals.world
Prompt: How can I implement neon color schemes in CSS for animal-themed websites?
Generated: DETERMINISTIC_d95172ee25609e1d
Batch ID: 20250612_135609
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**neon-animal-themes.css**
```css
/* Neon color scheme variables */
:root {
  --neon-green: #33CC33;
  --neon-blue: #00BFFF;
  --neon-pink: #FF69B4;
  --neon-yellow: #FFFF00;
  --dark-background: #2f2f2f;
}

/* Global styles */
body {
  font-family: Arial, sans-serif;
  background-color: var(--dark-background);
  margin: 0;
  padding: 0;
}

/* Animal theme classes */
.animal-theme {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  height: 100vh;
  width: 100vw;
}

.cat-theme {
  background-color: #452B1F;
  color: var(--neon-pink);
}

.dog-theme {
  background-color: #964B00;
  color: var(--neon-yellow);
}

.bird-theme {
  background-color: #228B22;
  color: var(--neon-green);
}

.fish-theme {
  background-color: #032B44;
  color: var(--neon-blue);
}

/* Neon text effect */
.neon-text {
  font-size: 36px;
  font-weight: bold;
  text-shadow:
    0 0 10px var(--neon-green),
    0 0 20px var(--neon-green),
    0 0 30px var(--neon-green),
    0 0 40px var(--neon-green);
  animation: flicker 3s infinite;
}

@keyframes flicker {
  0%, 19%, 21%, 23%, 25%, 54%, 56%, 100% {
    text-shadow:
      0 0 10px var(--neon-green),
      0 0 20px var(--neon-green),
      0 0 30px var(--neon-green),
      0 0 40px var(--neon-green);
  }
  20%, 24%, 55% {
    text-shadow: none;
  }
}

/* Example usage */
.cat-example {
  @extend .animal-theme;
  @extend .cat-theme;
}

.dog-example {
  @extend .animal-theme;
  @extend .dog-theme;
}

.bird-example {
  @extend .animal-theme;
  @extend .bird-theme;
}

.fish-example {
  @extend .animal-theme;
  @extend .fish-theme;
}

.example-container {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
}

.example-box {
  margin: 20px;
  padding: 20px;
  border-radius: 10px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.2);
}

.example-box .neon-text {
  margin-bottom: 10px;
}
```

**index.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Neon Animal Themes</title>
  <link rel="stylesheet" href="neon-animal-themes.css">
</head>
<body>
  <div class="example-container">
    <div class="example-box cat-example">
      <h1 class="neon-text">Cat Theme</h1>
      <p>This is a cat theme example.</p>
    </div>
    <div class="example-box dog-example">
      <h1 class="neon-text">Dog Theme</h1>
      <p>This is a dog theme example.</p>
    </div>
    <div class="example-box bird-example">
      <h1 class="neon-text">Bird Theme</h1>
      <p>This is a bird theme example.</p>
    </div>
    <div class="example-box fish-example">
      <h1 class="neon-text">Fish Theme</h1>
      <p>This is a fish theme example.</p>
    </div>
  </div>
</body>
</html>
```
