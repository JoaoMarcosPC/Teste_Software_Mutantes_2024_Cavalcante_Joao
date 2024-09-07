import math
import re
import pytest
from prime import gen_prime_eratosthenes, is_prime_simple, is_prime_re
from sympy import isprime

@pytest.mark.parametrize("n", [x for x in range(2,15) if is_prime_simple(x)])
def test_prime_simple(n):
    assert isprime(n)

@pytest.mark.parametrize("n", [x for x in range(2,15) if is_prime_simple(x)])
def test_prime_re(n):
    assert isprime(n)

@pytest.mark.parametrize("n", [x for x in range(16) if not is_prime_simple(x)])
def test_not_prime_simple(n):
    assert not isprime(n)

@pytest.mark.parametrize("n", [x for x in range(15) if not is_prime_simple(x)])
def test_not_prime_re(n):
    assert not isprime(n)

# Casos de teste adicionados
def test_is_prime_simple():
    assert is_prime_simple(11)

new_gpe = gen_prime_eratosthenes()
def test_gen_prime_eratosthenes():
    numbers = [next(new_gpe) for i in range(15)]
    test_numbers = [2, 3, 5, 7, 11, 13]

    if numbers == None:
        assert False

    for i in range(0, 4):
        if numbers[i] != test_numbers[i] and isPrime(numbers[i]):
            assert False
    assert True

# Casos de teste retirados

# gpe = gen_prime_eratosthenes()
# @pytest.mark.parametrize("n", [next(gpe) for i in range(15)])
# def test_prime_gpe(n):
#     assert isprime(n)