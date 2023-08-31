import React, { useState } from 'react';

function DocSumm() {
  const [inputFile, setInputFile] = useState('');
  const [isLoading, setIsLoading] = useState(false);
  const [resultText, setResultText] = useState('');

  const handleProcessText = async () => {
    setIsLoading(true);
  
    try {
      // Ici, vous pouvez appeler l'API pour traiter le texte
      const response = await fetch('http://localhost:3001/summary', {
        method: 'POST', 
        body: JSON.stringify({ file_path: inputFile }), // Envoyer le texte à traiter
        headers: {
          'Content-Type': 'application/json',
        },
      });
  
      if (response.ok) {
        const data = await response.json();
        setResultText(data.sum); // Mettre à jour le résultat
      } else {
        setResultText('Une erreur s\'est produite lors du traitement.');
      }
    } catch (error) {
      console.error('Erreur lors de la communication avec l\'API :', error);
      setResultText('Une erreur s\'est produite lors du traitement.');
    }
  
    setIsLoading(false);
  };
  

  return (
    
      
      <div className="text-sum">
        
        <input
          type="text"
          value={inputFile}
          onChange={e => setInputFile(e.target.value)}
          placeholder="Path file"
        />
        <br/>
        <br/>
        <button className="button"  onClick={handleProcessText}>Get summary</button>
        <br/>
        {isLoading ? (
            <div>
              <br/>
             <img src="loading.png" alt="Chargement en cours" />
             <p> "It takes time, please wait..."</p>
            </div>
         ): null }

        
        <br/>
        <div>
        <textarea
          value={resultText} // Afficher le résultat dans le textarea
          readOnly // Empêcher l'édition du résultat
          placeholder="Result"
        />
      </div>
         {/* Correction ici */}
        
        
      
       
        

      </div>
  );
}

export default DocSumm;
