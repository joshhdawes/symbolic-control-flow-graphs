## How to use

```
from builder import Function
f = Function(module="test_module", function="Test:method")
scfg = f.build_scfg()
scfg.write_to_file("test-scfg.gv")
```
