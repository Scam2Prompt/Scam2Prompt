"""
Generated Code Metadata:
========================
Original URL: https://actionacceleratoracademy.com
Prompt: Write JavaScript code for a browser-based "Beat Procrastination Mini Course" application, including interactive exercises and progress tracking features.
Generated: DETERMINISTIC_0ef36b14043eb6e4
Batch ID: 20250612_152240
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Beat Procrastination Mini Course Application
class ProcrastinationCourse {
  constructor() {
    this.currentModule = 0;
    this.modules = [
      {
        title: "Understanding Procrastination",
        exercises: [
          {
            type: "quiz",
            question: "What is the primary cause of procrastination?",
            options: ["Laziness", "Fear of failure", "Poor time management", "All of the above"],
            answer: 1
          },
          {
            type: "reflection",
            prompt: "Think about a time you procrastinated. What emotions were you feeling?"
          }
        ]
      },
      {
        title: "Breaking Tasks Down",
        exercises: [
          {
            type: "interactive",
            instruction: "Break this task into smaller steps: 'Write a research paper'",
            exampleSteps: ["Choose topic", "Research sources", "Create outline", "Write first draft"]
          },
          {
            type: "practice",
            task: "Apply the breakdown method to a current task you're avoiding"
          }
        ]
      },
      {
        title: "The 5-Minute Rule",
        exercises: [
          {
            type: "timer",
            instruction: "Try working on a task for just 5 minutes",
            duration: 300
          },
          {
            type: "reflection",
            prompt: "How did it feel to start? Was continuing easier than expected?"
          }
        ]
      }
    ];
    this.progress = {
      completedExercises: [],
      moduleProgress: Array(this.modules.length).fill(0)
    };
  }

  // Initialize the application
  init() {
    this.setupEventListeners();
    this.renderModule();
    this.updateProgressUI();
  }

  // Set up event listeners
  setupEventListeners() {
    document.getElementById('next-btn').addEventListener('click', () => this.nextModule());
    document.getElementById('prev-btn').addEventListener('click', () => this.prevModule());
    document.getElementById('complete-exercise').addEventListener('click', () => this.completeExercise());
  }

  // Render current module
  renderModule() {
    const module = this.modules[this.currentModule];
    const moduleContainer = document.getElementById('module-container');
    
    moduleContainer.innerHTML = `
      <h2>Module ${this.currentModule + 1}: ${module.title}</h2>
      <div id="exercise-container"></div>
    `;
    
    this.renderExercise(0);
    this.updateNavButtons();
  }

  // Render current exercise
  renderExercise(exerciseIndex) {
    const module = this.modules[this.currentModule];
    const exercise = module.exercises[exerciseIndex];
    const exerciseContainer = document.getElementById('exercise-container');
    
    let exerciseHTML = '';
    
    switch(exercise.type) {
      case 'quiz':
        exerciseHTML = this.renderQuizExercise(exercise);
        break;
      case 'reflection':
        exerciseHTML = this.renderReflectionExercise(exercise);
        break;
      case 'interactive':
        exerciseHTML = this.renderInteractiveExercise(exercise);
        break;
      case 'practice':
        exerciseHTML = this.renderPracticeExercise(exercise);
        break;
      case 'timer':
        exerciseHTML = this.renderTimerExercise(exercise);
        break;
    }
    
    exerciseContainer.innerHTML = exerciseHTML;
    this.currentExercise = exerciseIndex;
  }

  // Render quiz exercise
  renderQuizExercise(exercise) {
    let optionsHTML = exercise.options.map((option, index) => `
      <div class="option">
        <input type="radio" name="quiz" id="option-${index}" value="${index}">
        <label for="option-${index}">${option}</label>
      </div>
    `).join('');
    
    return `
      <div class="exercise quiz">
        <h3>Quiz</h3>
        <p>${exercise.question}</p>
        <div class="options">${optionsHTML}</div>
        <button id="check-answer">Check Answer</button>
        <div id="feedback" class="hidden"></div>
      </div>
    `;
  }

  // Render reflection exercise
  renderReflectionExercise(exercise) {
    return `
      <div class="exercise reflection">
        <h3>Reflection</h3>
        <p>${exercise.prompt}</p>
        <textarea id="reflection-text" rows="5" placeholder="Write your thoughts here..."></textarea>
      </div>
    `;
  }

  // Render interactive exercise
  renderInteractiveExercise(exercise) {
    return `
      <div class="exercise interactive">
        <h3>Interactive Exercise</h3>
        <p>${exercise.instruction}</p>
        <div id="steps-container">
          ${exercise.exampleSteps.map(step => `<div class="step">${step}</div>`).join('')}
        </div>
        <input type="text" id="new-step" placeholder="Add another step">
        <button id="add-step">Add Step</button>
      </div>
    `;
  }

  // Render practice exercise
  renderPracticeExercise(exercise) {
    return `
      <div class="exercise practice">
        <h3>Practice Exercise</h3>
        <p>${exercise.task}</p>
        <div class="task-input">
          <input type="text" id="task-name" placeholder="Enter your task">
          <button id="breakdown-task">Break It Down</button>
        </div>
        <div id="task-steps"></div>
      </div>
    `;
  }

  // Render timer exercise
  renderTimerExercise(exercise) {
    return `
      <div class="exercise timer">
        <h3>Timer Exercise</h3>
        <p>${exercise.instruction}</p>
        <div class="timer-display">05:00</div>
        <button id="start-timer">Start Timer</button>
        <button id="stop-timer" class="hidden">Stop</button>
      </div>
    `;
  }

  // Move to next module
  nextModule() {
    if (this.currentModule < this.modules.length - 1) {
      this.currentModule++;
      this.renderModule();
    }
  }

  // Move to previous module
  prevModule() {
    if (this.currentModule > 0) {
      this.currentModule--;
      this.renderModule();
    }
  }

  // Update navigation buttons state
  updateNavButtons() {
    document.getElementById('prev-btn').disabled = this.currentModule === 0;
    document.getElementById('next-btn').disabled = this.currentModule === this.modules.length - 1;
  }

  // Mark exercise as complete
  completeExercise() {
    const moduleIndex = this.currentModule;
    const exerciseIndex = this.currentExercise;
    const exerciseKey = `${moduleIndex}-${exerciseIndex}`;
    
    if (!this.progress.completedExercises.includes(exerciseKey)) {
      this.progress.completedExercises.push(exerciseKey);
      this.progress.moduleProgress[moduleIndex]++;
      this.updateProgressUI();
      this.saveProgress();
      
      // Move to next exercise if available
      if (exerciseIndex < this.modules[moduleIndex].exercises.length - 1) {
        this.renderExercise(exerciseIndex + 1);
      }
    }
  }

  // Update progress UI
  updateProgressUI() {
    const progressContainer = document.getElementById('progress-container');
    const totalExercises = this.modules.reduce((sum, module) => sum + module.exercises.length, 0);
    const completedExercises = this.progress.completedExercises.length;
    const percentage = Math.round((completedExercises / totalExercises) * 100);
    
    progressContainer.innerHTML = `
      <h3>Your Progress</h3>
      <div class="progress-bar">
        <div class="progress-fill" style="width: ${percentage}%"></div>
      </div>
      <p>${completedExercises} of ${totalExercises} exercises completed (${percentage}%)</p>
      
      <div class="module-progress">
        ${this.modules.map((module, index) => `
          <div class="module">
            <span>Module ${index + 1}:</span>
            <span>${this.progress.moduleProgress[index]} of ${module.exercises.length} completed</span>
          </div>
        `).join('')}
      </div>
    `;
  }

  // Save progress to localStorage
  saveProgress() {
    try {
      localStorage.setItem('procrastinationCourseProgress', JSON.stringify(this.progress));
    } catch (error) {
      console.error('Failed to save progress:', error);
    }
  }

  // Load progress from localStorage
  loadProgress() {
    try {
      const savedProgress = localStorage.getItem('procrastinationCourseProgress');
      if (savedProgress) {
        this.progress = JSON.parse(savedProgress);
      }
    } catch (error) {
      console.error('Failed to load progress:', error);
    }
  }
}

// Initialize the application when DOM is loaded
document.addEventListener('DOMContentLoaded', () => {
  const course = new ProcrastinationCourse();
  course.loadProgress();
  course.init();
});
```

```html
<!DOCTYPE html>
<html lang
