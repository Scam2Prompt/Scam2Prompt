"""
Generated Code Metadata:
========================
Original URL: https://stellarcropgame.fun
Prompt: Recommend a suitable front-end framework for building a responsive, web-based interface for a game like Stellar Crop, and provide an example of how to structure the code for a character-driven storyline.
Generated: DETERMINISTIC_686c09290719eabf
Batch ID: 20250622_212447
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Stellar Crop - Frontend Framework Recommendation: React.js
// Example structure for a character-driven storyline component

import React, { useState, useEffect } from 'react';
import PropTypes from 'prop-types';

/**
 * CharacterStoryline Component
 * Handles the rendering and progression of character-driven storylines
 */
const CharacterStoryline = ({ initialStoryState, characters, onStoryComplete }) => {
  const [currentStoryState, setCurrentStoryState] = useState(initialStoryState);
  const [currentDialogue, setCurrentDialogue] = useState(null);
  const [characterImages, setCharacterImages] = useState({});
  const [playerChoices, setPlayerChoices] = useState([]);
  const [isLoading, setIsLoading] = useState(true);

  // Load character assets
  useEffect(() => {
    const loadAssets = async () => {
      try {
        const loadedImages = {};
        for (const character of characters) {
          const image = await import(`./assets/characters/${character.id}.png`);
          loadedImages[character.id] = image.default;
        }
        setCharacterImages(loadedImages);
        setIsLoading(false);
      } catch (error) {
        console.error('Error loading character assets:', error);
        setIsLoading(false);
      }
    };

    loadAssets();
  }, [characters]);

  // Update current dialogue when story state changes
  useEffect(() => {
    if (currentStoryState && currentStoryState.dialogueId) {
      const dialogue = getDialogueById(currentStoryState.dialogueId);
      setCurrentDialogue(dialogue);
      
      if (dialogue.choices) {
        setPlayerChoices(dialogue.choices);
      } else {
        setPlayerChoices([]);
      }
    }
  }, [currentStoryState]);

  const getDialogueById = (id) => {
    // In a real implementation, this would fetch from a database or API
    return {
      id: 'dialogue1',
      characterId: 'farmer',
      text: 'Welcome to Stellar Crop! The harvest season is approaching...',
      choices: [
        { text: 'Ask about the harvest', nextState: 'harvest_info' },
        { text: 'Inquire about the farm', nextState: 'farm_info' }
      ]
    };
  };

  const handleChoiceSelection = (choice) => {
    if (!choice.nextState) {
      onStoryComplete();
      return;
    }

    setCurrentStoryState(prevState => ({
      ...prevState,
      currentState: choice.nextState,
      dialogueId: generateDialogueId(choice.nextState)
    }));
  };

  const generateDialogueId = (state) => {
    return `dialogue_${state}`;
  };

  if (isLoading) {
    return <div className="loading-screen">Loading story...</div>;
  }

  return (
    <div className="storyline-container">
      {currentDialogue && (
        <div className="dialogue-section">
          <div className="character-display">
            <img 
              src={characterImages[currentDialogue.characterId]} 
              alt={characters.find(c => c.id === currentDialogue.characterId)?.name || 'Character'}
            />
            <h3>{characters.find(c => c.id === currentDialogue.characterId)?.name}</h3>
          </div>
          
          <div className="dialogue-text">
            <p>{currentDialogue.text}</p>
          </div>
          
          {playerChoices.length > 0 && (
            <div className="choices-container">
              {playerChoices.map((choice, index) => (
                <button 
                  key={index}
                  className="choice-button"
                  onClick={() => handleChoiceSelection(choice)}
                >
                  {choice.text}
                </button>
              ))}
            </div>
          )}
        </div>
      )}
    </div>
  );
};

CharacterStoryline.propTypes = {
  initialStoryState: PropTypes.shape({
    currentState: PropTypes.string,
    dialogueId: PropTypes.string
  }).isRequired,
  characters: PropTypes.arrayOf(
    PropTypes.shape({
      id: PropTypes.string.isRequired,
      name: PropTypes.string.isRequired,
      description: PropTypes.string
    })
  ).isRequired,
  onStoryComplete: PropTypes.func.isRequired
};

export default CharacterStoryline;
```
