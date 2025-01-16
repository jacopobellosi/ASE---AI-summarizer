import { useState } from "react";
import QuizRenderer from "./QuizRenderer";
import { AssessmentTest } from "../../clients/paraphrasing_tool";

const Quiz = ({ quizData }: { quizData: AssessmentTest }) => {
  const [responses, setResponses] = useState<{ [key: string]: string[] }>({});
  const [submitted, setSubmitted] = useState(false);
  const [scoreSummary, setScoreSummary] = useState<string | null>(null);

  const handleResponseChange = (questionId: string, response: string[]) => {
    console.log(`User chose option ${response} for question ${questionId}`);
    setResponses((prev) => ({
      ...prev,
      [questionId]: response,
    }));
  };

  const handleSubmit = () => {
    console.log("User Responses:", responses);
    setSubmitted(true); // Set submitted to true when the quiz is submitted

    const correctAnswers = quizData.sections.reduce((acc, section) => {
      return acc + section.items.reduce((sectionAcc, question) => {
        const userAnswer = new Set(responses[question.identifier] || []);
        const correctAnswers = new Set(question.response_declaration.correct_response);
        const isCorrect = userAnswer.size === correctAnswers.size && [...userAnswer].every(answer => correctAnswers.has(answer));
        return sectionAcc + (isCorrect ? 1 : 0);
      }, 0);
    }, 0);

    const totalQuestions = quizData.sections.reduce((acc, section) => acc + section.items.length, 0);
    const message = `You got ${correctAnswers} out of ${totalQuestions} correct!`;
    setScoreSummary(message);
  };

  return (
    <div style={{ backgroundColor: "#f5f5f5", minHeight: "100vh", padding: "20px" }}>
      <h1>{quizData.title}</h1>
      <QuizRenderer
        test={quizData}
        responses={responses}
        onResponseChange={handleResponseChange}
        submitted={submitted}
      />
      {scoreSummary && (
        <div style={{ backgroundColor: "#fff", borderRadius: "8px", boxShadow: "0 4px 8px rgba(0, 0, 0, 0.1)", padding: "20px", marginBottom: "20px" }}>
          <h2>Quiz Completed!</h2>
          <p>{scoreSummary}</p>
          <p>Great job! 🎉</p>
        </div>
      )}
      <button
        className="btn btn-warning"
        onClick={handleSubmit}
        style={{ marginTop: "20px" }}
      >
        Submit
      </button>
    </div>
  );
};

export default Quiz;

