### "imports"
from .classes import Data

### "other-imports"
import csv
import io
import json
import six

### "csv-subclass"
class Csv(Data):
    """
    CSV type.
    """
    aliases = ['csv']

    ### "csv-settings"
    _settings = {
            'write-header' : ("Whether to write a header row first.", True),

            'csv-settings' : (
                "List of settings which should be passed to python csv library.",
                ['dialect', 'delimiter', 'lineterminator']),

            'dialect' : ("CSV dialect.", None),
            'delimiter' : ("A one-character string used to separate fields.", None),
            'lineterminator' : ("String used to terminate lines.", None)
            }

    ### "list-dialects"
    def list_dialects(self):
        return csv.list_dialects()

    ### "csv-present"
    def present(self):
        s = io.StringIO()

        kwargs = dict((k, v)
                for k, v in six.iteritems(self.setting_values())
                if v and (k in self.setting('csv-settings'))
                )

        writer = csv.DictWriter(s, list(self.data[0].keys()), **kwargs)

        if self.setting('write-header'):
            writer.writeheader()
        writer.writerows(self.data)
        
        return s.getvalue()

### "json-subclass"
class Json(Data):
    """
    JSON type.
    """
    aliases = ['json']

    _settings = {
            }

    def present(self):
        return json.dumps(self.data) 
