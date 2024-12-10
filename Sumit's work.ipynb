

import numpy as np
from pyldpc import make_ldpc, encode, decode, get_message
import random
import time
from flask import Flask, request, jsonify

# Function to simulate quantum channel with bit errors
def quantum_channel_simulation(data, error_rate=0.1):
    """Simulate quantum channel with bit errors."""
    noisy_data = []
    for bit in data:
        # Flip the bit with a probability equal to the error rate
        noisy_data.append(bit if random.random() > error_rate else 1 - bit)
    return noisy_data

# Create a parity-check matrix for LDPC
n, d_v, d_c = 15, 3, 5  # Parameters for LDPC
H, G = make_ldpc(n, d_v, d_c, systematic=True, sparse=True)

# Function to rank ECC methods
def rank_ecc_methods(ecc_methods, data, error_rate):
    rankings = []
    for method in ecc_methods:
        start_time = time.time()
        encoded = method["encode"](data)
        noisy_data = quantum_channel_simulation(encoded, error_rate)
        decoded = method["decode"](noisy_data)
        end_time = time.time()

        # Compute performance metrics
        error_corrected = sum(o != r for o, r in zip(data, decoded))
        rankings.append({
            "method": method["name"],
            "errors_corrected": error_corrected,
            "runtime": end_time - start_time
        })
    
    # Sort by errors corrected and runtime
    return sorted(rankings, key=lambda x: (-x["errors_corrected"], x["runtime"]))

# Function to simulate quantum key distribution workflow
def quantum_key_distribution_workflow(data, ecc_methods, error_rate):
    # Step 1: Simulate quantum channel
    noisy_data = quantum_channel_simulation(data, error_rate)

    # Step 2: Apply ECC and rank methods
    rankings = rank_ecc_methods(ecc_methods, data, error_rate)
    best_method = rankings[0]

    # Step 3: Use the best ECC for error correction
    encoded = best_method["encode"](data)
    noisy_data = quantum_channel_simulation(encoded, error_rate)
    corrected_data = get_message(G, decode(H, noisy_data, snr=5))  # Corrected this line

    return corrected_data, rankings

# Example usage
original_data = np.random.randint(2, size=G.shape[1])  # Generate random data
ecc_methods = [
    {"name": "LDPC", "encode": lambda x: encode(G, x, snr=5), "decode": lambda y: get_message(G, decode(H, y, snr=5))},
    # Add polar or turbo code implementations here
]
ranked_results = rank_ecc_methods(ecc_methods, original_data, error_rate=0.05)
print("Ranked Results:")
print(ranked_results)

corrected_data, rankings = quantum_key_distribution_workflow(
    original_data, ecc_methods, error_rate=0.05
)
print("Corrected Data:", corrected_data)
print("Rankings:", rankings)

app = Flask(__name__)

@app.route('/select_ecc', methods=['POST'])
def select_ecc():
    data = request.json
    ecc_methods = data.get("ecc_methods")
    error_rate = data.get("error_rate")
    # Assume original_data is provided or generated
    original_data = np.array(data.get("original_data"))  # Get original data from request
    if len(original_data) < G.shape[1]:  # Check if data length is sufficient
        return jsonify({"error": "Data length is too short"})
    rankings = rank_ecc_methods(ecc_methods, original_data, error_rate)
    return jsonify(rankings)

if __name__ == '__main__':
    app.run(debug=True)
