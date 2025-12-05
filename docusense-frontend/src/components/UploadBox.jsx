import React from "react";

const UploadBox = ({ onFileSelect, onUpload, loading, file }) => {
  return (
    <div className="border-2 border-dashed border-gray-300 bg-white dark:bg-gray-800 shadow-md p-10 rounded-2xl text-center transition-all">

      <h2 className="text-xl font-bold mb-4">Upload your document</h2>

      {/* Selected file name */}
      {file && (
        <p className="text-sm text-gray-600 dark:text-gray-300 mb-3">
          Selected: <strong>{file.name}</strong>
        </p>
      )}

      <input
        type="file"
        accept="application/pdf, image/*"
        onChange={(e) => onFileSelect(e.target.files[0])}
        className="mb-5"
      />

      <button
        onClick={onUpload}
        disabled={loading}
        className="px-6 py-3 bg-blue-600 text-white rounded-lg hover:bg-blue-700 disabled:opacity-50 flex items-center justify-center gap-2 mx-auto"
      >
        {loading && (
          <span className="animate-spin h-5 w-5 border-2 border-white border-t-transparent rounded-full"></span>
        )}

        {loading ? "Processing..." : "Summarize Document"}
      </button>
    </div>
  );
};

export default UploadBox;
