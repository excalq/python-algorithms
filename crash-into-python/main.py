def shout(message="Hi"):
    print("%s!" % message)

shout() # Prints "Hi!"
shout("I love python")
shout(message="And keyword arguments")

beverage = None
office = []
for fridge in office:
    if 'Coke' in fridge:
        beverage = fridge.remove('Coke')
        break
if not beverage:
    shout("Where's the @#$%ing Coke?")

mapping = {'foo': 'bar', 'fooo': 'baz'}
for key in mapping:
  print("%s=%s" % (key, mapping[key]))

for value in mapping.values():
  print("???=%s" % value)

for (k, v) in mapping.items():
  print("%s=%s" % (k, v))

print('-------------------------------')
def takes_all(required, *blargs, **blkwargs):
    # tuple of all positional (non-keyword) arguments
    print(blargs)

    # dictionary of all keyword arguments
    print(blkwargs)

takes_all('one', 'two', 'three', ['a','b','c'], opts={'four': 4, 'five': 5, 'six': 6})