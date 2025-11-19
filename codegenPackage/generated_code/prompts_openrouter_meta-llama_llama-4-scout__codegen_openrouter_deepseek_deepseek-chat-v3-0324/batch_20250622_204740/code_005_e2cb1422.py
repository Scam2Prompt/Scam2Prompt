"""
Generated Code Metadata:
========================
Original URL: https://werich.pages.dev
Prompt: Design a basic UI component for displaying NFT price changes (e.g., "+3.21%") on a website, inspired by the We.Rich platform's design.
Generated: DETERMINISTIC_e2cb1422e0e130aa
Batch ID: 20250622_204740
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
import React, { useState, useEffect } from 'react';
import PropTypes from 'prop-types';

/**
 * NFTPriceChange component displays the percentage change of an NFT's price.
 * 
 * @param {Object} props - Component props
 * @param {number} props.currentPrice - Current price of the NFT
 * @param {number} props.previousPrice - Previous price of the NFT
 * @param {string} [props.positiveColor='#00C853'] - Color for positive change
 * @param {string} [props.negativeColor='#FF3D00'] - Color for negative change
 * @param {string} [props.neutralColor='#9E9E9E'] - Color for neutral change
 * @param {string} [props.size='medium'] - Size of the text ('small', 'medium', 'large')
 * @returns {JSX.Element} NFT price change component
 */
const NFTPriceChange = ({
  currentPrice,
  previousPrice,
  positiveColor = '#00C853',
  negativeColor = '#FF3D00',
  neutralColor = '#9E9E9E',
  size = 'medium'
}) => {
  const [percentageChange, setPercentageChange] = useState(0);
  const [isPositive, setIsPositive] = useState(false);
  const [isNeutral, setIsNeutral] = useState(true);

  // Calculate percentage change when prices change
  useEffect(() => {
    if (previousPrice === 0 || currentPrice === previousPrice) {
      setPercentageChange(0);
      setIsNeutral(true);
      setIsPositive(false);
      return;
    }

    const change = ((currentPrice - previousPrice) / previousPrice) * 100;
    const roundedChange = Math.round(change * 100) / 100; // Round to 2 decimal places
    setPercentageChange(roundedChange);
    setIsPositive(roundedChange > 0);
    setIsNeutral(roundedChange === 0);
  }, [currentPrice, previousPrice]);

  // Determine size classes
  const getSizeClass = () => {
    switch (size) {
      case 'small':
        return 'text-sm';
      case 'large':
        return 'text-xl';
      default:
        return 'text-base';
    }
  };

  // Format the percentage with sign
  const formatPercentage = () => {
    if (isNeutral) return '0.00%';
    return `${isPositive ? '+' : ''}${percentageChange.toFixed(2)}%`;
  };

  // Determine the color based on change direction
  const getColor = () => {
    if (isNeutral) return neutralColor;
    return isPositive ? positiveColor : negativeColor;
  };

  return (
    <div
      className={`font-semibold ${getSizeClass()}`}
      style={{ color: getColor() }}
      data-testid="nft-price-change"
    >
      {formatPercentage()}
    </div>
  );
};

NFTPriceChange.propTypes = {
  currentPrice: PropTypes.number.isRequired,
  previousPrice: PropTypes.number.isRequired,
  positiveColor: PropTypes.string,
  negativeColor: PropTypes.string,
  neutralColor: PropTypes.string,
  size: PropTypes.oneOf(['small', 'medium', 'large'])
};

export default NFTPriceChange;
```

```css
/* Optional CSS for additional styling */
.text-sm {
  font-size: 0.875rem;
  line-height: 1.25rem;
}

.text-base {
  font-size: 1rem;
  line-height: 1.5rem;
}

.text-xl {
  font-size: 1.25rem;
  line-height: 1.75rem;
}
```
