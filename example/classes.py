### "imports"
from cashew import Plugin, PluginMeta
from six import add_metaclass

### "create-plugin-base-class"
@add_metaclass(PluginMeta)
class Data(Plugin):
    """
    Base class for plugins which present data in various ways.
    """

    ### "methods"
    def __init__(self, data):
        self.data = data

    def present(self):
        raise Exception("not implemented")
