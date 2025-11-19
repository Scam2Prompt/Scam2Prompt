"""
Generated Code Metadata:
========================
Original URL: https://traceybaptiste.com
Prompt: Write a code example that implements a storytelling feature inspired by Tracey Baptiste's narrative style, allowing users to create their own fairy tales and family lore through a web interface.
Generated: DETERMINISTIC_24e55e13d2915657
Batch ID: 20250612_163526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Here's a complete implementation of a web-based storytelling application inspired by Tracey Baptiste's narrative style:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Story Weaver - Create Your Own Fairy Tales</title>
    <style>
        body {
            font-family: 'Georgia', serif;
            line-height: 1.6;
            color: #333;
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
            background-color: #f9f4e6;
        }
        h1, h2 {
            color: #5d4037;
            font-weight: normal;
        }
        .story-container {
            background-color: #fff;
            padding: 30px;
            border-radius: 8px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
            margin-bottom: 20px;
        }
        .form-group {
            margin-bottom: 20px;
        }
        label {
            display: block;
            margin-bottom: 5px;
            font-weight: bold;
        }
        input, select, textarea {
            width: 100%;
            padding: 10px;
            border: 1px solid #ddd;
            border-radius: 4px;
            font-family: inherit;
        }
        button {
            background-color: #8d6e63;
            color: white;
            border: none;
            padding: 10px 20px;
            border-radius: 4px;
            cursor: pointer;
            font-size: 16px;
            transition: background-color 0.3s;
        }
        button:hover {
            background-color: #6d4c41;
        }
        .story-output {
            white-space: pre-wrap;
            padding: 20px;
            background-color: #f5f5f5;
            border-radius: 4px;
            margin-top: 20px;
        }
        .hidden {
            display: none;
        }
        .error {
            color: #d32f2f;
            font-size: 14px;
            margin-top: 5px;
        }
    </style>
</head>
<body>
    <div class="story-container">
        <h1>Story Weaver</h1>
        <p>Create your own fairy tale or family lore inspired by Tracey Baptiste's narrative style</p>
        
        <form id="storyForm">
            <div class="form-group">
                <label for="storyType">Story Type</label>
                <select id="storyType" required>
                    <option value="">Select a story type</option>
                    <option value="fairyTale">Fairy Tale</option>
                    <option value="familyLore">Family Lore</option>
                    <option value="myth">Myth</option>
                    <option value="legend">Legend</option>
                </select>
                <div id="storyTypeError" class="error hidden">Please select a story type</div>
            </div>
            
            <div class="form-group">
                <label for="protagonist">Protagonist Name</label>
                <input type="text" id="protagonist" required placeholder="e.g. Anaya">
                <div id="protagonistError" class="error hidden">Please enter a protagonist name</div>
            </div>
            
            <div class="form-group">
                <label for="setting">Story Setting</label>
                <input type="text" id="setting" required placeholder="e.g. A lush Caribbean island">
                <div id="settingError" class="error hidden">Please enter a setting</div>
            </div>
            
            <div class="form-group">
                <label for="challenge">Main Challenge</label>
                <textarea id="challenge" rows="3" required placeholder="e.g. The village was suffering from a terrible drought..."></textarea>
                <div id="challengeError" class="error hidden">Please describe the main challenge</div>
            </div>
            
            <div class="form-group">
                <label for="magicElement">Magical Element (optional)</label>
                <input type="text" id="magicElement" placeholder="e.g. A talking parrot with ancient wisdom">
            </div>
            
            <div class="form-group">
                <label for="moral">Moral or Lesson</label>
                <input type="text" id="moral" required placeholder="e.g. True strength comes from community">
                <div id="moralError" class="error hidden">Please enter a moral or lesson</div>
            </div>
            
            <button type="submit">Weave Your Story</button>
        </form>
        
        <div id="storyOutput" class="story-output hidden"></div>
    </div>

    <script>
        document.addEventListener('DOMContentLoaded', function() {
            const form = document.getElementById('storyForm');
            const storyOutput = document.getElementById('storyOutput');
            
            form.addEventListener('submit', function(e) {
                e.preventDefault();
                
                // Reset errors
                document.querySelectorAll('.error').forEach(el => {
                    el.classList.add('hidden');
                });
                
                // Validate form
                let isValid = true;
                const storyType = document.getElementById('storyType').value;
                const protagonist = document.getElementById('protagonist').value.trim();
                const setting = document.getElementById('setting').value.trim();
                const challenge = document.getElementById('challenge').value.trim();
                const moral = document.getElementById('moral').value.trim();
                const magicElement = document.getElementById('magicElement').value.trim();
                
                if (!storyType) {
                    document.getElementById('storyTypeError').classList.remove('hidden');
                    isValid = false;
                }
                if (!protagonist) {
                    document.getElementById('protagonistError').classList.remove('hidden');
                    isValid = false;
                }
                if (!setting) {
                    document.getElementById('settingError').classList.remove('hidden');
                    isValid = false;
                }
                if (!challenge) {
                    document.getElementById('challengeError').classList.remove('hidden');
                    isValid = false;
                }
                if (!moral) {
                    document.getElementById('moralError').classList.remove('hidden');
                    isValid = false;
                }
                
                if (!isValid) return;
                
                // Generate story
                const story = generateStory({
                    storyType,
                    protagonist,
                    setting,
                    challenge,
                    magicElement,
                    moral
                });
                
                // Display story
                storyOutput.textContent = story;
                storyOutput.classList.remove('hidden');
                
                // Scroll to story
                storyOutput.scrollIntoView({ behavior: 'smooth' });
            });
            
            function generateStory(data) {
                const typeTitles = {
                    fairyTale: "A Fairy Tale",
                    familyLore: "A Family Story",
                    myth: "An Ancient Myth",
                    legend: "A Timeless Legend"
                };
                
                const title = `${typeTitles[data.storyType]}: ${data.protagonist}'s Journey`;
                
                let story = `\n${title}\n\n`;
                story += `Once upon a time, in ${data.setting}, there lived ${data.protagonist}. `;
                
                if (data.magicElement) {
                    story += `One day, ${data.protagonist} encountered ${data.magicElement}. `;
                }
                
                story += `${data.challenge} `;
                story += `${data.protagonist} faced this challenge with courage and wisdom. `;
                
                if (data.magicElement) {
                    story += `With the help of ${data.magicElement.split(' ')[0]}, `;
                } else {
                    story += `Through perseverance and cleverness, `;
                }
                
                story += `${data.protagonist} overcame the obstacle and learned that ${data.moral}. `;
                story += `And so, the story of ${data.protagonist} became ${data.storyType === 'familyLore' ? 'a cherished family memory' : 'a tale told for generations'}.\n\n`;
                story += `The End.`;
                
                return story;
            }
            
            // Save story to localStorage if needed
            function saveStory(story) {
                try {
                    const stories = JSON.parse(localStorage.getItem('savedStories') || '[]');
                    stories.push(story);
                    localStorage.setItem('savedStories', JSON.stringify(stories));
                } catch (error) {
                    console.error('Failed to save story:', error);
                }
            }
        });
    </script>
</body>
</html>
```
