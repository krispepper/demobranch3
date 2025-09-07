# This is a sample Python file named 'hello_world.py'

def greet(name):
  """
  Thistakes a name as input and returns a hello message.
  """
  return f"Aloha, {name}!"

if __name__ == "__main__":
  # Call the greet function with a specific name
  message = greet("aloha world")
  print(message)

  # Get input from the user and greet them
  user_name = input("What's your name? ")
  print(greet(user_name))