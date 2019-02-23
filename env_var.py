from os import environ

environment = environ['MY_ENV']

print("Running in {} environment".format(environment))
