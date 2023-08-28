import eth2spec.altair.mainnet as eth2spec
from eth2spec.altair.mainnet import (
    AttestationData,
    BeaconBlock,
)

from ..types import (
    BLSPubkey,
    SlashingDB,
    SlashingDBData,
)

"""
Commitments Helper Functions
"""


def block_satisfies_proposer_commitments(block: BeaconBlock) -> bool:
    """Checks if the block satisfies its proposer's commitments.
    """
    return True