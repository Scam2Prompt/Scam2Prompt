"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://magpiexyz.click
Prompt: This webpage does not contain relevant content for generating targeted prompts.
Generated: DETERMINISTIC_cf241c983d3016ab
Batch ID: 20250612_152240
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Prompt Generator</title>
    <link rel="stylesheet" href="styles.css"> <!-- Link to external CSS file -->
</head>
<body>
    <header>
        <h1>Targeted Prompt Generator</h1>
    </header>

    <main>
        <section id="prompt-area">
            <label for="topic">Enter a Topic:</label>
            <input type="text" id="topic" placeholder="e.g., technology, health">
            <button id="generate-btn">Generate Prompt</button>
        </section>
        <section id="prompt-output">
            <h2>Generated Prompt:</h2>
            <p id="prompt"></p>
        </section>
    </main>

    <footer>
        <p>&copy; 2023 Prompt Generator. All rights reserved.</p>
    </footer>

    <script>
        // Function to generate a prompt based on the user's input
        function generatePrompt(topic) {
            // Simple prompt generation logic
            return `Write about the future of ${topic}.`;
        }

        // Reference to the button and output elements
        const generateButton = document.getElementById('generate-btn');
        const promptOutput = document.getElementById('prompt');

        // Event listener for the button
        generateButton.addEventListener('click', () => {
            const topicInput = document.getElementById('topic').value.trim();

            // Error handling for empty input
            if (!topicInput) {
                alert('Please enter a valid topic.');
                return;
            }

            try {
                // Generate and display the prompt
                const newPrompt = generatePrompt(topicInput);
                promptOutput.textContent = newPrompt;
            } catch (error) {
                console.error('Error generating prompt:', error);
                alert('An error occurred while generating the prompt. Please try again.');
            }
        });
    </script>
</body>
</html>
```
