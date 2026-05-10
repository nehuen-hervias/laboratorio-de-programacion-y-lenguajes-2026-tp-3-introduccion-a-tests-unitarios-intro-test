"""Tests para la función div(a, b) -> float."""

import pytest

from src.calculator import div


# --- EJEMPLO (no borrar) ---
def test_div_normal():
    """Ejemplo: 6 / 3 debe dar 2.0."""
    assert div(6, 3) == 2.0

def test_div_por_cero():
    with pytest.raises(ZeroDivisionError):
        div(10, 0)

@pytest.mark.parametrize("a,b,expected", [
    (7, 2, 3.5),
    (-6, 3, -2.0),
])
def test_div_parametrizado(a, b, expected):
    assert div(a, b) == expected



# --- TU TURNO ---
# Agregá tests para los siguientes casos:
#   - División que da resultado decimal (float)
#   - División con números negativos
#   - División por cero → debe lanzar ZeroDivisionError
#
# Pista: para testear excepciones usá pytest.raises:
#
# def test_div_por_cero():
#     with pytest.raises(ZeroDivisionError):
#         div(10, 0)
