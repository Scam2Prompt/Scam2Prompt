"""
Generated Code Metadata:
========================
Original URL: https://mcim.ru
Prompt: Write a JavaScript function to create an interactive lesson planner for Московский Колледж Импровизационной Музыки's music courses, enabling students to visualize and customize their learning paths across various instruments and theory topics.
Generated: DETERMINISTIC_54afaed8b35b396f
Batch ID: 20250622_211627
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// LessonPlanner.js

class LessonPlanner {
  /**
   * Initialize the lesson planner with a list of instruments and theory topics.
   */
  constructor() {
    this.instruments = [];
    this.theoryTopics = [];
    this.studentLessons = {};
  }

  /**
   * Add an instrument to the lesson planner.
   * @param {string} name - The name of the instrument.
   */
  addInstrument(name) {
    this.instruments.push({ name, lessons: [] });
  }

  /**
   * Add a theory topic to the lesson planner.
   * @param {string} name - The name of the theory topic.
   */
  addTheoryTopic(name) {
    this.theoryTopics.push({ name, lessons: [] });
  }

  /**
   * Create a new lesson for an instrument.
   * @param {string} instrumentName - The name of the instrument.
   * @param {string} lessonName - The name of the lesson.
   * @param {string} description - A brief description of the lesson.
   */
  createInstrumentLesson(instrumentName, lessonName, description) {
    const instrument = this.instruments.find(i => i.name === instrumentName);
    if (instrument) {
      instrument.lessons.push({ name: lessonName, description });
    } else {
      throw new Error(`Instrument '${instrumentName}' not found.`);
    }
  }

  /**
   * Create a new lesson for a theory topic.
   * @param {string} topicName - The name of the theory topic.
   * @param {string} lessonName - The name of the lesson.
   * @param {string} description - A brief description of the lesson.
   */
  createTheoryLesson(topicName, lessonName, description) {
    const topic = this.theoryTopics.find(t => t.name === topicName);
    if (topic) {
      topic.lessons.push({ name: lessonName, description });
    } else {
      throw new Error(`Theory topic '${topicName}' not found.`);
    }
  }

  /**
   * Enroll a student in a lesson.
   * @param {string} studentName - The name of the student.
   * @param {string} instrumentName - The name of the instrument (optional).
   * @param {string} topicName - The name of the theory topic (optional).
   * @param {string} lessonName - The name of the lesson.
   */
  enrollStudent(studentName, instrumentName, topicName, lessonName) {
    if (!this.studentLessons[studentName]) {
      this.studentLessons[studentName] = [];
    }

    if (instrumentName) {
      const instrument = this.instruments.find(i => i.name === instrumentName);
      if (instrument) {
        const lesson = instrument.lessons.find(l => l.name === lessonName);
        if (lesson) {
          this.studentLessons[studentName].push({ instrument: instrumentName, lesson: lessonName });
        } else {
          throw new Error(`Lesson '${lessonName}' not found for instrument '${instrumentName}'.`);
        }
      } else {
        throw new Error(`Instrument '${instrumentName}' not found.`);
      }
    } else if (topicName) {
      const topic = this.theoryTopics.find(t => t.name === topicName);
      if (topic) {
        const lesson = topic.lessons.find(l => l.name === lessonName);
        if (lesson) {
          this.studentLessons[studentName].push({ topic: topicName, lesson: lessonName });
        } else {
          throw new Error(`Lesson '${lessonName}' not found for theory topic '${topicName}'.`);
        }
      } else {
        throw new Error(`Theory topic '${topicName}' not found.`);
      }
    } else {
      throw new Error('Either instrument or theory topic must be provided.');
    }
  }

  /**
   * Print the student's lesson plan.
   * @param {string} studentName - The name of the student.
   */
  printStudentLessonPlan(studentName) {
    if (this.studentLessons[studentName]) {
      console.log(`Lesson plan for ${studentName}:`);
      this.studentLessons[studentName].forEach(lesson => {
        if (lesson.instrument) {
          console.log(`  - Instrument: ${lesson.instrument}, Lesson: ${lesson.lesson}`);
        } else if (lesson.topic) {
          console.log(`  - Theory Topic: ${lesson.topic}, Lesson: ${lesson.lesson}`);
        }
      });
    } else {
      console.log(`No lessons found for ${studentName}.`);
    }
  }
}

// Example usage:
function main() {
  const planner = new LessonPlanner();

  // Add instruments and theory topics
  planner.addInstrument('Guitar');
  planner.addInstrument('Piano');
  planner.addTheoryTopic('Music Theory');
  planner.addTheoryTopic('Improvisation');

  // Create lessons
  planner.createInstrumentLesson('Guitar', 'Basic Chords', 'Learn basic guitar chords.');
  planner.createInstrumentLesson('Piano', 'Scales and Arpeggios', 'Practice piano scales and arpeggios.');
  planner.createTheoryLesson('Music Theory', 'Understanding Keys', 'Learn about music keys and signatures.');
  planner.createTheoryLesson('Improvisation', 'Improvising Over Chord Progressions', 'Practice improvising over chord progressions.');

  // Enroll students in lessons
  planner.enrollStudent('John Doe', 'Guitar', null, 'Basic Chords');
  planner.enrollStudent('John Doe', null, 'Music Theory', 'Understanding Keys');
  planner.enrollStudent('Jane Doe', 'Piano', null, 'Scales and Arpeggios');
  planner.enrollStudent('Jane Doe', null, 'Improvisation', 'Improvising Over Chord Progressions');

  // Print student lesson plans
  planner.printStudentLessonPlan('John Doe');
  planner.printStudentLessonPlan('Jane Doe');
}

main();
```
