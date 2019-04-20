def test():
    # Here we can either check objects created in the solution code, or the
    # string value of the solution, available as __solution__. A helper for
    # printing formatted messages is available as __msg__. See the testTemplate
    # in the meta.json for details.

    # If an assertion fails, the message will be displayed
    assert "max_depth=3" in __solution__, "Are you setting the max depth to 3 for your Decision Tree ?"
    assert "train_test_split(X, Y, test_size=0.3, random_state=100)" in __solution__, "Are you setting correctly the test_size and random_state parameter ?"
    assert accuracy == 69, "Are you sure you computed correctly the accuracy?"
    __msg__.good("Well done! You managed to code your first Decision Tree!")
