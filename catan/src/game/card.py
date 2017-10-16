
class Card():
    def __init__(id, is_visible, is_playable):
        self.id = id
        self.is_visible = is_visible
        self.is_playable = is_playable



class Resource(Card):
    def __init__(id, type, is_visible, is_playable):
        Card.__init__(id, is_visible, is_playable)
        self.type = type


class Resource(Dev):
    def __init__(id, type, is_visible, is_playable):
        Card.__init__(id, is_visible, is_playable)
        self.type = type
