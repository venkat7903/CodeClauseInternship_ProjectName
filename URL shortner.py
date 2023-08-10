from pyshorteners import Shortener

user_input_url = input("Paste The URL here: ")
short_url = Shortener().tinyurl.short(user_input_url)
print("Shorted URL", short_url)