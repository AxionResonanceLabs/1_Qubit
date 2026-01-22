# Keyed Single-Qubit Scalar Signature

This repo contains a minimal single-qubit experiment:

- A secret key is mapped to an angle.
- That angle drives a fixed-depth unitary evolution on |0⟩.
- The final state is mapped to a scalar "magic number".

Public API:

```python
from experiment import run_experiment

state, (x, y, z), magic = run_experiment("AnyKeyYouLike")
print(magic)
