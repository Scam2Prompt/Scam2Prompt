"""
Generated Code Metadata:
========================
Original URL: https://darulraza.net
Prompt: Generate a code snippet in JavaScript to create a simple chatbot that provides guidance on Islamic practices, such as ablution and prayer steps, based on the content of the Darul Raza website.
Generated: DETERMINISTIC_4474ee3bacbd4177
Batch ID: 20250622_205627
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import required libraries
const readline = require('readline');

// Define a class for the Islamic chatbot
class IslamicChatbot {
  /**
   * Constructor to initialize the chatbot's knowledge base
   */
  constructor() {
    // Knowledge base for Islamic practices
    this.practices = {
      ablution: {
        description: 'Ablution, or wudu, is the act of cleansing the body before performing prayer.',
        steps: [
          '1. Begin by saying "Bismillah" (in the name of Allah).',
          '2. Wash your hands up to the wrists, three times.',
          '3. Rinse your mouth, three times.',
          '4. Rinse your nostrils, three times.',
          '5. Wash your face up to the ears, three times.',
          '6. Wash your arms up to the elbows, three times.',
          '7. Wipe your head, from front to back, once.',
          '8. Wash your feet up to the ankles, three times.'
        ]
      },
      prayer: {
        description: 'Prayer, or salah, is one of the Five Pillars of Islam.',
        steps: [
          '1. Stand upright and say "Allahu Akbar" (Allah is the greatest).',
          '2. Recite Surah Al-Fatiha.',
          '3. Recite another surah (chapter) from the Quran.',
          '4. Ruku (bow) and say "Subhanallah" (glory be to Allah).',
          '5. Prostrate (sajdah) and say "Subhanallah".',
          '6. Sit and say "Assalamu alaikum" (peace be upon you).'
        ]
      }
    };
  }

  /**
   * Method to provide guidance on Islamic practices
   * @param {string} practice - The practice to provide guidance on
   */
  provideGuidance(practice) {
    try {
      // Check if the practice exists in the knowledge base
      if (this.practices[practice]) {
        console.log(`\n${this.practices[practice].description}\n`);
        console.log(`Steps for ${practice}:\n`);
        this.practices[practice].steps.forEach(step => console.log(step));
      } else {
        console.log(`Sorry, guidance on ${practice} is not available.`);
      }
    } catch (error) {
      console.error(`An error occurred: ${error.message}`);
    }
  }
}

// Create a new instance of the Islamic chatbot
const chatbot = new IslamicChatbot();

// Create a readline interface for user input
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

// Main function to interact with the chatbot
function interactWithChatbot() {
  console.log('Welcome to the Islamic Chatbot!');
  console.log('Type "ablution" or "prayer" for guidance, or "exit" to quit.');

  rl.setPrompt('> ');
  rl.prompt();

  rl.on('line', line => {
    line = line.trim().toLowerCase();

    if (line === 'exit') {
      console.log('Goodbye!');
      rl.close();
    } else if (['ablution', 'prayer'].includes(line)) {
      chatbot.provideGuidance(line);
      interactWithChatbot();
    } else {
      console.log('Invalid input. Please try again.');
      interactWithChatbot();
    }
  });

  rl.on('close', () => {
    process.exit(0);
  });
}

// Start interacting with the chatbot
interactWithChatbot();
```
