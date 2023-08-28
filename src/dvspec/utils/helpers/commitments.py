from eth2spec.altair.mainnet import (
    BeaconBlock,
)

from ...eth_node_interface import (
    bn_get_block_satisfies_commitments,
)

"""
Commitments Helper Functions
"""


def block_satisfies_proposer_commitments(block: BeaconBlock) -> bool:
    """Checks if the block satisfies its proposer's commitments.
    """
    return bn_get_block_satisfies_commitments(block)