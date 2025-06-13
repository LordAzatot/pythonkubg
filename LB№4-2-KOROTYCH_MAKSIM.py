class Buffer:
    def __init__(self):
        self.data = []

    def add(self, *a):
        self.data.extend(a)
        while len(self.data) >= 5:
            # Беремо перші 5 елементів
            chunk = self.data[:5]
            print(f"Сума п’ятірки {chunk}: {sum(chunk)}")
            # Видаляємо ці 5 елементів
            self.data = self.data[5:]

    def get_current_part(self):
        return self.data
