from btcpy.setup import setup
setup('testnet')

# 2-of-2 Multisig Script
from btcpy.structs.crypto import PublicKey, PrivateKey
from btcpy.structs.script import MultisigScript
from btcpy.structs.address import P2shAddress
import os

# Generate two random private keys
private_key1 = PrivateKey.unhexlify(os.urandom(32).hex())
private_key2 = PrivateKey.unhexlify(os.urandom(32).hex())

# Derive the public keys
public_key1 = PrivateKey.unhexlify(private_key1.hexlify()).pub()
public_key2 = PrivateKey.unhexlify(private_key2.hexlify()).pub()

# Create a 2-of-2 multisig redeem script
redeem_script = MultisigScript(2, public_key1, public_key2, 2)

# Create a P2SH address from the redeem script
address = P2shAddress.from_script(redeem_script, mainnet=None)

print("Private Key 1:", private_key1)
print("Private Key 2:", private_key2)
print("Redeem Script:", redeem_script.hexlify())
print("Multisig Address:", address)

