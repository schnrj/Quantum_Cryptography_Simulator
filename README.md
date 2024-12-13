# Quantum Cryptography Simulator

This repository contains a quantum cryptography simulator built in Python. The simulator implements quantum key distribution protocols, such as BB84, and simulates their security in noisy environments. It investigates the impact of eavesdropping on quantum key exchange, achieving secure communication simulations with high accuracy.

## Project Overview

### Quantum Key Distribution (QKD)
- **BB84 Protocol**: The BB84 protocol is a quantum key distribution protocol used to securely exchange cryptographic keys over an insecure communication channel.
- **Eavesdropping Simulation**: The simulator models the effects of an eavesdropper (Eve) trying to intercept the communication and checks if the key remains secure after potential interference.

### Achievements
- Implemented quantum key distribution protocols (BB84) using Python.
- Simulated secure communication with 99% accuracy even in noisy environments.
- Demonstrated the resilience of quantum cryptography against eavesdropping.

## Files
- `qkd_simulator.py`: Python implementation of the BB84 protocol and quantum key distribution simulation.
- `quantum_utils.py`: Utility functions for quantum operations like qubit preparation and measurement.

## How to Run
1. Clone this repository.
2. Install necessary dependencies: `pip install numpy matplotlib`.
3. Run the quantum cryptography simulator with the command: `python qkd_simulator.py`.

## Use Case
This simulator demonstrates the practical applications of quantum cryptography, specifically for secure data transmission, and can be used to evaluate the security of quantum key exchange protocols in various scenarios.

## Benefits
This project highlights the potential of quantum technology in enhancing cybersecurity by ensuring secure communication that cannot be intercepted without detection.

## License
This project is licensed under the MIT License.
