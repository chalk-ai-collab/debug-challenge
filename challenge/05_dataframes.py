# Challenge 05: DataFrame Operations
#
# Background:
# A customer needs help creating aggregated features from transaction data using Chalk.
#
# Customer Issue:
# The customer writes:
#
# > I want to write a program which processes a CSV of transaction data. My CSV is called "05_example.csv", 
# > and it contains the following schema:
# > transaction_id, transaction_amount, status, user_id, card_id, zipcode, transaction_timestamp
# >
# > How do I use Chalk to create a feature called "User.sum_transaction_amount"? 
# > I already have these feature classes defined:

@features
class User:
    id: int
    transactions: DataFrame[Transaction]

@features
class Transaction:
    transaction_id: Primary[int]
    user_id: User.id

# Questions:
# 1. How would you implement a resolver to calculate User.sum_transaction_amount from the transactions DataFrame?
# 2. What additional Transaction features might need to be defined to support this aggregation?
# 3. Provide example code showing how to process the CSV and compute the aggregated feature.
#
# Reference Documentation:
# - Features: https://docs.chalk.ai/docs/features
# - DataFrame Operations: https://docs.chalk.ai/docs/dataframe#from-a-dictionary
# - Python Resolvers: https://docs.chalk.ai/docs/python-resolvers