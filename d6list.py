numbers = [1, "💖", 2, "🔥", 3, "⭐️", 4, "💖", 5, "🔥", 6, "⭐️", 7, "💖", 8, "🔥", 9, "⭐️", 10, "💖", 11, "🔥", 12, "⭐️", 13, "💖", 14, "🔥", 15, "⭐️", 16]
integers = []

sum = 0

for number in numbers:
  if type(number) == int:
    integers.append(number)

for integer in integers:
  sum += integer

print(sum)