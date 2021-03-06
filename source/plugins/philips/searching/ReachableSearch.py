from plugins.philips.SearchStrategy import SearchStrategy


class ReachableSearch(SearchStrategy):
    """
    Searches based on whether or not lights are reachable.
    Won't work when multiple devices are reachable.
    """

    @classmethod
    def search(cls, response, types):
        found = False
        for key, value in response.items():
            if value['state']['reachable'] and value['type'] in types:
                if found:
                    raise Exception("Multiple lights were found")
                else:
                    found = True
                    lamp_id = int(key)

        if not found:
            raise Exception("No lights were found")

        return lamp_id
