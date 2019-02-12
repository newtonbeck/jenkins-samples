from random import randint
from time import sleep

seconds_to_sleep = randint(1, 6)

print("Sleeping for {} seconds".format(seconds_to_sleep))

sleep(seconds_to_sleep)
