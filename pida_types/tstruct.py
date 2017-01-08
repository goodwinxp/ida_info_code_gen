from abc_type import IdaTypes
from types import IDA_TYPES


class IdaTStruct(IdaTypes):
    def __init__(self, ida_type=IDA_TYPES['struct']):
        self.ida_type = {'idt': ida_type, 'value': []}

    def decode(self, data):
        count = ord(data[0])
        offset = 1
        for i in range(0, count):
            from ida_decoder import decode_hybrid_type

            rbyte, value = decode_hybrid_type(ida_type=data[offset:])
            offset += rbyte
            self.ida_type['value'].append(value)

        return offset

    def get_type(self):
        return self.ida_type
