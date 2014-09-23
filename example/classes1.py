### "imports"
from classes import Data

### "other-imports"
import csv
import io
import json

### "csv-subclass"
class Csv(Data):
    """
    CSV type.
    """
    aliases = ['csv']

    def present(self):
        s = io.StringIO()
        writer = csv.DictWriter(s, fieldnames=[unicode(k) for k in self.data[0].keys()])

        writer.writeheader()
        writer.writerows(self.data)
        
        return s.getvalue()

### "json-subclass"
class Json(Data):
    """
    JSON type.
    """
    aliases = ['json']

    def present(self):
        return json.dumps(self.data) 

