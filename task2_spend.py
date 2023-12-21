# Spend Locked Funds
from cryptos import *
c = Bitcoin(testnet=True)

# Private keys and multisig address from the previous step
private_key1 = "26187e987e4d2a3761d5e7d10094e04a53d9169ce5e2ddc1cf4bc5a813b72368"
private_key2 = "5f08a758636d7f65c727d60f5bec9ee085b4ec846498185611944d1a578e1b58"
script = "5241041db51a89d50f0f315a7cf5eebdd78c5ff0cf0711a6b897939a7c700dd141be540fccd6ef333f657bc76509cc297e7ca2d312eac010b871364fbb5789e260d4fe41043aab0612236b039e1cc750165efd5128ff07a619f66f0889071e0c39b87cdeaf478d0243a5e2f991c519aa501191f1bc6cef2763340f702f132f8956af9aa5e552ae"
address = "2MvNVs58AM3vyXD9aDTkN1tUsc9XvqMSnuu"

# Create a transaction input (UTXO) &
# Create a transaction output to the desired destination
to_addr = "tb1qrtzcq4xhm9dsy8f8a4yfs4c92cpj3l3kg2tzae"
tx = c.preparetx(address, to_addr, 10000, fee=400)
print(tx)

# Create the transaction
for i in range(0, len(tx['ins'])):
    sig1 = c.multisign(tx, i, script, private_key1)
    sig2 = c.multisign(tx, i, script, private_key2)
    tx = apply_multisignatures(tx, i, script, sig1, sig2)

# Broadcast the transaction
c.pushtx(tx)






