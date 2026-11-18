# Convert scores to normalized weights: implementation

## What the example does

Subtracting the maximum makes exponentiation stable for large finite scores. Output weights sum approximately to one; empty input returns an empty list.

The public function is `solve(value)`. The JSON input contract can be seen in this concrete example:

```json
[
  1,
  2,
  3
]
```

Expected result:

```json
[
  0.09003057317038046,
  0.24472847105479764,
  0.6652409557748218
]
```

Run `python3 example.py` for the Python representation of the result. `solution.py` contains the full implementation and can also be imported by another script.

## Scope

The function implements exactly the behavior described above. It does not perform network or filesystem access. Python exceptions indicate unsupported input; the next lesson turns them into a command-line error response. Review the limitations before reusing it in an application.
