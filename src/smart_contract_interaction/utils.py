from web3.exceptions import BadFunctionCallOutput, ContractLogicError

from config import abi_erc20


def is_contract(address, w3):
    if type(address) != str:
        return False
    token = w3.eth.contract(w3.toChecksumAddress(address), abi=abi_erc20)
    try:
        token.functions.symbol().call()
        return True
    except (BadFunctionCallOutput, ContractLogicError, ValueError):
        return False

def get_contract_symbol(address, w3):
    token = w3.eth.contract(w3.toChecksumAddress(address), abi=abi_erc20)
    return token.functions.symbol().call()



