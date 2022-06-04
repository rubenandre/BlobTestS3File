import { useEffect } from 'react';
import './App.css';
import axios from 'axios';

function App() {
  useEffect(() => {
    axios('http://127.0.0.1:5000/', {
      method: 'GET',
      responseType: 'blob'
    })
    .then(response => {
        console.log(response)
        const file = new Blob(
          [response.data], 
          {type: 'application/pdf'});
        const fileURL = URL.createObjectURL(file);
        window.open(fileURL);
    })
    .catch(error => {
        console.log(error);
    });
  }, [])

  return (
    <div className="App">
    </div>
  );
}

export default App;
