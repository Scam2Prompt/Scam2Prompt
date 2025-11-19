"""
Generated Code Metadata:
========================
Original URL: https://larumberaradio.com
Prompt: Write a CSS style sheet for customizing the look of a radio station website, inspired by La Rumbera Radio's design.
Generated: DETERMINISTIC_c3cfd6281d56b6f7
Batch ID: 20250622_204903
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```css
/* 
  La Rumbera Radio Style Inspiration
  =====================================
  Custom CSS style sheet for radio station website.
*/

/* Global Styles */
* {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

body {
  font-family: Arial, sans-serif;
  line-height: 1.6;
  color: #333;
  background-color: #f9f9f9;
}

/* Header Styles */
.header {
  background-color: #007bff;
  color: #fff;
  padding: 1em;
  text-align: center;
}

.header img {
  width: 100px;
  height: 100px;
  margin: 0 auto;
  border-radius: 50%;
}

/* Navigation Styles */
.nav {
  background-color: #333;
  padding: 0.5em;
  text-align: center;
}

.nav ul {
  list-style: none;
  margin: 0;
  padding: 0;
}

.nav li {
  display: inline-block;
  margin-right: 20px;
}

.nav a {
  color: #fff;
  text-decoration: none;
}

.nav a:hover {
  color: #ccc;
}

/* Main Content Styles */
.main {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  padding: 2em;
}

.content {
  flex-basis: 60%;
  background-color: #fff;
  padding: 2em;
  margin: 20px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

.sidebar {
  flex-basis: 30%;
  background-color: #fff;
  padding: 2em;
  margin: 20px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

/* Player Styles */
.player {
  background-color: #333;
  color: #fff;
  padding: 1em;
  text-align: center;
}

.player iframe {
  width: 100%;
  height: 200px;
  border: none;
}

/* Footer Styles */
.footer {
  background-color: #007bff;
  color: #fff;
  padding: 1em;
  text-align: center;
  clear: both;
}

.footer p {
  margin-bottom: 10px;
}

/* Responsive Design */
@media (max-width: 768px) {
  .main {
    flex-direction: column;
  }
  
  .content, .sidebar {
    flex-basis: 100%;
    margin: 10px;
  }
}

@media (max-width: 480px) {
  .header img {
    width: 50px;
    height: 50px;
  }
  
  .nav li {
    display: block;
    margin-right: 0;
  }
}
```
