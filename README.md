# rubymarshal

rubymarshal is a library that decodes files in the Ruby marshal format (like .rxdata files).
Not all features of the format are currently supported.

# Usage examples
Parsing standard Ruby marshal files:
```python
import rubymarshal
with open(filename, "rb") as f:
    reader = rubymarshal.Reader(f)
    data = reader.read()

```

Parsing .rxdata files:
```python
import rubymarshal
from rubymarshal import rmxptypes   # Adds support for RPG Maker XP types

with open("System.rxdata", "rb") as f:
    reader = rubymarshal.Reader(f)
    data = reader.read()

print(data)
# #<RPG::System:0x01234567>
```

# Types

## class rubymarshal.Reader
Used for reading ruby marshal files.
Methods:

### \_\_init\_\_(stream: io.BytesIO)
Creates a new Reader object.
Arguments:
| Name | Description |
| ---- | ---- |
| stream | The file from which the data will be read. |

### read() -> Any
Reads next object in the file. This method usually needs to be called only once.

## class rubymarshal.RubyString
A string read from a ruby marshal file.
NOTE: This object doesn't support most str methods!
Methods:
### \_\_str\_\_() -> str
Convert this object into a string.

## class rubymarshal.RubyObject
A class that represents a ruby object. You can access its attributes like any other python object.
Methods:
### \_\_dir\_\_() -> List[str]
Returns all attributes of the object.

## class rubymarshal.Symbol
A Ruby symbol.
Methods:
### \_\_str\_\_() -> str
Returns the symbol as a string, without the : character at the beginning.

## class rubymarshal.DecodeError(RuntimeError)
Exception that is thrown when the reader encounters a decoding error.

## class rubymarshal.SymbolDecodeError(rubymarshal.DecodeError)
Exception that is thrown when the reader encounters a decoding error.

## class rubymarshal.ArrayDecodeError(rubymarshal.DecodeError)
Exception that is thrown when the reader encounters a decoding error.

## class rubymarshal.SymlinkDecodeError(rubymarshal.DecodeError)
Exception that is thrown when the reader encounters a decoding error.

## class rubymarshal.ObjlinkDecodeError(rubymarshal.DecodeError)
Exception that is thrown when the reader encounters a decoding error.

## class rubymarshal.rmxptypes.RMXPDecodeError(RuntimeError)
Exception that is thrown when the reader encounters a decoding error.

## class rubymarshal.rmxptypes.Tone
An RGSS Tone object.

Attributes:
| Name | Description |
| ---- | ---- |
| r | Red |
| g | Green |
| b | Blue |
| g | Gray |

## class rubymarshal.rmxptypes.Color
An RGSS Color object.

Attributes:
| Name | Description |
| ---- | ---- |
| r | Red |
| g | Green |
| b | Blue |
| a | Alpha |

## class rubymarshal.rmxptypes.Table
An RGSS Table object, usually used for map data.

Attributes:
| Name | Description |
| ---- | ---- |
| w | Width |
| h | Height |
| d | Depth |

Methods:
### \_\_getitem\_\_(xyz) -> int
Gets an integer at \[\*xyz\].

### \_\_setitem\_\_(xyz, v) -> int
Sets an integer at \[\*xyz\].