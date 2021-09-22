import check50

@check50.check() # tags the function as a check
def exists():
    """description - test"""
    check50.exists("hello.py")