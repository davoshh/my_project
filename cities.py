prompt = "\nPlease enter the name of a city you have visited: "
prompt += "\n(Enter 'quit' when you have finished.)"

while True:
    city = input(prompt)
    if city == "quit":
        break
    else:
        print(f"\nWow, I'd love to visit {city.title()}")
