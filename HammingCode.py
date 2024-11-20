class HammingCode:
    def __init__(self, data_length):
        """
        Initialize the HammingCode object.

        :param data_length: The length of the data to be encoded.
        """
        self.data_length = data_length
        self.codeword_length = 2 ** (data_length - 1).bit_length()
        self.parity_length = self.codeword_length - self.data_length
        self.mask = (1 << self.data_length) - 1

    def encode(self, data):
        """
        Encode the input data using Hamming code.

        :param data: The input data to be encoded.
        :return: The encoded codeword.
        """
        codeword = 0
        for i in range(self.data_length):
            if (data & (1 << i)) != 0:
                codeword ^= self._generate_codeword(i)
        return codeword

    def decode(self, codeword):
        """
        Decode the input codeword using Hamming code.

        :param codeword: The input codeword to be decoded.
        :return: The decoded data and the error location (if any).
        """
        syndrome = self._calculate_syndrome(codeword)
        error_location = self._locate_error(syndrome)
        if error_location != -1:
            codeword ^= 1 << error_location
        return codeword & self.mask, error_location

    def _generate_codeword(self, index):
        """
        Generate the codeword for a single data bit.

        :param index: The index of the data bit.
        :return: The codeword for the data bit.
        """
        codeword = 0
        for i in range(self.parity_length):
            if (index >> i) & 1:
                codeword ^= 1 << (self.data_length + i)
        return codeword

    def _calculate_syndrome(self, codeword):
        """
        Calculate the syndrome of the input codeword.

        :param codeword: The input codeword.
        :return: The syndrome of the codeword.
        """
        syndrome = 0
        for i in range(self.parity_length):
            parity = 0
            for j in range(self.codeword_length):
                if (j >> i) & 1:
                    parity ^= (codeword >> j) & 1
            syndrome |= parity << i
        return syndrome

    def _locate_error(self, syndrome):
        """
        Locate the error in the input syndrome.

        :param syndrome: The input syndrome.
        :return: The error location (if any), or -1 if no error is detected.
        """
        error_location = -1
        for i in range(self.codeword_length):
            if syndrome == (1 << i):
                error_location = i
                break
        return error_location

# Example usage:

hamming_code = HammingCode(11)
data = 0b110011
codeword = hamming_code.encode(data)
print(f"Codeword: {bin(codeword)}")

# Introduce a single-bit error
error_location = 4
codeword ^= 1 << error_location

# Decode the corrupted codeword
decoded_data, error_location = hamming_code.decode(codeword)
print(f"Decoded data: {bin(decoded_data)}")
print(f"Error location: {error_location}")


