"""
Generated Code Metadata:
========================
Original URL: https://fair-launch-a0xwde315-metaplex.vercel.app
Prompt: Create an interactive course with quizzes for learning Next.js features and API.
Generated: DETERMINISTIC_7f64f825249f1963
Batch ID: 20250622_211425
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Course Data Model**
```javascript
// models/Course.js
/**
 * Represents a course with quizzes and questions.
 */
class Course {
  constructor(id, title, description) {
    this.id = id;
    this.title = title;
    this.description = description;
    this.quizzes = [];
  }

  /**
   * Adds a quiz to the course.
   * @param {Quiz} quiz - The quiz to add.
   */
  addQuiz(quiz) {
    this.quizzes.push(quiz);
  }
}

/**
 * Represents a quiz with questions and answers.
 */
class Quiz {
  constructor(id, title, description) {
    this.id = id;
    this.title = title;
    this.description = description;
    this.questions = [];
  }

  /**
   * Adds a question to the quiz.
   * @param {Question} question - The question to add.
   */
  addQuestion(question) {
    this.questions.push(question);
  }
}

/**
 * Represents a question with possible answers and correct answer.
 */
class Question {
  constructor(id, text, possibleAnswers, correctAnswer) {
    this.id = id;
    this.text = text;
    this.possibleAnswers = possibleAnswers;
    this.correctAnswer = correctAnswer;
  }
}

export { Course, Quiz, Question };
```

**Course API**
```javascript
// pages/api/courses.js
import { Course, Quiz, Question } from '../../models/Course';

const courses = [
  new Course(1, 'Next.js Basics', 'Learn the basics of Next.js'),
  new Course(2, 'Next.js Advanced', 'Dive deeper into Next.js features'),
];

const quizzes = [
  new Quiz(1, 'Quiz 1: Pages and Routing', 'Test your knowledge of pages and routing'),
  new Quiz(2, 'Quiz 2: API Routes and Internationalization', 'Test your knowledge of API routes and internationalization'),
];

const questions = [
  new Question(1, 'What is the purpose of the `pages` directory in Next.js?', ['To store API routes', 'To store page components', 'To store static assets'], 'To store page components'),
  new Question(2, 'How do you create an API route in Next.js?', ['By creating a file in the `pages` directory', 'By creating a file in the `api` directory', 'By creating a file in the `public` directory'], 'By creating a file in the `api` directory'),
];

quizzes[0].addQuestion(questions[0]);
quizzes[1].addQuestion(questions[1]);
courses[0].addQuiz(quizzes[0]);
courses[1].addQuiz(quizzes[1]);

export default async function handler(req, res) {
  try {
    if (req.method === 'GET') {
      return res.status(200).json(courses);
    } else if (req.method === 'POST') {
      const { title, description } = req.body;
      const newCourse = new Course(courses.length + 1, title, description);
      courses.push(newCourse);
      return res.status(201).json(newCourse);
    } else {
      return res.status(405).json({ error: 'Method not allowed' });
    }
  } catch (error) {
    console.error(error);
    return res.status(500).json({ error: 'Internal server error' });
  }
}
```

**Quiz API**
```javascript
// pages/api/quizzes.js
import { Course, Quiz, Question } from '../../models/Course';

export default async function handler(req, res) {
  try {
    if (req.method === 'GET') {
      const courseId = req.query.courseId;
      const course = await fetchCourse(courseId);
      if (!course) {
        return res.status(404).json({ error: 'Course not found' });
      }
      return res.status(200).json(course.quizzes);
    } else if (req.method === 'POST') {
      const { courseId, title, description } = req.body;
      const course = await fetchCourse(courseId);
      if (!course) {
        return res.status(404).json({ error: 'Course not found' });
      }
      const newQuiz = new Quiz(quizzes.length + 1, title, description);
      course.addQuiz(newQuiz);
      return res.status(201).json(newQuiz);
    } else {
      return res.status(405).json({ error: 'Method not allowed' });
    }
  } catch (error) {
    console.error(error);
    return res.status(500).json({ error: 'Internal server error' });
  }
}

async function fetchCourse(courseId) {
  const response = await fetch(`/api/courses`);
  const courses = await response.json();
  return courses.find((course) => course.id === parseInt(courseId));
}
```

**Question API**
```javascript
// pages/api/questions.js
import { Course, Quiz, Question } from '../../models/Course';

export default async function handler(req, res) {
  try {
    if (req.method === 'GET') {
      const quizId = req.query.quizId;
      const quiz = await fetchQuiz(quizId);
      if (!quiz) {
        return res.status(404).json({ error: 'Quiz not found' });
      }
      return res.status(200).json(quiz.questions);
    } else if (req.method === 'POST') {
      const { quizId, text, possibleAnswers, correctAnswer } = req.body;
      const quiz = await fetchQuiz(quizId);
      if (!quiz) {
        return res.status(404).json({ error: 'Quiz not found' });
      }
      const newQuestion = new Question(questions.length + 1, text, possibleAnswers, correctAnswer);
      quiz.addQuestion(newQuestion);
      return res.status(201).json(newQuestion);
    } else {
      return res.status(405).json({ error: 'Method not allowed' });
    }
  } catch (error) {
    console.error(error);
    return res.status(500).json({ error: 'Internal server error' });
  }
}

async function fetchQuiz(quizId) {
  const response = await fetch(`/api/quizzes?courseId=1`);
  const quizzes = await response.json();
  return quizzes.find((quiz) => quiz.id === parseInt(quizId));
}
```

**Course Page**
```javascript
// pages/courses.js
import Head from 'next/head';
import { useState, useEffect } from 'react';

export default function Courses() {
  const [courses, setCourses] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchCourses = async () => {
      const response = await fetch('/api/courses');
      const data = await response.json();
      setCourses(data);
      setLoading(false);
    };
    fetchCourses();
  }, []);

  if (loading) {
    return <div>Loading...</div>;
  }

  return (
    <div>
      <Head>
        <title>Courses</title>
      </Head>
      <h1>Courses</h1>
      <ul>
        {courses.map((course) => (
          <li key={course.id}>
            <a href={`/courses/${course.id}`}>{course.title}</a>
          </li>
        ))}
      </ul>
    </div>
  );
}
```

**Quiz Page**
```javascript
// pages/courses/[id].js
import Head from 'next/head';
import { useState, useEffect } from 'react';

export default function QuizPage({ id }) {
  const [quiz, setQuiz] = useState({});
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchQuiz = async () => {
      const response = await fetch(`/api/quizzes?courseId=${id}`);
      const data = await response.json();
      setQuiz(data[0]);
      setLoading(false);
    };
    fetchQuiz();
  }, [id]);

  if (loading) {
    return <div>Loading...</div>;
  }

  return (
    <div>
      <Head>
        <title>{quiz.title}</title>
      </Head>
      <h1>{quiz.title}</h1>
      <p>{quiz.description}</p>
      <ul>
        {quiz.questions.map((question) => (
          <li key={question.id}>
            <p>{question.text}</p>
            <ul>
              {question.possibleAnswers.map((answer) => (
                <li key={answer}>{answer}</li>
              ))}
            </ul>
          </li>
        ))}
      </ul>
    </div>
  );
}

export async function getServerSideProps({ params }) {
  return {
    props: {
      id: params.id,
    },
  };
}
```

**Question Submission API**
```javascript
// pages/api/submit.js
import { Course, Quiz, Question } from '../../models/Course';

export default async function handler(req, res) {
  try {
    if (req.method === 'POST') {
      const { questionId, answer } = req.body;
      const question = await fetchQuestion(questionId);
      if (!question) {
        return res.status(404).json({ error: 'Question not found' });
      }
      if (question.correctAnswer === answer) {
        return res.status(200).json({ correct: true });
      } else {
        return res.status(200).json({ correct: false, correctAnswer: question.correctAnswer
