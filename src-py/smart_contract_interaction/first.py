from pprint import pprint
import time
import hexbytes as hb
from eth_utils import is_address
from pyvis.network import Network
from web3 import Web3, eth
from gql import gql, Client
from gql.transport.requests import RequestsHTTPTransport
from config import abi_erc20
from concurrent.futures import ThreadPoolExecutor

from utils import is_contract, get_contract_symbol


w3 = Web3(Web3.HTTPProvider("https://mainnet.infura.io/v3"))
last_block = w3.eth.get_block('latest')
last_block_number = last_block["number"]

address = None
counter = w3.eth.contract(address=address, abi=abi_erc20)