import numpy as np
import ldpc.codes
from ldpc.bplsd_decoder import BpLsdDecoder

H = ldpc.codes.hamming_code(5)

## The
bp_osd = BpLsdDecoder(
            H,
            error_rate = 0.1,
            bp_method = 'product_sum',
            max_iter = 2,
            schedule = 'serial',
            lsd_method = 'lsd_cs',
            lsd_order = 0
        )

syndrome = np.random.randint(size=H.shape[0], low=0, high=2).astype(np.uint8)

print(f"Syndrome: {syndrome}")
decoding = bp_osd.decode(syndrome)
print(f"Decoding: {decoding}")
decoding_syndrome = H@decoding % 2
print(f"Decoding syndrome: {decoding_syndrome}")