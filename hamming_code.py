def calculate_parity_positions(n):
    """Calculate positions of parity bits based on the length of the data"""
    positions=[]
    i=0
    while(2**i)<=n+len(positions):
        positions.append(2**i-1)
        i+=1
        return positions
    
def encode_hamming(data):
    """Encode data using hamming code."""
    n=len(data)
    parity_positions=calculate_parity_positions(n)
    total_length=n+len(parity_positions)
    encoded_data=['0']*total_length
   #insert data bits into non-parity positions
    j=0
    for i in range(1,total_length+1):
        if i not in parity_positions:
            encoded_data[i]=data[i]
            j+=1
   #calculate parity bits
    for parity_position in parity_positions:
        parity=0
        for i in range(1,total_length+1):
            if i & (parity_position+1) and i!=(parity_position+1):
                
