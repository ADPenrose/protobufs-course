# Needed to read and write to JSON
import google.protobuf.json_format as json_format

import proto.simple_pb2 as simple_pb2
import proto.complex_pb2 as complex_pb2
import proto.enumerations_pb2 as enumerations_pb2
import proto.oneofs_pb2 as oneofs_pb2
import proto.maps_pb2 as maps_pb2


def simple():
    return simple_pb2.Simple(
        id=42, is_simple=True, name="Arturo", sample_list=[1, 2, 3]
    )


def complex():
    # First, we define the Complex message, which is the parent of the other message present in the protobuf.
    message = complex_pb2.Complex()
    # Then, we define each one of the properties according to the protobuf schema.
    message.one_dummy.id = 4
    message.one_dummy.name = "Arturo"
    message.multiple_dummies.add(id=43, name="Nepo")
    message.multiple_dummies.add(id=44, name="Akemi")
    message.multiple_dummies.add(id=45, name="Lula")
    message.multiple_dummies.add(id=46, name="Tete")
    return message


def enums():
    return enumerations_pb2.Enumeration(
        # Without ordinal number
        # eye_color=enumerations_pb2.EYE_COLOR_GREEN
        # With ordinal number
        eye_color=1
    )


def oneofs():
    # Because of how we defined the protobuf, we can set either this:
    message = oneofs_pb2.Result(message="A message.")
    print(message)
    # Or this:
    message.id = 42
    print(message)


def maps():
    message = maps_pb2.MapExample()
    # Check if the key exists, and if not, create it
    message.ids["myid1"].id = 42
    message.ids["myid2"].id = 43
    message.ids["myid3"].id = 44
    print(message)


def file(message):
    path = "simple.bin"
    print("Write to file")
    print(message)
    with open(path, "wb") as f:
        bytes_as_str = message.SerializeToString()
        f.write(bytes_as_str)

    print("Read from file")
    with open(path, "rb") as f:
        t = type(message)
        # We need to init the object to be able to acces the FromString method, and to do that,
        # we obtain its type, and then call it as a function. We don't use the ParseFromString
        # method because the object was not defined explicitely. So we cannot store the data
        # inside of it.
        message2 = t().FromString(f.read())
        print(message2)


# From protobuf to JSON
def to_json(message):
    return json_format.MessageToJson(
        message, indent=2, preserving_proto_field_name=True
    )


# From JSON to protobuf
def from_json(json_str, type):
    # We use the type funcion to achieve the same functionality seen on the "read from file" in binary.
    return json_format.Parse(json_str, type(), ignore_unknown_fields=True)


if __name__ == "__main__":
    # print(simple())
    # print(complex())
    # print(enums())
    # print(oneofs())
    # print(maps())
    file(simple())
    # json_str = to_json(complex())
    # print(json_str)
    # print(from_json(json_str, complex_pb2.Complex))
    # print(from_json('{"id": 42, "unknown": "test"}', simple_pb2.Simple))
    pass
