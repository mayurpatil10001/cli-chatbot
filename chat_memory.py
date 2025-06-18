class ChatMemory:
    def __init__(self, window_size=3):
        self.memory = []
        self.window_size = window_size

    def add_turn(self, user, bot):
        self.memory.append((user, bot))
        if len(self.memory) > self.window_size:
            self.memory.pop(0)

    def get_history(self):
        return self.memory

    def update_last_bot_reply(self, bot_reply):
        if self.memory:
            user, _ = self.memory[-1]
            self.memory[-1] = (user, bot_reply)
