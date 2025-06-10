from flask import Flask, request, jsonify, render_template
from signal_generator import generate_signal
from dft_processor import compute_dft, compute_idft
import numpy as np

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    data = request.json
    t, signal = generate_signal(data['waveform'], data['frequency'], data['amplitude'], data['duration'], data['sampling_rate'])
    return jsonify({"time": t.tolist(), "signal": signal.tolist()})

@app.route('/transform', methods=['POST'])
def transform():
    signal = np.array(request.json['signal'])
    mag, phase = compute_dft(signal)
    return jsonify({"magnitude": mag, "phase": phase})

@app.route('/reconstruct', methods=['POST'])
def reconstruct():
    spec = np.array(request.json['spectrum'], dtype=complex)
    recon = compute_idft(spec)
    return jsonify({"reconstructed": recon.tolist()})

if __name__ == '__main__':
    app.run(debug=True)