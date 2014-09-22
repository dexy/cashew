from cashew import Plugin, PluginMeta
from six import add_metaclass

@add_metaclass(PluginMeta)
class Report(Plugin):
    """
    Report Base Class
    """
    _settings = {}
    _other_class_settings = {
            'document' : {
                'bar' : ("Bar setting.", None)
                }
            }

@add_metaclass(PluginMeta)
class Filter(Plugin):
    """
    Filter Base Class
    """
    _settings = {}
    _other_class_settings = {
            'document' : {
                'foo' : ("Foo setting", None)
                }
            }

@add_metaclass(PluginMeta)
class Document(Plugin):
    """
    Document Base Class
    """
    aliases = ['document']

class SomeKindOfDocument(Document):
    """
    Some kind.
    """
    aliases = ['somekind']

def test_other_class_settings():
    assert sorted(PluginMeta._store_other_class_settings['document']) == ['bar', 'foo']
    x = Document.create_instance('somekind')
    assert sorted(x.setting_values()) ==  ['aliases', 'bar', 'foo', 'help', 'install-dir']
