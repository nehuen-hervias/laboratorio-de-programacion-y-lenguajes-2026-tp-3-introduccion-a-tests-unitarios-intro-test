"""Tests para la función mul(a, b) -> float."""

import pytest

from src.calculator import mul


# --- EJEMPLO (no borrar) ---
def test_mul_positivos():
    """Ejemplo: 3 * 4 debe dar 12."""
    assert mul(3, 4) == 12

@pytest.mark.parametrize("a,b,expected", [
    (0, 5, 0),
    (-3, -4, 12),
    (3, -4, -12),
    (3, 1, 3),
    (1.5, 2.5, 3.75)
])
def test_mul_parametrizado(a, b, expected):
    assert mul(a, b) == expected


# --- TU TURNO ---
# Agregá tests para los siguientes casos:
#   - Multiplicar por cero
#   - Multiplicar dos números negativos (resultado positivo)
#   - Multiplicar un positivo y un negativo (resultado negativo)
#   - Multiplicar por 1 (elemento neutro)
#   - Multiplicar dos decimales (float)
#
# Pista: podés usar @pytest.mark.parametrize para probar varios casos a la vez.
