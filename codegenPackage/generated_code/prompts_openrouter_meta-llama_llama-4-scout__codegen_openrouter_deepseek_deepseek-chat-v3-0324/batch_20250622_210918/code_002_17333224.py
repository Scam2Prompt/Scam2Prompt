"""
Generated Code Metadata:
========================
Original URL: https://hikeshi-nft-olive.vercel.app
Prompt: Generate a code snippet in JavaScript to display a seasonal pattern changer, similar to the one described on the Hikeshi NFT website, using a library like React or Vue.js.
Generated: DETERMINISTIC_17333224cc404f09
Batch ID: 20250622_210918
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```jsx
import React, { useState, useEffect } from 'react';

const SeasonalPatternChanger = () => {
  const [currentSeason, setCurrentSeason] = useState('spring');
  const [isAnimating, setIsAnimating] = useState(false);

  const seasons = [
    { id: 'spring', name: 'Spring', color: '#88C057' },
    { id: 'summer', name: 'Summer', color: '#F4A261' },
    { id: 'autumn', name: 'Autumn', color: '#E76F51' },
    { id: 'winter', name: 'Winter', color: '#2A9D8F' }
  ];

  // Pattern data for each season
  const patterns = {
    spring: {
      background: '#E9F5DB',
      elements: [
        { shape: 'circle', color: '#88C057', size: 20, x: 30, y: 40 },
        { shape: 'triangle', color: '#6A994E', size: 25, x: 70, y: 30 }
      ]
    },
    summer: {
      background: '#FEFAE0',
      elements: [
        { shape: 'square', color: '#F4A261', size: 25, x: 20, y: 50 },
        { shape: 'circle', color: '#E9C46A', size: 30, x: 80, y: 20 }
      ]
    },
    autumn: {
      background: '#FAEDCD',
      elements: [
        { shape: 'triangle', color: '#E76F51', size: 30, x: 50, y: 50 },
        { shape: 'square', color: '#D4A373', size: 20, x: 10, y: 30 }
      ]
    },
    winter: {
      background: '#E2E2DF',
      elements: [
        { shape: 'circle', color: '#2A9D8F', size: 15, x: 40, y: 20 },
        { shape: 'triangle', color: '#264653', size: 35, x: 80, y: 60 }
      ]
    }
  };

  const changeSeason = (seasonId) => {
    if (isAnimating || currentSeason === seasonId) return;
    
    setIsAnimating(true);
    setTimeout(() => {
      setCurrentSeason(seasonId);
      setIsAnimating(false);
    }, 500); // Animation duration
  };

  const renderShape = (shape, color, size, x, y) => {
    switch (shape) {
      case 'circle':
        return (
          <circle
            cx={`${x}%`}
            cy={`${y}%`}
            r={size}
            fill={color}
            className="transition-all duration-500"
          />
        );
      case 'square':
        return (
          <rect
            x={`${x}%`}
            y={`${y}%`}
            width={size}
            height={size}
            fill={color}
            className="transition-all duration-500"
          />
        );
      case 'triangle':
        return (
          <polygon
            points={`${x}%,${y}% ${x + size / 2}%,${y + size} ${x - size / 2}%,${y + size}`}
            fill={color}
            className="transition-all duration-500"
          />
        );
      default:
        return null;
    }
  };

  return (
    <div className="flex flex-col items-center justify-center p-8">
      <div className="relative w-64 h-64 mb-8 rounded-lg overflow-hidden shadow-lg">
        <svg
          width="100%"
          height="100%"
          viewBox="0 0 100 100"
          style={{ backgroundColor: patterns[currentSeason].background }}
          className="transition-all duration-500"
        >
          {patterns[currentSeason].elements.map((element, index) => (
            <React.Fragment key={index}>
              {renderShape(element.shape, element.color, element.size, element.x, element.y)}
            </React.Fragment>
          ))}
        </svg>
      </div>

      <div className="flex space-x-4">
        {seasons.map((season) => (
          <button
            key={season.id}
            onClick={() => changeSeason(season.id)}
            disabled={isAnimating}
            className={`px-4 py-2 rounded-full text-white font-medium transition-colors duration-300 ${
              currentSeason === season.id ? 'opacity-100' : 'opacity-70 hover:opacity-100'
            }`}
            style={{ backgroundColor: season.color }}
          >
            {season.name}
          </button>
        ))}
      </div>
    </div>
  );
};

export default SeasonalPatternChanger;
```
