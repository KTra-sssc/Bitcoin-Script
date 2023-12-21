# Spend Locked Funds
from cryptos import *
c = Bitcoin(testnet=True)

# Private key and Bitcoin address from the previous step
private_key = "a90fe4a39087b178bbd7d3e5a2e886d471bf000111b6faa9c0638ea388ad8ab7"
public_key = "048b20041e2f0d8fdb426ea202dce472c9a699003557f64c8d8beef1862e92befb25a4cd2d464972a0646299eed4eb7cdc95acbe3bd4cb7f2b0f182bee37acc169"
address = "mgQXSQAoFbRtkn9t6Bawcvt79XXv42u67w"

# Create a transaction input (UTXO)
txIn = c.unspent(str(address))

# Create a transaction output to the desired destination
to_addr = "tb1qrtzcq4xhm9dsy8f8a4yfs4c92cpj3l3kg2tzae"
txOut = [{'value': 10000, 'address': to_addr}]


# Create the transaction
tx = c.mktx(txIn,txOut)
tx = c.signall(tx, private_key)
tx = serialize(tx)

# Broadcast the transaction
c.pushtx(tx)



