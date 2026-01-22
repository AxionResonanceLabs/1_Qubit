import numpy as np
import hashlib

# ---------------------------------
# 1. Key → angle
# ---------------------------------
def key_to_angle(key: str) -> float:
    """Map a secret string to a rotation angle in [0, 2π)."""
    h = hashlib.sha256(key.encode("utf-8")).hexdigest()
    x = int(h[:16], 16) / (16**16)
    return 2 * np.pi * x

# ---------------------------------
# 2. Single-qubit machinery
# ---------------------------------
zero = np.array([1+0j, 0+0j])

def Rx(a: float) -> np.ndarray:
    c = np.cos(a / 2)
    s = -1j * np.sin(a / 2)
    return np.array([[c, s],
                     [s, c]], dtype=complex)

def Ry(a: float) -> np.ndarray:
    c = np.cos(a / 2)
    s = np.sin(a / 2)
    return np.array([[c, -s],
                     [s,  c]], dtype=complex)

def Rz(a: float) -> np.ndarray:
    return np.array([[np.exp(-1j * a / 2), 0],
                     [0, np.exp(1j * a / 2)]], dtype=complex)

def bloch_coords(state: np.ndarray):
    rho = np.outer(state, np.conjugate(state))
    sx = np.array([[0, 1], [1, 0]], dtype=complex)
    sy = np.array([[0, -1j], [1j, 0]], dtype=complex)
    sz = np.array([[1, 0], [0, -1]], dtype=complex)
    x = np.real(np.trace(rho @ sx))
    y = np.real(np.trace(rho @ sy))
    z = np.real(np.trace(rho @ sz))
    return x, y, z

# ---------------------------------
# 3. Key-driven sequence
# ---------------------------------
def _build_base_unitary(theta: float) -> np.ndarray:
    a1 = theta / 3.0
    a2 = 2.0 * theta / 5.0
    a3 = -4.0 * theta / 7.0
    a4 = (theta * np.sqrt(2)) / 11.0
    return Rz(a2) @ Ry(a1) @ Rx(a3) @ Rz(a4)

def chaotic_stack(state: np.ndarray, depth: int, theta: float) -> np.ndarray:
    U = _build_base_unitary(theta)
    s = state.copy()
    for k in range(1, depth + 1):
        ak = theta * (2*k + 1) / (k**2 + 3)
        layer = Rz(ak / 3) @ Rx(-ak / 5) @ Ry(ak / 7)
        s = layer @ (U @ s)
    return s

# ---------------------------------
# 4. Public API
# ---------------------------------
def run_experiment(secret_key: str, depth: int = 9):
    """
    Deterministic single-qubit evolution producing a scalar signature.
    """
    theta = key_to_angle(secret_key)
    state = zero.copy()
    final_state = chaotic_stack(state, depth=depth, theta=theta)

    x, y, z = bloch_coords(final_state)
    magic_number = float(np.round(z * np.pi + x * np.e - y, 9))

    return final_state, (x, y, z), magic_number
