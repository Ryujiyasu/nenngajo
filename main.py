import io
import os
import json
import glob

from pprint import pprint

# Google Cloud client libraryのインポート
from google.cloud import vision
from google.cloud.vision import types

from google.protobuf.json_format import MessageToJsonimport io
import os
import json
import glob

from pprint import pprint

# Google Cloud client libraryのインポート
from google.cloud import vision
from google.cloud.vision import types

from google.protobuf.json_format import MessageToJson
text=data["fullTextAnnotation"]["text"]
texts=text.split("\n")
number=""
for text in texts:
    try:
        n=int(text)
        if len(text)==6:
            number=text
    except:
        pass

