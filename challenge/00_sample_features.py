# Sample Feature Definition
#
# This file demonstrates a basic Chalk feature class definition.
# It's provided as a reference for candidates who may be unfamiliar
# with Chalk's feature definition syntax.
#
# Note: This is not a challenge - just a reference example.

from chalk.features import features


@features
class User:
    id: int
    full_name: str