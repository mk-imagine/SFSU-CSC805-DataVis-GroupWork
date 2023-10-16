import React, { useEffect, useRef } from 'react';
import './App.css';
import tableau from 'tableau-api';

function App() {
  const vizContainer = useRef(null);

  const initTableau = () => {
    const vizUrl = 'http://public.tableau.com/views/RegionalSampleWorkbook/Storms';
    let viz = new window.tableau.Viz(vizContainer.current, vizUrl);
  };

  useEffect(() => {
    initTableau();
  }, [])

  return (
    <div className="App">
      <h1>This is React + tableau Demo</h1>
      <div ref={vizContainer} style={{ padding: "20px" }}></div>
    </div>
  );
}

export default App;
