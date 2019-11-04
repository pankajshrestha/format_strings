#Reference: https://realpython.com/python-f-strings/#f-strings-a-new-and-improved-way-to-format-strings-in-python

# Python 2 string formatting:
# % based formating
name = "Python2"
age = 20
print("Hello, %s. You are %s" % (name, age))


# string.format()
print("Hello, {}. You are {}".format(name, age))
print("Hello, {1}. You are {0}".format(age, name))
print("Hello, {name}. You are {age}".format(name = name,age = age))
#print("Hello, {name}. You are {age}".format(name,age))

# This is neat
person = {'name': name, 'age' : age}
print("Hello, {name}. You are {age}".format(**person))


# Python 3 f String formatting

name = "Python3"
age = "10"

# small f
print(f"Hello {name}. You are {age}")

# capital F
print(F"Hello {name}. You are {age}")

print(f"{ 2 * 10}")

def to_lowercase(input):
    return input.lower()

name = 'Capital Python3'    
print(f"{to_lowercase(name)} is in lowercase")


class Python3:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def __str__(self):
        return f"{self.first_name} {self.last_name} is {self.age}."
    

    def __repr__(self):
        return f"{self.first_name} {self.last_name} is {self.age} using Representation"


new_class = Python3("Python3", "No Last Name", 10)
print(f"{new_class}")

print(new_class)

print(f"{new_class!r}")


