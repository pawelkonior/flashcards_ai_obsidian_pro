**📝 1. Pytest i Testy Jednostkowe**

  

**🔹 Podstawy pytest**

• pytest to popularna biblioteka do testowania w Pythonie.

• Obsługuje **testy jednostkowe** (unit tests), **testy integracyjne** i **test-driven development (TDD)**.

**🔹 Instalacja**

```sh

pip install pytest

```

**🔹 Pisanie testów jednostkowych**

```python

def add(x, y):
    return x + y

def test_add():
    assert add(2, 3) == 5
    
```

**🔹 Uruchamianie testów**

```sh

pytest test_file.py  # Uruchomienie konkretnego pliku
pytest               # Uruchomienie wszystkich testów
pytest -v            # Szczegółowy output

```

#pytest #unit_tests #python

