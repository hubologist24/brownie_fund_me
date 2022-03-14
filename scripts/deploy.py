from brownie import FundMe, network, config, MockV3Aggregator
from scripts.helpful_scripts import (
    get_account,
    deploy_mocs,
    LOCAL_BLOCKCHAIN_ENVIRONMENTS,
)


def fund_me():
    account = get_account()
    print(network.show_active())

    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        price_feed_addres = config["networks"][network.show_active()][
            "eth_usd_price_feed"
        ]
        # "0x8A753747A1Fa494EC906cE90E9f37563A8AF630e"
    else:
        deploy_mocs()
        price_feed_addres = MockV3Aggregator[-1].address

    fund_me = FundMe.deploy(
        price_feed_addres,
        {"from": account},
        publish_source=config["networks"][network.show_active()].get("verify"),
    )
    print(f"Contract deployed to adrres {fund_me.address}")
    return fund_me


def main():
    fund_me()
