import React from 'react';
import TextSumm from './TextSumm'; // Assurez-vous que le chemin vers TextSumm est correct
import DocSumm from './DocSumm';
import { BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom';
import './App.css';

function App() {
  return (
    <div className="app">
      <Router>
        <header className="header">
                  
            <h1 className="title">Doc & text Summarizer</h1>
          
        </header>
        <p className="intro">Let's summarize books, project reports, or texts.<br/> Available languages: English and french.</p>
        <br/>
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/text_summ" element={<TextSumm />} />
          <Route path="/doc_summ" element={<DocSumm />} />
        </Routes>
      </Router>
    </div>
  );
}

function Home() {
  return (
    <div className="content">
      <div className="block">
        <Link to="/doc_summ" className="block-link">
        <br/>
             <img src="pdf_word.png" alt="Image 1" /> 
          <br/>
          <br/>
          <h2>Documents <br /> summarization</h2>
          <p className="txt">Click here <br />to summarize<br /> your documents<br /> (PDF, Word, TXT).</p>
        </Link>
      </div>
      <div className="vertical-line"></div>

      <div className="block">
        <Link to="/text_summ" className="block-link">
          <img src="texte.png" alt="Image 2" />
          
          <h2>Texts <br /> summarization</h2>
          <p className="txt">Click here <br />to paste text<br /> and summarize it.</p>
        </Link>
      </div>
    </div>
  );
}

export default App;
