from model.Device import Device
from plugins.mock.lock.ActivateLock import ActivateLock


class Lock(Device):

    def __init__(self):
        super().__init__()
        super().add_activator(ActivateLock())

    def setup(self):
        print("Mock lock is being setup")

    @classmethod
    def _get_organization(cls):
        return "Mock"

    @classmethod
    def _get_plugin_name(cls):
        return "Lock"

    @classmethod
    def _get_plugin_type(cls):
        return "Lock"

    @classmethod
    def _get_extra_required_info(cls) -> dict:
        return {"ip": "127.0.0.1", "port": "0", "maximum spin speed": "90"}