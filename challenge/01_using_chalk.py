from chalk.client import ChalkClient

if __name__ == '__main__':
    # The customer runs this file, and gets this error:
    c = ChalkClient(client_id="secret-12312", client_secret="id-abac1243aex")

    ## Error executing online query: error getting REST client: unauthenticated: Client ID and secret are invalid

    # What would you suggest to fix this?

    # After that issue is resolved, the customer runs this query:

    c.query(input={
        User.id: ["1"],
    }, output=[User.first_name])

    # and gets this output:

    ```
    Traceback (most recent call last):
File "/Users/andrew/chalk/fraud-template-staging/scripts/async_offline_query.py", line 11, in <module>
c.query(input={
    File "/Users/andrew/chalk/fraud-template-staging/venv/lib/python3.11/site-packages/chalk/client/client_impl.py", line 1831, in query
encoded_inputs, all_warnings = recursive_encode_inputs(input)
                               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
                               File "/Users/andrew/chalk/fraud-template-staging/venv/lib/python3.11/site-packages/chalk/features/_encoding/inputs.py", line 202, in recursive_encode_inputs
bulk_result, warnings = recursive_encode_bulk_inputs({k: [v] for k, v in inputs.items()}, options=options)
                        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
                        File "/Users/andrew/chalk/fraud-template-staging/venv/lib/python3.11/site-packages/chalk/features/_encoding/inputs.py", line 169, in recursive_encode_bulk_inputs
raise TypeError(
    TypeError: Input '['1']' for primary feature user.id must be of type int or str
    ```


    # What would you suggest to fix this?