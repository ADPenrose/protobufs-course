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


if __name__ == "__main__":
    # print(simple())
    # print(complex())
    # print(enums())
    # print(oneofs())
    print(maps())
