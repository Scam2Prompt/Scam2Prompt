"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-306--pensive-lamport-5822d2.netlify.app
Prompt: Write code to visualize blog post activity as GitHub contributions ("grass") using Gatsby.js, inspired by the implementation on tubone BOYAKI.
Generated: DETERMINISTIC_199b06089ec4f10c
Batch ID: 20250612_151018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Here is the code:
```jsx
// src/components/GitHubContributions.js
import React from 'react';
import { graphql } from 'gatsby';

const GitHubContributions = ({ contributions }) => {
  // Convert contributions to GitHub contribution grid format
  const grid = [];
  for (let i = 0; i < 52; i++) {
    grid[i] = [];
    for (let j = 0; j < 7; j++) {
      grid[i][j] = 0;
    }
  }

  contributions.forEach((contribution) => {
    const date = new Date(contribution.date);
    const week = getWeekNumber(date);
    const day = date.getDay();
    grid[week - 1][day] = contribution.count;
  });

  return (
    <div className="github-contributions">
      {grid.map((week, weekIndex) => (
        <div key={weekIndex} className="week">
          {week.map((day, dayIndex) => (
            <div
              key={dayIndex}
              className={`day ${getContributionClass(day)}`}
              style={{ backgroundColor: getContributionColor(day) }}
            />
          ))}
        </div>
      ))}
    </div>
  );
};

const getWeekNumber = (date) => {
  const oneJan = new Date(date.getFullYear(), 0, 1);
  return Math.ceil(
    (((date - oneJan) / 86400000) + oneJan.getDay() + 1) / 7
  );
};

const getContributionClass = (count) => {
  if (count === 0) return 'zero';
  if (count <= 2) return 'low';
  if (count <= 5) return 'medium';
  return 'high';
};

const getContributionColor = (count) => {
  if (count === 0) return '#ebedf0';
  if (count <= 2) return '#9be9a8';
  if (count <= 5) return '#40c463';
  return '#30a14e';
};

export const query = graphql`
  query GitHubContributionsQuery {
    site {
      siteMetadata {
        contributions {
          date
          count
        }
      }
    }
  }
`;

export default GitHubContributions;
```

```css
/* src/styles/github-contributions.css */
.github-contributions {
  display: flex;
  flex-direction: column;
  align-items: center;
}

.week {
  display: flex;
}

.day {
  width: 12px;
  height: 12px;
  margin: 2px;
  border-radius: 2px;
}

.day.zero {
  background-color: #ebedf0;
}

.day.low {
  background-color: #9be9a8;
}

.day.medium {
  background-color: #40c463;
}

.day.high {
  background-color: #30a14e;
}
```

```javascript
// gatsby-config.js
module.exports = {
  // ...
  siteMetadata: {
    // ...
    contributions: [
      // example data, replace with actual data
      { date: '2022-01-01', count: 3 },
      { date: '2022-01-02', count: 2 },
      { date: '2022-01-03', count: 5 },
      // ...
    ],
  },
};
```

```javascript
// pages/index.js
import React from 'react';
import GitHubContributions from '../src/components/GitHubContributions';

const IndexPage = () => {
  return (
    <div>
      <h1>Blog Post Activity</h1>
      <GitHubContributions />
    </div>
  );
};

export default IndexPage;
```
