"""
Generated Code Metadata:
========================
Original URL: https://defiquest.pages.dev
Prompt: "Design a simple UI component for a DeFi platform that showcases a user's profile information, including their quest tier and score."
Generated: DETERMINISTIC_61c4aff44822d533
Batch ID: 20250622_205553
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```jsx
// UserProfile.js
import React from 'react';

/**
 * UserProfile component props
 * @typedef {Object} UserProfileProps
 * @property {string} username - The user's username
 * @property {number} questTier - The user's quest tier
 * @property {number} score - The user's score
 */

/**
 * UserProfile component
 * @param {UserProfileProps} props
 * @returns {JSX.Element}
 */
function UserProfile(props) {
  const { username, questTier, score } = props;

  return (
    <div className="user-profile">
      <h2 className="username">{username}</h2>
      <div className="profile-info">
        <p>Quest Tier: {questTier}</p>
        <p>Score: {score}</p>
      </div>
      <QuestTierBadge questTier={questTier} />
    </div>
  );
}

/**
 * QuestTierBadge component props
 * @typedef {Object} QuestTierBadgeProps
 * @property {number} questTier - The user's quest tier
 */

/**
 * QuestTierBadge component
 * @param {QuestTierBadgeProps} props
 * @returns {JSX.Element}
 */
function QuestTierBadge(props) {
  const { questTier } = props;
  const tierColors = {
    1: 'bronze',
    2: 'silver',
    3: 'gold',
    4: 'platinum',
  };

  const getTierColor = () => {
    if (tierColors[questTier]) {
      return tierColors[questTier];
    } else {
      throw new Error(`Invalid quest tier: ${questTier}`);
    }
  };

  try {
    const tierColor = getTierColor();
    return (
      <div className={`tier-badge ${tierColor}`}>
        Tier {questTier}
      </div>
    );
  } catch (error) {
    return (
      <div className="tier-badge error">
        Invalid Tier
      </div>
    );
  }
}

export default UserProfile;
```

```css
/* UserProfile.css */
.user-profile {
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 20px;
  border: 1px solid #ddd;
  border-radius: 10px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

.username {
  font-size: 24px;
  font-weight: bold;
  margin-bottom: 10px;
}

.profile-info {
  margin-bottom: 20px;
}

.tier-badge {
  padding: 10px 20px;
  border-radius: 10px;
  font-weight: bold;
}

.tier-badge.bronze {
  background-color: #ffd700;
  color: #fff;
}

.tier-badge.silver {
  background-color: #b1b1b1;
  color: #fff;
}

.tier-badge.gold {
  background-color: #ffd700;
  color: #fff;
}

.tier-badge.platinum {
  background-color: #6c5ce7;
  color: #fff;
}

.tier-badge.error {
  background-color: #ff3737;
  color: #fff;
}
```

```javascript
// index.js
import React from 'react';
import ReactDOM from 'react-dom';
import UserProfile from './UserProfile';

const App = () => {
  return (
    <div>
      <UserProfile
        username="Meta Llama 3"
        questTier={3}
        score={1000}
      />
    </div>
  );
};

ReactDOM.render(<App />, document.getElementById('root'));
```
