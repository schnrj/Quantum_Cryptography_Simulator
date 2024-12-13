import numpy as np
import matplotlib.pyplot as plt
from quantum_utils import prepare_qubit, measure_qubit, eavesdrop

# Function to simulate BB84 Protocol
def bb84_protocol(num_bits=1000, noise_level=0.05):
    # Alice's preparation of qubits
    alice_bits = np.random.randint(0, 2, num_bits)  # Random 0s and 1s (Alice's key)
    alice_bases = np.random.randint(0, 2, num_bits)  # Random bases (0 = X, 1 = Z)
    
    alice_qubits = [prepare_qubit(bit, base) for bit, base in zip(alice_bits, alice_bases)]
    
    # Bob's measurement of qubits
    bob_bases = np.random.randint(0, 2, num_bits)  # Bob randomly chooses bases
    bob_results = [measure_qubit(qubit, base) for qubit, base in zip(alice_qubits, bob_bases)]
    
    # Eve's eavesdropping (introducing noise)
    eavesdropped_qubits = [eavesdrop(qubit, base, noise_level) for qubit, base in zip(alice_qubits, bob_bases)]
    
    # Post-processing (public discussion)
    # Alice and Bob compare their bases and discard mismatched ones
    matching_bases = alice_bases == bob_bases
    final_key = alice_bits[matching_bases]
    final_key_bob = bob_results[matching_bases]
    
    # Calculate the accuracy of the shared key
    accuracy = np.mean(final_key == final_key_bob) * 100
    
    print(f"Security of the key exchange: {accuracy}%")
    
    # Plot the security (accuracy) for various noise levels
    noise_range = np.linspace(0, 0.5, 10)
    accuracies = [bb84_protocol(num_bits, noise) for noise in noise_range]
    
    plt.plot(noise_range, accuracies, label="BB84 Security vs Noise")
    plt.xlabel("Noise Level")
    plt.ylabel("Key Exchange Accuracy (%)")
    plt.title("BB84 Protocol Security")
    plt.legend()
    plt.show()

if __name__ == "__main__":
    bb84_protocol(num_bits=1000, noise_level=0.05)
