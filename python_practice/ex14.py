from sys import argv

script, user_name = argv
prompt = "> "

print(f"Hi {user_name}, I'm the {script} script.")

likes = input(f"Do you like me {user_name}? \n")
print(f"ok so you {likes}")
