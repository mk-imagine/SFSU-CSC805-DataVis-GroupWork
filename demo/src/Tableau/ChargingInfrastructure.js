import React, { useEffect, useRef } from "react";
import "../App.css";
import tableau from "tableau-api";

function ChargingInfrastructure() {
  const vizContainer = useRef(null);

  const initTableau = () => {
    const vizUrl =
      "https://public.tableau.com/views/inf_dash/inf_dash";
    let viz = new window.tableau.Viz(vizContainer.current, vizUrl);
  };

  useEffect(() => {
    initTableau();
  }, []);

  return (
    <div className="layout">
      <h1>Charging Infrastructure</h1>
      <div ref={vizContainer} style={{ padding: "20px" }}></div>
    </div>
  );
}

export default ChargingInfrastructure;
