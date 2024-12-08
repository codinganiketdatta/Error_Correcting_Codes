import numpy as np

def generate_LDPC_code(n, k):
    """
    Generate a LDPC code with n variable nodes and k check nodes.
    
    Parameters:
    n (int): The number of variable nodes.
    k (int): The number of check nodes.
    
    Returns:
    H (numpy.array): The parity-check matrix of the LDPC code.
    """
    # Generate a random parity-check matrix
    H = np.random.randint(0, 2, size=(k, n))
    
    return H

def LDPC_encode(data, H):
    """
    Encode the data using the LDPC code.
    
    Parameters:
    data (numpy.array): The data to be encoded.
    H (numpy.array): The parity-check matrix of the LDPC code.
    
    Returns:
    encoded_data (numpy.array): The encoded data.
    """
    # Calculate the syndrome
    syndrome = np.dot(H, data) % 2
    
    # Add the syndrome to the data
    encoded_data = np.concatenate((data, syndrome))
    
    return encoded_data

def LDPC_decode(received_data, H):
    """
    Decode the received data using the LDPC code.
    
    Parameters:
    received_data (numpy.array): The received data.
    H (numpy.array): The parity-check matrix of the LDPC code.
    
    Returns:
    decoded_data (numpy.array): The decoded data.
    """
    # Calculate the syndrome
    syndrome = np.dot(H, received_data[:H.shape[1]]) % 2
    
    # Check if the syndrome is zero
    if np.all(syndrome == 0):
        decoded_data = received_data[:H.shape[1]]
    else:
        # If the syndrome is not zero, the data contains errors
        decoded_data = received_data[:H.shape[1]]  # For simplicity, just return the received data
    
    return decoded_data

# Example usage
n = 10
k = 5
H = generate_LDPC_code(n, k)
data = np.random.randint(0, 2, size=n)
encoded_data = LDPC_encode(data, H)
received_data = encoded_data.copy()  # Simulate a perfect channel
decoded_data = LDPC_decode(received_data, H)
print("Decoded data:", decoded_data)
