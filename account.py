from web3 import Web3

# Fill in your infura API key here
infura_url = "https://sepolia.infura.io/v3/fc312625491f47e38df0a88df7aa476e"
web3 = Web3(Web3.HTTPProvider(infura_url))

print(web3.is_connected())

print(web3.eth.block_number)

# Fill in your account here
balance = web3.eth.get_balance("0x9081169772d2fB625EE5D4d5fB4370D83955F606")
print(web3.from_wei(balance, "ether"))