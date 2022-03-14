from tarfile import BLOCKSIZE
from brownie import network, accounts, config, MockV3Aggregator
from web3 import Web3

LOCAL_BLOCKCHAIN_ENVIRONMENTS = ["development", "ganache-local"]
FORKED_LOCAL_ENVIRONMENTS = ["mainnet-fork-dev", "mainnet-fork"]
DECIMALS = 8
STARTING_PRICE = 20000000000


def get_account():
    if (
        network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS
        or network.show_active() in FORKED_LOCAL_ENVIRONMENTS
    ):
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])


def deploy_mocs():
    if len(MockV3Aggregator) <= 0:
        print(f"active network is {network.show_active()}")
        print("Deploying mocks...")
        MockV3Aggregator.deploy(18, Web3.toWei(2000, "ether"), {"from": get_account()})
        print("deployed")
        # recent -1
        price_feed_addres = MockV3Aggregator[-1].address
