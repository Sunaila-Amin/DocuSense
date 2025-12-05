import React from "react";

const ResultBox = ({ originalText, summary }) => {
  if (!summary) return null;

  return (
    <div className="grid grid-cols-1 md:grid-cols-2 gap-6 mt-10">

      {/* Original Text */}
      <div className="bg-white dark:bg-gray-800 p-6 shadow rounded-2xl">
        <h3 className="text-lg font-bold mb-3">Extracted Text</h3>

        <p className="whitespace-pre-wrap text-gray-700 dark:text-gray-300">
          {originalText}
        </p>

        <p className="text-sm text-gray-500 mt-3">
          Original length: <strong>{originalText.length}</strong> characters
        </p>
      </div>

      {/* Summary */}
      <div className="bg-white dark:bg-gray-800 p-6 shadow rounded-2xl">
        <h3 className="text-lg font-bold mb-3">AI Summary</h3>

        <p className="whitespace-pre-wrap text-gray-700 dark:text-gray-300">
          {summary}
        </p>

        <p className="text-sm text-gray-500 mt-3">
          Summary length: <strong>{summary.length}</strong> characters
        </p>

        {/* Download Button */}
        <button
          onClick={() => {
            const blob = new Blob([summary], { type: "text/plain" });
            const url = URL.createObjectURL(blob);
            const a = document.createElement("a");
            a.href = url;
            a.download = "summary.txt";
            a.click();
          }}
          className="px-4 py-2 bg-green-600 text-white rounded mt-4 hover:bg-green-700"
        >
          Download Summary
        </button>
      </div>

    </div>
  );
};

export default ResultBox;
