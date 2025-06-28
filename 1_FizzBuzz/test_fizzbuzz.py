from fizzbuzz import fizzbuzz

def test_returns_number_as_string():
    assert fizzbuzz(1) == "1"
    assert fizzbuzz(2) == "2"

def test_returns_fizz_for_multiples_of_3():
    assert fizzbuzz(3) == "Fizz"
    assert fizzbuzz(6) == "Fizz"

def test_returns_buzz_for_multiples_of_5():
    assert fizzbuzz(5) == "Buzz"
    assert fizzbuzz(10) == "Buzz"

def test_returns_fizzbuzz_for_multiples_of_3_and_5():
    assert fizzbuzz(15) == "FizzBuzz"
    assert fizzbuzz(30) == "FizzBuzz"
    