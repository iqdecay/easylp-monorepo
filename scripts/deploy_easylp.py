from scripts.helpful_scripts import get_account
from brownie import EasyLp, config

def deploy_easylp():
    account = get_account()
    easylp = EasyLp.deploy({"from": account})
    print("Deployed EasyLp")
    return easylp

def main():
    deploy_easylp()