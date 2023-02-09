from .context import utils

def test_say_hello():
        assert utils.Say_hello("Adrian") == "Hello Adrian"
        assert utils.Say_hello("Zoey") == "Hello Zoey"
