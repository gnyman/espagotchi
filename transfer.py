import sys
import zlib
import base64

def process_file(filename):
    # Read the input file
    with open(filename, 'r') as f:
        content = f.read()
    
    # Compress with level 3
    compressed = zlib.compress(content.encode(), level=3)
    
    # Base64 encode the compressed data
    base64_data = base64.b64encode(compressed).decode()
    
    # Create the output script
    output_script = f"""import os
import uzlib
import ubinascii
c='{base64_data}'
def setup_espagotchi():
    try:
        os.mkdir('/lib/espagotchi')
    except OSError:
        pass
def write_module(b64_data):
    decoded = ubinascii.a2b_base64(b64_data)
    with open('/lib/espagotchi/__init__.py', 'w') as f:
        f.write(uzlib.decompress(decoded))
write_module(c)"""
    
    print(output_script)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <input_file>")
        sys.exit(1)
    
    input_file = sys.argv[1]
    process_file(input_file)