# 2-of-2 Multisig Script
from cryptos import *
c = Bitcoin(testnet=True)

from btcpy.setup import setup
setup('testnet')

from btcpy.structs.address import Address
import os

# Generate two random private keys
private_key1 = sha256(os.urandom(32))
private_key2 = sha256(os.urandom(32))

# Derive the public keys
public_key1 = c.privtopub(private_key1)
public_key2 = c.privtopub(private_key2)
public_keys = [public_key1, public_key2]

# Create a 2-of-2 multisig redeem script &
# Create a P2SH address from the redeem script
script, address = c.mk_multisig_address(public_keys, 2)

# Use btcpy to check the method that specify the address
addr = Address.from_string(address)
print("Generate method: ", type(addr))

print("Private Key 1:", private_key1)
print("Private Key 2:", private_key2)
print("Redeem Script:", script)
print("Multisig Address:", address)

