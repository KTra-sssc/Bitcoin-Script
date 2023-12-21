# P2PKH Script
from cryptos import *
c = Bitcoin(testnet=True)

from btcpy.setup import setup
setup('testnet')

from btcpy.structs.address import Address
import os

# Generate a random private key
private_key = sha256(os.urandom(32))

# Derive the public key and Bitcoin address
public_key = c.privtopub(private_key)
address = c.pubtoaddr(public_key)

# Use btcpy to check the method that specify the address
addr = Address.from_string(address)
print("Generate method: ", type(addr))

print("Private Key:", private_key)
print("Public Key:", public_key)
print("Bitcoin Address:", address)





