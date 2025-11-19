"""
Generated Code Metadata:
========================
Original URL: https://adamhome.vn
Prompt: "Design a UI component for a painting services website that allows customers to select colors and visualize their painting project, inspired by the color selection tools on adamhome.vn."
Generated: DETERMINISTIC_c27c7d9a4d477976
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
import React, { useState, useEffect } from 'react';
import styled from 'styled-components';

// Color palette data
const COLOR_PALETTE = [
  { name: 'Snow White', hex: '#FFFFFF' },
  { name: 'Pearl White', hex: '#F5F5F5' },
  { name: 'Ivory', hex: '#FFFFF0' },
  { name: 'Sky Blue', hex: '#87CEEB' },
  { name: 'Mint Green', hex: '#98FF98' },
  { name: 'Lavender', hex: '#E6E6FA' },
  { name: 'Coral', hex: '#FF7F50' },
  { name: 'Sandstone', hex: '#D3C5A5' },
  { name: 'Charcoal', hex: '#36454F' },
  { name: 'Midnight Blue', hex: '#191970' },
];

// Styled components
const Container = styled.div`
  max-width: 800px;
  margin: 0 auto;
  padding: 2rem;
  font-family: 'Arial', sans-serif;
`;

const Title = styled.h2`
  color: #333;
  margin-bottom: 1.5rem;
  text-align: center;
`;

const ColorGrid = styled.div`
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(100px, 1fr));
  gap: 1rem;
  margin-bottom: 2rem;
`;

const ColorCard = styled.div`
  cursor: pointer;
  padding: 1rem;
  border-radius: 8px;
  text-align: center;
  transition: transform 0.2s;
  border: ${props => props.selected ? '3px solid #333' : '1px solid #ddd'};
  transform: ${props => props.selected ? 'scale(1.05)' : 'none'};
  
  &:hover {
    transform: scale(1.05);
  }
`;

const ColorPreview = styled.div`
  width: 100%;
  height: 80px;
  border-radius: 4px;
  margin-bottom: 0.5rem;
  background-color: ${props => props.color};
`;

const ColorName = styled.p`
  margin: 0;
  font-size: 0.9rem;
  font-weight: ${props => props.selected ? 'bold' : 'normal'};
`;

const PreviewArea = styled.div`
  width: 100%;
  height: 300px;
  border-radius: 8px;
  margin-top: 2rem;
  background-color: ${props => props.color || '#f5f5f5'};
  border: 1px solid #ddd;
  position: relative;
  overflow: hidden;
`;

const RoomLabel = styled.div`
  position: absolute;
  bottom: 1rem;
  left: 1rem;
  background-color: rgba(0, 0, 0, 0.7);
  color: white;
  padding: 0.5rem 1rem;
  border-radius: 4px;
`;

const ErrorMessage = styled.div`
  color: #d32f2f;
  background-color: #fde8e8;
  padding: 1rem;
  border-radius: 4px;
  margin-top: 1rem;
  text-align: center;
`;

const ColorPicker = () => {
  const [selectedColor, setSelectedColor] = useState(null);
  const [error, setError] = useState(null);

  const handleColorSelect = (color) => {
    try {
      setSelectedColor(color);
      setError(null);
    } catch (err) {
      setError('Failed to select color. Please try again.');
      console.error('Color selection error:', err);
    }
  };

  return (
    <Container>
      <Title>Choose Your Paint Color</Title>
      
      {error && <ErrorMessage>{error}</ErrorMessage>}
      
      <ColorGrid>
        {COLOR_PALETTE.map((color) => (
          <ColorCard
            key={color.hex}
            onClick={() => handleColorSelect(color)}
            selected={selectedColor && selectedColor.hex === color.hex}
          >
            <ColorPreview color={color.hex} />
            <ColorName selected={selectedColor && selectedColor.hex === color.hex}>
              {color.name}
            </ColorName>
          </ColorCard>
        ))}
      </ColorGrid>
      
      <PreviewArea color={selectedColor?.hex}>
        {selectedColor && (
          <RoomLabel>
            {selectedColor.name} - {selectedColor.hex}
          </RoomLabel>
        )}
      </PreviewArea>
    </Container>
  );
};

export default ColorPicker;
```
