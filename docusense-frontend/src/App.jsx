import React, { useState } from "react";
import UploadBox from "./components/UploadBox";
import ResultBox from "./components/ResultBox";

function App() {
  const [file, setFile] = useState(null);
  const [result, setResult] = useState({});
  const [loading, setLoading] = useState(false);

  const handleUpload = async () => {
    if (!file) return alert("Please select a file!");

    setLoading(true);

    const formData = new FormData();
    formData.append("file", file);

    try {
      const response = await fetch("http://127.0.0.1:8000/summarize", {
        method: "POST",
        body: formData,
      });

      const data = await response.json();
      setResult(data);

      if (!response.ok) {
        alert(data.detail || "Error processing document");
      }
    } catch (error) {
      alert("Error connecting to backend.");
    }

    setLoading(false);
  };

  return (
    <div className="max-w-5xl mx-auto py-10 px-6 dark:bg-gray-900 dark:text-white min-h-screen">
      <h1 className="text-3xl font-bold text-center mb-8">
        DocuSense – AI Document Summarizer
      </h1>

      <div className="bg-white dark:bg-gray-800 p-10 rounded-2xl shadow-xl">
        <UploadBox
          onFileSelect={setFile}
          onUpload={handleUpload}
          loading={loading}
          file={file}
        />

        <ResultBox
          originalText={result.original_text}
          summary={result.summary}
        />
      </div>
    </div>
  );
}

export default App;
