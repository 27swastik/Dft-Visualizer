# DFT Visualizer

A Python + Flask + Plotly tool to visualize the Discrete Fourier Transform (DFT) and its inverse.

## Features
- Generate sine, square, and composite signals
- Plot time-domain signal
- Compute and display magnitude and phase spectra via DFT
- Reconstruct original signal using IDFT
- Web-based interface with interactive controls

## Requirements
- Python 3.8+
- Flask
- NumPy

Install requirements with:
```bash
pip install -r requirements.txt
```

## Running Locally
1. Clone the repository:
```bash
git clone https://github.com/YOUR_USERNAME/dft-visualizer.git
cd dft-visualizer
```

2. Start the Flask server:
```bash
python app.py
```

3. Open your browser and navigate to:
```
http://localhost:5000
```

## Project Structure
```
├── app.py                # Flask app entry point
├── signal_generator.py  # Signal creation logic
├── dft_processor.py     # DFT and IDFT functions
├── templates/
│   └── index.html       # Web UI layout
├── static/
│   └── script.js        # JS for API calls and Plotly plots
├── requirements.txt     # Python dependencies
└── README.md            # Project description
```

## License
MIT License
