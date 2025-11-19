"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-47--gracious-swanson-bcc8c1.netlify.app
Prompt: Develop a VueJS component for showcasing a developer's skills and location, inspired by Tim Mansell's portfolio content.
Generated: DETERMINISTIC_a6b089b417009353
Batch ID: 20250612_151018
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "http://www.w3.org/2000/svg": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```vue
<template>
  <div class="developer-info">
    <div class="skills-section">
      <h2 class="section-title">Skills</h2>
      <div class="skills-container">
        <div 
          v-for="(skill, index) in skills" 
          :key="index" 
          class="skill-item"
        >
          <span class="skill-name">{{ skill.name }}</span>
          <div class="skill-level">
            <div 
              class="skill-level-bar" 
              :style="{ width: skill.level + '%' }"
            ></div>
          </div>
        </div>
      </div>
    </div>

    <div class="location-section">
      <h2 class="section-title">Location</h2>
      <div class="location-content">
        <div class="location-icon">
          <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor">
            <path d="M12 2C8.13 2 5 5.13 5 9c0 5.25 7 13 7 13s7-7.75 7-13c0-3.87-3.13-7-7-7zm0 9.5c-1.38 0-2.5-1.12-2.5-2.5s1.12-2.5 2.5-2.5 2.5 1.12 2.5 2.5-1.12 2.5-2.5 2.5z"/>
          </svg>
        </div>
        <div class="location-details">
          <p class="location-text">{{ location.city }}, {{ location.country }}</p>
          <p class="timezone-text">Timezone: {{ location.timezone }}</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'DeveloperInfo',
  data() {
    return {
      skills: [
        { name: 'JavaScript', level: 90 },
        { name: 'Vue.js', level: 85 },
        { name: 'HTML/CSS', level: 95 },
        { name: 'Node.js', level: 80 },
        { name: 'Git', level: 75 }
      ],
      location: {
        city: 'London',
        country: 'United Kingdom',
        timezone: 'GMT/BST'
      }
    }
  }
}
</script>

<style scoped>
.developer-info {
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
  max-width: 600px;
  margin: 0 auto;
  padding: 20px;
  color: #333;
}

.section-title {
  font-size: 1.5rem;
  margin-bottom: 1rem;
  color: #2c3e50;
  border-bottom: 2px solid #42b983;
  padding-bottom: 0.5rem;
}

.skills-container {
  margin-bottom: 2rem;
}

.skill-item {
  margin-bottom: 1rem;
}

.skill-name {
  display: inline-block;
  width: 120px;
  font-weight: 600;
}

.skill-level {
  display: inline-block;
  width: calc(100% - 130px);
  height: 10px;
  background-color: #e0e0e0;
  border-radius: 5px;
  overflow: hidden;
  vertical-align: middle;
}

.skill-level-bar {
  height: 100%;
  background-color: #42b983;
  border-radius: 5px;
  transition: width 0.5s ease;
}

.location-content {
  display: flex;
  align-items: center;
  gap: 1rem;
}

.location-icon svg {
  width: 24px;
  height: 24px;
  fill: #42b983;
}

.location-details {
  flex: 1;
}

.location-text {
  font-weight: 600;
  margin-bottom: 0.25rem;
}

.timezone-text {
  color: #666;
  font-size: 0.9rem;
}

@media (max-width: 480px) {
  .skill-name {
    width: 100px;
  }
  
  .skill-level {
    width: calc(100% - 110px);
  }
}
</style>
```
