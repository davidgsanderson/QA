books = {"Stephen King" : ["It", "The Shining", "Holly"], "Jane Austen" : ["Pride and Prejudice", "Sense and Sensibilty", "Emma"], "Charles Dickens" : ["Oliver Twist", "Great Expectations", "A Christmas Carol"]}

author = input("what author are you looking for?")

result = ", ".join(books.get(author, []))

print(result or "author not found")



