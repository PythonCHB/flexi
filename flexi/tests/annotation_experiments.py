"""
annotation experiments
"""

from __future__ import annotations

import inspect
import dataclasses




class Custom:
    pass


@dataclasses.dataclass
class Example:
    x: int
    y: float
    z: list
    c: Custom

e = Example(3, 4.5, [1, 2, 3], Custom())

print("fields are:")
fields = {f.name: f.type for f in dataclasses.fields(e)}
for f in fields.items():
    print(f)

annots = inspect.get_annotations(Example, eval_str=True)
print("annotations are:\n", annots)

# let's use them
x = fields['x']("34")
y = fields['y']("3.4")
z = fields['z']((3, 4, 5, 6))
c = fields['c']()

print(f"{x=}")
print(f"{y=}")
print(f"{z=}")
print(f"{c=}")






