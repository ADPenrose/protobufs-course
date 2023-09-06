# Phonebook exercise
import proto.addressbook_pb2 as addressbook_pb2
import sys

# Creating a person manually
# person = addressbook_pb2.Person(name="Arturo", id=12345, email="arturo@me.com")
# phones = person.phones.add(number="555-1234", type=addressbook_pb2.Person.HOME)


# Creating a person with user input
def add_person(person):
    # Create a new person
    person.id = int(input("Id: "))
    person.name = input("Name: ")
    person.email = input("Email: ")

    # Adding all of the phone numbers of the user
    while True:
        user_number = input("Phone number (or blank to finish): ")
        if user_number == "":
            break

        phone_number = person.phones.add(number=user_number)

        phone_type = input("Phone type (mobile, work or home): ")
        if phone_type == "mobile":
            phone_number.type = addressbook_pb2.Person.MOBILE
        elif phone_type == "work":
            phone_number.type = addressbook_pb2.Person.WORK
        elif phone_type == "home":
            phone_number.type = addressbook_pb2.Person.HOME
        else:
            print("Invalid phone type; using mobile as default.")


# The sys.argv is used to fetch a list of strings representing the arguments
# (as separated by spaces) on the command-line. If the file is run without specifying
# the address book file, then a message indicating that will be displayed.
if len(sys.argv) != 2:
    print("Usage:", sys.argv[0], "ADDRESS_BOOK_FILE")
    sys.exit(-1)

# Create the address book object, so that we can use it to read and write.
address_book = addressbook_pb2.AddressBook()

# We try to read the data from the file to check that said file exists.
# If the file does not exist, then we create a new one. If the file exists,
# then the data inside of it is first parsed/deserialized (from binary to protobuf),
# and then it is given to the address_book object, so that it is considered for the next
# write operation (which will contain the data from the file, and the new data given by
# the user).
try:
    with open(sys.argv[1], "rb") as f:
        address_book.ParseFromString(f.read())
except IOError:
    print(sys.argv[1] + ": Could not open file.  Creating a new one.")

# Add an address
add_person(address_book.people.add())

# Write the address book back to a file in binary
with open(sys.argv[1], "wb") as f:
    f.write(address_book.SerializeToString())
