document.getElementById('signal-form').onsubmit = async function(e) {
    e.preventDefault();
    const form = e.target;
    const data = Object.fromEntries(new FormData(form));
    for (let k in data) data[k] = parseFloat(data[k]) || data[k];

    const sigRes = await fetch('/generate', {
        method: 'POST', headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(data)
    });
    const sigData = await sigRes.json();

    Plotly.newPlot('time-domain', [{x: sigData.time, y: sigData.signal, type: 'scatter'}], {title: 'Time Domain'});

    const dftRes = await fetch('/transform', {
        method: 'POST', headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({signal: sigData.signal})
    });
    const dftData = await dftRes.json();

    Plotly.newPlot('magnitude', [{y: dftData.magnitude, type: 'bar'}], {title: 'Magnitude Spectrum'});
    Plotly.newPlot('phase', [{y: dftData.phase, type: 'bar'}], {title: 'Phase Spectrum'});
};
