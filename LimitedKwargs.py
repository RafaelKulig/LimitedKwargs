class LimitedKwargs:
    VALID_KEYS = {'a', 'b', 'c', 'd', 'e', 'f'}
    KEY_MAP = {'a': 'g', 'b': 'h', 'c': 'i', 'd': 'j', 'e': 'k', 'f': 'l'}

    def __init__(self, **kwargs):
        invalid_keys = set(kwargs) - self.VALID_KEYS
        if invalid_keys:
            print('Invalid key(s). These will be ignored:')
            for key in invalid_keys:
                print(f"\t- {key}")
            print("Type \033[94m\033[4mLimitedKwargs.VALID_KEYS\033[0m for valid keys.")

        self.dictionary = {
            self.KEY_MAP[key]: kwargs.get(key)
            for key in self.VALID_KEYS
            if key in kwargs
        }