"""Tests para la función mean(values) -> float."""

import pytest

from src.calculator import mean


# --- EJEMPLO (no borrar) ---
def test_mean_lista_simple():
    """Ejemplo: el promedio de [2, 4, 6] debe dar 4.0."""
    assert mean([2, 4, 6]) == 4.0

@pytest.mark.parametrize("values,expected", [
    ([5], 5.0),
    ([-1, -2, -3], -2.0),
    ([1.5, 2.5, 3.5], 2.5)
])
def test_mean_parametrizado(values, expected):
    assert mean(values) == expected

def test_mean_lista_vacia():
     with pytest.raises(ValueError):
         mean([])
# --- TU TURNO ---
# Agregá tests para los siguientes casos:
#   - Lista con un solo elemento (el resultado debe ser ese mismo elemento)
#   - Lista con números negativos
#   - Lista con números decimales (float)
#   - Lista vacía → debe lanzar ValueError
#
# Pista: para testear excepciones usá pytest.raises:
#
# def test_mean_lista_vacia():
#     with pytest.raises(ValueError):
#         mean([])
