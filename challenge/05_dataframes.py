# A customer writes in saying:
# 
#   I want to write a program which processes a csv of transaction data. My csv is called "05_example.csv", and it contains the following schema:
#   transaction_id, transaction_amount, status, user_id, card_id, zipcode, transaction_timestamp
#
#   How do I use Chalk to create a feature called "User.sum_transaction_amount"? I already have these feature class defined:


@features
class User:
  id: int
  transactions: DataFrame[Transaction]

@features
class Transaction:
  transaction_id: Primary[int]
  user_id: User.id

# Please review the documentation here:
#
#  0) https://docs.chalk.ai/docs/features
#  1) https://docs.chalk.ai/docs/dataframe#from-a-dictionary
#  2) https://docs.chalk.ai/docs/python-resolvers
#
# for reference.
 
