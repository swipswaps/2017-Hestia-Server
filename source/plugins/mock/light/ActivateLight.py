from model.Activator import Activator
from model.util.stringToBool import string_to_bool


class ActivateLight(Activator):
    def __init__(self):
        super().__init__()
        self._state = True

    @property
    def name(self):
        return "On/Off"

    @property
    def type(self):
        return "bool"

    @property
    def state(self):
        return self._state

    def set_state_with_string(self, value):
        self._state = string_to_bool(value)

    def perform(self, devicerequired_info):
        if self.state:
            print("light goes on")
        else:
            print("light goes off")