from abc_type import IdaTypes
from ida_types import IDA_TYPES
from serializer_ida_type import serialize_to_string


class IdaTTypedef(IdaTypes):
    def __init__(self, ida_type=IDA_TYPES['typedef']):
        self.ida_type = {'idt': ida_type, 'value': None}

    def decode(self, data):
        import ida_decoder

        rbyte, value = ida_decoder.decode_hybrid_type(data)
        self.ida_type['value'] = value

        return rbyte

    def get_type(self):
        return self.ida_type

    def to_string(self, session):
        return serialize_to_string(self.ida_type['value'], session)\
                   .replace(' {name}', '')\
                   .replace('{ptr}', '') + '{ptr} {name}'

    def from_dict(self, data):
        self.ida_type = data
