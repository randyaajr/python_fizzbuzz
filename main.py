for number in range(0, 501):
  if number % 4 == 0 and number % 7 == 0:
    print("fizzbuzz")
  elif number % 4 == 0:
    print("fizz")
  elif number % 7 == 0:
    print("buzz")
  else:
    print(number)
