"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-306--pensive-lamport-5822d2.netlify.app
Prompt: Write code to visualize blog post activity as GitHub contributions ("grass") using Gatsby.js, inspired by the implementation on tubone BOYAKI.
Generated: DETERMINISTIC_199b06089ec4f10c
Batch ID: 20250612_151018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// gatsby-config.js
module.exports = {
  siteMetadata: {
    title: `Blog Post Activity Grass`,
    description: `Visualize blog post activity as GitHub-like contribution graph.`,
    author: `Your Name`,
  },
  plugins: [`gatsby-plugin-react-helmet`, `gatsby-plugin-sharp`, `gatsby-transformer-sharp`],
};

// src/components/ContributionGraph.js
import React from 'react';
import PropTypes from 'prop-types';
import styles from './ContributionGraph.module.css';

const ContributionGraph = ({ activityData }) => {
  /**
   * activityData is an array of objects, each representing
   * daily blog activity with `date` and `count` properties.
   * Example:
   * [
   *   { date: '2023-01-01', count: 5 },
   *   { date: '2023-01-02', count: 3 },
   *   ...
   * ]
   */

  // Generate the graph as a grid-like structure
  // GitHub grass has a maximum of 7 rows (days of a week)
  const weeks = Array.from({ length: 52 }, () => Array(7).fill(0));

  activityData.forEach(({ date, count }) => {
    const dateObj = new Date(date);
    const week = Math.floor(dateObj.getTime() / (1000 * 60 * 60 * 24 * 7)) % 52;
    const day = dateObj.getDay(); // Sunday = 0, Monday = 1, ..., Saturday = 6
    weeks[week][day] = count;
  });

  return (
    <div className={styles.graph}>
      {weeks.map((week, weekIndex) => (
        <div key={weekIndex} className={styles.week}>
          {week.map((count, dayIndex) => (
            <div
              key={dayIndex}
              className={styles.day}
              style={{
                backgroundColor: `rgba(0, 128, 0, ${Math.min(count / 10, 1)})`, // Scale color intensity
              }}
              title={`Activity: ${count}`}
            ></div>
          ))}
        </div>
      ))}
    </div>
  );
};

ContributionGraph.propTypes = {
  activityData: PropTypes.arrayOf(
    PropTypes.shape({
      date: PropTypes.string.isRequired,
      count: PropTypes.number.isRequired,
    })
  ).isRequired,
};

export default ContributionGraph;

// src/components/ContributionGraph.module.css
.graph {
  display: flex;
  flex-wrap: wrap;
  gap: 2px;
}
.week {
  display: flex;
  flex-direction: column;
}
.day {
  width: 12px;
  height: 12px;
  border-radius: 2px;
  border: 1px solid #ccc;
  box-sizing: border-box;
}

// src/pages/index.js
import React from 'react';
import { Helmet } from 'react-helmet';
import ContributionGraph from '../components/ContributionGraph';

const sampleActivityData = [
  { date: '2023-01-01', count: 2 },
  { date: '2023-01-02', count: 5 },
  { date: '2023-01-03', count: 3 },
  { date: '2023-01-04', count: 7 },
  { date: '2023-01-05', count: 4 },
  // Add more sample data as required
]; 

const IndexPage = () => (
  <div>
    <Helmet>
      <title>Blog Post Activity Grass</title>
      <meta name="description" content="Visualize blog post activity as GitHub-like contribution graph." />
    </Helmet>
    <h1>Blog Post Activity Visualization</h1>
    <ContributionGraph activityData={sampleActivityData} />
  </div>
);

export default IndexPage;

// Ensure dependencies are installed:
// 1. Run `npm install gatsby react react-dom gatsby-plugin-react-helmet prop-types`
// 2. Use `gatsby develop` to start the development server.
```
