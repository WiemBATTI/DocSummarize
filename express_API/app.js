const express = require('express');
const bodyParser = require('body-parser');
const { exec } = require('child_process');
const cors = require('cors'); // Importer le module cors
const app = express();
const port=  process.env.PORT || 3001



//app.listen(port, () => { console.log('Listening on port 3000')});
// Middleware pour analyser le corps des demandes en JSON
app.use(bodyParser.json());

// Configuration CORS
const corsOptions = {
  origin: 'http://localhost:3000', // Remplacez par l'URL de votre application React
  methods: 'GET,HEAD,PUT,PATCH,POST,DELETE',
  credentials: true,
  optionsSuccessStatus: 204,
};

app.use(cors(corsOptions)); // Utiliser le middleware cors avec les options configurées


// Point d'extrémité pour le résumé
app.post('/summary', (req, res) => {
  // Chemin absolu vers l'exécutable Python
  const pythonExecutable = 'C:\\Users\\ASUS CORE I5\\AppData\\Local\\Programs\\Python\\Python311\\python.exe';

  // Chemin absolu vers le script Python
  const pythonScriptPath = 'D:\\GSI2\\Stage_Technix\\doc_summarize\\NLP_project\\doc.py';

  // Arguments à passer au script Python (par exemple, le chemin du fichier)
  const file_path = req.body.file_path; // Récupérer le chemin du fichier depuis le corps de la requête POST

  const command = `"${pythonExecutable}" "${pythonScriptPath}" "${file_path}"`;

  // Exécuter le script Python avec le chemin du fichier en tant qu'argument
  exec(command, (error, stdout, stderr) => {    if (error) {
      console.error(`Erreur: ${error}`);
      //console.error(`stderr: ${stderr}`);
      return res.status(500).json({ error: 'Erreur lors de l\'exécution du script Python' });
    }
    // Traitement des résultats et renvoi de la réponse
    const resultat = stdout.trim();  // Supprimer les retours à la ligne et espaces // Cela dépend du format de sortie de votre script Python
    //res.json({ l :lang.encode('utf-8')});

    const encodedLang = Buffer.from(resultat, 'utf-8');
    res.json({ sum: encodedLang.toString() });
    //res.setHeader('Content-Type', 'application/json; charset=utf-8'); // Définir l'encodage pour la réponse JSON
    //res.end(JSON.stringify(response));
  });
});



// Endpoint pour le traitement du texte brut
app.post('/text', (req, res) => {

    // Chemin absolu vers l'exécutable Python
    const pythonExecutable = 'C:\\Users\\ASUS CORE I5\\AppData\\Local\\Programs\\Python\\Python311\\python.exe';

    // Chemin absolu vers le script Python
    const pythonScriptPath = 'D:\\GSI2\\Stage_Technix\\doc_summarize\\NLP_project\\text.py';
  
    // Arguments à passer au script Python (par exemple, le chemin du fichier)
    const text = req.body.text; // Récupérer le texte depuis le corps de la requête POST
  
    const command = `"${pythonExecutable}" "${pythonScriptPath}" "${text}"`;

    // Exécuter le script Python avec le chemin du fichier en tant qu'argument
    exec(command, (error, stdout, stderr) => {    if (error) {
      console.error(`Erreur: ${error}`);
      //console.error(`stderr: ${stderr}`);
      return res.status(500).json({ error: 'Erreur lors de l\'exécution du script Python' });
    }
    // Traitement des résultats et renvoi de la réponse
    const resultat = stdout.replace(/\r\n/g, " ");  // Supprimer les retours à la ligne et espaces // Cela dépend du format de sortie de votre script Python
    //res.json({ l :lang.encode('utf-8')});

    const encodedLang = Buffer.from(resultat, 'utf-8');
    res.json({ sum: encodedLang.toString() });
    //res.setHeader('Content-Type', 'application/json; charset=utf-8'); // Définir l'encodage pour la réponse JSON
    //res.end(JSON.stringify(response));
});
  
  // Traiter le texte brut
  // ...
  //res.send('Traitement du texte terminé.');
});


// Démarrer le serveur
app.listen(port, () => {
  console.log(`Le serveur Express écoute sur le port ${port}`);
});


