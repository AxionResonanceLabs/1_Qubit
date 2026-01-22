# Keyed Single‑Qubit Evolution — Scalar Signature Experiment

## Overview

This repository contains a minimal quantum experiment:

> A deterministic single‑qubit evolution that produces a stable scalar signature from a secret key.

- One qubit  
- Fixed depth  
- No randomness  
- Deterministic, unitary evolution  
- Keyed scalar “magic number” as output  

The internal operator construction is intentionally hidden in the public interface.  
This is not a product and not a cryptosystem — it is a **phenomenon** and a **conversation starter**.

---

## Concept

1. A secret key is mapped to a continuous parameter \(\theta \in [0, 2\pi)\).
2. \(\theta\) drives a fixed‑depth unitary evolution on \(|0\rangle\).
3. The final state is mapped to a scalar signature via a deterministic readout function.

Observable properties:

- **Reproducible:** same key → same scalar  
- **Sensitive:** small key changes → large scalar changes  
- **Opaque:** scalar does not reveal the operators  
- **Unitary:** no noise, no dissipation  
- **Minimal:** one qubit, fixed depth, no ancilla  

---

## Quick start

```bash
git clone <your-repo-url>
cd <your-repo>
python examples/demo.py
