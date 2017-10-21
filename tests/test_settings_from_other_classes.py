from cashew import Plugin, PluginMeta

class Report(Plugin, metaclass=PluginMeta):
    """
    Report Base Class
    """
    _settings = {}
    _other_class_settings = {
            'document' : {
                'bar' : ("Bar setting.", None)
                }
            }

class Filter(Plugin, metaclass=PluginMeta):
    """
    Filter Base Class
    """
    _settings = {}
    _other_class_settings = {
            'document' : {
                'foo' : ("Foo setting", None)
                }
            }

class Document(Plugin, metaclass=PluginMeta):
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
