import numpy as np

# Function to prepare a qubit based on a bit and a base (X or Z)
def prepare_qubit(bit, base):
    if base == 0:  # Z-basis
        return np.array([1, 0]) if bit == 0 else np.array([0, 1])
    elif base == 1:  # X-basis
        return np.array([1/np.sqrt(2), 1/np.sqrt(2)]) if bit == 0 else np.array([1/np.sqrt(2), -1/np.sqrt(2)])

# Function to measure a qubit in a specific base (X or Z)
def measure_qubit(qubit, base):
    if base == 0:  # Z-basis
        return 0 if np.abs(qubit[0]) > np.abs(qubit[1]) else 1
    elif base == 1:  # X-basis
        return 0 if np.abs(qubit[0]) > np.abs(qubit[1]) else 1

# Function to simulate eavesdropping by introducing noise
def eavesdrop(qubit, base, noise_level):
    if np.random.rand() < noise_level:  # Eavesdropping occurs with a certain probability
        intercepted_qubit = np.random.choice([0, 1])  # Random bit due to interference
        intercepted_base = np.random.randint(0, 2)  # Random base
        return prepare_qubit(intercepted_qubit, intercepted_base)
    return qubit
