# Phonebook exercise
import proto.addressbook_pb2 as addressbook_pb2
import sys


# Iterate through all of the people in the address book and print their info
def print_people_info(people):
    for person in people.people:
        print("Person ID: ", person.id)
        print("Person Name: ", person.name)
        print("Person Email: ", person.email)
        for phone in person.phones:
            print("Phone Number: ", phone.number)
            print("Phone Type: ", phone.type)


# The sys.argv is used to fetch a list of strings representing the arguments
# (as separated by spaces) on the command-line. If the file is run without specifying
# the address book file, then a message indicating that will be displayed.
if len(sys.argv) != 2:
    print("Usage:", sys.argv[0], "ADDRESS_BOOK_FILE")
    sys.exit(-1)

# Create the address book object, so that we can use it to read and write.
address_book = addressbook_pb2.AddressBook()

# We try to read the data from the file to check that said file exists.
# If the file does not exist, then we say so to the user. If the file exists,
# then the data inside of it is first parsed/deserialized (from binary to protobuf),
# and then it is given to the address_book object, so that it is considered for the next
# write operation (which will contain the data from the file, and the new data given by
# the user).
try:
    with open(sys.argv[1], "rb") as f:
        address_book.ParseFromString(f.read())
except IOError:
    print("Could not open file. Check if the address book file exists.")
else:
    print_people_info(address_book)
