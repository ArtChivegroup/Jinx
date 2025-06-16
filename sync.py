import random
import string
import time
import hashlib
import os

def generate_key(epoch_time=None):
    """Generate a unique 8-char alphanumeric key based on current 3-hour window."""
    if epoch_time is None:
        epoch_time = int(time.time())
    window = epoch_time // (3 * 3600)
    hash_input = f"JinxSyncKey{window}".encode()
    hashed = hashlib.sha256(hash_input).hexdigest()
    chars = string.ascii_letters + string.digits
    random.seed(int(hashed[:8], 16))
    key = ''.join(random.choices(chars, k=8))
    return key

def write_key(filepath):
    # Pastikan direktori tujuan ada
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    key = generate_key()
    with open(filepath, "w") as f:
        f.write(key + "\n")

if __name__ == "__main__":
    write_key("Jinx/files/Sync")
